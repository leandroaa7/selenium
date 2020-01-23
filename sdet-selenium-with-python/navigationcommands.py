# -*- coding: utf-8 -*-
# VÍDEO - 4/45 Selenium with Python Tutorial 4-WebDriver Navigational Commands
'''
AGENDA
Navigation commands
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("http://newtours.demoaut.com/")

print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")

time.sleep(5)

print(driver.title)

#retorna para uma página anterior
driver.back()

print(driver.title)

#retorna para uma página posterior
driver.forward()

print(driver.title)

driver.close()