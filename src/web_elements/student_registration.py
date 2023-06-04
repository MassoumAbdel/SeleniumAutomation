# Test Case
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.utilities import *
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

# Locators
mobile_xpath = '//input[@id="userNumber"]'
subject_xpath = "//input[@id='subjectsInput']"

# male_xpath = '//input[@id="gender-radio-1"]/..'
male_box_xpath = '//input[@id="gender-radio-1"]'
male_xpath = f'{male_box_xpath}/..' # xpath parent element of male_box_xpath input

# male_xpath = "//label[contains(text(),"Male")]/.."
female_xpath = "//input[@id='gender-radio-2']/.."

sports_xpath = '//input[@id="hobbies-checkbox-1"]/..'
sports_box_xpath = '//input[@id="hobbies-checkbox-1"]'
# sports_xpath = f'/{sports_box_xpath}/..'

# sports_css_selector = 'input#hobbies-checkbox-1'

reading_xpath = '//input[@id="hobbies-checkbox-2"]/..'
reading_box_xpath = '//input[@id="hobbies-checkbox-2"]'
# reading_css_selector = 'input#hobbies-checkbox-2'

music_xpath = '//input[@id="hobbies-checkbox-3"]/..'
music_box_xpath = '//input[@id="hobbies-checkbox-3"]/..'
# music_css_selector = 'input#hobbies-checkbox-3'

month_select_xpath = '//select[@class="react-datepicker__month-select"]'
year_select_xpath = '//select[@class="react-datepicker__year-select"]'

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

print(' 1 - open the student registration form')
driver.get(host)
print('Zoom the page to 75%')
driver.execute_script("document.body.style.zoom='75%'")
disable_google_ads(driver)

# Enter name,
print(" 2 - Enter name ...")
fname_input = driver.find_element(By.ID, 'firstName')
fname_input.send_keys("Abdelmounim")
time.sleep(2)
fname_input.clear()
fname_input.send_keys(fname)

# Enter last name
print(" 3 - last name - use locator")
# driver.find_element(By.CLASS_NAME, 'mr-sm-2 form-control').send_keys(lname)
driver.find_element(By.ID, 'lastName').send_keys(lname)

# Enter email
print(" 4 - Enter your email - use locator")
# driver.find_element(By.CLASS_NAME, 'mr-sm-2 form-control').send_keys(email)
driver.find_element(By.ID, 'userEmail').send_keys(email)
time.sleep(5)

# Select Gender: Male (radio)
print(" 5 - Select Gender: Male (radio)")
elem = driver.find_element(By.XPATH, male_xpath)
male_box = driver.find_element(By.XPATH, male_box_xpath)
print(f"Is Male gender Selected-before: {male_box.is_selected()}")
elem.click()
print(f"Is Male gender Selected-after: {male_box.is_selected()}")
# alternative way of clicking with javascript code executor
# driver.execute_script("argument[0].click();", elem)

# Enter Mobile, Subjects, Current Address
print(' 6 - Entering the mobile number ....')
driver.find_element(By.XPATH, mobile_xpath).send_keys(mobile_num)
driver.find_element(By.XPATH, subject_xpath).send_keys("John registration entry")


# Select/Enter data of birth
print(" 7 - Select/Enter data of birth - drop down list")
# click on date of birth
print("# click on date of birth")
driver.find_element(By.ID, "dateOfBirthInput").click()
# select month
print(" select month")
select_month = Select(driver.find_element(By.XPATH, month_select_xpath))
select_month.select_by_visible_text('April')
# select_month.select_by_index(3) ['January','February','March','April',..]
# select year
print(" select year")
select_year = Select(driver.find_element(By.XPATH, year_select_xpath))
select_year.select_by_value('2000')
# click on date = 25
print(" click on date = 25")
day = "025" # always pass 3 digits, with leading zeros if needed
day_xpath = f"//div[contains(@class, 'react-datepicker__day--{day}') and not(contains(@class, 'outside-month'))]"
driver.find_element(By.XPATH, day_xpath).click()


# Select Checkboxes (multi select)
print(" 8 - Select Checkboxes (multi select)")
sport_checkbox = driver.find_element(By.CSS_SELECTOR, sports_xpath)
sport_input = driver.find_element(By.CSS_SELECTOR, sports_box_xpath)

print("  8-1 check if selected: before and after checking.")
print(f"Is Sport-before: {sport_input.is_selected()}")
sport_checkbox.click()
print(f"Is Sport-after: {sport_input.is_selected()}")

driver.find_element(By.CSS_SELECTOR, reading_xpath).click()
driver.find_element(By.CSS_SELECTOR, music_xpath).click()


# picture upload (input, type=file)
# Select State first, then City (kind of drop down - not selectable element)
time.sleep(10)

# 11 click if enable then click Submit, scrolling might be needed
# driver.execute_script("argument[0].scrollIntoView();", elem)
# driver.execute_script("argument[0].click();", elem)

print(" ************* Complete, closing the browser ************ ")
driver.close() # close the current tab
# driver.quit() # close the browser




