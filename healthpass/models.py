from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    # overwrite the first_name, last_name, and email field
    first_name = models.CharField(max_length=300, blank=False)
    last_name = models.CharField(max_length=300, blank=False)
    email = models.EmailField(blank=False, unique=True)

    # Define groups and user_permissions with unique related_name arguments
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')


"""BloodWork and Info utility function"""

def user_directory_path(instance, filename):
    # file will be uploaded to
    # MEDIA_ROOT/photos/user_<id>/%Y/%m/%d/<filename>
    now = datetime.now()
    date_str = now.strftime("%Y/%m/%d")
    return "photos/user_{0}/{1}/{2}".format(instance.owner.id, date_str, filename)

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


"""General Info"""

class Gender(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    gender = models.CharField(
        max_length=5,
        choices=GENDER_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.gender)

class Relationship(models.Model):
    RELATIONSHIP_CHOICES = [
        ("Grandfather", "GF"),
        ("Grandmother", "GM"),
        ("Father", "F"),
        ("Mother", "M"),
        ("Uncle", "U"),
        ("Aunt", "A"),
        ("Son", "S"),
        ("Daughter", "D"),
        ("Grandson", "GS"),
        ("Granddaughter", "GD"),
        ("Brother", "BRO"),
        ("Sister", "SIS"),
        ("Cousin", "C"),
        ("Nephew", "N"),
        ("Niece", "NC"),
    ]
    relationship = models.CharField(
        max_length=50,
        choices=RELATIONSHIP_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.relationship)

class Immunization(models.Model):
    IMMUNIZATION_CHOICES = [
        ("Hepatitis B", "HEPB"),
        ("Diphtheria, Tetanus, and Whooping Cough(Pertussis)", "DTAP"),
        ("Haemophilus Influenzae Type B", "HIB"),
        ("Polio", "IPV"),
        ("Pneumococcal", "PCV"),
        ("Rotavirus", "RV"),
        ("Influenza", "FLU"),
        ("Chickenpox", "VARICELLA"),
        ("Measles, Mumps, Rubella", "MMR"),
        ("Hepatitis A", "HEPA"),
        ("Human Papillomavirus", "HPV"),
        ("Meningococcal Conjugate", "MENACWY"),
        ("Serogroup B Meningococcal", "MENB"),
        ("Pentavalent", "MENABCWY"),
        ("Shingles", "ZOSTER"),
    ]
    immunization = models.CharField(
        max_length=300,
        choices=IMMUNIZATION_CHOICES,
        unique=True,
    )
    
    def __str__(self):
        return "{0}".format(self.immunization)

class Allergy(models.Model):
    ALLERGY_CHOICES = [
        ("Balsam of Peru", "Balsam of Peru"),
        ("Buckwheat", "Buckwheat"),
        ("Celery", "Celery"),
        ("Egg", "Egg"),
        ("Fish", "Fish"),
        ("Fruit", "Fruit"),
        ("Garlic", "Garlic"),
        ("Oats", "Oats"),
        ("Maize", "Maize"),
        ("Milk", "Milk"),
        ("Mustard", "Mustard"),
        ("Peanut", "Peanut"),
        ("Poultry Meat", "Poultry Meat"),
        ("Red Meat", "Red Meat"),
        ("Rice", "Rice"),
        ("Sesame", "Sesame"),
        ("Shellfish", "Shellfish"),
        ("Soy", "Soy"),
        ("Sulfites", "Sulfites"),
        ("Tartrazine", "Tartrazine"),
        ("Tree nut", "Tree nut"),
        ("Wheat", "Wheat"),
        ("Tetracycline", "Tetracycline"),
        ("Dilantin", "Dilantin"),
        ("Tegretol", "Tegretol"),
        ("Penicillin", "Penicillin"),
        ("Cephalosporins", "Cephalosporins"),
        ("Sulfonamides", "Sulfonamides"),
        ("Non-steroidal anti-inflammatories", "Non-steroidal anti-inflammatories"),
        ("Intravenous contrast dye", "Intravenous contrast dye"),
        ("Local anesthetics", "Local anesthetics"),
        ("Pollen", "Pollen"),
        ("Cat", "Cat"),
        ("Dog", "Dog"),
        ("Insect sting", "Insect sting"),
        ("Mold", "Mold"),
        ("Perfume", "Perfume"),
        ("Cosmetics", "Cosmetics"),
        ("Semen", "Semen"),
        ("Latex", "Latex"),
        ("Cold stimuli", "Cold stimuli"),
        ("House dust mite", "House dust mite"),
        ("Nickel", "Nickel"),
        ("Gold", "Gold"),
        ("Chromium", "Chromium"),
        ("Cobalt", "Cobalt"),
        ("Formaldehyde", "Formaldehyde"),
        ("Photographic developers", "Photographic developers"),
        ("Fungicide", "Fungicide"),
        ("Dimethylaminopropylamine", "Dimethylaminopropylamine"),
        ("Latex", "Latex"),
        ("Paraphenylenediamine", "Paraphenylenediamine"),
        ("Glyceryl monothioglycolate", "Glyceryl monothioglycolate"),
        ("Toluenesulfonamide formaldehyde", "Toluenesulfonamide formaldehyde"),
    ]
    allergy = models.CharField(
        max_length=400,
        choices=ALLERGY_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.allergy)

class Country(models.Model):
    COUNTRY_CHOICES = [
        # AFRICA COUNTRIES
        ("Algeria", "DZA"),
        ("Angola", "AGO"),
        ("Benin", "BEN"),
        ("Botswana", "BWA"),
        ("Burkina Faso", "BFA"),
        ("Burundi", "BDI"),
        ("Cameroon", "CMR"),
        ("Cape Verde", "CPV"),
    ]
    country = models.CharField(
        max_length=150,
        choices=COUNTRY_CHOICES,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.country)

class GeneralInfo(models.Model):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="owner_general_info",
    )
    gender = models.ForeignKey(
        Gender,
        on_delete=models.SET_NULL,
        null=True,
        related_name="gender_general_info",
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        related_name="country_general_info",
    )
    passport_number = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(
        help_text="Please use the following format: <em>YYYY-MM-DD</em>."
    )
    weight = models.FloatField(
        null=True,
        blank=True,
        help_text="Please Enter your weight value in float 98.0",
    )
    name_of_emergency_contact = models.CharField(
        max_length=300,
        null=False,
        blank=False,
    )
    relationship = models.ForeignKey(
        Relationship,
        on_delete=models.SET_NULL,
        null=True,
        related_name="relationship_general_info",
    )
    email_of_emergency_contact = models.EmailField(
        null=True,
        blank=True,
    )
    phone_number_of_emergency_contact = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text="Please start your phone number with your country code first",
    )
    immunizations = models.ManyToManyField(
        Immunization,
        related_name="immunization_general_info",
    )
    allergies = models.ManyToManyField(
        Allergy,
        related_name="allergy_general_info",
    )


"""Urinalysis"""

class Color(models.Model):
    COLOR_CHOICES = [
        ("Pale", "Pale"),
        ("Dark Yellow", "Dark Yellow"),
        ("Other", "Other Colors"),
    ]
    color = models.CharField(
        max_length=13,
        choices=COLOR_CHOICES,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.color)

class Appearance(models.Model):
    APPEARANCE_CHOICES = [
        ("Clear", "Clear"),
        ("Hazy", "Hazy"),
        ("Slightly Cloudy", "Slightly Cloudy"),
    ]
    appearance = models.CharField(
        max_length=20,
        choices=APPEARANCE_CHOICES,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.appearance)

class Glucose(models.Model):
    GLUCOSE_CHOICES = [
        ("Negative", "Negative"),
        ("Positive", "Positive"),
    ]
    glucose = models.CharField(
        max_length=12,
        choices=GLUCOSE_CHOICES,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.glucose)

class Bilirubin(models.Model):
    BILIRUBIN_CHOICES = [
        ("Positive", "Positive"),
        ("Negative", "Negative"),
    ]
    bilirubin = models.CharField(
        max_length=12,
        choices=BILIRUBIN_CHOICES,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.bilirubin)

class Ketone(models.Model):
    KETONE_CHOICES = [
        ("Positive", "Positive"),
        ("Negative", "Negative"),
    ]
    ketone = models.CharField(
        max_length=12,
        choices=KETONE_CHOICES,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.ketone)

class Blood(models.Model):
    BLOOD_CHOICES = [
        ("Negative", "Negative"),
        ("Positive", "Positive"),
    ]
    blood = models.CharField(
        max_length=12,
        choices=BLOOD_CHOICES,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.blood)

class Protein(models.Model):
    PROTEIN_CHOICES = [
        ("Negative", "Negative"),
        ("Positive", "Positive"),
    ]
    protein = models.CharField(
        max_length=12,
        choices=PROTEIN_CHOICES,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.protein)

class Nitrite(models.Model):
    NITRITE_CHOICES = [
        ("Positive", "Positive"),
        ("Negative", "Negative"),
    ]
    nitrite = models.CharField(
        max_length=12,
        choices=NITRITE_CHOICES,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.nitrite)

class MicroscopicIndicated(models.Model):
    MICROSCOPIC_CHOICES = [
        ("Negative", "Negative"),
        ("Positive", "Positive"),
    ]
    microscopic_indicated = models.CharField(
        max_length=12,
        choices=MICROSCOPIC_CHOICES,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return "{0}".format(self.microscopic_indicated)

"""Write a simple validator for ph field, urobilinogen, specific gravity"""

def validate_specific_gravity_field(value):
    """
    This is a custom validator to
    validate the range of specific gravity
    values shouldn't be greater than
    1.035 or less than 1.003 if given or
    leave the field empty.
    """
    max_value = 1.035
    min_value = 1.003

    if not (min_value <= value <= max_value):
        raise ValidationError(
            _('The value must be between %(min_value)s and %(max_value)s, or leave the field empty.'),
            params={'min_value': min_value, 'max_value': max_value},
        )

def validate_ph_field(value):
    """
    This is a custom validator to validate
    the ph field the range of this field
    values should be between 5.0 to 8.0
    if given or leave as empty.
    """
    min_value = 5.0
    max_value = 8.0

    if not (min_value <= value <= max_value):
        raise ValidationError(
            _('The value must be between %(min_value)s and %(max_value)s, or leave the field empty.'),
            params={'min_value': min_value, 'max_value': max_value},
        )

def validate_urobilinogen_field(value):
    """
    This is a custom validator to validate
    the urobilinogen field the range of this
    field values should be between 0.1 to 1.0
    if given or leave as empty.
    """
    min_value = 0.1
    max_value = 1.0

    if not (min_value <= value <= max_value):
        raise ValidationError(
            _('The value must be between %(min_value)s and %(max_value)s, or leave the field empty.'),
            params={'min_value': min_value, 'max_value': max_value},
        )

class Urinalysis(models.Model):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="owner_urinalysis",
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.SET_NULL,
        null=True,
        related_name="color_urinalysis",
    )
    appearance = models.ForeignKey(
        Appearance,
        on_delete=models.SET_NULL,
        null=True,
        related_name="appearance_urinalysis",
    )
    glucose = models.ForeignKey(
        Glucose,
        on_delete=models.SET_NULL,
        null=True,
        related_name="glucose_urinalysis",
    )
    bilirubin = models.ForeignKey(
        Bilirubin,
        on_delete=models.SET_NULL,
        null=True,
        related_name="bilirubin_urinalysis",
    )
    ketone = models.ForeignKey(
        Ketone,
        on_delete=models.SET_NULL,
        null=True,
        related_name="ketone_urinalysis",
    )
    blood = models.ForeignKey(
        Blood,
        on_delete=models.SET_NULL,
        null=True,
        related_name="blood_urinalysis",
    )
    protein = models.ForeignKey(
        Protein,
        on_delete=models.SET_NULL,
        null=True,
        related_name="protein_urinalysis",
    )
    nitrite = models.ForeignKey(
        Nitrite,
        on_delete=models.SET_NULL,
        null=True,
        related_name="nitrite_urinalysis",
    )
    microscopic_indicated = models.ForeignKey(
        MicroscopicIndicated,
        on_delete=models.SET_NULL,
        null=True,
        related_name="microscopic_indicated_urinalysis",
    )
    ph = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[validate_ph_field],
        help_text="values in 1 decimal place e.g 1.0, 2.0, 2.5, and so on.",
    )
    specific_gravity = models.DecimalField(
        max_digits=4,
        decimal_places=3,
        null=True,
        blank=True,
        validators=[validate_specific_gravity_field],
        help_text="values in 3 decimal place e.g 0.001, 2.3456, and so on.",
    )
    urobilinogen = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[validate_urobilinogen_field],
        help_text="values in 1 decimal place e.g 2.3, 4.5, and so on.",
    )
