
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigate_to_enquiries(login_page, dashboard_page, select_dropdown_option, driver):
    """
    Test to navigate from the login page to the Enquiries tab via the Business Dev tab.
    """
    # Step 1: Log in
    login_page.navigate_to_login()
    login_page.select_team()
    login_page.select_role(select_dropdown_option, "Admin")  # Adjust role as needed
    login_page.enter_credentials("god@father.com", "Dummy@123")
    login_page.click_login()

    # Validate navigation to dashboard
    dashboard_url = "https://tsm-uat.swabhavtechlabs.com/dashboard"
    WebDriverWait(driver, 15).until(
        EC.url_to_be(dashboard_url),
        f"Expected to be on {dashboard_url}, but was on {driver.current_url}"
    )
    assert driver.current_url == dashboard_url, "Failed to navigate to dashboard."

    # Step 2: Navigate to Business Development
    dashboard_page.navigate_to_business_dev()

    # Step 3: Navigate to Enquiries tab
    dashboard_page.navigate_to_enquiries()

    # Step 4: Validate navigation to Enquiries page
    expected_enquiry_url = "https://tsm-uat.swabhavtechlabs.com/company/enquiry?limit=20&offset=0&isActive=1"
    WebDriverWait(driver, 15).until(
        EC.url_to_be(expected_enquiry_url),
        f"Expected to be on {expected_enquiry_url}, but was on {driver.current_url}"
    )
    assert driver.current_url == expected_enquiry_url, "Failed to navigate to Enquiries page."
