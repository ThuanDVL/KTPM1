# File: test_case_textbox.py

"""
Test Case: Submit Text Box form with valid inputs
Steps:
1. Truy cập trang https://demoqa.com/text-box
2. Nhập đầy đủ thông tin hợp lệ
3. Nhấn Submit
4. Kiểm tra kết quả hiển thị đúng
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

# Điền thông tin
driver.find_element(By.ID, "userName").send_keys("Nguyen Van A")
driver.find_element(By.ID, "userEmail").send_keys("email@example.com")
driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street")
driver.find_element(By.ID, "permanentAddress").send_keys("456 Another Street")

# Submit form
driver.find_element(By.ID, "submit").click()
time.sleep(2)

# Kiểm tra output
output = driver.find_element(By.ID, "output").text
assert "Nguyen Van A" in output
assert "email@example.com" in output
print("✅ TC Passed")

driver.quit()