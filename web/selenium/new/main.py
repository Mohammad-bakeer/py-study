import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from dotenv import load_dotenv, dotenv_values
from selenium.webdriver.common.by import By  # Import the By class
load_dotenv()




# Save and load cookies


driver = webdriver.Chrome()


driver.get("https://www.google.com")
x =driver.find_element(By.CLASS_NAME, "gb_E")
print(x.text)


driver.close()