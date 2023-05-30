# Test Case
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Automation Test steps :
print("# Google search manual test (needs to be automated)")
print("# Launch the Chrome browser")

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver = webdriver.Chrome()
print('maximizing the browser window')
driver.maximize_window()
time.sleep(1)

# Sample of different locator:
driver.get('https://demoqa.com/links')
time.sleep(2)
driver.find_element(By.LINK_TEXT, 'Created').click()

time.sleep(5)
print('Clicking the No Content link based on the partial text')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Content').click()
time.sleep(10)

# XPath with text
print(" clicking the Created ...")
created_xpath = '//a[text()="Created"]' # same as this text xpath -> '//a[@id="created"]'
driver.find_element(By.XPATH, created_xpath).click()
time.sleep(5)

print(" clicking the Bad Request ...")
badrequest_xpath = '//a[contains(text(),"Request")]' # same as finds 'Bad Request' link
driver.find_element(By.XPATH, badrequest_xpath).click()
time.sleep(5)

print(" clicking the Unauthorized ...")
unauthorized_xpath = '//a[contains(@id, "unauthor")]'
driver.find_element(By.XPATH, unauthorized_xpath).click()
time.sleep(5)
