import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def setup_browser(request):
    """Fixture to set up and tear down the WebDriver."""
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://tsm-uat.swabhavtechlabs.com/forms/register?code=MICSOFT004&type=req&src=em&reccode=ANI6920331")
    request.cls.browser = browser  # Attach the browser to the test class
    yield
    browser.quit()

@pytest.mark.usefixtures("setup_browser")
class TestUserAddForm:
    """Test class for the user add form."""

    def fill_input(self, xpath, value):
        """Helper method to fill input fields."""
        input_element = self.browser.find_element(By.XPATH, xpath)
        input_element.clear()
        input_element.send_keys(value)

    @pytest.mark.parametrize("fname, lname, phone, email, linkedin", [
        ("Nidan", "Gavali", "1234567890", "testuser1@gmail.com", "www.linkedin.com/user1"),
        ("John", "Doe", "9876543210", "testuser2@gmail.com", "www.linkedin.com/user2"),
    ])
    def test_fill_user_form(self, fname, lname, phone, email, linkedin):
        """Test the user form with parameterized data."""
        # Fill form fields with parameterized data
        self.fill_input("(//input[@placeholder='eg. John'])[1]", fname)
        self.fill_input("(//input[@placeholder='eg. Doe'])[1]", lname)
        self.fill_input("(//input[@placeholder='eg. 9877865643'])[1]", phone)
        self.fill_input("(//input[@placeholder='eg. johndoe@gmail.com'])[1]", email)
        self.fill_input("(//input[@formcontrolname='linkedInUrl'])[1]", linkedin)

        # Click the Next button
        next_btn = self.browser.find_element(By.XPATH, "(//button[@type='submit'][normalize-space()='Next'])[1]")
        next_btn.click()

        # Wait for potential next page or response
        time.sleep(5)

        # Example assertion to check for form submission
        assert "success" in self.browser.page_source.lower(), "Form submission failed or did not progress as expected."
