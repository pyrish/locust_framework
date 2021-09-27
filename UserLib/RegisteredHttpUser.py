from locust import between
from UserLib.AbstractUser import AbstractUser
from CommonLib.UserLoader import UserLoader


class RegisteredHttpUser(AbstractUser):
    wait_time = between(1, 2)
    abstract = True

    def verify_login_success(self, response, email):
        pass

    def on_start(self):
        # Fetch one user, and login, store cookie and user info
        user_obj = UserLoader.get_user()
        print(user_obj)
        print(user_obj['username'])
        print(user_obj['password'])

    def on_stop(self):
        pass