from selenium import webdriver
import sys
import os

username="498612950"
passwd="People123$"

browser = webdriver.Chrome("/usr/local/bin/chromedriver")
browser.get("http://www.sydneytoday.com/login?destination=/")

#browser.implicity_wait(10)


elem=browser.find_element_by_id("tel")
elem.send_keys(username)

elem=browser.find_element_by_id("password")
elem.send_keys(passwd)

elem=browser.find_element_by_id("user-login")
elem.click()

#elem=browser.find_element_by_id("jBox2")
#elem.close()

url="http://www.sydneytoday.com/user/myposts"
browser.get(url)
