from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.google.com")

search = browser.find_element(By.XPATH, '//*[@id="APjFqb"]')
search.send_keys("Python")
search.send_keys(Keys.ENTER)


browser.quit()