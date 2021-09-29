from locust import events
from UserLib.RegisteredHttpUser import RegisteredHttpUser
from UserLib.GuestHttpUser import GuestHttpUser
from TaskSetLib.CategoryNavigate import CategoryNavigate
from TaskSetLib.MyAccountNavigate import MyAccountNavigate
from TaskSetLib.ViewCart import ViewCart
from CommonLib.UserLoader import UserLoader

@events.test_start.add_listener
def on_test_start(**kwargs):
    UserLoader.load_users()

@events.test_stop.add_listener
def on_test_stop(**kwargs):
    pass


class UserGroupA(RegisteredHttpUser):
    weight = 1
    RegisteredHttpUser.tasks = [MyAccountNavigate, CategoryNavigate, ViewCart]

class UserGroupB(GuestHttpUser):
    weight = 4
    GuestHttpUser.tasks = [CategoryNavigate, ViewCart]



