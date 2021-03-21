# BASE_LINK = "getinvolved.ncsu.edu/organization/"

class Organization:

    def __init__(self, name, description, link, img):
        self.name = name
        self.description = description
        self.link = link
        self.img = img
    #     self.category = category
    #     self.orgid = orgid
    #     self.email = email

    #     self.tags = []
    #     self.events = []
    #     if tags != None:
    #         for interest in tags:
    #             self.tags.append(interest)
    #     if events != None:
    #         for event in events:
    #             self.events.append(event)

    # def getlink(self):
    #     return BASE_LINK + self.orgid


    