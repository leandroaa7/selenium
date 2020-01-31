# -*- coding: utf-8 -*-
# 7/45 Selenium with Python Tutorial 7-WebDriver Explicit wait
'''
Agenda
Waits
-Explicit Wait

Material de apoio
-https://medium.com/@lflucasferreira/entendendo-os-tipos-de-espera-no-selenium-webdriver-2b7adda4db59
-https://medium.com/dev-cave/webdriverwait-fazendo-o-selenium-esperar-a093abeb747b
-http://www.macoratti.net/vb_xpath.htm
-https://www.w3schools.com/xml/xml_xpath.asp
-https://www.guru99.com/xpath-selenium.html#1

Espera Explícita
a espera explícita diz ao WebDriver para esperar por uma condição para poder continuar os testes

'''

from selenium import webdriver
import time

#modulo para utilizar estratégias de localizador (por id, xpath, name etc)
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()

#espera implicita de 5 segundos
driver.implicitly_wait(5)

#maximiza a janela do navegador
driver.maximize_window()

driver.get('https://www.expedia.com/')

#buscar botão de voos
#driver.find_element_by_id('tab-flight-tab-hp').click()

#outra forma de buscar o botão de voos
driver.find_element(By.ID,"tab-flight-tab-hp").click() #Flights button

#função de espera do python
'''
usar o time.sleep() do python ou Thread.Sleep() do Java não é uma boa prática, pois 
depende do navegador e da máquina
por isso, use o WebDriverWait  
'''
time.sleep(2)

#localizar o elemento de origem do passageiro e digitar o nome
#driver.find_element_by_id('flight-origin-hp-flight').send_keys("SFO") 
driver.find_element(By.ID,'flight-origin-hp-flight').send_keys("SFO")
time.sleep(2)

#localizar o elemento de destino do passageiro e digitar o nome
#driver.find_element_by_id('flight-origin-hp-flight').send_keys("NYC")
driver.find_element(By.ID,'flight-destination-hp-flight').send_keys("NYC")

#limpa o campo 
driver.find_element(By.ID,"flight-departing-hp-flight").clear()
#localizar elemento de data de partida e digitar o valor da data de partida
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("12/10/2020")

#limpa o campo
driver.find_element(By.ID,'flight-returning-hp-flight').clear()
#localizar elemento de data de retorno e digitar o valor da data de retorno
driver.find_element(By.ID,'flight-returning-hp-flight').send_keys("15/10/2020")

#localizar elemento do botão submit pelo XPATH
'''
XPATH é uma sintaxe para definir partes de um arquivo XML
com ele é possível localizar qualquer elemento pelo DOM
'''
button_xpath = "/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[7]/label/button"
driver.find_element(By.XPATH, button_xpath).click() #search

'''
TENTATIVA DO VÍDEO
#explicit wait, o valor 10 é o máximo de tempo suportado
wait = WebDriverWait(driver,10)

input_xpath = "//*[@id='stopFilter_stops-0']"
#espera o elemento até que ele seja clicável
element = wait.until(EC.element_to_be_clickable((By.XPATH,input_xpath)))
#no video funcionou sem o timer.sleep()
time.sleep(3)
element.click()
#driver.quit()
'''

'''
TENTATIVA MAIS ELABORADA
try:
    input_xpath = "//*[@id='stopFilter_stops-0']"
    wait = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,input_xpath))) 
    #nao sei porque mas com dois click funciona!
    wait.click()
    wait.click()
finally:
    driver.quit()
    #pass
'''

