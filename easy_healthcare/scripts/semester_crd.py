from academic_feedback_sys.models import Semester
from django.core.exceptions import ObjectDoesNotExist

def run(*args):
    # check the length of the array to check for errors
    if not (1 < len(args) < 3):
        print("\nThe number of the command line args is less than 2 or it is greater than 2, it should be 2 after --scripts-args")
        print("<python> <manage.py> <runscript> <filename> <--scripts-args> <create, read, or delete> <semester>")
        return
    operation = args[0]
    semester = args[1]
    crud_operations = ["create", "read", "update", "delete"]
    if operation.lower() not in crud_operations:
        print("\nfirst argument must be a valid crud operation you gave me {0} as the crud operation :(".format(operation))
        print("These are the crud operations available create, read, and delete. You can only do one at a time.")
        return
    try:
        semester = int(semester)
    except Exception:
        print("\nThe second argument semester must me a number given {0}.".format(semester))
        return
    else:
        try:
            if operation.lower() == "create":
                row = Semester.objects.create(semester=semester)
                print(row)
            elif operation.lower() == "read":
                row_or_rows = Semester.objects.get(semester=semester) 
                print(row_or_rows)                
            else:
                rnum_or_rnums = Semester.objects.filter(semester=semester).delete()
                print("\nThe number of row(s) deleted is {0}.".format(rnum_or_rnums))
        except ObjectDoesNotExist as e:
            print("\nThis error occured: {0}.".format(e))
        except Exception:
            print("\nThis semester already exist in the database.")
