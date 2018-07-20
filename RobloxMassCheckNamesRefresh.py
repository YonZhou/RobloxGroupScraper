from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException

import time

profileNamesList = []
joinableLinks = []

inputNames = open('exportMembers.txt', 'r')

profileNamesListTemp = inputNames.read().splitlines()

for i in profileNamesListTemp:
    profileNamesList.append(i.split(' ', 1)[0])

print(profileNamesList)


browser = webdriver.Chrome()

browser.get('https://www.roblox.com/')
browser.find_element_by_id('horizontal-login-username').send_keys('checkonlinexd')
browser.find_element_by_id('horizontal-login-password').send_keys('testing123')
browser.find_element_by_id('horizontal-login-password').send_keys(Keys.RETURN)
WebDriverWait(browser,5).until(EC.presence_of_element_located((By.ID, 'home-avatar-thumb')))
browser.get('https://www.roblox.com/search/users?keyword=')
WebDriverWait(browser,3).until(EC.presence_of_element_located((By.ID, 'player-search-page')))


for name in profileNamesList:

    browser.get('https://www.roblox.com/search/users?keyword=' + name)
    #WebDriverWait(browser,3).until(EC.presence_of_element_located((By.CLASS_NAME, 'ng-hide')))
    #browser.find_element_by_xpath('//*[@id="player-search-page"]/div[2]/div[1]/div[1]/div/input').clear()
    #browser.find_element_by_xpath('//*[@id="player-search-page"]/div[2]/div[1]/div[1]/div/input').send_keys(name)
    #browser.find_element_by_xpath('//*[@id="player-search-page"]/div[2]/div[1]/div[1]/div/input').send_keys(Keys.RETURN)

    #time.sleep(3)
    #'//*[@id="player-search-page"]/div[2]/div[2]' xpath for none found

    #WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,',')))

    #WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="player-search-page"]/div[2]/div[1]/div[2]')))

    try: 
        WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="player-search-page"]/div[2]/ul/li[1]/div/div')))
    except TimeoutException:
        pass
    src = BeautifulSoup(browser.page_source,"html.parser")

    if src.find("a",attrs={"class":"text-link text-overflow avatar-status-link ng-binding ng-scope"}):
        joinableLinks.append(name)
        print(name)

browser.close()

exportFile = open('joinableMembers.txt', 'w')
for member in joinableLinks:
    exportFile.write("%s\n" % member)

exportFile.close()

print(joinableLinks)