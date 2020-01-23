from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#inicia uma nova instância do firefox
driver = webdriver.Firefox() 
#realiza uma requisição HTTP do tipo GET, pelo firefox
driver.get("http://www.python.org") 

#verifica se no título da requisição contém "Python"
assert "Python" in driver.title

#busca um elemento pelo nome
elem = driver.find_element_by_name("q")

elem.clear()

#envia comando do teclado
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
driver.close()