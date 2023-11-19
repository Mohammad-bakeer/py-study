from selenium import webdriver
from selenium.webdriver.common.by import By  



browser = webdriver.Chrome()
browser.get("https://www.python.org/")

event_times = browser.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = browser.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name":event_names[n].text
    }
print(events)

browser.quit() 