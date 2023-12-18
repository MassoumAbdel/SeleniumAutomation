from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utilities import *

logfile = f"{ROOT_DIR}/logs/{get_str_day()}.log"
log = create_logger(logfile)

class BasePage:
    """
    Abstract class that defines shared browser and all necessary/mostly used selenium methods.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wdwait = WebDriverWait(driver, 15)


    # enter text
        # by using ID
    def enter_text_by_id(self, locator_id, text_to_enter):
        try:
            log.info("entering the text by ID ..")
            # element = self.driver.find_element(By.ID, locator_id)
            element = self.wdwait.until(EC.presnece_of_element_located(By.ID, locator_id))
            element.clear()
            element.send_keys(text_to_enter)
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occured: {err}")
            screenshot = ROOT_DIR +"/reports/screenshots/enter_text_by_id_error.png"
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")

        # by using Xpath
    def enter_text_by_xpath(self, xpath, text_to_enter):
        try:
            log.info("entering the text by Xpath ..")
            # element = self.driver.find_element(By.XPATH, xpath)
            element = self.wdwait.until(EC.presnece_of_element_located(By.XPATH, xpath))
            element.clear()
            element.send_keys(text_to_enter)
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occurred: {err}")
            screenshot = ROOT_DIR +"/reports/screenshots/enter_text_by_xpath_error.png"
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")

    # click element
        # by using Xpath
    def click_element_by_xpath(self, xpath):
        try:
            log.info("clicking element by Xpath ..")
            # element = self.driver.find_element(By.XPATH, xpath)
            element = self.wdwait.until(EC.element_to_be_clickable(By.XPATH, xpath))
            element.click()
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occurred: {err}")
            screenshot = ROOT_DIR +"/reports/screenshots/click_element_by_xpath_error.png"
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")

        # by using ID
    def click_element_by_id(self, locator_id):
        try:
            log.info("clicking element by ID ..")
            # element = self.driver.find_element(By.XPATH, xpath)
            element = self.wdwait.until(EC.element_to_be_clickable(By.ID, locator_id))
            element.click()
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occurred: {err}")
            screenshot = ROOT_DIR +"/reports/screenshots/click_element_by_id_error.png"
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")

    # get text
        # by using Xpath
    def get_text_by_xpath(self, xpath):
        try:
            log.info("getting the text by Xpath ..")
            # element = self.driver.find_element(By.XPATH, xpath)
            element = self.wdwait.until(EC.presnece_of_element_located(By.XPATH, xpath))
            return element.text
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occurred: {err}")
            screenshot = ROOT_DIR + "/reports/screenshots/get_text_by_xpath_error.png"
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")


        # by using ID
    def get_text_by_id(self, locator_id):
        try:
            log.info("getting the text by ID ..")
            # element = self.driver.find_element(By.XPATH, xpath)
            element = self.wdwait.until(EC.presnece_of_element_located(By.ID, locator_id))
            return element.text
        except (NoSuchElementException, TimeoutException) as err:
            log.error(f"Selenium error occurred: {err}")
            screenshot = ROOT_DIR + "/reports/screenshots/get_text_by_id_error.png"
            self.driver.save_screenshot(screenshot)
            log.warning(f"please check the screenshot here: {screenshot}")

