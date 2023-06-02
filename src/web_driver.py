import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# test data
host = "https://demoqa.com/browser-windows"
temp_host = "https://demoqa.com/automation-practice-form"

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
# driver = webdriver.Chrome()
print('maximizing the browser window')
driver.maximize_window()
driver.implicitly_wait(10) # default time out to find the element

print('# open the host, name (name of the browser)')
driver.get(host)
print(f"url of host: '{driver.current_url}'")
print(f'WebDriver Name: {driver.name}')

print('# open the temp_host')
driver.get(temp_host)
print(f"url temp host: {driver.current_url}")
time.sleep(2)

print('# back to original host')
driver.back()
print(f"url of host: '{driver.current_url}'")
time.sleep(2)

print('# forward to temp host')
driver.forward()
print(f"url of host: '{driver.current_url}'")
time.sleep(2)

print('# back to original host then refresh')
driver.back()
print(f"url of host: '{driver.current_url}'")
driver.refresh()
time.sleep(2)

print("# get current_url, title")
first_url = driver.current_url
print(f"Title : {driver.title}\nFirst Page URL: {first_url}")
time.sleep(5)

print("# get current_window_handle and save in a variable")
tab1_handle = driver.current_window_handle
print(f" tab1 handle: {tab1_handle}")

print("# click on New Tab button, this will open new tab")
new_tab_button = driver.find_element(By.CSS_SELECTOR, "#tabButton")
new_tab_button.click()
time.sleep(2)

print("# get window_handles and save it in a list variable")
handles = driver.window_handles # this is the list of IDs
print(f"windows handles: {handles}")
tab2_handle = handles[1]

# assert compare object1 with object2 returns (true/ false), if false display that error message
assert handles[0] == tab1_handle, "Error: tab1 handle verification failed."
# assert handles[0] == tab1_handle + "11", "Error: tab1 handle verification failed."
# assert add(3,5) == 8
print("# switch to new tab")

print("# get the current_url and title")

print("# verify that url is different from first url")

print("# close the tab with driver.close()")

print("# switch to main tab")

print("# get current_url and verify that it is the same as first url")

print("# close the browser (all tabs) -> driver.quit()")
driver.quit()
print(" ------------------  ")






