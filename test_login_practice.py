import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Practice Test Automation Login Test")
@allure.description("Test login functionality on practicetestautomation.com with valid credentials.")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_practice_site():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open login page"):
            driver.get("https://practicetestautomation.com/practice-test-login/")

        with allure.step("Enter username and password"):
            username = driver.find_element(By.ID, "username")
            username.send_keys("student")
            password = driver.find_element(By.ID, "password")
            password.send_keys("Password123")

        with allure.step("Click submit button"):
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()

        with allure.step("Validate login success message"):
            driver.implicitly_wait(3)
            msg = driver.find_element(By.TAG_NAME, "h1").text
            allure.attach(msg, name="Login Result Text", attachment_type=allure.attachment_type.TEXT)

            assert "Logged In Successfully" in msg, "Login failed: Success message not found."

    except Exception as e:
        try:
            allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        except:
            pass
        raise e

    finally:
        driver.quit()
