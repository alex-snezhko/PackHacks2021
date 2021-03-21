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

# name desc link img

class Club:
    def __init__(self, name, desc, link, img):
        self.name = name
        self.desc = desc
        self.link = link
        self.img = img

options = wd.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = wd.Chrome(executable_path = "C:/Users/selen/chromedriver/chromedriver.exe", options = options)

links = []
with open('links.txt', 'r') as infile:
    links = infile.readlines()

links2 = []
for i in range(len(links)):
    new_link = "https://getinvolved.ncsu.edu/organization/" + links[i]
    links2.append(new_link.rstrip())
links = links2

database = []
for i in range(748, 750):
    print("\ncurrent: \n", i, "/", 749, "\n")
    print("\n", links[i], "\n")
    driver.get(links[i])

    name = uni.normalize("NFKD", driver.find_element_by_xpath("//h1").get_attribute('textContent')).strip()
    desc = uni.normalize("NFKD", driver.find_element_by_xpath("//div[@class='bodyText-large userSupplied']").get_attribute('textContent')).replace('\xad', '').replace('\n', "").strip()
    try: 
        img = driver.find_element_by_xpath("//h1/preceding-sibling::img").get_attribute('src')
    except nsee:
        img = ""
    
    if i != 0:
        with open('clubs3.json', 'r') as infile:
            database = json.loads(infile.read())

    c = Club(name, desc, links[i], img)
    database.append(vars(c))

    with open('clubs3.json', 'w') as outfile:
        outfile.write(json.dumps(database, indent=4))

driver.close()
