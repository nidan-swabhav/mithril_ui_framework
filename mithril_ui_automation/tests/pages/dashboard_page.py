from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    """
    Page Object for the Dashboard.
    """
    def __init__(self, driver):
        self.driver = driver
        self.search = (By.XPATH,"//span[@class='search-menu text-center']/input[@type='search']")
        self.dropdown = (By.XPATH,"//div[@id='cdk-overlay-0']")
        self.business_dev_tab = (By.CSS_SELECTOR, "a.nav-link.menu-style.ng-star-inserted.active-menu")
        self.enquiries_tab = (By.CSS_SELECTOR, "a[href='/company/enquiry']")


    def search_and_select(self, search_text, select_text):
        """Enter search text and select a specific option from the dropdown."""
        search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search)
        )
        search_field.clear()  # Clear any previous input
        search_field.send_keys(search_text)  # Enter the search term

        # Wait for the dropdown to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.dropdown)
        )

        # Loop through the options and click the one matching 'select_text'
        dropdown_items = self.driver.find_elements(*self.dropdown)
        for item in dropdown_items:
            if select_text in item.text:  # Check if the option matches the text you want
                item.click()  # Click on the matching item
                break
        else:
            print(f"No matching option found for: {select_text}")
            raise Exception(f"Option with text '{select_text}' not found in the dropdown")

    def navigate_to_enquiries(self):
        """Click on the 'Enquiries' tab under 'Business Dev'."""
        try:
            # Wait for the overlay/spinner to disappear
            WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ngx-spinner-overlay"))
            )

            # Now, wait for the Enquiries tab to be clickable and click it
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.enquiries_tab)
            ).click()
            
            # Optionally, verify the page loaded correctly
            WebDriverWait(self.driver, 15).until(
                EC.url_contains("/company/enquiry")
            )

        except Exception as e:
            print(f"Error navigating to Enquiries: {e}")
            self.driver.save_screenshot("enquiries_navigation_error.png")
            raise

    def navigate_to_business_dev(self):
        """
        Click on the 'Business Dev' tab from the dashboard.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.business_dev_tab)
        ).click()
