from locust import task, SequentialTaskSet
from CommonLib.UtilHelper import UtilHelper
from CommonLib.LogModule import *


class ViewCart(SequentialTaskSet):

    @task
    def get_all_cart_items(self):
        header = UtilHelper.get_base_header_with_cookie(self.user.get_cookie())
        with self.client.get("/index.php?controller=order", headers=header, catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get all cart items, Statuscode: " + str(response.status_code))
                Logger.log_message("Failed to get all cart items", LogType.ERROR)
                
            else:
                if 'Shopping-cart summary' in response.text:
                    response.success()
                else:
                    response.failure("Failed to get all cart items, Text: " + response.text)
                    Logger.log_message("Failed to get all cart items", LogType.ERROR)

    @task
    def exit_navigation(self):
        self.interrupt()