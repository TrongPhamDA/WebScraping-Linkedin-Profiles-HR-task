# Import các thư viện cần dùng
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# pip install python-time
from time import sleep
# hoặc dùng method có sẵn của selenium
# driver.implicitly_wait(2)


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

# để file chromedrive.exe ở cùng file main.py
driver = webdriver.Chrome()
# Maximizing window
driver.maximize_window()
# Hoặc cung cấp path chi tiết của ChromeDriver
# driver = webdriver.Chrome("C:\\Users\\Phanl\\Desktop\\GitHub\\WebScraping-Linkedin-Profiles-HR-task\\chromedriver.exe")

url = "https://www.linkedin.com/login"
driver.get(url)
print("\n-- Open Chrome & jump to LinkedIn login site --")
# delay 2s mỗi khi làm 1 thao tác
driver.implicitly_wait(2)


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
print(f"-- Login : {username} --")
sleep(2)


# Task 2: Search các profile mong muốn theo từ khóa

# Định vị được khung search (ngay sau logo "in")
# Full Xpath lúc này không còn hoạt động do không cố định, Xpath đã thành Xpath động, 
# chuyển sang kết hợp tìm với Xpath với tên class
search_field = driver.find_element_by_xpath('//*[@class="search-global-typeahead__input always-show-placeholder"]')

# Nhập vị trí công việc cần tìm người
# thêm từ khóa: people, jobs, groups để tìm profile, công việc, nhóm tương ứng
# search_keys = input(f"---\nEnter job title: ")
search_keys = "data analyst"
# search_keys = search_keys.strip()
# search_field.send_keys(search_keys)
# tự ấn ENTER sau khi send_keys() từ khóa
# vì không tìm ra nút search
# search_field.send_keys(Keys.RETURN)

# tuy nhiên, LinkedIn đã phát triển, nên search theo send_keys() sẽ tìm không đúng yêu cầu
# chuyển qua get theo url
search_url = f"https://www.linkedin.com/search/results/people/?keywords={search_keys}&origin=SWITCH_SEARCH_VERTICAL&sid=yRI"
driver.get(search_url)

# Task 3: Sử dụng Beautiful Soup 4 để lấy dữ liệu từ web









print(f"-- Searching : {search_keys}")

# Nên để 1 dòng thông báo như thế này để biết chương trình của mình đã chạy từ đầu tới cuối
print('\n-- DONE --')