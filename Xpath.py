from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.product_image = (By.XPATH, "//img[contains(@class, 'image-gallery-image')]")
        self.product_name = (By.XPATH, "//h2[contains(@class, 'chakra-heading')]")
        self.product_description = (
            By.XPATH, "//div[contains(@class, 'chakra-card__body')]/p[contains(text(), 'Description')]"
        )
        self.product_price = (
            By.XPATH, "//div[contains(@class, 'chakra-card__body')]/p[contains(text(), '$')]"
        )
        self.login_button = (By.XPATH, "//a[@href='/signin']")
        self.register_button = (By.XPATH, "//a[@href='/signup']")
        self.add_to_bag_button = (
            By.XPATH, "//button[contains(text(), 'Add to Cart') or contains(text(), 'Add to Bag')]"
        )

    def click_login_button(self):
        """Click nút đăng nhập"""
        self.driver.find_element(*self.login_button).click()

    def click_register_button(self):
        """Click nút đăng ký"""
        self.driver.find_element(*self.register_button).click()

    def click_add_to_bag_button(self):
        """Click nút thêm vào giỏ hàng"""
        self.driver.find_element(*self.add_to_bag_button).click()

    def get_product_name(self):
        """Lấy tên sản phẩm (có xử lý lỗi nếu không tìm thấy)"""
        return self._get_text_safe(self.product_name)

    def get_product_description(self):
        """Lấy mô tả sản phẩm"""
        return self._get_text_safe(self.product_description)

    def get_product_price(self):
        """Lấy giá sản phẩm"""
        return self._get_text_safe(self.product_price)

    def is_product_image_displayed(self):
        """Kiểm tra ảnh sản phẩm có hiển thị không"""
        try:
            return self.driver.find_element(*self.product_image).is_displayed()
        except NoSuchElementException:
            return False

    def _get_text_safe(self, locator):
        """Hàm phụ để lấy text an toàn"""
        try:
            return self.driver.find_element(*locator).text
        except NoSuchElementException:
            return "[Không tìm thấy]"
