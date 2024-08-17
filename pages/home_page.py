from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class HomePage(BasePage):
    # Locators
    COOKIE_ACCEPT_BUTTON = (By.ID, "wt-cli-accept-all-btn")
    COMPANY_MENU = (By.LINK_TEXT, "Company")
    CAREERS_MENU = (By.LINK_TEXT, "Careers")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://useinsider.com/")
        self.driver.maximize_window()

    def accept_cookies(self):
        try:
            self.click_element(self.COOKIE_ACCEPT_BUTTON)
            print("Cookies accepted.")
            return True
        except Exception:
            return False

    def navigate_to_careers(self):
        try:
            self.click_element(self.COMPANY_MENU)
            time.sleep(3)
            self.click_element(self.CAREERS_MENU)
            return True
        except Exception:
            return False


