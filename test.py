# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")


a = driver.get_cookies()


# get all cookies in scope of session
print(a)



