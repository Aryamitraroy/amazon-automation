from pages_new.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchResultsPage(BasePage):
    PRODUCT_TITLES = (By.CSS_SELECTOR, "h2 span")

    def get_product_titles(self):
        return self.find_elements(*self.PRODUCT_TITLES)

    def click_product(self, index):
        products = self.get_product_titles()
        products[index].click()