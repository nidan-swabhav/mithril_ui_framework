import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """Fixture to initialize and quit the WebDriver."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def select_dropdown_option(driver):
    """Fixture to select an option from the dropdown."""

    def _select_dropdown_option(option_text):
        # Locate the dropdown container
        dropdown_container = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.ng-select-container'))
        )

        # Click the dropdown to open it
        dropdown_container.click()

        # Locate the option element by its text content
        option_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@role='option' and contains(text(), '{option_text}')]")
            )
        )

        # Click the option to select it
        option_element.click()

    return _select_dropdown_option

def test_dropdown_selection(driver, select_dropdown_option):
    """Test case to verify dropdown selection."""

    # Open the webpage (use the appropriate URL)
    driver.get("https://tsm-uat.swabhavtechlabs.com/login")

    driver.maximize_window()

    talent_btn = driver.find_element(By.XPATH,"//button[@class='btn btn-outline-primary']")
    talent_btn.click()

    # Select an option from the dropdown
    select_dropdown_option("Admin")  # Replace "Talent" with the desired option text

    # Add assertions to verify the selection
    selected_option = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ng-value"))
    )
    assert "Admin" in selected_option.text

    username = driver.find_element(By.ID,"user-email")
    username.send_keys("god@father.com")

    password = driver.find_element(By.ID,"user-password")
    password.send_keys("Dummy@123")

    login_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
    login_btn.click()

    time.sleep(30)

