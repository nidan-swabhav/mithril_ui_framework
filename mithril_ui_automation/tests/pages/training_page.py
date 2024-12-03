from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TrainingPage:
    """
    Class for training page interactions.
    """
    def __init__(self, driver):
        self.driver = driver
        self.training_url = "https://tsm-uat.swabhavtechlabs.com/training/batch/master"
        self.training_btn = (By.CSS_SELECTOR, "a.nav-link.menu-style.ng-star-inserted.active-menu")
        self.add_batch_btn = (By.NAME, "Add New Batch")

    def navigate_to_training_via_menu(self):
        """
        Navigates to the training page via the application menu to preserve session.
        """
        # Locate and click the menu option for Training
        training_menu = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.nav-link.menu-style.ng-star-inserted"))
        )
        training_menu.click()

        # Wait until the training URL is loaded
        WebDriverWait(self.driver, 15).until(
            EC.url_contains("/training/batch/master"),
            "Failed to navigate to the training page."
        )

    def is_logged_out(self):

        """Checks if the user is logged out by looking for login elements."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "user-email"))
            )
            return True
        except TimeoutException:
            return False


    def add_batch(self):
        """
        Clicks the 'Add New Batch' button after ensuring it is clickable.
        """
        add_batch_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.add_batch_btn),
            "Add New Batch button is not clickable."
        )
        add_batch_button.click()
