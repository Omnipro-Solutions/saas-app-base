import requests
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from omni_pro_base.models.users import User


class SettingsBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username=None, password=None):
        login_valid = settings.ADMIN_LOGIN == username
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=settings.ADMIN_USERNAME)
                user.email = settings.ADMIN_LOGIN
                user.first_name = settings.ADMIN_FIRST_NAME
                user.last_name = settings.ADMIN_LAST_NAME
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class AppUserBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        try:
            response = requests.post(
                settings.AUTH_APP_SERVICE_URL,
                json={"email": username, "password": password},
            )
            response.raise_for_status()
            response_data = response.json()
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            user_data = response_data["user"]
            user = User(username=user_data["username"])
            user.email = user_data["email"]
            user.first_name = user_data["first_name"]
            user.last_name = user_data["last_name"]
            user.is_staff = user_data["is_staff"]
            user.is_superuser = user_data["is_superuser"]
            user.is_active = user_data["is_active"]
            user.save()
        except Exception:
            return None
        return user

    def get_user(self, user_id: int):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
