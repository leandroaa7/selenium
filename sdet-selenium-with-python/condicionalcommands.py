# -*- coding: utf-8 -*-
# Vídeo 5/45 Selenium with Python Tutorial 5-WebDriver Conditional Commands
''' 
Agenda
Condicional Commands
-is_displayed()
-is_enabled()
-is_selected()

caso não apareça os atributos das classes no VSCode basta clicar ctrl + shift + p 
e digigar python interpreter para selecionar o interpretador
 '''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://newtours.demoaut.com/")

user_ele = driver.find_element_by_name('userName')

#retorna true/false se o elemento está sendo exibido para o usuário
print(user_ele.is_displayed())

#retorna true/false se o elemento está habilitado
print(user_ele.is_enabled())

password_ele = driver.find_element_by_name('password')

print(password_ele.is_displayed())
print(password_ele.is_enabled())

#envia o texto "mercury para o elemento"
user_ele.send_keys("mercury")
password_ele.send_keys("mercury")

driver.find_element_by_name("login").click()

#existe dois radio buttons, o comando abaixo busca o radio pelo seu valor
#já que o name é similar 
roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")

#retorna true/false caso o elemento esteja selecionado
print("status of round trip radio button",roundtrip_radio.is_selected())

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")

print("status of oneway radio button",onetrip_radio.is_selected())


