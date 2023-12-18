from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from src.pages.base_page import BasePage
from src.utilities import *

logfile = f"{ROOT_DIR}/logs/{get_str_day()}.log"
log = create_logger(logfile)


class RegistrationPage(BasePage):
    """
    page Object Model of forms page, defines all attributes and methods of the page (Building Blocks).
    """

    # Locators (Attributes):
    __mobile_xpath = '//input[@id="userNumber"]'
    __subject_xpath = "//input[@id='subjectsInput']"
    # male_xpath = '//input[@id="gender-radio-1"]/..'
    __male_box_xpath = '//input[@id="gender-radio-1"]'
    __male_xpath = f'{__male_box_xpath}/..'  # xpath parent element of male_box_xpath input element
    # male_xpath = "//label[contains(text(),"Male")]/.."
    __female_box_xpath = "//input[@id='gender-radio-2']/.."
    __female_xpath = f'{__female_box_xpath}/..'  # xpath parent element of female_box_xpath input element

    __sports_box_xpath = '//input[@id="hobbies-checkbox-1"]'
    __sports_xpath = f'/{__sports_box_xpath}/..'
    # sports_xpath = '//input[@id="hobbies-checkbox-1"]/..'
    # sports_css_selector = 'input#hobbies-checkbox-1'

    __reading_xpath = '//input[@id="hobbies-checkbox-2"]/..'
    # reading_box_xpath = '//input[@id="hobbies-checkbox-2"]'
    # reading_css_selector = 'input#hobbies-checkbox-2'

    __music_xpath = '//input[@id="hobbies-checkbox-3"]/..'
    # music_box_xpath = '//input[@id="hobbies-checkbox-3"]/..'
    # music_css_selector = 'input#hobbies-checkbox-3'

    __month_select_xpath = '//select[@class="react-datepicker__month-select"]'
    __year_select_xpath = '//select[@class="react-datepicker__year-select"]'

    # Element: <input id="uploadPicture" type="file" lang="en" class="form-control-file">
    __upload_picture_xpath = '//input[@id="uploadPicture"]'
    __submit_xpath = "//button[@id='submit']"

    # methods
    def enter_name(self, first_name):
        log.info(" 2 - Enter name ...")
        self.enter_text_by_id('firstName', first_name)

    def enter_last_name(self, last_name):
        log.info(" 3 - last name - use different locators")
        self.enter_text_by_id('lastName', last_name)

    def enter_email(self, email):
        log.info(" 4 - Enter your email")
        self.enter_text_by_id('userEmail', email)
        time.sleep(0.5)
    def select_gender(self, gender: str):
        log.info(" Selecting the Gender")
        if gender.lower() =='male':
            log.info(" 5 - Select Gender: Male (radio)")
            element = self.driver.find_element(By.XPATH, self.__male_box_xpath)
            log.info(f"Is Male gender Selected-before: {element.is_selected()}")
            self.click_element_by_xpath(self.__male_xpath)
            log.info(f"Is Male gender Selected-after: {element.is_selected()}")
        elif gender.lower() == 'female':
            log.info(" 5 - Select Gender: Female (radio)")
            element = self.driver.find_element(By.XPATH, self.__female_box_xpath)
            log.info(f"Is Female gender Selected-before: {element.is_selected()}")
            self.click_element_by_xpath(self.__female_xpath)
            log.info(f"Is Female gender Selected-after: {element.is_selected()}")
    def enter_mobile_number(self, mobile_number):
        log.info(' 6 - Entering the mobile number ....')
        self.enter_text_by_xpath(self.__mobile_xpath, mobile_number)

    def set_date_of_birth(self, day: str, month: str, year: str):
        log.info(" 7 - Select/Enter data of birth - drop down list")
        log.info("# click on Date of Birth")
        self.click_element_by_id("dateOfBirthInput")

        log.info(" select month")
        select_month = Select(self.driver.find_element(By.XPATH, self.__month_select_xpath))
        select_month.select_by_visible_text(month.title())
        # select_month.select_by_visible_index(3) ['January','February','March','April','May'..]

        log.info(" select year")
        select_year = Select(self.driver.find_element(By.XPATH, self.__year_select_xpath))
        select_year.select_by_value(year)

        log.info(f" click on Day = {day}")
        day_xpath = f"//div[contains(@class, 'react-datepicker__day--{day}') and not(contains(@class, 'outside-month'))]"
        self.click_element_by_xpath(day_xpath)

    def enter_subject(self, subject):
        log.info(' 6 - Entering the Subjects ....')
        self.enter_text_by_xpath(self.__subject_xpath, subject)
    def select_hobbies(self, hobbies: list):

        if 'sports' in hobbies:
            log.info(" 8 - Select Hobbies Checkboxes (multi select)")
            sport_input = self.driver.find_element(By.XPATH, self.__sports_box_xpath)
            # sport_checkbox = driver.find_element(By.CSS_SELECTOR, sports_xpath)
            # sport_input = driver.find_element(By.CSS_SELECTOR, sports_box_xpath)
            log.info("  8-1 check if selected: before and after checking.")

            log.info(f"Is Sport-before: {sport_input.is_selected()}")
            self.click_element_by_xpath(self.__sports_xpath)
            log.info(f"Is Sport-after: {sport_input.is_selected()}")

        if 'reading' in hobbies:
            self.click_element_by_xpath(self.__reading_xpath)
            # driver.find_element(By.CSS_SELECTOR, reading_xpath).click()

        if 'music' in hobbies:
            self.click_element_by_xpath(self.__music_xpath)
            # driver.find_element(By.CSS_SELECTOR, music_xpath).click()

        if not hobbies:
            log.warning("No hobbies entered, hobbies selection was not made.")
    def upload_picture(self, file_path):
        log.info(" 9 - picture upload (input, type=file)")
        log.info(f"File absolute path: '{file_path}")
        select_picture = self.driver.find_element(By.XPATH, self.__upload_picture_xpath)
        select_picture.send_keys(self.picture_path)

    def enter_address(self, address):
        pass

    def select_state_city(self, state_city):
        pass

    def submit_form(self):
        # self.click_element_by_xpath(self.__submit_xpath)

        # option 2: using javascript click
        submit_button = self.wdwait.until(EC.visibility_of_element_located(By.XPATH, self.__submit_xpath))
        self.driver.execute_script("argument[0].scrollIntoView();", submit_button)
        self.driver.execute_script("argument[0].click();", submit_button)
        time.sleep(2)




