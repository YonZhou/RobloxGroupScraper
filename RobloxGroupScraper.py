from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

membersList = []
membersLinkList = []
running = True

browser = webdriver.Chrome()
browser.get("https://www.roblox.com/groups/group.aspx?gid=7013")

def updatePage():
    global src
    src = BeautifulSoup(browser.page_source,"html.parser")

updatePage()

WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, 'GroupsPeople_Members')))
browser.find_element_by_id('GroupsPeople_Members').click()

#todo: create an outer loop to scroll through each option on drop-down(start from here)

select = Select(browser.find_element_by_id('ctl00_cphRoblox_rbxGroupRoleSetMembersPane_dlRolesetList'))

numRoles = len(select.options)

for countRoles in range(0,numRoles):

    select = Select(browser.find_element_by_id('ctl00_cphRoblox_rbxGroupRoleSetMembersPane_dlRolesetList'))

    select.select_by_index(countRoles)

    time.sleep(2) #change this to wait until new appears such as wait for index to update? idk

    updatePage()

    if src.find("div",attrs={"class":"paging_pagenums_container"}):
        pageNums = int(src.find("div",attrs={"class":"paging_pagenums_container"}).text) # add fix for no page nums(1 page, error is nontype)
    else:
        pageNums = 1

    for i in range(1,pageNums+1):
        #pageEnter = browser.find_element_by_id('ctl00_cphRoblox_rbxGroupRoleSetMembersPane_dlUsers_Footer')
        #pageEnter.click()
        print(pageNums)
        if pageNums != 1:
            WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, 'ctl00_cphRoblox_rbxGroupRoleSetMembersPane_dlUsers_Footer_ctl01_PageTextBox')))
            pageEnter = browser.find_element_by_id('ctl00_cphRoblox_rbxGroupRoleSetMembersPane_dlUsers_Footer_ctl01_PageTextBox')
            pageEnter.clear()
            pageEnter.send_keys(str(i))
            pageEnter.send_keys(Keys.RETURN)

        temp = []
        while len(temp) < 1:
            updatePage()
            temp = src.findAll("div",attrs={"class":"GroupMember"})
            print (len(temp))

        temp.clear()

        membersClass = src.findAll("div",attrs={"class":"GroupMember"})

        for member in membersClass:
            membersList.append(member.text.strip())

        for member in membersClass:
            membersLinkList.append(member.find('a').attrs['href']) #find href in a type

browser.close()

exportFile = open('exportMembers.txt', 'w')
exportLinks = open('exportLinks.txt', 'w')

for entity in membersList:
    exportFile.write("%s\n" % entity)
for entity in membersLinkList:
    exportLinks.write("%s\n" % entity)

exportFile.close()
print(membersList)
print(membersLinkList)
print(len(membersList))
print(len(membersLinkList))
    
