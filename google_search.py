from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Variables
host = "https://www.google.com"
my_keyword = 'ai' # or you could get it from the user by asking them about the word and save it
# my_keyword = input("Enter the keyword you want to search")

 # Test Steps start here
print(" Google search manual test (needs to be automated)")
print("Launch the Chrome browser")

# Created the object for chromedriver that talks to chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver = webdriver.Chrome()
print("Maximizing the browser window")
driver.maximize_window()

time.sleep(1)

print("open the google.com page")
driver.get(host)
# time.sleep(10)

print("search for 'ai' and hit enter")
# identifier used to search that element from HTML document
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys(my_keyword)
search_box.send_keys(Keys.ENTER)

print("save the search result ")
search_result = driver.find_element(By.ID, 'result-stats')
print(f"Search result of ai: {search_result.text}")
# Sample:  About 10,890,000,000 results (0.66 seconds)

print("close the browser")
driver.close() # close the tab

