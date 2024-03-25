from .owners import OWNERCREATEVIEW, OWNERLISTVIEW, OWNERUPDATEVIEW, OWNERDELETEVIEW
from .models import BloodWork

# create your views
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
