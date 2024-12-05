from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BatchPage:
    """
    Batch Page Object for navigating and interacting with the Batch page.
    """
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "batch_tb": (By.CSS_SELECTOR, "a[href='/training/batch/master']"),
            "add_batch_btn": (By.CSS_SELECTOR, "button.btn.btn-submit-swabhav.left-margin.material-icons-button.ng-star-inserted"),
            "batch_form": (By.CSS_SELECTOR, "div.modal-dialog.modal-xl"),
            "batch_name": (By.XPATH, "(//input[@placeholder='eg: Java01'])[2]"),
            "intake_field": (By.XPATH, "//input[@formcontrolname='totalIntake']"),
            "course_dropdown": (By.CSS_SELECTOR, "select.form-select.ng-untouched.ng-pristine.ng-invalid"),
            "select_salesperson": (By.XPATH,"(//select[@formcontrolname='salesPersonID'])[1]")
        }

    def click_element(self, locator_name, wait_time=10, action="click"):
        """
        Generic method to click or interact with an element.
        """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(self.locators[locator_name])
        )
        if action == "click":
            element.click()
        return element

    def navigate_to_batch(self):
        """Navigate to the Batch page."""
        self.click_element("batch_tb")

    def click_add_batch_btn(self):
        """Click the 'Add Batch' button."""
        self.click_element("add_batch_btn")

    def verify_form_appears(self):
        """Verify that the batch form is visible."""
        form = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators["batch_form"])
        )
        return form.is_displayed()

    def input_text(self, locator_name, text_value):
        """
        Input text into a field after clearing it.
        """
        input_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators[locator_name])
        )
        input_field.clear()
        input_field.send_keys(str(text_value))

    def verify_input_value(self, locator_name, expected_value):
        """
        Verify the input field contains the expected value.
        """
        field = self.driver.find_element(*self.locators[locator_name])
        actual_value = field.get_attribute("value").strip()
        assert actual_value == str(expected_value), f"Expected '{expected_value}' but got '{actual_value}'."

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

    def select_course_from_dropdown(self, course_name):
        """
        Select a course from the dropdown.
        """
        # Wait for the course dropdown to be visible
        dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators["course_dropdown"])  # Reference dictionary for course dropdown
        )

        # Create Select object and choose the option by visible text
        select = Select(dropdown_element)
        select.select_by_visible_text(course_name)

    def verify_course_selection(self, expected_course_name):
        """
        Verify that the selected course matches the expected course.
        """
        dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators["course_dropdown"])  # Reference dictionary for course dropdown
        )

        select = Select(dropdown_element)
        selected_option = select.first_selected_option
        actual_course_name = selected_option.text

        assert actual_course_name == expected_course_name, f"Expected course '{expected_course_name}', but got '{actual_course_name}'."

    def select_salesperson(self, salesperson):
        """
        Select a SalesPerson.
        """
        # Wait for the course dropdown to be visible
        dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators["select_salesperson"])  # Reference dictionary for course dropdown
        )

        # Create Select object and choose the option by visible text
        select = Select(dropdown_element)
        select.select_by_visible_text(salesperson)
        