# Generated by Django 4.2.7 on 2024-05-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academic_feedback_sys", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
            name="subject",
            field=models.CharField(
                choices=[
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
                ],
                max_length=20,
                unique=True,
            ),
        ),
    ]
