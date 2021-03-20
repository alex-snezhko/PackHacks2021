import Organization
from datetime import datetime

BASE_LINK = "getinvolved.ncsu.edu/events/"

class Event:

    def __init__(self, name, description, organization, starttime, endtime, eventid, location):
        self.name = name
        self.description = description
        self.organization = organization
        self.starttime = starttime
        self.endtime = endtime
        self.eventid = eventid
        self.location = location

    def getlink(self):
        return BASE_LINK + self.eventid