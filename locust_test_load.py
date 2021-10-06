from locust import events
from UserLib.RegisteredHttpUser import RegisteredHttpUser
from UserLib.GuestHttpUser import GuestHttpUser
from TaskSetLib.CategoryNavigate import CategoryNavigate
from TaskSetLib.MyAccountNavigate import MyAccountNavigate
from TaskSetLib.ViewCart import ViewCart
from CommonLib.UserLoader import UserLoader
from CommonLib.LogModule import Logger

@events.test_start.add_listener
def on_test_start(**kwargs):
    # print(kwargs['environment'].parsed_options)
    # prints all the arguments passed when running the file
    if kwargs['environment'].parsed_options.logfile:
        Logger.init_logger(__name__, kwargs['environment'].parsed_options.logfile)
    UserLoader.load_users()
    Logger.log_message(".......... Initiating Load Test ..........")

@events.test_stop.add_listener
def on_test_stop(**kwargs):
    Logger.log_message(".......... Load Test Completed ..........")


class UserGroupA(RegisteredHttpUser):
    weight = 4
    RegisteredHttpUser.tasks = [MyAccountNavigate, CategoryNavigate, ViewCart]

class UserGroupB(GuestHttpUser):
    weight = 1
    GuestHttpUser.tasks = [CategoryNavigate, ViewCart]



