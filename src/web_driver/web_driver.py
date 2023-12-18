import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# test data
host = "https://demoqa.com/browser-windows"
temp_host = "https://demoqa.com/automation-practice-form"
expected_tab2_msg = "This is a sample page"


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
tab1_url = driver.current_url
print(f"Title : {driver.title}\nFirst Page URL: {tab1_url}")
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
driver.switch_to.window(tab2_handle)

print("# get the current_url and title")
tab2_url = driver.current_url
print(f"Tab2 Title: {driver.title}\nTab2 URL: {tab2_url}.")

print("# verify that url is different from first url")
print(f" tab2 url verification : {tab2_url != tab1_url}")
assert tab2_url != tab1_url, "ERROR: new tab URL verification failed."
print(" Verify the text displayed.")
tab2_msg_element = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
print(f" tab2 message (text) verification : {tab2_msg_element.text == expected_tab2_msg}")
assert tab2_msg_element.text == expected_tab2_msg, "ERROR: new tab message verification failed."

print(f" tab2 message (text) visibility verification (is_displayed): {tab2_msg_element.is_displayed()}")
assert tab2_msg_element.is_displayed(), "ERROR: new tab message visibility verification failed."

print("# close the tab with driver.close()")
driver.close()

print("# switch to main tab")
driver.switch_to.window(tab1_handle)
time.sleep(5)

print("# get current_url and verify that it is the same as first url")
print(f"URL after switching to first tab: {driver.current_url}")

print("# close the browser (all tabs) -> driver.quit()")
driver.quit()






