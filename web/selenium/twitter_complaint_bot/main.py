import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
load_dotenv()

DWS = 350
UPS = 150
X_EMAIL = os.getenv("X_EM")
X_PASSWORD = os.getenv("X_PS")
X_URL = "https://twitter.com/i/flow/login"
SP_TEST_URL = "https://www.speedtest.net/"
USER_NAME = os.getenv("USR")
class InternetSpeedXBot:
    def __init__(self):
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        test_page = webdriver.Chrome()
        test_page.get(SP_TEST_URL)
        #right now while testing this code,I am in low internet speed area, because of that its 60, later will be changed to 10 or less (needs testing)
        time.sleep(60)
        #used x-path the first time but it didnt work for somereason 
        go_button = test_page.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        time.sleep(90)
        
        self.dws = test_page.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        
        self.ups = test_page.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        
        print(self.dws, self.ups)

    def tweet_at_provider(self):
        page = webdriver.Chrome()
        page.get(X_URL)
        time.sleep(20)
        
        email = page.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(X_EMAIL)
        
        next_button = page.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(5)
        
        user_name = page.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        user_name.send_keys(USER_NAME)
        
        time.sleep(3)
        next_button_2 = page.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        next_button_2.click()
        time.sleep(5)

        pass_input = page.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_input.send_keys(X_PASSWORD)
        time.sleep(3)

        login_button = page.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_button.click()

        time.sleep(20)
        
        tweet_input = page.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div')
        #not sending test results or complaint
        tweet_input.send_keys("Helloo")
        time.sleep(10)

        post_button = page.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]')
        post_button.click()


        time.sleep(15)

        page.quit()



bot = InternetSpeedXBot()
bot.tweet_at_provider()
