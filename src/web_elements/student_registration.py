# Test Case
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.registration_page import *
from src.utilities import *

# create a log file
logfile = f"{ROOT_DIR}/logs/{get_str_day()}_student_registration.log"
log = create_logger(logfile)

config_file = f"{ROOT_DIR}/data/registration.yaml"
data = load_yaml_file(config_file)

# Test data:
host = 'https://demoqa.com/automation-practice-form'
fname = 'john'
lname = 'doe'
email = 'johndoe@email.com'
mobile_num = '1234567899'
gender = 'Male'
dob = '01/01/2000'
subjects = 'john doe registry form'
# picture_path = '../../data/html-dom.svg'
# picture_path = 'C:/dev/SeleniumAutomation/data/html-dom.svg'   OR
# picture_path = ROOT_DIR + '\data\html-dom.svg'
picture_path = f'{ROOT_DIR}\data\html-dom.svg'
state = 'NCR'
city = 'Delhi'
birth_day = "025"  # always pass 3 digits, with leading zeros if needed
birth_month = "April"
birth_year = "2000"
hobbies_list = ['sports', 'reading']

# print("# Student Registration form - Automated steps)")
log.info("*********  Student Registration form - Automated steps  ************")
log.info("# Launch the Chrome browser")
log.warning("this was the warning message ...")
log.error("test case failed!!!   ------ just kidding..")
log.debug("tiny details and mini steps executions ...") # this one wouldn't show because
                                             # we set log on INFO and debug is below the level we set (INFO)

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver = webdriver.Chrome()
log.info('maximizing the browser window')
# driver.maximize_window()
driver.implicitly_wait(10)

def test_scenario1():
    try:
        # Automation Test steps :
        mobilenum1 = data['scenario1']['mobilenumber']

        registration_page = RegistrationPage(driver)

        log.info(' 1 - open the student registration form')
        driver.get(host)
        time.sleep(0.5)
        # print('Zoom the page to 75%')
        # driver.execute_script("document.body.style.zoom='80%'")
        disable_google_ads(driver)

        registration_page.enter_name(fname)
        registration_page.enter_name(lname)
        registration_page.enter_email(email)
        registration_page.select_gender('male')
        # registration_page.select_gender('female')
        registration_page.enter_mobile_number(mobile_num)
        registration_page.enter_subject("John registration entry")
        registration_page.set_date_of_birth(birth_day, birth_month, birth_year)
        registration_page.select_hobbies(hobbies_list)
        # registration_page.select_hobbies(hobbies=['sports', 'reading'])
        registration_page.upload_picture(picture_path)

        # 10 Select State first, then City (kind of drop down - not selectable element)
        registration_page.submit_form()

# more steps can be added to verify  and validate the data that was entered
# click close to close the confirmation window


    except (NoSuchElementException, TimeoutException) as err:
        log.error(f"Selenium error occured: {err}")
        screenshot = ROOT_DIR +"/reports/screenshots/student_regist_error.png"
        driver.save_screenshot(screenshot)
        log.warning(f"please check the screenshot here: {screenshot}")
    finally:
        log.info(" ************* Complete, closing the browser ************ ")
        # driver.close() # close the current tab
        driver.quit() # close the browser

def test_scenario2():
    mobilenum2 = data['scenario2']['mobilenumber']
    print(mobilenum2)

test_scenario1()
test_scenario2()

