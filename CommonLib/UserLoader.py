import csv
import os


class UserLoader:

    #user_list will contain all the user credentials from user.csv file
    user_list = []
    csv_file_path = os.getcwd() + "/Data/user.csv"

    @staticmethod
    def load_users():
        reader = csv.DictReader(open(UserLoader.csv_file_path))
        for line_elem in reader:
            UserLoader.user_list.append(line_elem)
        print(UserLoader.user_list)

    @staticmethod
    def get_user():
        # If user_list is not loaded
        if len(UserLoader.user_list) < 1:
            UserLoader.load_users()
        user_obj = UserLoader.user_list.pop()
        return user_obj