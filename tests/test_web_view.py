from selenium.webdriver.ie.webdriver import WebDriver

from pages.webView_page import WebViewPage

def test_invalid_url(driver):
    page= WebViewPage(driver)
    page.click_on_catalog_menu()
    page.click_webView()
    #assert page.get_header_text() =="Webview"
    page.enter_url("https://google.com")
    page.click_goto_button()
    assert page.get_error_message() == 'Please provide a correct https url.'