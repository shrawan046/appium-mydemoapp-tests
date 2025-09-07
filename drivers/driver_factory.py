from appium import webdriver
from appium.options.android import UiAutomator2Options
import yaml

def create_driver(platform="android"):
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)[platform]

    options = UiAutomator2Options().load_capabilities({
        "platformName": config["platformName"],
        "appium:deviceName": config["deviceName"],
        "appium:platformVersion": config["platformVersion"],
        "appium:automationName": config["automationName"],
        "appium:app": config["app"],
        "appium:appPackage": config["appPackage"],
        "appium:appActivity": config["appActivity"],
        "appium:noReset": config["noReset"],
        "appium:newCommandTimeout": config["newCommandTimeout"],
        "appium:connectHardwareKeyboard": config["connectHardwareKeyboard"]
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver
