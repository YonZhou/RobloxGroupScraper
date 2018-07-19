from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

membersList = [[]]
running = True
i = 1

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
#how to select from dropdown: ex) second option: select.select_by_index(1)
select.select_by_index(1)

time.sleep(2) #change this to wait until new appears such as wait for index to update? idk

updatePage()

if src.find("div",attrs={"class":"paging_pagenums_container"}):
    pageNums = int(src.find("div",attrs={"class":"paging_pagenums_container"}).text) # add fix for no page nums(1 page, error is nontype)
else:
    pageNums = 1

while i <= pageNums:
    #pageEnter = browser.find_element_by_id('ctl00_cphRoblox_rbxGroupRoleSetMembersPane_dlUsers_Footer')
    #pageEnter.click()
    #todo: find and update pagenums for each selection, same class and text just need to update(done)
    print(pageNums)
    if pageNums != 1:
        WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, 'ctl00_cphRoblox_rbxGroupRoleSetMembersPane_dlUsers_Footer_ctl01_PageTextBox')))
        pageEnter = browser.find_element_by_id('ctl00_cphRoblox_rbxGroupRoleSetMembersPane_dlUsers_Footer_ctl01_PageTextBox')
        pageEnter.clear()
        pageEnter.send_keys(str(i))
        pageEnter.send_keys(Keys.RETURN)
    #time.sleep(2)
    temp = []
    while len(temp) < 1:
        updatePage()
        temp = src.findAll("div",attrs={"class":"GroupMember"})
        print (len(temp))

    temp.clear()

    membersClass = src.findAll("div",attrs={"class":"GroupMember"})

    for member in membersClass:
        membersList.append(member.text.strip())

    i = i + 1

print(membersList)
print(len(membersList))
    
