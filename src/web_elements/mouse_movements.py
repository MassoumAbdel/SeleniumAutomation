from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.utilities import *
# utilities has import time , import for by..., so you don't have to import them again

# Test Data
host = "https://demoqa.com/droppable"

# Automation Test Steps:
print(" # Mouse Movements - drag and drop action")
print(" # Launch the chrome browser")

# created the object for chromedriver that talks to chrome browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver = webdriver.Chrome()
print('maximizing the browser window')
# driver.maximize_window()
driver.implicitly_wait(5)


print ("# open the host webpage (default simple tab)")
driver.get(host)
disable_google_ads(driver)

print("# verify the message in the droppable box 'Drop here'" )
droppable_xpath = "//div[@id='droppable']"
before_msg = driver.find_element(By.XPATH,droppable_xpath).text
print(f"Before message: '{before_msg}'")
time.sleep(2)

print("# hold the Drag Me object and drop it to droppable box ")
actions = ActionChains(driver)
draggable_elem = driver.find_element(By.ID,'draggable')
droppable_elem = driver.find_element(By.ID,'droppable')

print("performing the action....")
actions.drag_and_drop(draggable_elem, droppable_elem).perform()

print("# verify the message in the droppable box 'Dropped!'")
after_msg = driver.find_element(By.XPATH,droppable_xpath).text
print(f"After message: '{after_msg}'")

print("Scenarios is completed.")

print(" ************ Hover over scenario started ***********")
driver.get("https://jqueryui.com/tooltip/")
disable_google_ads(driver)

print("Switching to the frame and finding the age elem")
driver.switch_to.frame(driver.find_element(By.CLASS_NAME,'demo-frame'))
age_elem = driver.find_element(By.ID,'age')

print("performing the actions ...")
actions = ActionChains(driver)
actions.move_to_element(age_elem).perform()
print("getting  the text of tooltip...")
tooltip_msg = driver.find_element(By.XPATH, "//div[contains(@id, 'ui-id-')]/div").text
print(f"Tooltip message: '{tooltip_msg}' .")

print("Closing the Browser...")

time.sleep(10)
driver.quit()







