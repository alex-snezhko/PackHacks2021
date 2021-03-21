import Organization
from datetime import datetime

BASE_LINK = "getinvolved.ncsu.edu/events/"

class Event:

    def __init__(self, name, description, time, location, link, imglink):
        self.name = name
        self.description = description
        self.time = time
        self.location = location
        self.link = link
        self.imglink = imglink

    # def getlink(self):
    #     return BASE_LINK + self.eventid