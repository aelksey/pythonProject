import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url ="https://resh.edu.ru/"
os.environ['PATH'] += r"C:\Users\IT-1\PycharmProjects\pythonProject\webdriver"
driver = webdriver.Edge()
driver.get(url)
#//*[@id="username"]
#//*[@id="password"]
#//*[@id="login"]/button
#//*[@id="content"]/div/a

driver.find_element_by_class_name("header__submenu _clickable d-tc").click()
driver.find_element_by_class_name("fs-subj__grid").click()

#while True:
#    driver.find_element_by_xpath('//*[@id="username"]').send_keys("tomsmith")
#    driver.find_element_by_xpath('//*[@id="password"]').send_keys("SuperSecretPassword!")
#    driver.find_element_by_xpath('//*[@id="login"]/button').click()
#    driver.find_element_by_xpath('//*[@id="content"]/div/a').click()