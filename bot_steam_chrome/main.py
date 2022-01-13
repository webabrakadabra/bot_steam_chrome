from selenium import webdriver
from config import *

browser = webdriver.Chrome(path_chrome_browser_driver)
browser.get(start_site_url)
