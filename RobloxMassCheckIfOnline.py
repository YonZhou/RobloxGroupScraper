from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

profileLinksList = []
joinableLinks = []

inputLinks = open('exportLinks.txt', 'r')

profileLinksList = inputLinks.read().splitlines()


browser = webdriver.Chrome()

browser.get('https://www.roblox.com/')
browser.find_element_by_id('horizontal-login-username').send_keys('checkonlinexd')
browser.find_element_by_id('horizontal-login-password').send_keys('testing123')
browser.find_element_by_id('horizontal-login-password').send_keys(Keys.RETURN)
WebDriverWait(browser,3).until(EC.presence_of_element_located((By.ID, 'home-avatar-thumb')))

for profile in profileLinksList:
    browser.get(profile)
    WebDriverWait(browser,3).until(EC.presence_of_element_located((By.ID, 'profile-message-btn')))
    src = BeautifulSoup(browser.page_source,"html.parser")
    if src.find("a",attrs={"class":"avatar-status game"}):
        joinableLinks.append(profile)
        print(profile)

browser.close()

exportFile = open('joinableMembers.txt', 'w')
for member in joinableLinks:
    exportFile.write("%s\n" % member)

exportFile.close()

print(joinableLinks)