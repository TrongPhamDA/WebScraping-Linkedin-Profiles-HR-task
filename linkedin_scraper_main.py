# Import các thư viện cần dùng
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# pip install python-time
from time import sleep

print("-- Finish importing packages --")

# Task 1: Đăng nhập vào LinkedIn
# Lưu trữ thông tin email / password ở 1 file khác
filename = "userpass.txt"
credential = open(filename, "r")
lines = credential.readlines()

# Quy định trong file userpass.txt chỉ chứa 2 dòng
# dòng đầu tiên index 0 chứa email
# dòng thứ 2 index 1 chứa password
# strip() để loại bỏ dấu xuống dòng
username = lines[0].strip()
password = lines[1].strip()

# Open Chrome và truy cập vào LinkedIn login site
driver = webdriver.Chrome()
url = "https://www.linkedin.com/login"
driver.get(url)
print("-- Open Chrome & jump to LinkedIn login site --")
# delay 2s mỗi khi làm 1 thao tác
sleep(2)

# Định vị các đối tượng (inspect đối tượng - tìm code HTML của đối tượng):

# khung email
email_field = driver.find_element_by_id("username")
# send_keys() để gửi email vào khung này:
email_field.send_keys(username)
sleep(2)

# khung password
# password_field = driver.find_element_by_id("password")
password_field = driver.find_element_by_name("session_password")
password_field.send_keys(password)
sleep(2)

# nút bấm Sign in
# không tìm thấy id hay name, nên chuyển qua xpath
# lưu ý là xpath có thể thay đổi - nên kiểm tra kỹ trước khi quyết định dùng
# chuột phải lên html code của nút sign in > Copy > Copy full Xpath
login_field = driver.find_element_by_xpath("/html/body/div/main/div[2]/div[1]/form/div[3]/button")
# click() để thao tác bấm chuột trái lên nút sign in
login_field.click()
sleep(2)
print(f"-- Login: {username} --")

# Nên để 1 dòng thông báo như thế này để biết chương trình của mình đã chạy từ đầu tới cuối
print('\n-- DONE --')

