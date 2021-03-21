# # --------------------------------------------------------------------
# # Get Involved Scraper
# #
# # Scrapes club information from
# # https://getinvolved.ncsu.edu/organizations
# # --------------------------------------------------------------------

# import sys
# import time
# import requests as req
# import json
# import unicodedata as uni
# from bs4 import BeautifulSoup as bs
# from selenium import webdriver as wd
# from selenium.common.exceptions import NoSuchElementException as nsee
# from selenium.common.exceptions import ElementClickInterceptedException as ecie
# from selenium.webdriver.support.ui import WebDriverWait as wait
# from selenium.webdriver.support import expected_conditions as ec

# # Creates a club class
# class Club:
#     def __init__(self, name, desc):
#         self.name = name
#         self.desc = desc

# # Sets base URL
# base_url = "https://getinvolved.ncsu.edu"

# # Sets up the Chrome web driver
# options = wd.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
# driver = wd.Chrome(executable_path = "C:/Users/selen/chromedriver/chromedriver.exe", options = options)
# driver.get(base_url + "/organizations")

# # Uses the web driver to open the get involved site
# html = driver.page_source
# page = bs(html, 'html.parser')
# all_clubs = page.select("a[href*='organization/']")

# # Incrementally saves club information
# current_ten = 0
# for i in range(74):
#     try:
#         print()
#         print("len: ", len(all_clubs))
#         print()

#         # Gets the links to the next 10 clubs that have loaded
#         for j in range(10):
#             start = str(all_clubs[current_ten + j]).find("organization") + len("organization/")
#             end = str(all_clubs[current_ten + j]).find("\" ")
#             link = str(all_clubs[current_ten + j])[start : end]

#             # Uses the web driver to get each club page and scrape information
#             with open('clubs.json', 'w') as out:
#                 driver.get(base_url + "/organization/" + link)

#                 name = uni.normalize("NFKD", driver.find_element_by_xpath("//h1").get_attribute('textContent')).strip()
#                 desc = uni.normalize("NFKD", driver.find_element_by_xpath("//div[@class='bodyText-large userSupplied']").get_attribute('textContent')).replace('\xad', '').replace('\n', "").strip()
                
#                 club = Club(name, desc)
#                 json.dump(vars(club), out)
#                 driver.back()

#         # Loads next 10
#         time.sleep(1)
#         load_more_button = driver.find_element_by_xpath("//button[@tabindex='0' and @type='button']")
#         load_more_button.click()
#         current_ten = current_ten + 10

#         html = driver.page_source
#         page = bs(html, 'html.parser')
#         all_clubs = page.select("a[href*='organization/']")
#     except ecie:
#         driver.close()
#         sys.exit("\tERROR: Couldn't load all clubs")# --------------------------------------------------------------------
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

links = []
with open('links.txt', 'r') as inFile:
    links = inFile.readlines()


database = []
driver = wd.Chrome(executable_path = "C:/Users/selen/chromedriver/chromedriver.exe", options = options)

for i in range(548, 750):
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
