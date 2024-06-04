from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout
from django.urls import reverse
from django.utils.http import urlencode
from guardian.models import UserObjectPermission
from .models import Student, ClassLevel, Score, Semester, Grade, Subject
from .forms import ClassLevelForm, SemesterForm, SubjectForm, ScoreForm
import datetime
# Create your views here.

# global utility variables
cookie_time = 60 * 60 * 3
access_denied_error_template = "academic_feedback_sys/no_permission.html"

# global utility functions
def set_view_cookies(view_request):
    login_url = reverse('login') + '?' + urlencode({"next": view_request.path})
    redirect_login_response = redirect(login_url)
    redirect_login_response.set_cookie("session-cookie", "short-cookie")
    redirect_login_response.set_cookie("timed-cookie", "long-cookie", max_age=cookie_time)
    return redirect_login_response

# Custom Error Views
def custom_error_403(request, exception=None):
    return render(request, access_denied_error_template, status=403)

# Teacher Views
@login_required
def TeacherHome(request):
    template_name = "academic_feedback_sys/teacher_home.html"
    # check cookies even though the user is logged in from a previous session
    # if any of the cookie has expired first logout the user.
    # and the redirect to the login page with a next parameter
    # add cookies and return the response
    if not request.COOKIES.get("session-cookie", None) or not request.COOKIES.get("timed-cookie", None):
        logout(request)
        redirect_login_response = set_view_cookies(request)
        return redirect_login_response
    # now check if this user is a staff because some people can create healthpass login
    # and would want to login
    if request.user.is_staff == True:
        # create a context saving the teacher's object
        # can be gotten from request object easily
        # then return a response from the render object
        context_variable = {}
        logged_teacher_obj = request.user
        context_variable["logged_teacher_obj"] = logged_teacher_obj
        return render(request, template_name, context_variable)
    # if the user isn't a staff send the person to a 403 error page
    # TODO later, but for now just pass
    raise PermissionDenied

@login_required
def TeacherProfile(request):
    template_name = "academic_feedback_sys/teacher_profile.html"
    # check cookies even though the user is logged in from a previous session
    # if any of the cookie has expired first logout the user.
    # and the redirect to the login page with a next parameter
    # add cookies and return the response
    if not request.COOKIES.get("session-cookie", None) or not request.COOKIES.get("timed-cookie", None):
        logout(request)
        redirect_login_response = set_view_cookies(request)
        return redirect_login_response
    pass

@login_required
def TeacherStudents(request):
    template_name = "academic_feedback_sys/teacher_students.html"
    # check cookies even though the user is logged in from a previous session
    # if any of the cookie has expired first logout the user.
    # and the redirect to the login page with a next parameter
    # add cookies and return the response
    if not request.COOKIES.get("session-cookie", None) or not request.COOKIES.get("timed-cookie", None):
        logout(request)
        redirect_login_response = set_view_cookies(request)
        return redirect_login_response
    # now check if this user is a staff because some people can create healthpass login
    # and would want to login to this app
    if request.user.is_staff == True:
        # create a context variable to store all students
        # of that class teacher and a id integer list
        # to store the student id's
        id_list = None
        context_variable = {}
        class_teacher = request.user
        # get the class teacher student, based on permission
        # this returns a row of the student(s) that the class
        # teacher as permission to edit their grade
        # but not exactly the students but we have an information
        # we need in those rows i.e the object_pk which is the
        # student primary key i.e id in string
        class_teacher_perm_students = UserObjectPermission.objects.filter(user=class_teacher).all()
        # extract all ids in strings and convert to integers
        # using list comprehension
        id_list = [int(row.object_pk) for row in class_teacher_perm_students]
        # then get all student objects now using this id list
        class_teacher_students = Student.objects.filter(id__in=id_list)
        # now I have all student we can now store it in the context variable
        # and also store class teacher object
        context_variable["class_teacher"] = class_teacher
        context_variable['students'] = class_teacher_students
        return render(request, template_name, context_variable)
    raise PermissionDenied

@login_required
def TeacherRecentGraded(request):
    pass

@login_required
def TeacherEditStudentGrade(request, first_name, middle_name, last_name):
    template_name = "academic_feedback_sys/teacher_edit_student_grade.html"
    error_template = "academic_feedback_sys/no_edit_permission.html"
    if request.method == "GET":
        # check cookies even though the user is logged in from a previous session
        # if any of the cookie has expired first logout the user.
        # and the redirect to the login page with a next parameter
        # add cookies and return the response
        if not request.COOKIES.get("session-cookie", None) or not request.COOKIES.get("timed-cookie", None):
            logout(request)
            redirect_login_response = set_view_cookies(request)
            return redirect_login_response
        # now check if this user is a staff because some people can create healthpass login
        # and would want to login
        if request.user.is_staff == True:
            # Take the first_name, middle_name, and last_name to get the student
            # object clicked on, then first check if the student exists
            clicked_student_exists = Student.objects.filter(
                first_name=first_name.capitalize(),
                middle_name=middle_name.capitalize(),
                last_name=last_name.capitalize(),
            ).exists()
            if not clicked_student_exists:
                raise PermissionDenied
            
            clicked_student = Student.objects.filter(
                first_name=first_name.capitalize(),
                middle_name=middle_name.capitalize(),
                last_name=last_name.capitalize(),
            ).first()
            # Get the loggedin User
            loggedin_user = request.user
            # now check if the loggedin user has permission to edit
            # student grade as the class teacher of that student
            if not loggedin_user.has_perm("edit_student_grade", clicked_student):
                return render(request, error_template)
            # since user has the permission to edit student grade
            # we have to create a context variable to take the first_name,
            # middle_name, last_name, then classlevel, semester, subject, and
            # score modelform object to put in our form.
            # we need to automate this stuff
            # first let us get a list of the subjects
            all_subjects = ["Mathematics", "English", "Physics", "Chemistry", "Biology", "Geography", "Civics", "Agricultural Science", "Economics", "Commerce", "Government", "Nutrition", "Religious Studies", "Technical Drawing", "Literature in English", "Accounting", "Marketing"]
            all_subjects_length = len(all_subjects)

            # get the classlevel, semester, score, and subject modelform object
            class_level_form = ClassLevelForm()
            semester_form = SemesterForm()
            subject_form = SubjectForm()
            score_form = ScoreForm()

            # create a context to take first_name, middle_name, last_name
            context_variable = {}
            context_variable["first_name"] = first_name.capitalize()
            context_variable["middle_name"] = middle_name.capitalize()
            context_variable["last_name"] = last_name.capitalize()

            # then do dict comphrehension to get a dictionary of subject name and their subject object
            # and also subject score name and score object
            subjects = {all_subjects[i]: subject_form for i in range(0, all_subjects_length)}
            scores = {all_subjects[i]: score_form for i in range(0, all_subjects_length)}

            # then store these subjects and scores in context variabel along with class_level_form
            # object and semester_form object
            context_variable["subjects"] = subjects
            context_variable["scores"] = scores
            context_variable["class_level_form"] = class_level_form
            context_variable["semester_form"] = semester_form

            # check for session message
            if request.session.get("success_message", None):
                context_variable["success_message"] = request.session.get("success_message")
                del request.session["success_message"]
            return render(request, template_name, context_variable)
        raise PermissionDenied
    
    if request.method == "POST":
        # check if the student exists again and if the loggedinUser has
        # permission to still edit grade
        # Take the first_name, middle_name, and last_name to get the student
        # object clicked on, then first check if the student exists
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        clicked_student_exists = Student.objects.filter(
            first_name=first_name.capitalize(),
            middle_name=middle_name.capitalize(),
            last_name=last_name.capitalize(),
        ).exists()
        if not clicked_student_exists:
            raise PermissionDenied
        clicked_student = Student.objects.filter(
            first_name=first_name.capitalize(),
            middle_name=middle_name.capitalize(),
            last_name=last_name.capitalize(),
        ).first()
        # Get the loggedin User
        loggedin_user = request.user
        # now check if the loggedin user has permission to edit
        # student grade as the class teacher of that student
        if not loggedin_user.has_perm("edit_student_grade", clicked_student):
            return render(request, error_template)
        # get class level and semester values to get their corresponding objects
        class_level = request.POST.get('class_level')
        semester = request.POST.get('semester')
        class_level_obj = ClassLevel.objects.filter(class_level=class_level).first()
        semester_obj = Semester.objects.filter(semester=semester).first()
        # get the scores and subect list using .getlist() method
        subject_list = request.POST.getlist("subject")
        score_list = request.POST.getlist("score")
        # convert both subject list to set to see if a subject was repeated
        # then this is an error then render the form back with an error message
        subject_set = set(subject_list)

        if len(subject_list) != len(subject_set):
            all_subjects = ["Mathematics", "English", "Physics", "Chemistry", "Biology", "Geography", "Civics", "Agricultural Science", "Economics", "Commerce", "Government", "Nutrition", "Religious Studies", "Technical Drawing", "Literature in English", "Accounting", "Marketing"]
            all_subjects_length = len(all_subjects)

            # get the classlevel, semester, score, and subject modelform object
            class_level_form = ClassLevelForm()
            semester_form = SemesterForm()
            subject_form = SubjectForm()
            score_form = ScoreForm()

            # create a context to take first_name, middle_name, last_name
            context_variable = {}
            context_variable["first_name"] = first_name.capitalize()
            context_variable["middle_name"] = middle_name.capitalize()
            context_variable["last_name"] = last_name.capitalize()

            # then do dict comphrehension to get a dictionary of subject name and their subject object
            # and also subject score name and score object
            subjects = {all_subjects[i]: subject_form for i in range(0, all_subjects_length)}
            scores = {all_subjects[i]: score_form for i in range(0, all_subjects_length)}

            # then store these subjects and scores in context variabel along with class_level_form
            # object and semester_form object
            context_variable["subjects"] = subjects
            context_variable["scores"] = scores
            context_variable["class_level_form"] = class_level_form
            context_variable["semester_form"] = semester_form
            context_variable["duplicate_subject_error"] = "You selected a Subject more than once please correctly select the subjects."

            return render(request, template_name, context_variable)
        
        subjects_dict = {f"{subject_list[i]}": Subject.objects.filter(subject=subject_list[i]).first() for i in range(0, len(subject_list))}
        scores_dict = {f"{subject_list[i]}": Score.objects.filter(score=int(score_list[i])).first() for i in range(0, len(score_list))}

        # now it is time to create the grade using the Grade class
        Grade.objects.create(
            student=clicked_student,
            class_level=class_level_obj,
            semester=semester_obj,
            math=subjects_dict["MATHS"],
            math_score=scores_dict["MATHS"],
            english=subjects_dict["ENG"],
            english_score=scores_dict["ENG"],
            physics=subjects_dict["PHYS"],
            physics_score=scores_dict["PHYS"],
            chemistry=subjects_dict["CHEM"],
            chemistry_score=scores_dict["CHEM"],
            biology=subjects_dict["BIOL"],
            biology_score=scores_dict["BIOL"],
            geography=subjects_dict["GEOG"],
            geography_score=scores_dict["GEOG"],
            civics=subjects_dict["CIVS"],
            civics_score=scores_dict["CIVS"],
            agricultural_science=subjects_dict["AGRIC"],
            agricultural_science_score=scores_dict["AGRIC"],
            economics=subjects_dict["ECON"],
            economics_score=scores_dict["ECON"],
            commerce=subjects_dict["COMR"],
            commerce_score=scores_dict["COMR"],
            government=subjects_dict["GOVT"],
            government_score=scores_dict["GOVT"],
            nutrition=subjects_dict["NUTR"],
            nutrition_score=scores_dict["NUTR"],
            religious_studies=subjects_dict["RELISTUD"],
            religious_studies_score=scores_dict["RELISTUD"],
            technical_drawing=subjects_dict["TECHDRAW"],
            technical_drawing_score=scores_dict["TECHDRAW"],
            literature_in_english=subjects_dict["LITER"],
            literature_in_english_score=scores_dict["LITER"],
            accounting=subjects_dict["ACCT"],
            accounting_score=scores_dict["ACCT"],
            marketing=subjects_dict["MKT"],
            marketing_score=scores_dict["MKT"],
            semester_year=datetime.date.today(),
        )
        # save a session message saying the grade has been saved
        request.session["success_message"] = f"Student {first_name} {middle_name} {last_name} grade has been saved!!!"
        return redirect(request.path)

