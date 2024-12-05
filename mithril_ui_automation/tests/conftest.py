"""
Fixtures
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login import LoginPage
from pages.bd_page import BusinessDev
from pages.training_page import TrainingPage
from pages.dashboard_page import DashboardPage
from pages.batch_page import BatchPage
# pylint: disable=line-too-long

@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and quit the WebDriver."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    """
    Function for calling log in page.
    """
    return LoginPage(driver)

@pytest.fixture
def select_dropdown_option(driver):
    """
    Function to select dropdown options
    """
    def select_option(option_text):
        dropdown = driver.find_element(By.CSS_SELECTOR, ".ng-select-container")
        dropdown.click()
        option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option' and contains(text(), '{option_text}')]"))
        )
        option.click()
    return select_option

@pytest.fixture
def bd_page(driver):
    return BusinessDev(driver)

@pytest.fixture
def training_page(driver):
    return TrainingPage(driver)

@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver)

@pytest.fixture
def batch_page(driver):
    return BatchPage(driver)
