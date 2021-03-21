class User:
    def __init__(self, name, password, department = None, interests = None):
        self.name = name
        self.password = password
        self.department = department
        self.interests = []
        if interests != None:
            for interest in interests:
                self.interests.append(interest)

    def getRecommendedOrganizations(self):
        # TODO Get recommended organizations based on the selected interests and organizations
        pass

    def getRecommendedEvents(self):
        # TODO Get recommended events based on the selected interests and organizations
        pass