from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

login_steam = input("Введіть коректний логін Steam: ")
passw_steam = input("Введіть коректний пароль Steam: ")

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
#print(dir(webdriver))
driver.get("http://store.steampowered.com")
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global_action_menu"]/a'))).send_keys(Keys.ENTER)
login = wait.until(EC.element_to_be_clickable((By.ID, 'input_username'))).send_keys(login_steam)
passwd = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_password"]'))).send_keys(passw_steam)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_btn_signin"]/button'))).send_keys(Keys.ENTER)

# driver.find_element(By.XPATH, '//*[@id="global_action_menu"]/a').send_keys(Keys.ENTER)

