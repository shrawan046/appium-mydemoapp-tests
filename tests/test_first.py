from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

def test_launch_app():
    caps = {
        "platformName": "Android",
        "appium:platformVersion": "16.0",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:app": "D:\\ApiDemos-debug.apk",  # change if path differs
        "appium:noReset": True
    }

    # Start a session
    driver = webdriver.Remote("http://127.0.0.1:4723", options=AppiumOptions().load_capabilities(caps))

    # Small pause to let app load
    time.sleep(2)

    # Example: Tap "App" menu on ApiDemos home screen
    app_menu = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "App")
    app_menu.click()

    time.sleep(2)

    # Example: Tap "Alert Dialogs"
    alert_dialogs = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alert Dialogs")
    alert_dialogs.click()

    time.sleep(2)

    # Verify that "OK Cancel dialog with a message" option is visible
    dialog_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OK Cancel dialog with a message")
    assert dialog_option.is_displayed()

    driver.quit()
