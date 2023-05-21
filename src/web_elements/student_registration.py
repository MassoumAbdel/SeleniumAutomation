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

print('open the student registration form')
driver.get(host)
print('Zoom the page to 75%')
driver.execute_script("document.body.style.zoom='75%'")

# Enter Mobile, Subjects, current Address
fname_input = driver.find_element(By.ID, 'firstName')
fname_input.send_keys("sadjgdgjv")
time.sleep(2)
fname_input.clear()
fname_input.send_keys(fname)


# Enter name, last name, email
# Select Gender: Male (radio)
# Select/Enter data of birth
# Select Checkboxes (multi select)
# picture upload (input, type=file)
# Select State first, then City (kind of drop down)


