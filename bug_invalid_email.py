# File: bug_invalid_email.py

"""
Bug Report: Submit Text Box với email sai định dạng
Steps:
1. Truy cập https://demoqa.com/text-box
2. Nhập email sai định dạng (vd: 'abc123')
3. Nhấn Submit
4. Hệ thống vẫn chấp nhận và hiển thị dữ liệu sai
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

driver.find_element(By.ID, "userName").send_keys("Nguyen Van B")
driver.find_element(By.ID, "userEmail").send_keys("abc123")  # Email sai
driver.find_element(By.ID, "currentAddress").send_keys("Some Address")
driver.find_element(By.ID, "permanentAddress").send_keys("Other Address")

driver.find_element(By.ID, "submit").click()
time.sleep(2)

output = driver.find_element(By.ID, "output").text
print("🔍 Output sau submit với email sai:", output)

# Expected: Không nên hiển thị output
if "abc123" in output:
    print("❌ Bug: Hệ thống chấp nhận email sai định dạng!")
else:
    print("✅ Passed: Email sai bị từ chối.")

driver.quit()