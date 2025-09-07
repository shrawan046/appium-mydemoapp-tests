from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

class WebViewPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Locators
        self.catalog_menu_xpath = '//android.view.ViewGroup[@content-desc="open menu"]/android.widget.ImageView'
        self.webView_option_id = 'container header'
        self.header_webView_xpath = "//android.widget.TextView[@text='Webview']"
        self.url_input_box_id = 'URL input field'
        self.go_to_site_button_id = 'Go To Site button'
        self.error_message_xpath = "//*[@text='Please provide a correct https url.']"

    # Actions
    def click_on_catalog_menu(self):
        self.driver.find_element(AppiumBy.XPATH, self.catalog_menu_xpath).click()

    def click_webView(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.webView_option_id).click()

    def enter_url(self, url: str):
        input_box = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.url_input_box_id)
        input_box.clear()
        input_box.send_keys(url)

    def click_goto_button(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.go_to_site_button_id).click()

    # Getters (for assertions in tests)
    def get_header_text(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.header_webView_xpath).text

    def get_error_message(self):
        return self.driver.find_element(AppiumBy.XPATH, self.error_message_xpath).text
