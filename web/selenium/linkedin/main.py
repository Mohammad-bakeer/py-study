import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv, dotenv_values
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

AC_EMAIL = os.getenv("AC_E")
AC_PASSWORD = os.getenv("AC_P")
PHONE = "123456789"

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(AC_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(AC_PASSWORD)
password_field.send_keys(Keys.ENTER)

# code till here is tested and working, but after this its not tested to not disturb the people, but should be working fine, tested some of it alone but without sending applications

all_listings = driver.find_elements(
    By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element(
            By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element(
            By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(
                By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(
                By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(
            By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
