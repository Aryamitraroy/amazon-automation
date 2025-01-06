from selenium import webdriver
from pages_new.home_page_new import HomePage
from pages_new.login_page import LoginPage
from pages_new.product_page import ProductPage
from pages_new.search_result_page import SearchResultsPage
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

try:
    # Home Page
    home_page = HomePage(driver)
    home_page.search_product("iPhone 13")
    time.sleep(3)

    # Search Results Page
    search_results_page = SearchResultsPage(driver)
    products = search_results_page.get_product_titles()
    print(f"Total Results: {len(products)}")
    for i, product in enumerate(products):
        print(f"{i + 1}: {product.text}")
    search_results_page.click_product(3)
    time.sleep(3)

    # Switch to New Tab
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)

    # Product Page
    product_page = ProductPage(driver)
    product_page.click_buy_now()
    time.sleep(3)

    # Login Page
    login_page = LoginPage(driver)
    login_page.enter_email("aryamitras99@gmail.com")
    login_page.click_continue()
    login_page.enter_password("arya1996")
    login_page.click_sign_in()
    error_message = login_page.get_error_message()
    print("Error Message:", error_message)

finally:
    driver.quit()