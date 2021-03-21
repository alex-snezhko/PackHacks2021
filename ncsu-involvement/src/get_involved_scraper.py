# --------------------------------------------------------------------
# Get Involved Scraper
#
# Scrapes club information from
# https://getinvolved.ncsu.edu/organizations
# --------------------------------------------------------------------

import sys
import time
import requests as req
import json
import unicodedata as uni
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.common.exceptions import NoSuchElementException as nsee
from selenium.common.exceptions import ElementClickInterceptedException as ecie
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec

# Sets up the Chrome web driver
options = wd.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = wd.Chrome(executable_path = "C:/Users/selen/chromedriver/chromedriver.exe", options = options)
base_url = "https://getinvolved.ncsu.edu/organization/"

# Creates a club class
class Club:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

# Reads in all links
links = []
with open('links.txt', 'r') as inFile:
    links = inFile.readlines()


# Incrementally saves clubs
database = []
driver = wd.Chrome(executable_path = "C:/Users/selen/chromedriver/chromedriver.exe", options = options)
for i in range(748, 750):
    print()
    print("current: ", i)
    print()

    driver.get(base_url + links[i])
    name = uni.normalize("NFKD", driver.find_element_by_xpath("//h1").get_attribute('textContent')).strip()
    desc = uni.normalize("NFKD", driver.find_element_by_xpath("//div[@class='bodyText-large userSupplied']").get_attribute('textContent')).replace('\xad', '').replace('\n', "").strip()
    club = Club(name, desc)

    if i != 0:
        with open('clubs.json', 'r') as infile:
            database = json.loads(infile.read())

    database.append(vars(club))

    with open('clubs.json', 'w') as outfile:
        outfile.write(json.dumps(database, indent=4))
