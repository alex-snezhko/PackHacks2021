import json
# from Organization import Organization
# from User import User
# from Event import Event

class Manager:

    def __init__(self):
        self.users = self.load_users()
        self.organizations = self.load_organizations()
        self.events = self.load_events()

    def login(self, username, password):
        # print("Users", self.users)
        for user in self.users:
            if user['username'] == username and user['password'] == password:
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
        user_array = [{'username': 'avs', 'password': '1234', 'department': 'Computer Science', 'interests': ['Technology']}]
        
        users = []

        for user in user_array:
            users.append({'username': user["username"], 'password': user["password"], 'department': user['department'], 'interests': user['interests']})

        return users

    def load_organizations(self):
        with open("clubs.json", "r") as myfile:
            data = myfile.read()
        orgs = json.loads(data)

        organizations = []

        for org in orgs:
            organizations.append({'name': org["name"], 'desc': org["desc"], 'link': org['link'], 'img': org['img']})

        return organizations

    def load_events(self):
        with open("events.json", "r") as myfile:
            data = myfile.read()
        es = json.loads(data)

        events = []

        for event in es:
            events.append({'name': event["name"], 'desc': event["desc"], 'time': event['time'], 'loc': event['loc'], 'link': event['link'], 'img': event['img']})

        return events

    def getUserByName(self, username):
        for user in self.users:
            if user['username'] == username:
                return user
        return None

    def getOrgByName(self, name):
        for organization in self.organizations:
            if organization['name'] == name:
                return organization
        return None

    def getEventByName(self, name):
        for event in self.events:
            if event['name'] == name:
                return event
        return None

