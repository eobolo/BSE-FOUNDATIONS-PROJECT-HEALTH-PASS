import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Subject(models.Model):
    SUBJECTS = [
        ("MATHS", "Mathematics"),
        ("ENG", "English"),
        ("PHYS", "Physics"),
        ("CHEM", "Chemistry"),
        ("BIOL", "Biology"),
        ("GEOG", "Geography"),
        ("CIVS", "Civics"),
        ("AGRIC", "Agricultural Science"),
        ("ECON", "Economics"),
        ("COMR", "Commerce"),
        ("GOVT", "Government"),
        ("NUTR", "Nutrition"),
        ("RELISTUD", "Religious Studies"),
        ("TECHDRAW", "Technical Drawing"),
        ("LITER", "Literature in English"),
        ("ACCT", "Accounting"),
        ("MKT", "Marketing"),
    ]

    subject = models.CharField(
        max_length=20,
        choices=SUBJECTS,
        unique=True,
    )

    def __str__(self):
        return "<{0}> class, subject name: {1}.".format(
            self.__class__.__name__,
            self.get_subject_display(),
        )

class Teacher(models.Model):
    staff = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="teacher",
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        null=True,
        related_name="teachers",
    )
    def __str__(self):
        return "<{0}> class, names: {1} {2} {3}.".format(
            self.__class__.__name__,
            self.staff.first_name,
            self.staff.last_name,
            self.subject.get_subject_display(),
        )


class Student(models.Model):
    first_name = models.CharField(
        max_length=300,
    )
    middle_name = models.CharField(
        max_length=300,
    )
    last_name = models.CharField(
        max_length=300,
    )
    secret_password = models.UUIDField(
            default=uuid.uuid4,
            editable=False,
    )
    teachers = models.ManyToManyField(
        Teacher,
        related_name="students",
    )

    class Meta:
        permissions = (
            ('edit_student_grade', 'update_student_grade'),
        )

    def __str__(self):
        return "<{0}> class, names: {1} {2} {3}.".format(
            self.__class__.__name__,
            self.first_name,
            self.middle_name,
            self.last_name,
        )

class ClassLevel(models.Model):
    CLASS_LEVEL = [
        ("F4", "Form 4"),
        ("F5", "Form 5"),
        ("F6", "Form 6"),
        ("SS1", "Senior School 1"),
        ("SS2", "Senior School 2"),
        ("SS3", "Senior School 3"),
    ]
    class_level = models.CharField(
        max_length=15,
        choices=CLASS_LEVEL,
        unique=True,
    )

    def __str__(self):
        return "<{0}> class, class_level {1}.".format(
            self.__class__.__name__,
            self.get_class_level_display()
        )

class Score(models.Model):
    SCORES = [(i, str(i)) for i in range(0, 101)]
    score = models.IntegerField(
        choices=SCORES,
        unique=True,
    )

    def __str__(self):
        return "<{0}> class, score: {1}.".format(
            self.__class__.__name__,
            self.score,
        )

class Semester(models.Model):
    SEMESTER = [(i, str(i)) for i in range(1, 4)]
    semester = models.IntegerField(
        choices=SEMESTER,
        unique=True,
    )

    def __str__(self):
        return "<{0}> class, semester {1}.".format(
            self.__class__.__name__,
            self.semester,
        )


class Grade(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="grades",
    )
    class_level = models.ForeignKey(
        ClassLevel,
        on_delete=models.PROTECT,
        null=False,
        related_name="class_grades",
    )
    semester = models.ForeignKey(
        Semester,
        on_delete=models.PROTECT,
        null=False,
        related_name="semester_grades",
    )
    math = models.ForeignKey(
        Subject,
        related_name='math_grades',
        null=False,
        on_delete=models.PROTECT
    )
    math_score = models.ForeignKey(
        Score,
        related_name='math_score',
        null=False,
        on_delete=models.PROTECT
    )
    english = models.ForeignKey(
        Subject,
        related_name='english_grades',
        null=False,
        on_delete=models.PROTECT
    )
    english_score = models.ForeignKey(
        Score,
        related_name='english_score',
        null=False,
        on_delete=models.PROTECT
    )
    physics = models.ForeignKey(
        Subject,
        related_name='physics_grades',
        null=False,
        on_delete=models.PROTECT
    )
    physics_score = models.ForeignKey(
        Score,
        related_name='physics_score',
        null=False,
        on_delete=models.PROTECT
    )
    chemistry = models.ForeignKey(
        Subject,
        related_name='chemistry_grades',
        null=False,
        on_delete=models.PROTECT
    )
    chemistry_score = models.ForeignKey(
        Score,
        related_name='chemistry_score',
        null=False,
        on_delete=models.PROTECT
    )
    biology = models.ForeignKey(
        Subject,
        related_name='biology_grades',
        null=False,
        on_delete=models.PROTECT
    )
    biology_score = models.ForeignKey(
        Score,
        related_name='biology_score',
        null=False,
        on_delete=models.PROTECT
    )
    geography = models.ForeignKey(
        Subject,
        related_name='geography_grades',
        null=False,
        on_delete=models.PROTECT
    )
    geography_score = models.ForeignKey(
        Score,
        related_name='geography_score',
        null=False,
        on_delete=models.PROTECT
    )
    civics = models.ForeignKey(
        Subject,
        related_name='civics_grades',
        null=False,
        on_delete=models.PROTECT
    )
    civics_score = models.ForeignKey(
        Score,
        related_name='civics_score',
        null=False,
        on_delete=models.PROTECT
    )
    agricultural_science = models.ForeignKey(
        Subject,
        related_name='agricultural_science_grades',
        null=False,
        on_delete=models.PROTECT
    )
    agricultural_science_score = models.ForeignKey(
        Score,
        related_name='agricultural_science_score',
        null=False,
        on_delete=models.PROTECT
    )
    economics = models.ForeignKey(
        Subject,
        related_name='economics_grades',
        null=False,
        on_delete=models.PROTECT
    )
    economics_score = models.ForeignKey(
        Score,
        related_name='economics_score',
        null=False,
        on_delete=models.PROTECT
    )
    commerce = models.ForeignKey(
        Subject,
        related_name='commerce_grades',
        null=False,
        on_delete=models.PROTECT
    )
    commerce_score = models.ForeignKey(
        Score,
        related_name='commerce_score',
        null=False,
        on_delete=models.PROTECT
    )
    government = models.ForeignKey(
        Subject,
        related_name='government_grades',
        null=False,
        on_delete=models.PROTECT
    )
    government_score = models.ForeignKey(Score,
        related_name='government_score',
        null=False,
        on_delete=models.PROTECT
    )
    nutrition = models.ForeignKey(
        Subject,
        related_name='nutrition_grades',
        null=False,
        on_delete=models.PROTECT
    )
    nutrition_score = models.ForeignKey(
        Score,
        related_name='nutrition_score',
        null=False,
        on_delete=models.PROTECT
    )
    religious_studies = models.ForeignKey(
        Subject,
        related_name='religious_studies_grades',
        null=False,
        on_delete=models.PROTECT
    )
    religious_studies_score = models.ForeignKey(Score,
        related_name='religious_studies_score',
        null=False,
        on_delete=models.PROTECT
    )
    technical_drawing = models.ForeignKey(Subject,
        related_name='technical_drawing_grades',
        null=False,
        on_delete=models.PROTECT
    )
    technical_drawing_score = models.ForeignKey(Score,
        related_name='technical_drawing_score',
        null=False, 
        on_delete=models.PROTECT
    )
    literature_in_english = models.ForeignKey(Subject,
        related_name='literature_in_english_grades',
        null=False,
        on_delete=models.PROTECT
    )
    literature_in_english_score = models.ForeignKey(
        Score,
        related_name='literature_in_english_score',
        null=False,
        on_delete=models.PROTECT
    )
    accounting = models.ForeignKey(
        Subject,related_name='accounting_grades',
        null=False,
        on_delete=models.PROTECT
    )
    accounting_score = models.ForeignKey(
        Score,
        related_name='accounting_score',
        null=False,
        on_delete=models.PROTECT
    )
    marketing = models.ForeignKey(
        Subject,
        related_name='marketing_grades',
        null=False,
        on_delete=models.PROTECT
    )
    marketing_score = models.ForeignKey(
        Score,
        related_name='marketing_score',
        null=False,
        on_delete=models.PROTECT
    )
    semester_year = models.DateField()
