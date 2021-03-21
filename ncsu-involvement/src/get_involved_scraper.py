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

options = wd.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = wd.Chrome(executable_path = "C:/Users/selen/chromedriver/chromedriver.exe", options = options)

base_url = "https://getinvolved.ncsu.edu/organizations?categories=11563"

academic_code = 11563
advocacy_code = 11564
ambassador_code = 11565
college_code = 11566
frat_code = 11567
global_code = 11568
religious_code = 11570
service_code = 11571
social_code = 11572
sports_code = 11573
student_code = 11575
sustainability_code = 12744
technology_code = 11576
visual_code = 11577
wellness_code = 11578

driver.get(base_url)
time.sleep(1)

load_more_button = driver.find_element_by_xpath("//button[@tabindex='0' and @type='button']")
load_more_button.click()

# database = []
# for i in range(328):
#     print()
#     print("current: ", i)
#     print()

#     load_more_button = driver.find_element_by_xpath("//button[@tabindex='0' and @type='button']")
#     try:
#         time.sleep(1)
#         load_more_button.click()
#     except nsee:
#         done = True
#         driver.close()
#         sys.exit("\tDONE")

    # if i != 0:
    #     with open('imgs.txt', 'r') as infile:
    #         database = infile.readlines()

    # database.append(img)

    # with open('imgs.txt', 'w') as outfile:
    #     for j in range(len(database)):
    #         outfile.write(database[j])
    #     outfile.write("\n")

# Incrementally saves club photos
# print("Saving photos...")
# database = []
# for i in range(0, 750):
#     print()
#     print("current: ", i)
#     print()

#     driver.get(base_url + links[i])
#     img = ""
#     try: 
#         img = driver.find_element_by_xpath("//h1/preceding-sibling::img").get_attribute('src')
#         # img = driver.find_element_by_tag_name('img').get_attribute('src')
#     except nsee:
#         img = ""

#     if i != 0:
#         with open('imgs.txt', 'r') as infile:
#             database = infile.readlines()

#     database.append(img)

#     with open('imgs.txt', 'w') as outfile:
#         for j in range(len(database)):
#             outfile.write(database[j])
#         outfile.write("\n")
