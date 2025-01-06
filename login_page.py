from pages_new.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "ap_email")
    CONTINUE_BUTTON = (By.ID, "continue")
    PASSWORD_INPUT = (By.ID, "ap_password")
    SIGN_IN_BUTTON = (By.ID, "signInSubmit")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".a-list-item")

    def enter_email(self, email):
        self.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_continue(self):
        self.find_element(*self.CONTINUE_BUTTON).click()

    def enter_password(self, password):
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_sign_in(self):
        self.find_element(*self.SIGN_IN_BUTTON).click()

    def get_error_message(self):
        return self.find_element(*self.ERROR_MESSAGE).text