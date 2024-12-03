"""Tests for Log in functionality"""

import pytest
# pylint: disable=line-too-long

@pytest.mark.smoke
@pytest.mark.parametrize("user_email, user_password, expected_role,expected_url",[
    ("god@father.com", "Dummy@123", "Admin","https://tsm-uat.swabhavtechlabs.com/dashboard"),
    ("aniket.pardeshi@swabhavtechlabs.com", "Dummy@123", "SalesPerson","https://tsm-uat.swabhavtechlabs.com/talent/matrix"),
])
def test_team_login(login_page, select_dropdown_option, user_email, user_password, expected_role, expected_url):
    """
    Test ID: 01
    Test Name: Test to check that team can log in.
    Test Assignee: Nidan Gavali
    Test Importance: Moderate
    Test Steps:
        1. User accesses the login page.
        2. User selects the role.
        3. User adds credentials.
        4. User clicks on the login button.
    Expected Output: User can log in.
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

@pytest.mark.parametrize("user_email, user_password,expected_url",[
    ("jayeshborse7777@gmail.com", "Dummy@123","https://tsm-uat.swabhavtechlabs.com/talent/dashboard?batchID=2925cc4b-b03c-44e3-a9ea-93865d50fe9e"),
])
def test_talent_login(login_page,user_email,user_password,expected_url):
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

    login_page.select_talent()

    # Enter credentials
    login_page.enter_credentials(user_email,user_password)

    # Click login button
    login_page.click_login()

    # Wait and validate successful login
    login_page.verify_login_url(expected_url)

# def test_bd_login(driver, select_dropdown_option):
#     """
#     Test ID: 01
#     Test Name: Test to check that user can Admin log in.
#     Test Assignee : Nidan Gavali
#     Test Importance: Moderate
#     Test steps:
#                     1.User access the login page.
#                     2.User selects the Admin role.
#                     3.User Adds credentials.
#                     4.User clicks on login button.
#     Expected Output: User can Log in using admin credentials.
#     """

#     # Open the webpage
#     driver.get("https://tsm-uat.swabhavtechlabs.com/login")

#     #Maximize the window
#     driver.maximize_window()

#     #select from Talent or Team.
#     talent_btn = driver.find_element(By.XPATH,"//button[@class='btn btn-outline-primary']")
#     talent_btn.click()

#     # Select an option from the dropdown
#     select_dropdown_option("BD")  # Replace "Talent" with the desired option text

#     # Add assertions to verify the selection
#     selected_option = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".ng-value"))
#     )
#     assert "BD" in selected_option.text

#     # Add Admin Credentials
#     username = driver.find_element(By.ID,"user-email")
#     username.send_keys("aniket.pardeshi@swabhavtechlabs.com")

#     password = driver.find_element(By.ID,"user-password")
#     password.send_keys("Dummy@123")

#     #Click on Login Button
#     login_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
#     login_btn.click()

#     time.sleep(10)
