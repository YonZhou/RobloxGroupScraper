from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

membersList = []
running = True


browser = webdriver.Chrome()
browser.get("https://www.roblox.com/Groups/Group.aspx?gid=3336691")

src = BeautifulSoup(browser.page_source ,"html.parser")
pageNums = src.find("div",attrs={"class":"paging_pagenums_container"}).text

while running:
    browser.find_element_by_id('ctl00_cphRoblox_rbxGroupRoleSetMembersPane_dlUsers_Footer').click()

    membersClass = src.findAll("div",attrs={"class":"GroupMember"})

    for member in membersClass:
        membersList.append(member.text.strip())

    print(membersList)

    running = False

    
