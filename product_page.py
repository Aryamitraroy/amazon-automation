from pages_new.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    BUY_NOW_BUTTON = (By.ID, "buy-now-button")

    def click_buy_now(self):
        self.find_element(*self.BUY_NOW_BUTTON).click()