# Test Case
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# test data:
host = 'https://demoqa.com/automation-practice-form'
fname = 'john'
lname = 'doe'
email = 'johndoe@email.com'
gender = 'Male'
dob = '01/01/2000'
subjects = 'john doe registry form'
picture_path = '../../data/html-dom.svg'
state = 'NCR'
city = 'Delhi'

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


print('open the student registration form')
driver.get(host)
print('Zoom the page to 75%')
driver.execute_script("document.body.style.zoom='75%'")

# Enter Mobile, Subjects, current Address
fname_input = driver.find_element(By.ID, 'firstName')
fname_input.send_keys("Abdelmounim")
time.sleep(2)
fname_input.clear()
fname_input.send_keys(fname)

# Enter name, last name, email
print("last name - use locator")
# driver.find_element(By.ID, 'lastName')
driver.find_element(By.ID, 'lastName').send_keys(lname)
time.sleep(5)

print("Enter your email - use locator")
# driver.find_element(By.CLASS_NAME, 'mr-sm-2 form-control').send_keys(email)
driver.find_element(By.ID, 'userEmail').send_keys(email)
time.sleep(5)


# Select Gender: Male (radio)
# Select/Enter data of birth
# Select Checkboxes (multi select)
# picture upload (input, type=file)
# Select State first, then City (kind of drop down)

print(" ************* Complete, closing the browser ************ ")
driver.close() # close the current tab
# driver.quit() # close the browser

