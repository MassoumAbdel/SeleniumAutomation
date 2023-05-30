# Test Case
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# created the object for chromedriver that talks to chrome browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver = webdriver.Chrome()
print('maximizing the browser window')
driver.maximize_window()
time.sleep(1)

driver.get("https://www.walmart.com/search?q=pc")
all_add_buttons = driver.find_elements(By.XPATH, '//button[@data-automation-id="add-to-cart"]')
# above it returns you the list
all_add_buttons[0].click()
print(all_add_buttons)
print()
time.sleep(10)

driver.get("https://www.walmart.com/search?q=pc")
first_add_button = driver.find_element(By.XPATH,'//div[@data-item-id="5VABX8K9MORO"]//button[@data-automation-id="add-to-cart"]').click()
print('**** first_add_button **** \n', first_add_button)
time.sleep(10)



# CSS Selector vs XPath
all_add_buttons_css = 'button[@data-automation-id=add-to-cart]'
all_add_buttons_xpath = '//button[@data-automation-id="add-to-cart"]'

all_add_id_css = 'button#add-to-cart]'
all_add_id_xpath = '//button[@id="add-to-cart"]'

all_add_class_css = 'button.add-to-cart]'
all_add_class_xpath = '//button[@class="add-to-cart"]'

element_parent__xpath = '//button[@class="add-to-cart"]'