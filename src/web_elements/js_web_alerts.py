# Test Case
import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.utilities import disable_google_ads

# Automation Test Steps:
print(" # Google search manual test (needs to be automated)")
print(" # Launch the chrome browser")

# created the object for chromedriver that talks to chrome browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver = webdriver.Chrome()
print('maximizing the browser window')
# driver.maximize_window()
driver.implicitly_wait(5)

# Variables
HOST = "https://demoqa.com/alerts"

# Switching to frame and back to the main html
print(" ******************* iFrame scenario started  ***************")
print("Switching to frame and back to the main html")
driver.get("https://demoqa.com/frames")
disable_google_ads(driver)
driver.switch_to.frame(driver.find_element(By.ID,'frame1')) # switch for the frames inside the text
frame1_msg = driver.find_element(By.ID, 'sampleHeading').text
print(f"Text inside the iframe : {frame1_msg}")
driver.switch_to.default_content()

print(" ******************* Alerts scenario started  ***************")
driver.get(HOST)
disable_google_ads(driver)

# prompt_button = driver.find_element(By.ID,'promtButton')

wdwait = WebDriverWait(driver, 10)
prompt_button = wdwait.until(EC.element_to_be_clickable((By.ID,'promtButton')))

print("clicking the promtButton ...")
prompt_button.click()
time.sleep(1)

print("Create an object of alert class")
prompt_alert = driver.switch_to.alert

# Switching to frame and back to the main html
driver.switch_to.frame(driver.find_element(By.ID,'frame1')) # switch for the frames inside the text
frame1_msg = driver.find_element(By.ID, 'sampleHeading').text
print(f"Text inside the iframe : {frame1_msg}")
driver.switch_to.default_content()

print(f"text of alert: '{prompt_alert.text}'")
print("entering the name")
prompt_alert.send_keys('AWESOMEE!!')
time.sleep(3)
print("accepting the alert")
prompt_alert.accept()
time.sleep(3)
result_msg = driver.find_element(By.ID,'promptResult').text
print(f"Checkpoint of the result: '{result_msg}'")

print("2. click the promtButton ...")
prompt_button = wdwait.until(EC.element_to_be_clickable((By.ID, 'promtButton')))
prompt_button.click()

print("Create an object of alert class")
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys('CANCEEEL!!')
prompt_alert.dismiss()

# Explicit wait
# WebDriverWait, Expected_conditions
# result_status = driver.find_element(By.ID,'promptResult').is_displayed()

# result_status = WebDriverWait(driver, 10).until_not(
#    expected_conditions.presence_of_element_located( (By.ID,'promptResult') ))
wdwait = WebDriverWait(driver, 5)
result_status = wdwait.until_not(EC.presence_of_element_located( (By.ID,'promptResult') ))

print(f"Checkpoint of the result: '{result_status}'")
time.sleep(10)

