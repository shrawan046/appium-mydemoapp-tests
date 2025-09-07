from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName' : "emulator-5554"
}

url = 'http://localhost:4723'

driver= webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value= 'Chrome')
el.click()
#driver.find_element(by=AppiumBy.XPATH, value= "//*[@text= 'Search Google or type URL'").send_keys("shrawan kumar")