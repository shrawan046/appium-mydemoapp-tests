from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

def test_click_catalog():
    caps = {
          "platformName": "Android",
          "appium:platformVersion": "16.0",
          "appium:deviceName": "emulator-5554",
          "appium:automationName": "UiAutomator2",
          "appium:app": "D:\\app\\MyDemoApp.apk",
          "appium:noReset": True,
          "appium:appPackage": "com.saucelabs.mydemoapp.rn",
          "appium:appActivity": "com.saucelabs.mydemoapp.rn.MainActivity",
          "appium:ensureWebviewsHavePages": True,
          "appium:nativeWebScreenshot": True,
          "appium:newCommandTimeout": 3600,
          "appium:connectHardwareKeyboard": True
}


    # Start a session
    url = 'http://127.0.0.1:4723'

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps))
    # Small pause to let app load
    driver.implicitly_wait(10)
    el= driver.find_element(AppiumBy.XPATH, value= '//android.view.ViewGroup[@content-desc="open menu"]/android.widget.ImageView')
    el.click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'container header').click()
    driver.quit()

if __name__ == "__main__":
    test_click_catalog()
