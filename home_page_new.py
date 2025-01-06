from pages_new.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")

    def search_product(self, product_name):
        search_box = self.find_element(*self.SEARCH_BOX)
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)