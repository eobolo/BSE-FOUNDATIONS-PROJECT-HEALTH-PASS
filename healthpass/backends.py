from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.backends import BaseBackend
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from .models import CustomUser


# create CustomBackend Class
class CustomBackend(BaseBackend):
    # define the authenticate method
    # takes in username or email
    def authenticate(self, request, username_or_email=None, password=None):
        # get the custom user using username_email
        check_custom_user = CustomUser.objects.filter(
                Q(username=username_or_email) | Q(email=username_or_email)
        ).first()
        if not check_custom_user:
            return None
        # check if the password given in plain text
        # is same with the hashed one of this custom_user
        pwd_valid = check_password(
                password,
                check_custom_user.password,
        )
        if not pwd_valid:
            return None
        return check_custom_user

    # define the get_user to know the user authenticated
    # user can use username or user primary key
    def get_user(self, username_id):
        try:
            return CustomUser.objects.get(
                    Q(id=username_id) | Q(username=username_id)
            )
        except ObjectDoesNotExist:
            return None
