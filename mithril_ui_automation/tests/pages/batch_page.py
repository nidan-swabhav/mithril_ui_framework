"""Batch Page File"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# pylint: disable=line-too-long
class BatchPage:
    """
    Batch Page Object for navigating and interacting with the Batch page.
    """
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "batch_tb": (By.CSS_SELECTOR, "a[href='/training/batch/master']"),
            "add_new_batch_btn": (By.CSS_SELECTOR, "button.btn.btn-submit-swabhav.left-margin.material-icons-button.ng-star-inserted"),
            "batch_form": (By.CSS_SELECTOR, "div.modal-dialog.modal-xl"),
            "batch_name": (By.XPATH, "(//input[@placeholder='eg: Java01'])[2]"),
            "intake_field": (By.XPATH, "//input[@formcontrolname='totalIntake']"),
            "course_dropdown": (By.XPATH, "//select[@class='form-select ng-untouched ng-pristine ng-invalid'][1]"),
            "select_salesperson": (By.XPATH, "(//select[@formcontrolname='salesPersonID'])[1]"),
            "batch_status": (By.XPATH, "(//select[@class='form-select ng-untouched ng-pristine ng-valid'])[5]"),
            "batch_type": (By.XPATH, "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[8]/select[1]"),
            "requirement_input": (By.XPATH, "//ng-select[@placeholder='Select requirement']//input[@type='text']"),
            "requirement_option": (By.XPATH, "//div[@role='listbox']"),
            "add_batch_btn": (By.XPATH, "//button[normalize-space()='Add Batch']"),
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

    def input_text(self, locator_name, text_value):
        """
        Input text into a field after clearing it.
        """
        input_field = self.wait_for_element(locator_name)
        input_field.clear()
        input_field.send_keys(str(text_value))

    def select_dropdown(self, locator_name, visible_text):
        """
        Select an option from a dropdown by visible text.
        """
        dropdown_element = self.wait_for_element(locator_name)
        select = Select(dropdown_element)
        select.select_by_visible_text(visible_text)

    def verify_input_value(self, locator_name, expected_value):
        """
        Verify the input field contains the expected value.
        """
        field = self.driver.find_element(*self.locators[locator_name])
        actual_value = field.get_attribute("value").strip()
        assert actual_value == str(expected_value), f"Expected '{expected_value}' but got '{actual_value}'."

    def verify_dropdown_selection(self, locator_name, expected_text):
        """
        Verify the selected option in a dropdown matches the expected text.
        """
        dropdown_element = self.driver.find_element(*self.locators[locator_name])
        select = Select(dropdown_element)
        selected_option = select.first_selected_option
        actual_text = selected_option.text
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'."

    def input_and_select_requirement(self, requirement_text):
        """
        Input a requirement and select an option from the displayed list.
        """
        # Step 1: Input text into the requirement field
        input_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators["requirement_input"])
        )
        input_field.clear()
        input_field.send_keys(requirement_text)

        # Step 2: Wait for options to appear
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.locators["requirement_option"])
        )

        # Step 3: Select the first matching option
        for option in options:
            if requirement_text.lower() in option.text.lower():
                option.click()
                return

        # Step 4: Raise an exception if no matching option is found
        raise Exception(f"No matching option found for '{requirement_text}'")
    
    def verify_batch_creation(self):
        """Verify the batch creation success message or new batch in the list."""
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='success-message-class']"))  # Replace with actual locator
        )
        assert "Batch created successfully" in success_message.text, "Batch creation failed or success message not displayed."


    def navigate_to_batch(self):
        """Navigate to the Batch page."""
        self.click_element("batch_tb")

    def click_add_new_batch_btn(self):
        """Click the 'Add Batch' button."""
        self.click_element("add_new_batch_btn")

    def verify_form_appears(self):
        """Verify that the batch form is visible."""
        form = self.wait_for_element("batch_form")
        return form.is_displayed()

    def input_batch_name(self, batch_name):
        """Input batch name into the form."""
        self.input_text("batch_name", batch_name)

    def verify_batch_name(self, expected_name):
        """Verify the batch name input matches the expected value."""
        self.verify_input_value("batch_name", expected_name)

    def input_intake(self, intake_value):
        """Input integer value into the Intake field."""
        if not isinstance(intake_value, int):
            raise ValueError(f"Expected an integer, but got {type(intake_value).__name__}")
        self.input_text("intake_field", intake_value)

    def verify_intake(self, expected_value):
        """Verify the Intake field contains the expected integer value."""
        self.verify_input_value("intake_field", expected_value)

    def select_course(self, course_name):
        """Select a course from the dropdown."""
        self.select_dropdown("course_dropdown", course_name)

    def verify_course_selection(self, expected_course_name):
        """Verify that the selected course matches the expected course."""
        self.verify_dropdown_selection("course_dropdown", expected_course_name)

    def select_salesperson(self, salesperson):
        """Select a SalesPerson."""
        self.select_dropdown("select_salesperson", salesperson)

    def verify_salesperson(self, expected_salesperson):
        """Verify that the selected salesperson matches the expected salesperson."""
        self.verify_dropdown_selection("select_salesperson", expected_salesperson)

    def select_batch_status(self, batch_status):
        """Select a Batch Status."""
        self.select_dropdown("batch_status", batch_status)

    def select_batch_type(self, batch_type):
        """Select a Batch Type."""
        self.select_dropdown("batch_type", batch_type)

    def select_requirement(self, requirement):
        """Select a Batch Requirement."""
        self.select_dropdown("requirement", requirement)

    def click_add_batch_btn(self):
        """Click the 'Add Batch' button."""
        self.click_element("add_batch_btn")

