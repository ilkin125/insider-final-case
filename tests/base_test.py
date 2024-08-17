import time
import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self._outcome = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        if any(error[1] for error in self._outcome.errors):
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_filename = f"screenshot_{timestamp}_failed.png"
            self.driver.save_screenshot(screenshot_filename)
            print(f"Failed screenshot {screenshot_filename} saved.")
        else:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_filename = f"screenshot_{timestamp}_success.png"
            self.driver.save_screenshot(screenshot_filename)
            print(f"Success screenshot {screenshot_filename} saved.")

        self.driver.quit()
