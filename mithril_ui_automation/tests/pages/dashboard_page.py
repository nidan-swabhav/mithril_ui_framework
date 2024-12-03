from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    """
    Page Object for the Dashboard.
    """
    def __init__(self, driver):
        self.driver = driver
        self.business_dev_tab = (By.XPATH, "//a[contains(text(),'Business Dev')]")
        self.enquiries_tab = (By.XPATH, "//a[contains(text(),'Enquiries')]")

    def navigate_to_business_dev(self):
        """
        Click on the 'Business Dev' tab from the dashboard.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.business_dev_tab)
        ).click()

    def navigate_to_enquiries(self):
        """
        Click on the 'Enquiries' tab under 'Business Dev'.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.enquiries_tab)
        ).click()
