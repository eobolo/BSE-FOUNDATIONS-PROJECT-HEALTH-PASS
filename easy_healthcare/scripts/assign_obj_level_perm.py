from academic_feedback_sys.models import Student
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm
from django.core.exceptions import ObjectDoesNotExist

class UserDoesNotExistsError(Exception):
    def __init__(self, message="doesn't exist."):
        super().__init__(message)

def run(*args):
    message = ""
    while True:
        mistake = input("do you want to stop teacher-student assignment, answer yes or no? ")
        if mistake.lower() == "yes":
            print("quitting scripts...")
            break

        count_trial = 1
        while True:
            try:
                username = input("Enter teacher's username: ")
                check_if_user_exists = User.objects.filter(username=username).first()
                if not check_if_user_exists:
                    count_trial += 1
                    raise UserDoesNotExistsError
            except UserDoesNotExistsError as userr:
                message = f"User with username {username} {userr}"
                print(f"\n{message}.")
                print("follow instructions after Error message.")
                if count_trial % 4 == 0:
                    outcome = input("Do you want to still input User/Teacher username, answer yes or no ? ")
                    if outcome.lower() == "yes":
                        continue
                    else:
                        # set count trial to zero meaning user doesn't want to go on with assignment
                        count_trial = 0
                        break
            else:
                break

        # to see if the user didn't want to go on with the assignment
        if count_trial == 0:
            print("quitting scripts...")
            break

        count_trial = 1
        while True:
            try:
                first_name = input("Enter student first name: ")
                middle_name = input("Enter student middle name: ")
                last_name = input("Enter student last name: ")
                check_if_student_exists = Student.objects.get(
                    first_name=first_name.capitalize(),
                    middle_name=middle_name.capitalize(),
                    last_name=last_name.capitalize(),
                )
            except ObjectDoesNotExist:
                message = f"Student {first_name} {middle_name} {last_name} doesn't exist."
                print(f"\n{message}.")
                print("follow instructions after Error message.")
                count_trial += 1
                if count_trial % 4 == 0:
                    outcome = input("Do you want to still input student names, answer yes or no ? ")
                    if outcome.lower() == "yes":
                        continue
                    else:
                        count_trial = 0
                        break
            else:
                break

        if count_trial == 0:
            print("quitting scripts...")
            break

        # check if user/teacher has permissions already
        if check_if_user_exists.has_perm("edit_student_grade", check_if_student_exists):
            print(f"\nUser/Teacher with {username} already has permissions on student {first_name} {middle_name} {last_name}.")
            outcome = input("Do you want to still assign students to teachers, answer yes or no ? ")
            if outcome.lower() == "yes":
                continue
            else:
                print("quitting scripts...")
                break

        # assign edit permission to teacher
        assign_perm('edit_student_grade', check_if_user_exists, check_if_student_exists)
        if check_if_user_exists.has_perm("edit_student_grade", check_if_student_exists):
            print(f"permission granted to {check_if_user_exists.first_name} {check_if_user_exists.last_name} :)")
            outcome = input("Do you want to still assign students to teachers, answer yes or no ? ")
            if outcome.lower() == "yes":
                continue
            else:
                print("quitting scripts...")
                break
