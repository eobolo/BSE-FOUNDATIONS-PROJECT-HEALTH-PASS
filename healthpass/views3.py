from .owners import OWNERCREATEVIEW, OWNERLISTVIEW, OWNERUPDATEVIEW, OWNERDELETEVIEW
from .models import BloodWork, GeneralInfo

# create your views
# blood work
class BloodWorkCreateView(OWNERCREATEVIEW):
    model = BloodWork
    fields = [
        "hb_genotype",
        "sickling_test",
        "blood_group",
        "malaria_parasite",
        "hepatitis_a",
        "hepatitis_b",
        "hiv",
        "vdrl",
        "hpylori",
        "rhesus_antigen",
        "blood_work_image_file",
    ]

class BloodWorkListView(OWNERLISTVIEW):
    model = BloodWork

class BloodWorkUpdateListView(OWNERLISTVIEW):
    model = BloodWork
    template_name = "healthpass/bloodwork_updatelist.html"

class BloodWorkUpdateView(OWNERUPDATEVIEW):
    model = BloodWork
    fields = [
        "hb_genotype",
        "sickling_test",
        "blood_group",
        "malaria_parasite",
        "hepatitis_a",
        "hepatitis_b",
        "hiv",
        "vdrl",
        "hpylori",
        "rhesus_antigen",
        "blood_work_image_file",
    ]

class BloodWorkDeleteListView(OWNERLISTVIEW):
    model = BloodWork
    template_name = "healthpass/bloodwork_deletelist.html"

class BloodWorkDeleteView(OWNERDELETEVIEW):
    model = BloodWork

# general info
class GeneralInfoCreateView(BloodWorkCreateView):
    model = GeneralInfo
    fields = [
        "gender",
        "country",
        "passport_number",
        "date_of_birth",
        "weight",
        "name_of_emergency_contact",
        "relationship",
        "email_of_emergency_contact",
        "phone_number_of_emergency_contact",
        "immunizations",
        "allergies",
    ]

class GeneralInfoListView(BloodWorkListView):
    model = GeneralInfo

class GeneralInfoUpdateListView(BloodWorkUpdateListView):
    model = GeneralInfo
    template_name = "healthpass/generalinfo_updatelist.html"

class GeneralInfoUpdateView(BloodWorkUpdateView):
    model = GeneralInfo
    fields = [
        "gender",
        "country",
        "passport_number",
        "date_of_birth",
        "weight",
        "name_of_emergency_contact",
        "relationship",
        "email_of_emergency_contact",
        "phone_number_of_emergency_contact",
        "immunizations",
        "allergies",
    ]

class GeneralInfoDeleteListView(BloodWorkDeleteListView):
    model = GeneralInfo
    template_name = "healthpass/generalinfo_deletelist.html"

class GeneralInfoDeleteView(BloodWorkDeleteView):
    model = GeneralInfo
