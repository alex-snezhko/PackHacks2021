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
        return []

    def load_organizations(self):
        return []

    def load_events(self):
        return []

    def getUserByName(self, username):
        for user in self.users:
            if user.name == username:
                    return user
        return None

    def getOrgById(self, orgid):
        for organization in self.organizations:
            if organization.orgid == orgid:
                    return organization
        return None

    def getEventById(self, eventid):
        for event in self.events:
            if event.eventid == eventid:
                    return event
        return None

