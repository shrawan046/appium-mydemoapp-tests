from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from drivers.chrome_driver_factory import create_driver_android


class AboutPage:
    HEADER_NAME = "About"
    TITLE_NAME= 'SAUCELABS'
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.group_of_pages = 'android.view.ViewGroup'
        self.click_menu_item_id ='menu item about'
        self.header_ui_automater='new UiSelector().text("About")'
        self.header_demo_app_ui_automater='new UiSelector().className("android.widget.ImageView").instance(3)'
        self.title_ui_automater ='new UiSelector().className("android.widget.ImageView").instance(4)'
        self.click_on_website_link ='//android.widget.TextView[@text="Go to the Sauce Labs website."]'


    def click_about(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.click_menu_item_id).click()

    def verify_header(self):
        el_text = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.header_ui_automater).text
        print(el_text)
        return el_text == self.HEADER_NAME

    def verify_title(self):
        el_image= self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.title_ui_automater)
        assert el_image.is_displayed()

    def go_to_website_without_chrome(self):
        # Tap on the element
        el = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Go to the Sauce Labs website.")'
        )
        rect = el.rect
        x = rect['x'] + rect['width'] / 2
        y = rect['y'] + rect['height'] / 2

        actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.pointer_action.move_to_location(x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pointer_up()
        actions.perform()

        # ✅ Verify Chrome is launched
        current_package = self.driver.current_package
        assert "chrome" in current_package.lower()

    from drivers.android_driver_factory import create_driver_android

    def go_to_website(self):
        # Step 1: tap link in AUT
        el = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Go to the Sauce Labs website.")'
        )
        rect = el.rect
        x = rect['x'] + rect['width'] / 2
        y = rect['y'] + rect['height'] / 2

        actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.pointer_action.move_to_location(x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pointer_up()
        actions.perform()

        # Step 2: launch Chrome driver session using chrome_browser profile
        chrome_driver = create_driver_android("chrome_browser")

        try:
            current_url = chrome_driver.current_url
            print("Chrome URL:", current_url)
            assert "saucelabs.com" in current_url.lower()

            heading = chrome_driver.find_element("xpath", "//h1[contains(.,'Build apps users love')]")
            assert heading.is_displayed()
        finally:
            chrome_driver.quit()

    def verify_web_page(self):
        self.driver.switch_to.context("WEBVIEW_chrome")
        heading = self.driver.find_element("xpath", "//h1[contains(.,'Build apps users love')]")
        assert heading.is_displayed()
        self.driver.switch_to.context("NATIVE_APP")



