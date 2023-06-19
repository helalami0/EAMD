import discord
from pathlib import Path
import json
from datetime import datetime

class UsersManager():
    # def __init__(self):

    def load_user_data(self):
        script_path = Path(__file__)
        json_path = script_path.parent / 'user_data.json'

        try:
            with open(str(json_path), 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}


    def save_user_data(self, data):
        script_path = Path(__file__)
        json_path = script_path.parent / 'user_data.json'

        with open(str(json_path), 'w') as file:
            json.dump(data, file, indent=4)

    def update_user_data(self, user):
        user_data = self.load_user_data()

        user_name = user.name
        last_connected = str(datetime.now())

        if user_name in user_data:
            user_data[user_name]['last_connected'] = last_connected
        else:
            user_data[user_name] = {
                'last_connected': last_connected,
            }

        self.save_user_data(user_data)

    def get_user_lastconnection(self, user):
        user_data = self.load_user_data()

        user_name = user.name

        if user_name in user_data:
            return user_data[user_name]['last_connected']
        else:
            return False
