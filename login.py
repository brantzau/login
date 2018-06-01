# coding: utf-8
from selenium.webdriver.common.by import By
from selenium import webdriver
import sys
import os

#username="498612950"
#username="498484359"
username="459656262"
#username="459656331"

passwd="People123$"

browser = webdriver.Chrome("/usr/local/bin/chromedriver")
browser.get("http://www.sydneytoday.com/login?destination=/")

browser.implicitly_wait(5)


elem=browser.find_element_by_id("tel")
elem.send_keys(username)

elem=browser.find_element_by_id("password")
elem.send_keys(passwd)

elem=browser.find_element_by_id("user-login")
elem.click()

browser.implicitly_wait(10)
browser.refresh()

url="http://www.sydneytoday.com/user/myposts"
browser.get(url)

browser.implicitly_wait(5)
browser.refresh()

#account-yp > div > div > div:nth-child(1) > div.col-xs-2 > div > a:nth-child(1) > button
#//*[@id="account-yp"]/div/div/div[1]/div[3]/div/a[1]/button

elem=browser.find_element_by_xpath('//*[@id="account-yp"]/div/div/div[1]/div[3]/div/a[1]/button')
elem.click()
browser.implicitly_wait(2)
browser.refresh()

#elem=browser.find_element_by_xpath("//*[@id="account-yp"]/div/div/div[2]/div[3]/div/a[1]/button)
#elem.click()
#browser.implicitly_wait(2)


#elem=browser.find_element_by_xpath("//*[@id="account-yp"]/div/div/div[1]/div[3]/div/a[1]/button")
#elem.click()
#browser.implicitly_wait(2)

#Log off
elem=browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/a[3]")
#button=elem.find_element_by_xpath("//icon-sign-in")
elem.click()

#url="http://www.sydneytoday.com/globals/logout"
#browser.get(url)
#browser.refresh()

#browser.quit()
