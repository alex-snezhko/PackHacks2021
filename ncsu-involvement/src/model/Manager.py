import json
from Organization import Organization
from User import User

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
        # Save the users and organizations in plain text as JSON
        pass

    def load_users(self):
        with open("users.json", "r") as myfile:
            data = myfile.read()

        user_array = json.loads(data)
        users = []

        for user in user_array:
            users.append(User(user["username"], user["password"]))

        return users

    def load_organizations(self):
        with open("clubs.json", "r") as myfile:
            data = myfile.read()

        orgs = json.loads(data)

        organizations = []

        for org in orgs:
            organizations.append(Organization(org["name"], org["desc"]))

        return organizations

    def load_events(self):
        return []

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

    def getEventById(self, eventid):
        for event in self.events:
            if event.eventid == eventid:
                    return event
        return None

