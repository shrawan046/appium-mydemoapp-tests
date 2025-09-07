import yaml
from appium import webdriver
from appium.options.android import UiAutomator2Options


def load_config(profile: str):
    with open("config.yaml", "r") as f:
        configs = yaml.safe_load(f)
    return configs[profile]


def create_driver_android(profile: str = "android_app"):
    """Create and return an Appium driver based on profile."""
    config = load_config(profile)

    options = UiAutomator2Options().load_capabilities({
        "platformName": config["platformName"],
        "appium:deviceName": config["deviceName"],
        "appium:platformVersion": config["platformVersion"],
        "appium:automationName": config["automationName"],
        "appium:app": config.get("app"),   # only for app profile
        "appium:appPackage": config.get("appPackage"),
        "appium:appActivity": config.get("appActivity"),
        "appium:browserName": config.get("browserName"),
        "appium:adbExecTimeout": config.get("adbExecTimeout"),
        "appium:noReset": config["noReset"],
        "appium:newCommandTimeout": config.get("newCommandTimeout", 300),
        "appium:connectHardwareKeyboard": config.get("connectHardwareKeyboard", True),
        "appium:chromedriverAutodownload": config.get("chromedriverAutodownload", True)
    })
    return webdriver.Remote("http://127.0.0.1:4723", options=options)
