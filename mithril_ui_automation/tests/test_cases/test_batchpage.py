"""
Tests for Batch Page
"""
import time
import pytest

# pylint: disable=line-too-long
@pytest.mark.Salesperson
@pytest.mark.parametrize("user_email, user_password, expected_role,expected_url",[
    ("nidan@swabhavtechlabs.com", "Dummy@123", "SalesPerson","https://tsm-uat.swabhavtechlabs.com/talent/matrix"),
    # ("aniket.pardeshi@swabhavtechlabs.com", "Dummy@123", "SalesPerson","https://tsm-uat.swabhavtechlabs.com/talent/matrix"),
])
def test_sales_login(select_dropdown_option,login_page,user_email,user_password,expected_url,expected_role,batch_page):
    """
    Test ID: 01
    Test Name: Test to check that Talent can log in
    Test Assignee: Nidan Gavali
    Test Importance: Moderate
    Test Steps:
        1. User accesses the login page.
        2. User adds credentials.
        3. User clicks on the login button.
    Expected Output: Talent can log in.
    """
    login_page.navigate_to_login()

    # Select "Team"
    login_page.select_team()
    login_page.select_role(select_dropdown_option,expected_role)

    # Enter credentials
    login_page.enter_credentials(user_email,user_password)

    # Click login button
    login_page.click_login()

    # Wait and validate successful login
    login_page.verify_login_url(expected_url)

    batch_page.navigate_to_batch()
    # batch_page.add_batch_btn()

    batch_page.click_add_new_batch_btn()

    batch_page.input_batch_name("Auto5")

    input_value = 5
    batch_page.input_intake(input_value)

    batch_page.verify_intake(input_value)

    course_name = "Amazon Web Services"  # Replace with the actual course name from the dropdown
    batch_page.select_course(course_name)
    # batch_page.verify_course_selection(course_name)

    salesperson = "Nidan Sales"
    batch_page.select_salesperson(salesperson)
    batch_page.verify_salesperson(salesperson)

    batch_page.select_batch_status("Upcoming")

    batch_page.select_batch_type("B2B")
    batch_page.input_and_select_requirement("MICSOFT001")

    batch_page.click_add_batch_btn()

    time.sleep(10)
