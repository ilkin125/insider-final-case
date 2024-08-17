from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CareersPage(BasePage):
    # Locators
    LOCATIONS_SECTION = (By.CSS_SELECTOR, "[data-id='8ab30be']")
    TEAMS_SECTION = (By.CSS_SELECTOR, "[data-id='b6c45b2']")
    LIFE_AT_INSIDER_SECTION = (By.CSS_SELECTOR, "[data-id='a8e7b90']")
    SEE_ALL_TEAMS_LINK = (By.XPATH, "//a[text()='See all teams']")
    JOB_ITEM = (By.LINK_TEXT, "Quality Assurance")
    JOB_TITLE = (By.CSS_SELECTOR, ".job-title")
    SHOW_POSITIONS = (By.LINK_TEXT, "See all QA jobs")
    LOCATION_DROPDOWN_BUTTON = (By.CSS_SELECTOR, ".select2-selection--single")
    ISTANBUL_TURKEY_OPTION = (By.XPATH, "//li[contains(text(), 'Istanbul, Turkey')]")
    QA_TEXT_CONTAINER = (By.ID, "select2-filter-by-department-container")
    JOB_LISTINGS = (By.CSS_SELECTOR, ".position-list-item")
    JOB_DEPARTMENT = (By.CSS_SELECTOR, ".position-department")
    JOB_LOCATION = (By.CSS_SELECTOR, ".position-location")
    VIEW_ROLE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-navy.rounded.pt-2.pr-5.pb-2.pl-5")

    def verify_sections(self):
        locations_present = self.is_visible(self.LOCATIONS_SECTION)
        print("Locations section is present:", locations_present)

        teams_present = self.is_visible(self.TEAMS_SECTION)
        print("Teams section is present:", teams_present)

        life_at_insider_present = self.is_visible(self.LIFE_AT_INSIDER_SECTION)
        print("Life at Insider section is present:", life_at_insider_present)

        return locations_present and teams_present and life_at_insider_present

    def click_see_all_teams(self):
        try:
            teams_section = self.wait.until(EC.visibility_of_element_located(self.TEAMS_SECTION))
            see_all_teams_link = teams_section.find_element(*self.SEE_ALL_TEAMS_LINK)
            actions = ActionChains(self.driver)
            actions.move_to_element(see_all_teams_link).perform()
            see_all_teams_link.click()
            return True
        except Exception:
            return False

    def click_qa_page(self):
        try:
            job_to_click = self.wait.until(EC.visibility_of_element_located(self.JOB_ITEM))
            actions = ActionChains(self.driver)
            actions.move_to_element(job_to_click).perform()
            job_to_click.click()
            return True
        except Exception:
            return False

    def click_see_all_qa_jobs(self):
        try:
            print("You are in Quality Assurance page.")
            qa_job_click = self.wait.until(EC.visibility_of_element_located(self.SHOW_POSITIONS))
            qa_job_click.click()
            return True
        except Exception:
            return False
