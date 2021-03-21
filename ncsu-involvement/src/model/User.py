import Organization

class User:
    def __init__(self, name, password, majors = None, minors = None, interests = None, organizations = None):
        self.name = name
        self.password = password
        self.majors = []
        self.minors = []
        self.interests = []
        self.organizations = []
        if majors != None:
            for major in majors:
                self.majors.append(major)
        if minors != None:
            for minor in minors:
                self.minors.append(minor)
        if interests != None:
            for interest in interests:
                self.interests.append(interest)
        if organizations != None:
            for organization in organizations:
                self.organizations.append(organization)

    def getRecommendedOrganizations(self):
        # Get recommended organizations based on the selected interests and organizations
        pass

    def getRecommendedEvents(self):
        # Get recommended organizations based on the selected interests and organizations
        pass