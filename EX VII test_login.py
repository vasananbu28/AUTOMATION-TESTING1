
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from datetime import datetime

# Page class for Login Page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.ID, "submit")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

class SecureAreaPage:
    def __init__(self, driver):
        self.driver = driver
        self.message_header = (By.TAG_NAME, "h1")

    def get_message(self):
        return self.driver.find_element(*self.message_header).text

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()

def test_login_valid_user(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("student")
    login_page.enter_password("Password123")

    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"screenshots/screenshot_{timestamp}.png"
    driver.save_screenshot(file_name)
    print(f"Screenshot saved as: {file_name}")

    login_page.click_submit()

    secure_area = SecureAreaPage(driver)
    msg = secure_area.get_message()
    assert "Logged In Successfully" in msg, "Login failed"
