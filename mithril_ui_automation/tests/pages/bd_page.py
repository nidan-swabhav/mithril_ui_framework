from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BusinessDev:
    """
    Page Object for the Business Development (BD) Page.
    """
    def __init__(self, driver):
        self.driver = driver
        self.enquiry_nav = (By.XPATH, "//a[contains(text(),'Enquiries')]")
        self.enquiry_url = "https://tsm-uat.swabhavtechlabs.com/company/enquiry"

    def navigate_to_enquiry(self):
        """
        Navigate to the Enquiry Page using the menu.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.enquiry_nav)
        ).click()

        # Validate the navigation
        WebDriverWait(self.driver, 15).until(
            EC.url_to_be(self.enquiry_url),
            "Failed to navigate to the Enquiry Page."
        )
