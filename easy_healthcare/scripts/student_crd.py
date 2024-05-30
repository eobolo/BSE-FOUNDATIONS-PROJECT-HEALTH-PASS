from academic_feedback_sys.models import Student, Teacher, User
from django.core.mail import EmailMessage
from django.conf import settings
import re


"""utility class"""
class EmailError(Exception):
    def __init__(self, message="Email not valid"):
        super().__init__(message)


class CrudError(Exception):
    def __init__(self, message="is not a crud operation, here are the crud operations we have create, read, delete."):
        super().__init__(message)


class StudentExistsError(Exception):
    def __init__(self, message="Student already exists in the database, cannot create a duplicate!!!"):
        super().__init__(message)


"""utility function"""
def is_valid_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    return bool(pattern.match(email))

def send_html_email(credential, email, school_name="child's"):
    subject = 'student credential from  your {0} school'.format(school_name)
    message = 'This is the credential to check child result {0}'.format(credential)
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    html_content = '<h1>This is an mail message.</h1>'

    email = EmailMessage(subject, message, from_email, recipient_list)
    email.content_subtype = 'html'  # Main content is now text/html
    email.send()


def run(*args):
    message = "\nfollow these instructions to perform crud on student"
    operations = ["create", "read", "delete"]
    student_teachers = []
    while True:
        try:
            operation = input("Enter the operation you want to do i.e create, read, or delete: ")
            if operation not in operations:
                raise CrudError
        except CrudError as e:
            print("\nThis error occured {0} {1}".format(operation, e))
            message = "follow the instructions again after seeing the error"
            print(message)
            continue
        else:
            while True:
                try:
                    guardian_email = input("Enter a correct guardian email so a credential can be sent to check student grade: ")
                    email_valid = is_valid_email(guardian_email)
                    if not email_valid:
                        raise EmailError("Email {0} not valid, put a valid one.".format(guardian_email))
                except EmailError as e:
                    print("\nThis error occured: {0}.".format(e))
                    message = "follow the instructions again after seeing the error"
                    print(message)
                    outcome = input("Do you want to still give an email, if your operation is create you must i.e yes, if not, not compulsory i.e  no: \n")
                    if outcome.lower() == "no" and operation.lower() != "create":
                        break
                    else:
                        continue
                else:
                    break
            while True:
                try:
                    teacher_username = input("Enter teacher username: ")
                    check_user_exists = User.objects.get(username=teacher_username)
                    check_teacher_exists = Teacher.objects.get(staff=check_user_exists)
                except Exception as e:
                    print("\nThis error occured: {0}.".format(e))
                    message = "follow the instructions again after seeing the error"
                    print(message)
                    outcome = input("Do you still want to check teacher username yes or no: \n")
                    if outcome.lower() == "yes":
                        continue
                    else:
                        break
                else:
                    student_teachers.append(check_teacher_exists)
                    outcome = input("Do you want to add another teacher for the student yes or no ? ")
                    if outcome.lower() == "yes":
                        continue
                    else:
                        break
            while True:
                first_name = input("Enter student first name: ")
                middle_name = input("Enter student middle name: ")
                last_name = input("Enter student last name: ")
                if operation.lower() == "create":
                    try:
                        check_student_exists = Student.objects.filter(
                            first_name=first_name.capitalize(),
                            middle_name=middle_name.capitalize(),
                            last_name=last_name.capitalize(),
                        ).exists()
                        if check_student_exists:
                            raise StudentExistsError
                    except StudentExistsError as e:
                        print("\nThis error occured: {0}.".format(e))
                        message = "follow the instructions again after seeing the error"
                        print(message)
                        break
                    else:
                        add_student = Student.objects.create(
                            first_name=first_name.capitalize(),
                            middle_name=middle_name.capitalize(),
                            last_name=last_name.capitalize(),
                        )
                        add_student.teachers.set(student_teachers)
                        add_student.save()
                        send_html_email(add_student.secret_password, guardian_email, "African Leadership University")
                        print(add_student)
                        break
                elif operation.lower() == "read":
                    try:
                        get_student = Student.objects.get(
                            first_name=first_name.capitalize(),
                            middle_name=middle_name.capitalize(),
                            last_name=last_name.capitalize(),
                        )
                    except Exception as e:
                        print("\nThis error occured: {0}.".format(e))
                        message = "follow the instructions again after seeing the error"
                        print(message)
                        outcome = input("Do you still want to perform {0} operation on that student yes or no: ".format(operation))
                        if outcome.lower() == "yes":
                            continue
                        else:
                            break
                    else:
                        print(get_student)
                        break
                else:
                    try:
                        delete_student = Student.objects.filter(
                            first_name=first_name.capitalize(),
                            middle_name=middle_name.capitalize(),
                            last_name=last_name.capitalize(),
                        ).delete()
                    except Exception as e:
                        print("\nThis error occured: {0}.".format(e))
                        message = "follow the instructions again after seeing the error"
                        print(message)
                        outcome = input("Do you still want to perform {0} operation on that student yes or no: ".format(operation))
                        if outcome.lower() == "yes":
                            continue
                        else:
                            break
                    else:
                        print(delete_student)
                        break
            outcome = input("Do you want to do another operation on a student again yes or no? ")
            if outcome.lower() == "yes":
                continue
            else:
                break
    return
