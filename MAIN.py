from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
Navegador = webdriver.Chrome(service=servico)

#http://10.98.4.40:8080/MicroStrategy/servlet/mstrWeb



