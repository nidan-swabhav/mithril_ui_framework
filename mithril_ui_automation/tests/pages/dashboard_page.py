from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    """
    Page Object for the Dashboard.
    """
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "search_box" : (By.XPATH,"//span[@class='search-menu text-center']/input[@type='search']"),
            "dropdown" : (By.XPATH,"//div[@id='cdk-overlay-0']"),
            "business_dev_tab" : (By.XPATH, "//span[contains(text(),'Business Dev')]"),
            "enquiries_tab"  : (By.XPATH, "//a[normalize-space()='Enquiries']"),
        }

    def wait_for_element(self, locator_name, wait_time=10, condition=EC.visibility_of_element_located):
        """
        Generic method to wait for an element based on a specific condition.
        """
        return WebDriverWait(self.driver, wait_time).until(
            condition(self.locators[locator_name])
        )

    def click_element(self, locator_name):
        """Click on an element after ensuring it's clickable."""
        element = self.wait_for_element(locator_name, condition=EC.element_to_be_clickable)
        element.click()

    def select_bd_tab(self):
        """Navigate to the Batch page."""
        self.click_element("business_dev_tab")
