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
