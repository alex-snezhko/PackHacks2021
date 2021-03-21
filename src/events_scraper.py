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

class Event:
    def __init__(self, name, desc, time, loc, link, img):
        self.name = name
        self.desc = desc
        self.time = time
        self.loc = loc
        self.link = link
        self.img = img

options = wd.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = wd.Chrome(executable_path = "C:/Users/selen/chromedriver/chromedriver.exe", options = options)

links = []
database = []
for i in range(109):
    with open('event_links.txt', 'r') as infile:
        links = infile.readlines()

    links2 = []
    for j in range(len(links)):
        links2.append(links[j].rstrip())
    links = links2

    print("\ncurrent: \n", i, "/", 108, "\n")
    print("\n", links[i], "\n")
    driver.get(links[i])

    name = uni.normalize("NFKD", driver.find_element_by_xpath("//h1[@class='summary']").get_attribute('textContent')).strip()
    try:
        desc = uni.normalize("NFKD", driver.find_element_by_xpath("//div[@class='description']").get_attribute('textContent')).strip()
    except nsee:
        desc = uni.normalize("NFKD", driver.find_element_by_xpath("//p[@class='description']").get_attribute('textContent')).strip()
    time = driver.find_element_by_xpath("//p[@class='dateright']/abbr").get_attribute('textContent').strip()
    try:
        loc = driver.find_element_by_xpath("//p[@class='location']/a").get_attribute('textContent').strip()
    except nsee:
        loc = "Virtual Event"
    try:
        loc = loc + ", " + driver.find_element_by_xpath("//p[@class='location']/span").text
    except nsee:
        loc = loc + ""
    try:
        img = driver.find_element_by_xpath("//img[@class='img_big_square']").get_attribute('src')
    except nsee:
        img = ""

    if i != 0:
        with open('events.json', 'r') as infile:
            database = json.loads(infile.read())

    e = Event(name, desc, time, loc, links[i], img)
    database.append(vars(e))

    with open('events.json', 'w') as outfile:
        outfile.write(json.dumps(database, indent=4))

driver.close()
