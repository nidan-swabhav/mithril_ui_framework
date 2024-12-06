""" Requirement Page Locator """
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# pylint: disable=line-too-long

class RequirementsPage:
    """Class for interacting with the Requirements Page"""

    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "requirements_page": (By.XPATH, "//span[contains(text(),'Requirements')]"),
            "view_details_btn": (By.XPATH,"//div[@class='req-table-template-style ng-star-inserted']//div[1]//app-requirement-card[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[4]//div[1]//div[1]",),
            "candidate_count": (By.CSS_SELECTOR, ".font-md-style.fw-bold.candidate-count"),
            "current_status_btn":(By.CSS_SELECTOR,"button.btn.btn-default.text-wrap.w-100.h-100"),
            "edit_status_option": (By.CSS_SELECTOR,"i.material-icons-outlined.cursor-pointer.fs-16.fw-400.me-2"),
            "status_dropdown" : (By.CSS_SELECTOR,"ul.dropdown-menu.show"),
            "change_status" : (By.CSS_SELECTOR,"div#ab96dfd93597-1 > .ng-star-inserted")
        }

    def wait_for_element(self, locator_name, wait_time=15, condition=EC.visibility_of_element_located):
        """
        Generic method to wait for an element based on a specific condition.
        :param locator_name: The name of the locator in the locators dictionary.
        :param wait_time: Time to wait before throwing TimeoutException (default: 15 seconds).
        :param condition: The expected condition to wait for (default: visibility_of_element_located).
        """
        return WebDriverWait(self.driver, wait_time).until(
            condition(self.locators[locator_name])
        )

    def click_element(self, locator_name):
        """
        Click on an element after ensuring it's clickable.
        :param locator_name: The name of the locator in the locators dictionary.
        """
        element = self.wait_for_element(locator_name, condition=EC.element_to_be_clickable)
        element.click()

    def select_dropdown(self, locator_name, visible_text):
        """
        Select an option from a dropdown by visible text.
        """
        dropdown_element = self.wait_for_element(locator_name)
        select = Select(dropdown_element)
        select.select_by_visible_text(visible_text)

    def navigate_to_requirements_pg(self):
        """Navigate to the Requirements page."""
        self.click_element("requirements_page")

    def click_view_details(self):
        """Click on the 'View Details' button for the first requirement."""
        self.click_element("view_details_btn")

    def click_candidate_count(self):
        """
        Click on the 'Candidate Count' after ensuring the spinner (if any) is gone.
        Handles dynamic spinners by checking invisibility of all spinners.
        """
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "ngx-spinner-overlay"))
        )
        self.click_element("candidate_count")

    def click_status(self):
        """method clicks on current status"""
        self.click_element("current_status_btn")

    def click_edit(self):
        self.click_element("edit_status_option")
    
    def shortlist_candidate(self,candidate_status):
        self.select_dropdown("status_dropdown",candidate_status)
