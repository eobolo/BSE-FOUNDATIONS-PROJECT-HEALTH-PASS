from academic_feedback_sys.models import Score
from django.core.exceptions import ObjectDoesNotExist

def run(*args):
    # check the length of the array to check for errors
    if not (1 < len(args) < 3):
        print("\nThe number of the command line args is less than 2 or it is greater than 2, it should be 2 after --scripts-args")
        print("<python> <manage.py> <runscript> <filename> <--scripts-args> <create, read, or delete> <score>")
        return
    operation = args[0]
    score = args[1]
    crud_operations = ["create", "read", "delete"]
    if operation.lower() not in crud_operations:
        print("\nfirst argument must be a valid crud operation you gave me {0} as the crud operation :(".format(operation))
        print("These are the crud operations available create, read, and delete. You can only do one at a time.")
        return
    try:
        score = int(score)
    except Exception:
        print("\nThe second argument score must me a number given {0}.".format(score))
        return
    else:
        try:
            if operation.lower() == "create":
                for i in range (1, score + 1):
                    row = Score.objects.create(score=i)
                    print(row)
            elif operation.lower() == "read":
                row_or_rows = Score.objects.get(score=score) 
                print(row_or_rows)
            else:
                rnum_or_rnums = Score.objects.filter(score=score).delete() 
                print("\nThe number of row(s) deleted is {0}.".format(rnum_or_rnums))
        except ObjectDoesNotExist as e:
            print("\nThis error occured: {0}.".format(e))
        except Exception:
            print("\nThis score does not exist in the database.")
