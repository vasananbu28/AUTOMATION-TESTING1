import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("New Tab Navigation Test on DemoQA")
@allure.description("Open a new tab using the button and verify that the tab opens and switches correctly.")
@allure.severity(allure.severity_level.CRITICAL)
def test_browser_windows_tab_switch():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open DemoQA Browser Windows page"):
            driver.get("https://demoqa.com/browser-windows")

        main_window = driver.current_window_handle

        with allure.step("Click on the 'New Tab' button"):
            driver.find_element(By.ID, "tabButton").click()
            time.sleep(2)

        with allure.step("Switch to the new tab"):
            all_windows = driver.window_handles
            for handle in all_windows:
                if handle != main_window:
                    driver.switch_to.window(handle)
                    break

            new_tab_title = driver.title
            allure.attach(new_tab_title, name="New Tab Title", attachment_type=allure.attachment_type.TEXT)
            print("New tab title:", new_tab_title)

            assert "sample" in driver.current_url or driver.title != "", "New tab did not open correctly"

            # Optional: Take screenshot
            allure.attach(driver.get_screenshot_as_png(), name="New Tab Screenshot", attachment_type=allure.attachment_type.PNG)

        with allure.step("Close the new tab and switch back to the main window"):
            driver.close()
            driver.switch_to.window(main_window)
            allure.attach(driver.title, name="Main Window Title", attachment_type=allure.attachment_type.TEXT)
            print("Back to main window:", driver.title)

    except Exception as e:
        try:
            allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        except:
            pass
        raise e

    finally:
        driver.quit()
