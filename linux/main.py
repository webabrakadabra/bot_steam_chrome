from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#wait = WebDriverWait(driver, 10)
driver.maximize_window()
#print(dir(webdriver))
driver.get("https://store.steampowered.com/")
#wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global_action_menu"]/a'))).click()
#//*[@id="global_action_menu"]/a
login = driver.find_elements(By.ID, 'language_dropdown')