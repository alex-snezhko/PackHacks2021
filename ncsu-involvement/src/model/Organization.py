BASE_LINK = "getinvolved.ncsu.edu/organization/"

class Organization:

    def __init__(self, name, description, category, orgid, email = None, tags = None, events = None):
        self.name = name
        self.description = description
        self.category = category
        self.orgid = orgid
        self.email = email

        self.tags = []
        self.events = []
        if tags != None:
            for interest in tags:
                self.tags.append(interest)
        if events != None:
            for event in events:
                self.events.append(event)

    def getlink(self):
        return BASE_LINK + self.orgid


    