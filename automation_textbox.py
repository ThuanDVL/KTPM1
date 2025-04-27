# File: automation_textbox.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

# Nhập dữ liệu hợp lệ
fields = {
    "userName": "Nguyen Van Test",
    "userEmail": "test@example.com",
    "currentAddress": "Test Address 1",
    "permanentAddress": "Test Address 2"
}

for field_id, value in fields.items():
    driver.find_element(By.ID, field_id).send_keys(value)

driver.find_element(By.ID, "submit").click()
time.sleep(2)

# Kiểm tra kết quả
output = driver.find_element(By.ID, "output").text
assert all(val in output for val in fields.values())
print("✅ Automation Passed")

driver.quit()