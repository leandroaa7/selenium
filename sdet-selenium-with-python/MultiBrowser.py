# -*- coding: utf-8 -*-
# VÍDEO - Selenium with Python Tutorial 3-WebDriver Commands

'''
Agenda
Basic WebDriver commands
Capture title of the page
Capture URL of the page
Closing & quitting browsers
'''

''' Para entender melhor sobre XPath veja https://www.w3schools.com/xml/xpath_syntax.asp'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#inicia uma nova instância do chrome
#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver = webdriver.Firefox()
driver.get("http://demo.automationtesting.in/Windows.html")

#apresenta na tela o título da página
print(driver.title) 

#apresenta na tela a URL atual
print(driver.current_url)

#buscar elemento pelo xpath e clicar nele
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

#esperar 5 segundos para ir para o próximo comando
time.sleep(5)

#fechar a aba atual
driver.close()

#fechar o navegador
driver.quit()