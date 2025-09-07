from appium import webdriver
from appium.options.android import UiAutomator2Options
import yaml
import os


def load_config(platform: str):
    """Load config from YAML file based on platform key (android / android_app)."""
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)[platform]


def create_driver_android(platform: str = "android_app"):
    """Create and return an Appium driver for Android devices/emulators."""
    config = load_config(platform)

    options = UiAutomator2Options().load_capabilities({
        "platformName": config["platformName"],
        "appium:deviceName": config["deviceName"],
        "appium:platformVersion": config["platformVersion"],
        "appium:automationName": config["automationName"],
        "appium:app": config["app"],
        "appium:appPackage": config["appPackage"],
        "appium:appActivity": config["appActivity"],
        "appium:chromedriverAutodownload": config.get("chromedriverAutodownload", True),
        "appium:noReset": config["noReset"],
        "appium:newCommandTimeout": config["newCommandTimeout"],
        "appium:connectHardwareKeyboard": config["connectHardwareKeyboard"]
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)  # ✅ implicit wait so tests don’t fail on small delays
    return driver
