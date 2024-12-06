"""
Tests for Requirements Page
"""
import time
import pytest

# pylint: disable=line-too-long
@pytest.mark.Req
@pytest.mark.parametrize("user_email, user_password, expected_role,expected_url",[
    ("nidan@swabhavtechlabs.com", "Dummy@123", "SalesPerson","https://tsm-uat.swabhavtechlabs.com/talent/matrix")
])
def test_requirement_page(select_dropdown_option,login_page,user_email,user_password,expected_url,expected_role,requirements_page):
    """
    Test ID: 01
    Test Name: Test to check Reuirement navigation
    Test Assignee: Nidan Gavali
    Test Importance: Moderate
    Test Steps:
        1. User accesses the login page.
        2. User adds credentials.
        3. User clicks on the login button.
    Expected Output: Talent can access requirement.
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

    requirements_page.navigate_to_requirements_pg()

    requirements_page.click_view_details()

    requirements_page.click_candidate_count()

    requirements_page.click_status()
    candidate_status = "Shortlisted"
    requirements_page.shortlist_candidate(candidate_status)
    # requirements_page.click_edit()



    time.sleep(20)