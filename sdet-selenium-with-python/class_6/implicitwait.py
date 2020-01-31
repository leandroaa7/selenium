# -*- coding: utf-8 -*-
# 6/45 Selenium with Python Tutorial 6-WebDriver Implicit wait
'''
Agenda
Waits
-Implicit Wait

Material de apoio
-https://medium.com/@lflucasferreira/entendendo-os-tipos-de-espera-no-selenium-webdriver-2b7adda4db59
-https://medium.com/dev-cave/webdriverwait-fazendo-o-selenium-esperar-a093abeb747b

Espera Implicita
É o tipo de espera do Selenium que aguarda por um tempo determinado,
é indicado quando se trabalha bastante com javascript ou AJAX
Aguardar de forma implícita é, aguardar elementos ou elemento de forma genérica.
'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://newtours.demoaut.com/")

#wait some time here
driver.implicitly_wait(10)

#verificar o título da página 
assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name('userName').send_keys("mercury")
driver.find_element_by_name('password').send_keys("mercury")
driver.find_element_by_name("login").click()


