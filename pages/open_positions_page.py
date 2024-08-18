import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class OpenPositionsPage(BasePage):
    # Locators
    LOCATION_DROPDOWN_BUTTON = (By.CSS_SELECTOR, ".select2-selection--single")
    ISTANBUL_TURKEY_OPTION = (By.XPATH, "//li[contains(text(), 'Istanbul, Turkey')]")
    QA_TEXT_CONTAINER = (By.ID, "select2-filter-by-department-container")
    JOB_LISTINGS = (By.CSS_SELECTOR, ".position-list-item")
    JOB_DEPARTMENT = (By.CSS_SELECTOR, ".position-department")
    JOB_LOCATION = (By.CSS_SELECTOR, ".position-location")
    VIEW_ROLE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-navy.rounded.pt-2.pr-5.pb-2.pl-5")

    def select_istanbul_turkey(self):
        try:
            self.driver.execute_script("window.scrollBy(0, 500);")

            wait = WebDriverWait(self.driver, 30)
            while True:
                try:
                    qa_text = self.driver.find_element(*self.QA_TEXT_CONTAINER).text
                    if "Quality Assurance" in qa_text:
                        print("'Quality Assurance' text is now visible.")
                        break
                except:
                    pass
                time.sleep(1)
            dropdown_button = self.wait.until(EC.element_to_be_clickable(self.LOCATION_DROPDOWN_BUTTON))
            dropdown_button.click()

            istanbul_option = self.wait.until(EC.element_to_be_clickable(self.ISTANBUL_TURKEY_OPTION))
            istanbul_option.click()

            print("Selected 'Istanbul, Turkey' from the location dropdown.")
            time.sleep(3)
            return True
        except Exception:
            return False

    def verify_job_listings(self):
        self.driver.execute_script("window.scrollBy(0, 150);")
        time.sleep(4)
        job_listings = self.driver.find_elements(*self.JOB_LISTINGS)

        if not job_listings:
            print("No job listings found.")
            return False

        for job in job_listings:
            try:
                department = job.find_element(*self.JOB_DEPARTMENT).text
                location = job.find_element(*self.JOB_LOCATION).text
                assert department == "Quality Assurance", f"Expected 'Quality Assurance' but found '{department}'"
                assert location == "Istanbul, Turkey", f"Expected 'Istanbul, Turkey' but found '{location}'"
            except AssertionError:
                return False
            except Exception:
                return False

        print("All job listings have 'Quality Assurance' department and 'Istanbul, Turkey' location.")
        return True

    def hover_and_click_view_role(self):
        try:
            first_job_listing = self.wait.until(EC.visibility_of_element_located(self.JOB_LISTINGS))
            actions = ActionChains(self.driver)
            actions.move_to_element(first_job_listing).perform()
            print("Hovered over the first job listing.")
            view_role_button = first_job_listing.find_element(By.LINK_TEXT, "View Role")
            view_role_button.click()
            print("Clicked 'View Role' link.")
            time.sleep(10)
            return True
        except Exception:
            return False
