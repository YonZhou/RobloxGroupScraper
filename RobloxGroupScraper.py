from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

membersList = []
running = True
i = 1


browser = webdriver.Chrome()
browser.get("https://www.roblox.com/Groups/Group.aspx?gid=3336691")

src = BeautifulSoup(browser.page_source ,"html.parser")
pageNums = int(src.find("div",attrs={"class":"paging_pagenums_container"}).text)

while i <= pageNums:
    #pageEnter = browser.find_element_by_id('ctl00_cphRoblox_rbxGroupRoleSetMembersPane_dlUsers_Footer')
    #pageEnter.click()
    pageEnter = browser.find_element_by_id('ctl00_cphRoblox_rbxGroupRoleSetMembersPane_dlUsers_Footer_ctl01_PageTextBox')
    pageEnter.clear()
    pageEnter.send_keys(str(i))
    pageEnter.send_keys(Keys.RETURN)

    time.sleep(2)

    src = BeautifulSoup(browser.page_source ,"html.parser")
    membersClass = src.findAll("div",attrs={"class":"GroupMember"})

    for member in membersClass:
        membersList.append(member.text.strip())

    i = i + 1

print(membersList)
    
