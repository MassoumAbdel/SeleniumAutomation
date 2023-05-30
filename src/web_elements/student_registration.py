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
mobile_num = '1234567890'
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

print('open the student registration form')
driver.get(host)
print('Zoom the page to 75%')
driver.execute_script("document.body.style.zoom='75%'")

# Enter name,
print(" # Enter name ...")
fname_input = driver.find_element(By.ID, 'firstName')
fname_input.send_keys("Abdelmounim")
time.sleep(2)
fname_input.clear()
fname_input.send_keys(fname)

# Enter last name
print("last name - use locator")
# driver.find_element(By.CLASS_NAME, 'mr-sm-2 form-control').send_keys(lname)
driver.find_element(By.ID, 'lastName').send_keys(lname)

# Enter email
print("Enter your email - use locator")
# driver.find_element(By.CLASS_NAME, 'mr-sm-2 form-control').send_keys(email)
driver.find_element(By.ID, 'userEmail').send_keys(email)
time.sleep(5)

# Enter Mobile, Subjects, Current Address
print('entering the mobile number ....')
mobile_xpath = '//input[@id="userNumber"]'
driver.find_element(By.XPATH, mobile_xpath).send_keys(mobile_num)

subject_xpath = "//input[@id='subjectsInput']"
driver.find_element(By.XPATH, subject_xpath).send_keys("John registration entry")


# Select Gender: Male (radio)

# Select/Enter data of birth

# Select Checkboxes (multi select)
sports_css_selector = 'input#hobbies-checkbox-1'
sports_xpath = '//input[@id="hobbies-checkbox-1"]'

reading_css_selector = 'input#hobbies-checkbox-2'
music_css_selector = 'input#hobbies-checkbox-3'
driver.find_element(By.CSS_SELECTOR, sports_css_selector).click()
driver.find_element(By.CSS_SELECTOR, reading_css_selector).click()
driver.find_element(By.CSS_SELECTOR, music_css_selector).click()
time.sleep(10)


# picture upload (input, type=file)
# Select State first, then City (kind of drop down)

print(" ************* Complete, closing the browser ************ ")
driver.close() # close the current tab
# driver.quit() # close the browser

