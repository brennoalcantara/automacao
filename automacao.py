# # recomendo usar o jupyter para testar o código partes por partes. Se utilizar outra IDE você encontrará um problema que em breve será
# solucionado. O navegador irá fechar sozinho em IDE diferente do Jupyter, ao finalizar a automação.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 


service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)
browser.get("https://m.oglobo.globo.com/ultimas-noticias")
browser.find_element(By.CSS_SELECTOR, '#onesignal-slidedown-cancel-button').click()
browser.find_element(By.CLASS_NAME, 'fechar-modal').click()
browser.find_element(By.CLASS_NAME, 'cookie-banner-lgpd_accept-button').click()
browser.find_element(By.CLASS_NAME, 'burger').click()
browser.get("https://oglobo.globo.com/brasil/")
browser.find_element(By.ID, 'top_search_icon')
