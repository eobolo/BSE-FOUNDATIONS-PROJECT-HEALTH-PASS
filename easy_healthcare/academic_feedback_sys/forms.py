from django.forms import ModelForm
from .models import ClassLevel, Semester, Subject, Score

class ClassLevelForm(ModelForm):
    class Meta:
        model = ClassLevel
        fields = "__all__"

class SemesterForm(ModelForm):
    class Meta:
        model = Semester
        fields = "__all__"

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = "__all__"