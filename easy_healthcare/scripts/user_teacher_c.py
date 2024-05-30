from django.contrib.auth.models import User
from academic_feedback_sys.models import Subject, Teacher
import re

"""utility class"""
class EmailError(Exception):
    def __init__(self, message="Email not valid"):
        super().__init__(message)


"""utility function"""
def is_valid_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    return bool(pattern.match(email))


def run(*args):
    message = "\nfollow these instructions to create a user/teacher"
    print(message)
    while True:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        username = input("Enter your username: ")
        email = input("Enter a correct email: ")
        password = input("Enter your password: ")
        subject = input("Enter subject teacher teaches: ")
        try:
            email_valid = is_valid_email(email)
            if not email_valid:
                raise EmailError("Email {0} not valid, put a valid one.".format(email))
        except EmailError as e:
            print("\nThis error occured: {0}.".format(e))
            message = "follow the instructions again after seeing the error"
            print(message)
            continue
        else:
            try:
                auth_user_obj = User.objects.create_user(
                    first_name=first_name.capitalize(),
                    last_name=last_name.capitalize(),
                    username=username,
                    email=email,
                    password=password,
                    is_staff=True,
                )
            except Exception as e:
                print("\nThis error occured: {0}.".format(e))
                message = "follow the instructions again after seeing the error"
                print(message)
                continue
            else:
                try:
                    subject_obj = Subject.objects.get(subject=subject.upper())
                except Exception as e:
                    # delete the user created
                    user_obj = User.objects.filter(username=username)
                    user_obj.delete()
                    print("\nThis error occured: {0}.".format(e))
                    message = "follow the instructions again after seeing the error"
                    print(message)
                    continue
                else:
                    teacher_obj = Teacher.objects.create(
                        staff=auth_user_obj,
                        subject=subject_obj,
                    )
                    print(teacher_obj)
                outcome = input("Do you want to add another teacher yes or no? ")
                if outcome.lower() == "yes":
                    continue
                else:
                    break
