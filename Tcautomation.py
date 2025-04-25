import unittest
import configparser
import HtmlTestRunner
import sys
import os
from selenium.webdriver.common.by import By

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class ST23ATestCaseAuto(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get("https://demoqa.com/webtables")  # Có thể thay bằng self.login_url nếu cần

    def test_enter_data_successfully(self):
        # Step 1: Tap on Add button
        btnAdd = self.driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']")
        btnAdd.click()

        # Step 2: Enter firstname = 'Duy'
        txtFirstName = self.driver.find_element(By.XPATH, "//input[@id='firstName']")
        txtFirstName.send_keys("Duy")

        # Step 3: Enter lastname = 'Le'
        txtLastName = self.driver.find_element(By.XPATH, "//input[@id='lastName']")
        txtLastName.send_keys("Le")

        # Step 4: Enter Email = 'leduy@donga.edu.vn'
        txtEmail = self.driver.find_element(By.ID, "userEmail")
        txtEmail.send_keys("leduy@donga.edu.vn")

        # Step 5: Enter Age = '18'
        txtAge = self.driver.find_element(By.CSS_SELECTOR, "#age")
        txtAge.send_keys("18")

        # Step 6: Enter Salary = '20000000'
        txtSalary = self.driver.find_element(By.XPATH, "//input[@id='salary']")
        txtSalary.send_keys("20000000")

        # Step 7: Enter Department = 'IT'
        txtDepartMent = self.driver.find_element(By.XPATH, "//input[@id='department']")
        txtDepartMent.send_keys("IT")

        # Step 8: Click submit button
        self.driver.find_element(By.ID, "submit").click()

        # Step 9: Check data appears on table
        table = self.driver.find_element(By.XPATH, "//div[@class='rt-table']")
        self.assertIn("leduy@donga.edu.vn", table.text, "❌ Thêm dữ liệu thất bại!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
