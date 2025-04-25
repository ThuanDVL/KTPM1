import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestDemoQAForm(unittest.TestCase):
    def setUp(self):
        """Khởi tạo trình duyệt"""
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.maximize_window()

    def test_fill_form(self):
        """Test điền form và xác nhận gửi thành công"""
        driver = self.driver

        # Step 1: Nhập First Name
        driver.find_element(By.ID, "firstName").send_keys("Ngo")

        # Step 2: Nhập Last Name
        driver.find_element(By.ID, "lastName").send_keys("Quoc Khanh")

        # Step 3: Nhập Email
        driver.find_element(By.ID, "userEmail").send_keys("khanh104087@donga.edu.vn.com")

        # Step 4: Chọn giới tính
        driver.find_element(By.XPATH, "//label[text()='Male']").click()

        # Step 5: Nhập số điện thoại
        driver.find_element(By.ID, "userNumber").send_keys("0123456789")

        # Step 6: Chọn ngày sinh
        driver.find_element(By.ID, "dateOfBirthInput").click()
        driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("2000")
        driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("January")
        driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='1']").click()

        # Step 7: Nhập Subject
        subject = driver.find_element(By.ID, "subjectsInput")
        subject.send_keys("Maths")
        subject.send_keys(Keys.RETURN)

        # Step 8: Chọn Hobbies
        driver.find_element(By.XPATH, "//label[text()='Sports']").click()

        # Step 9: Nhập địa chỉ
        driver.find_element(By.ID, "currentAddress").send_keys("123 Đường ABC, Quận XYZ, Thành phố HCM")

        # Step 10: Chọn State và City
        driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
        driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.RETURN)
        driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
        driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.RETURN)

        # Step 11: Click Submit (dùng JS click để tránh lỗi không thấy phần tử)
        driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "submit"))

        # Step 12: Kiểm tra form được submit thành công
        modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "modal-content"))
        )
        self.assertIn("Thanks for submitting the form", modal.text)

        print("✅ Test Passed: Form đã được gửi thành công!")

    def tearDown(self):
        """Đóng trình duyệt sau khi test"""
        time.sleep(3)  # Đợi xem kết quả trước khi đóng
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
