from locust import between
from locust.exception import StopUser
from UserLib.AbstractUser import AbstractUser
from CommonLib.UserLoader import UserLoader
from CommonLib.UtilHelper import UtilHelper


class RegisteredHttpUser(AbstractUser):
    wait_time = between(1, 2)
    abstract = True

    def verify_login_success(self, response, email):
        if response.status_code != 200 or 'Authentication Failed' in response.text:
            response.failure("Failed to login, user: " + email + " Status code: " + str(response.status_code))
            raise StopUser() # if login fails, skip this user and move on to the next one
        return True

    def on_start(self):
        # Fetch one user, and login, store cookie and user info
        user_obj = UserLoader.get_user()
        form_data = {'email': user_obj['username'], 'passwd':['password'],
                    'back':['my-account'], 'SubmitLogin':''}
        with self.client.post("/index.php?controller=authentication", form_data, headers=UtilHelper.get_base_header(), catch_response=True) as response:
            if self.verify_login_success(response, user_obj['username']):
                #Logger.log_message("Login successful with user : " + user_obj['username'], LogType.INFO)
                super().set_email(user_obj['username']) # comes from AbstractUser.py
                super().set_cookie(response.cookies) # comes from AbstractUser.py

    def on_stop(self):
        pass