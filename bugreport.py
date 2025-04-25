from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re  # Import thư viện regex để kiểm tra số điện thoại

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Hàm kiểm tra số điện thoại hợp lệ (phải có đúng 10 chữ số)
def is_valid_phone(phone_number):
    return re.fullmatch(r"\d{10}", phone_number) is not None  # Chỉ chấp nhận 10 chữ số

# Nhập First Name
driver.find_element(By.ID, "firstName").send_keys("Ngo")
# Nhập Last Name
driver.find_element(By.ID, "lastName").send_keys("Quoc Khanh")
# Nhập Email
driver.find_element(By.ID, "userEmail").send_keys("khanh104087@donga.edu.vn.com")
# Chọn giới tính
driver.find_element(By.XPATH, "//label[text()='Male']").click()

# Kiểm tra và nhập số điện thoại
phone_input = driver.find_element(By.ID, "userNumber")
phone_number = "0123456789"  # Thử nghiệm với số hợp lệ

if is_valid_phone(phone_number):
    phone_input.send_keys(phone_number)
    print("✅ Số điện thoại hợp lệ, tiếp tục form.")
else:
    print("❌ Số điện thoại không hợp lệ! Hãy nhập số đúng 10 chữ số.")
    driver.quit()  # Thoát nếu số điện thoại không hợp lệ

# Nhập các trường còn lại
driver.find_element(By.ID, "dateOfBirthInput").click()
driver.find_element(By.XPATH, "//option[text()='2000']").click()
driver.find_element(By.XPATH, "//option[text()='January']").click()
driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='1']").click()

# Chọn Subject
subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("Maths")
subject.send_keys(Keys.RETURN)

# Chọn Hobbies
driver.find_element(By.XPATH, "//label[text()='Sports']").click()

# Nhập địa chỉ
driver.find_element(By.ID, "currentAddress").send_keys("123 Đường ABC, Quận XYZ, Thành phố HCM")

# Chọn State & City
driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.RETURN)
driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.RETURN)

# Click Submit
driver.find_element(By.ID, "submit").click()

# Kiểm tra xác nhận
modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
assert "Thanks for submitting the form" in modal.text
print("✅ Form đã được submit thành công!")

# Đợi 3 giây rồi đóng trình duyệt
time.sleep(3)
driver.quit()
