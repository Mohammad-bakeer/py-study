from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()
browser.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on.
cookie = browser.find_element(By.ID,"cookie")

#Get upgrade item ids.
items = browser.find_elements(By.CSS_SELECTOR,"#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 7
five_min = time.time() + 60*10 # 10minutes

while True:
    cookie.click()

    #Every 7 seconds:
    if time.time() > timeout:

        #Get all upgrade <b> tags
        all_prices = browser.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        #Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        
        #Get current cookie count
        money_element = browser.find_element(By.ID,"money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        try:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
            browser.find_element(By.ID,to_purchase_id).click()
                
        except ValueError:
            pass
        
        #Add another 5 seconds until the next check
        timeout = time.time() + 10

    #After 10 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = browser.find_element(By.ID,"cps").text
        print(cookie_per_s)
        break

