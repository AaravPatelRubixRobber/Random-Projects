#USES A WEBDRIVER TO OPEN THE COOKIE CLICKER WEBSITE AND AUTOMATICALLY CLICK FOR COOKIES

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#makes driver stuff
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#goes to CC
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)#waits 5 secs for page to load

#defines variables
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]


#makes action chain
actions = ActionChains(driver)
for i in range(1):
    actions.click(cookie)

while True:
    actions.perform()
    count = int(cookie_count.text.split(' ')[0])
    for item in items:
        i = item.text
        value = int(i)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
    
