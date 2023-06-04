import logging
import time
from os.path import abspath, dirname

import yaml
from selenium.webdriver.common.by import By

# __file__ -> utilities.py
# abspath(__file__) -> C:\dev\SeleniumAutomation\src\utilities.py
# dirname(abspath(__file__)) -> C:\dev\SeleniumAutomation\src\
ROOT_DIR = dirname(dirname(abspath(__file__)))  # C:\dev\SeleniumAutomation\


def disable_google_ads(driver):
    google_ads_iframe_xpath = "//iframe[contains(@id, 'google_ads_iframe_')]"

    all_iframes = driver.find_elements(By.XPATH, google_ads_iframe_xpath)
    if len(all_iframes) > 0:
        print("Ad Found\n")
        driver.execute_script("""
            var elems = document.getElementsByTagName("iframe"); 
            for(var i = 0, max = elems.length; i < max; i++)
                 {
                     elems[i].hidden=true;
                 }
                              """)
        print('Total Ads: ' + str(len(all_iframes)))
    else:
        print('No frames found')


def load_yaml_file(filepath):
    try:
        print("****** reading yaml file *******************")
        with open(filepath, 'r') as stream:
            file_content = yaml.safe_load(stream)
        # return file_content
    except FileNotFoundError as err:
        print("Incorrect file path is provided")
        print(f"FileNotFoundError: {err}")
        raise
    else:
        print("Else statement in try except, only after try block")
        return file_content
    finally:
        print("Finally: This will execute whatever happens")


def create_logger(file):
    logging.basicConfig(filename=file,
                        level=logging.INFO,
                        format='%(asctime)-15s [%(levelname)s]: %(message)s',
                        filemode='a')
    return logging.getLogger()


def get_str_day():
    return time.strftime("%Y%m%d")


def get_str_day_min_sec():
    return time.strftime("%Y%m%d-%H%M%S")