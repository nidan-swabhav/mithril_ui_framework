"""
Login class functionality
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# pylint: disable=line-too-long

class LoginPage:
    """
    Login Class
    """
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tsm-uat.swabhavtechlabs.com/login"
        self.talent_btn = (By.XPATH, "//button[@class='btn btn-primary']")
        self.team_btn = (By.XPATH, "//button[@class='btn btn-outline-primary']")
        self.user_email = (By.ID, "user-email")
        self.user_password = (By.ID, "user-password")
        self.login_btn = (By.XPATH, "//button[contains(text(),'Login')]")
        self.selected_role = (By.CSS_SELECTOR, ".ng-value")

    def navigate_to_login(self):
        """
        function to navigate to login page
        """
        self.driver.get(self.url)
        self.driver.maximize_window()

    def select_talent(self):
        """
        function to select the type of user
        """
        self.driver.find_element(*self.talent_btn).click()

    def select_team(self):
        """
        function to select the type of user
        """
        self.driver.find_element(*self.team_btn).click()


    def select_role(self, select_dropdown_option, role):
        """
        function to select the role from dropdwon.
        """
        select_dropdown_option(role)
        selected_option = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.selected_role)
        )
        assert role in selected_option.text, f"Expected role {role} not found in dropdown."

    def enter_credentials(self, email, password):
        """
        function to enter the credentials
        """
        self.driver.find_element(*self.user_email).send_keys(email)
        self.driver.find_element(*self.user_password).send_keys(password)

    def click_login(self):
        """
        function to click on login page.
        """
        self.driver.find_element(*self.login_btn).click()

    def verify_login_url(self, expected_url):
        """
        function to verify login page
        """
        WebDriverWait(self.driver, 15).until(EC.url_to_be(expected_url))
        assert self.driver.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.current_url}"
