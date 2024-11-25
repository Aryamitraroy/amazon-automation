from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#  Set up the browser
driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

# Search for "iPhone 13"
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("iPhone 13")
search_box.send_keys(Keys.ENTER)
time.sleep(3)

# Find all product titles

product_titles = driver.find_elements(By.CSS_SELECTOR, "h2 span")
print("Total Results:", len(product_titles))

# Find the all Count of product

for i, title in enumerate(product_titles):
    print(f"{i + 1}: {title.text}")



product_titles[3].click()
time.sleep(3)

# Open Another Window

driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

# Buy New product

buy_now_button = driver.find_element(By.ID, "buy-now-button")
buy_now_button.click()
time.sleep(3)

#Enter the Email id

email_input = driver.find_element(By.ID, "ap_email")
email_input.send_keys("aryamitra1996@gmail.com")
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

# enter the password

password_input = driver.find_element(By.ID, "ap_password")
password_input.send_keys("arya1996")
sign_in_button = driver.find_element(By.ID, "signInSubmit")
sign_in_button.click()


password_input = driver.find_element(By.ID, "ap_password")
password_input.send_keys("arya1996")
sign_in_button = driver.find_element(By.ID, "signInSubmit")
sign_in_button.click()

error_message = driver.find_element(By.CSS_SELECTOR, ".a-list-item")
print("Error Message:", error_message.text)





