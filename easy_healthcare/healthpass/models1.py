from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import datetime

# Create your models here.
class CustomUser(AbstractUser):
    # overwrite the first_name, last_name, and email field
    first_name = models.CharField(max_length=300, blank=False)
    last_name = models.CharField(max_length=300, blank=False)
    email = models.EmailField(blank=False, unique=True)

    # Define groups and user_permissions with unique related_name arguments
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')

# Info utility function
def user_directory_path(instance, filename):
    # file will be uploaded to
    # MEDIA_ROOT/photos/user_<id>/%Y/%m/%d/<filename>
    return "photos/user_{0}/{1}{2}".format(instance.owner.id, filename)

class HbGenotype(models.Model):
    HAEMOGLOBIN_CHOICES = [
        ("AA", "no_haemoglobin_disorder"),
        ("AS", "sickle_cell_trait"),
        ("SS", "sickle_cell_disease"),
        ("SC", "sickle_cell_haemoglobin_c_disease"),
        ("CC", "haemoglobin_c_disease"),
        ("AC", "sickle_cell_mutation"),
    ]
    hb_genotype = models.CharField(
        max_length=2,
        choices=HAEMOGLOBIN_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.hb_genotype)

class SicklingTest(models.Model):
    SICKLING_CHOICES = [
        ("yes", "positive"),
        ("no", "negative"),
    ]
    sickling_test = models.CharField(
        max_length=3,
        choices=SICKLING_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.sickling_test)

class BloodGroup(models.Model):
    BLOOD_GROUP_CHOICES = [
        ("AA", "blood_type_A"),
        ("AO", "blood_type_A+o"),
        ("BB", "blood_type_B"),
        ("BO", "blood_type_B+o"),
        ("AB", "blood_type_AB"),
        ("OO", "blood_type_O"),
    ]
    blood_group = models.CharField(
        max_length=2,
        choices=BLOOD_GROUP_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.blood_group)

class MalariaParasite(models.Model):
    MALARIA_CHOICES = [
        ("yes", "positive"),
        ("no", "negative"),
    ]
    malaria_parasite = models.CharField(
        max_length=3,
        choices=MALARIA_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.malaria_parasite)

class HepatitisA(models.Model):
    HEPATITIS_A_CHOICES = [
        ("yes", "positive"),
        ("no", "negative"),
    ]
    hepatitis_a = models.CharField(
        max_length=3,
        choices=HEPATITIS_A_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.hepatitis_a)

class HepatitisB(models.Model):
    HEPATITIS_B_CHOICES = [
        ("yes", "positive"),
        ("no", "negative"),
    ]
    hepatitis_b = models.CharField(
        max_length=3,
        choices=HEPATITIS_B_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.hepatitis_b)

class HIV(models.Model):
    HIV_CHOICES = [
        ("yes", "positive"),
        ("no", "negative"),
    ]
    hiv = models.CharField(
        max_length=3,
        choices=HIV_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.hiv)

class VDRL(models.Model):
    VDRL_CHOICES = [
        ("yes", "positive"),
        ("no", "negative"),
    ]
    vdrl = models.CharField(
        max_length=3,
        choices=VDRL_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.vdrl)

class HPYLORI(models.Model):
    HPYLORI_CHOICES = [
        ("yes", "positive"),
        ("no", "negative"),
    ]
    hpylori = models.CharField(
        max_length=3,
        choices=HPYLORI_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.hpylori)

class RhesusAntigen(models.Model):
    RH_ANTIGEN_CHOICES = [
        ("A+", "rhesus_positve_a"),
        ("A-", "rhesus_negative_a"),
        ("B+", "rhesus_positive_b"),
        ("B-", "rhesus_negative_b"),
        ("AB+", "rhesus_positive_ab"),
        ("AB-", "rhesus_negative_ab"),
        ("O+", "rhesus_positive_o"),
        ("O-", "rhesus_negative_o"),
    ]
    rhesus_antigen = models.CharField(
        max_length=3,
        choices=RH_ANTIGEN_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.rhesus_antigen)

class BloodWork(models.Model):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="owner_blood_work",
    )
    hb_genotype = models.ForeignKey(
        HbGenotype,
        on_delete=models.SET_NULL,
        null=True,
        related_name="hb_genotype_blood_work",
    )
    sickling_test = models.ForeignKey(
        SicklingTest,
        on_delete=models.SET_NULL,
        null=True,
        related_name="sickling_test_blood_work",
    )
    blood_group = models.ForeignKey(
        BloodGroup,
        on_delete=models.SET_NULL,
        null=True,
        related_name="blood_group_blood_work",
    )
    malaria_parasite = models.ForeignKey(
        MalariaParasite,
        on_delete=models.SET_NULL,
        null=True,
        related_name="malaria_parasite_blood_work",
    )
    hepatitis_a = models.ForeignKey(
        HepatitisA,
        on_delete=models.SET_NULL,
        null=True,
        related_name="hepatitis_a_blood_work",
    )
    hepatitis_b = models.ForeignKey(
        HepatitisB,
        on_delete=models.SET_NULL,
        null=True,
        related_name="hepatitis_b_blood_work",
    )
    hiv = models.ForeignKey(
        HIV,
        on_delete=models.SET_NULL,
        null=True,
        related_name="hiv_blood_work",
    )
    vdrl = models.ForeignKey(
        VDRL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="vdrl_blood_work",
    )
    hpylori = models.ForeignKey(
        HPYLORI,
        on_delete=models.SET_NULL,
        null=True,
        related_name="hpylori_blood_work",
    )
    rhesus_antigen = models.ForeignKey(
        RhesusAntigen,
        on_delete=models.SET_NULL,
        null=True,
        related_name="rhesus_antigen_blood_work",
    )
    blood_work_image_file = models.FileField(
        upload_to=user_directory_path,
    )
