from selenium import webdriver
from selenium.webdriver.common.by import By  

browser = webdriver.Chrome()
browser.get("https://en.wikipedia.org/wiki/Main_Page")

num = browser.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(num.text)