"""Tests for Training functionality"""
from pages.training_page import TrainingPage
# pylint: disable=line-too-long


def test_training_page_access(driver, login_page, select_dropdown_option,training_page):
    """
    Test to verify that the user can access the training page after logging in.
    """
    # Step 1: Log in
    login_page.navigate_to_login()
    login_page.select_team()
    login_page.select_role(select_dropdown_option, "Admin")
    login_page.enter_credentials("god@father.com", "Dummy@123")
    login_page.click_login()

    # Step 2: Navigate to the training page
    training_page = TrainingPage(driver)
    training_page.navigate_to_training_via_menu()

    # Step 3: Validate training page access
    assert driver.current_url == "https://tsm-uat.swabhavtechlabs.com/training/batch/master", \
        "Failed to reach training page after login."
