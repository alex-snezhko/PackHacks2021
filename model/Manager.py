import json
from Organization import Organization
from User import User
from Event import Event

class Manager:

    def __init__(self):
        self.users = self.load_users()
        self.organizations = self.load_organizations()
        self.events = self.load_events()

    def login(self, username, password):
        for user in self.users:
            if user.name == username and user.password == password:
                return user
        return None

    def save(self):
        # TODO Save the users and organizations in database
        pass

    def load_users(self):
        # TODO fetch list of all users from database
        # with open("users.json", "r") as myfile:
        #     data = myfile.read()
        # user_array = json.loads(data)
        user_array = [{'username': 'avs', 'password': '1234'}]
        
        users = []

        for user in user_array:
            users.append(User(user["username"], user["password"]))

        return users

    def load_organizations(self):
        with open("../clubs.json", "r") as myfile:
            data = myfile.read()
        orgs = json.loads(data)

        organizations = []

        for org in orgs:
            organizations.append(Organization(org["name"], org["desc"], org['link'], org['img']))

        return organizations

    def load_events(self):
        with open("../events.json", "r") as myfile:
            data = myfile.read()
        es = json.loads(data)

        events = []

        for event in es:
            events.append(Event(event["name"], event["desc"], event['time'], event['loc'], event['link'], event['img']))

        return events

    def getUserByName(self, username):
        for user in self.users:
            if user.name == username:
                return user
        return None

    def getOrgByName(self, name):
        for organization in self.organizations:
            if organization.name == name:
                return organization
        return None

    def getEventByName(self, name):
        for event in self.events:
            if event.name == name:
                return event
        return None

