from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AmazonPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def go_to_homepage(self):
        self.driver.get("https://www.amazon.in")
        self.driver.maximize_window()

    def search_product(self, keyword):
        search_box = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='twotabsearchtextbox']")))
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
                                                                        

    def click_first_product(self):
        logger.info("Clicking on the first product...")
        first_product = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result'] a")
        ))

        first_product.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])


    def add_to_cart(self):
        try:
            add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']")))
            add_button.click()
        except Exception as e:
            self.driver.save_screenshot("add_to_cart_fail.png")
            raise e


    def get_price(self):
        try:
            price = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='attach-accessory-cart-subtotal']")))
            return price.text
        except:
            return "Price not found"
