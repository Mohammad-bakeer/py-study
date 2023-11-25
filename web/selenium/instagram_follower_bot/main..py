import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
load_dotenv()


I_EMAIL = os.getenv("I_EM")
I_PASSWORD = os.getenv("I_PS")
URL = "https://www.instagram.com/"

i_page = webdriver.Chrome()
i_page.get(URL)

time.sleep(5)
username_input = i_page.find_element(By.CSS_SELECTOR, 'input[name="username"]')
username_input.send_keys(I_EMAIL)

password_input = i_page.find_element(By.CSS_SELECTOR, 'input[name="password"]')
password_input.send_keys(I_PASSWORD)

login_button = i_page.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_button.click()
time.sleep(12)

not_now_button = i_page.find_element(By.CSS_SELECTOR, 'div.x1i10hfl[role="button"][tabindex="0"]')
not_now_button.click()

not_now_button = i_page.find_element(By.CSS_SELECTOR, 'button._a9--._ap36._a9_1[tabindex="0"]')
not_now_button.click()
time.sleep(10)

span_element = i_page.find_element(By.CSS_SELECTOR, 'span._ap3a._aaco._aacw._aacx._aad7._aade')
span_element.click()

time.sleep(7)
link_element = i_page.find_element(By.CSS_SELECTOR, 'a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd[role="link"][tabindex="0"]')
link_element.click()

time.sleep(5)

follower_element = i_page.find_element(By.CSS_SELECTOR, 'div._aano')
for i in range(10):
    
    all_buttons = i_page.find_elements(By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-._ap30')
    for button in all_buttons:
        try:
            time.sleep(2)
            button.click()
            time.sleep(1)
        except ElementClickInterceptedException:
            cancel_button = i_page.find_element(By.CSS_SELECTOR, 'button._a9--._ap36._a9_1[tabindex="0"]')
            cancel_button.click()

    i_page.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_element)

    time.sleep(5)





time.sleep(500)
i_page.quit()


"""

login_link = i_page.find_element(By.CSS_SELECTOR, 'a.x1i10hfl[href*="/accounts/login/?next=https%3A%2F%2Fwww.instagram.com%2Ftotal_devops%2F"]')

login_link.click()
time.sleep(5)

#search_link = i_page.find_element(By.CSS_SELECTOR, 'a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz')
#search_link.click()

"""