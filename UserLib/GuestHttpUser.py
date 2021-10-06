from locust import between
from UserLib.AbstractUser import AbstractUser
from CommonLib.UtilHelper import UtilHelper


class GuestHttpUser(AbstractUser):
    wait_time = between(1, 2)
    abstract = True

    def on_start(self):
        with self.client.get("/index.php", headers=UtilHelper.get_base_header(), catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to navigate to Home Page with Guest user, Status code: " + str(response.status_code))
                # Logger
            else:
                super().set_cookie(response.cookies)
                # print(" -- GUEST USER COOKIES -- ")
                # print(UtilHelper.get_base_header_with_cookie(response.cookies))

    def on_stop(self):
        pass
