# Generated by Django 4.2.7 on 2024-06-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academic_feedback_sys", "0003_alter_student_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
