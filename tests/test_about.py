
from pages.aboutPage import AboutPage

from pages.webView_page import WebViewPage

def test_about_content(driver):
    page= WebViewPage(driver)
    about_page= AboutPage(driver)
    page.click_on_catalog_menu()
    about_page.click_about()
    assert about_page.verify_header()
    about_page.verify_title()
    about_page.go_to_website_without_chrome()
    #about_page.verify_web_page()