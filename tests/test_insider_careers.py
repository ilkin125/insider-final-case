import unittest
from base_test import BaseTest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.open_positions_page import OpenPositionsPage


class TestInsiderCareers(BaseTest):
    def test_careers_page(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.accept_cookies(),
                        "Cookie accept button not found or not clickable")
        self.assertTrue(home_page.navigate_to_careers(),
                        "Exception occurred while navigating to Careers page")
        careers_page = CareersPage(self.driver)

        self.assertTrue(careers_page.verify_sections(),
                        "Not all sections are visible")
        self.assertTrue(careers_page.click_see_all_teams(),
                        "Failed to click 'See all teams' link.")
        self.assertTrue(careers_page.click_qa_page(),
                        "Failed to click Quality Assurance page.")
        self.assertTrue(careers_page.click_see_all_qa_jobs(),
                        "Failed to click 'See all QA jobs'.")
        open_positions_page = OpenPositionsPage(self.driver)

        self.assertTrue(open_positions_page.select_istanbul_turkey(),
                        "Failed to select 'Istanbul, Turkey' from the location dropdown.")
        self.assertTrue(open_positions_page.verify_job_listings(),
                        "Not all jobs are visible")
        self.assertTrue(open_positions_page.hover_and_click_view_role(),
                        "Failed to hover over and click 'View Role'.")


if __name__ == "__main__":
    unittest.main()
