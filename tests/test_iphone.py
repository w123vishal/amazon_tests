from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.amazon_page import AmazonPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_iphone():
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    page = AmazonPage(driver)
    try:
        page.go_to_homepage()
        page.search_product("iPhone")
        sleep(5)
        page.click_first_product()
        sleep(2)
        page.add_to_cart()
        sleep(3)
        price = page.get_price()
        logger.info(f"iPhone Price: {price}")
    finally:
        driver.quit()
