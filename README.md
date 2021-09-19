# WebScraping-Linkedin-Profiles-HR-task
Cào hàng ngàn profile LinkedIn cho bộ phận HR spam tuyển dụng

Làm cách nào để cào hàng ngàn hồ sơ trên LinkedIn cho bộ phận HR
Mà chỉ tốn vài phút?

--
Techical plan:
- Task 1: Login LinkedIn
	+ Task 1.1 Login
		* Open Chrome browser
		* Nhập đường link LinkedIn
	+ Task 1.2
		* Nhập thông tin User / Password
		* Nhấn nút Log in
- Task 2: Search "keywords" mà chúng ta cần crawl
- Task 3: Mở các URL dẫn đến các profile vừa lấy được
- Task 4: Tiếp tục scrape các thông tin chi tiết có trong các profile --> từ đó ghi ra file .csv

--
Các Library & Module cần được import
- selenium : thao tác với Chrome
pip install selenium

- chromedriver : cho selenium làm việc với Chrome
cần kiểm tra Chrome version trong máy tính trước
Cài Đặt > Giới thiệu về Chrome > Phiên bản 93.0.4577.82

rồi tải về Chrome Driver tương ứng:
https://chromedriver.chromium.org/downloads
tìm version driver cập nhật mới nhất đúng với phiên bản Chrome (93.0.4577.63)
https://chromedriver.storage.googleapis.com/index.html?path=93.0.4577.63

Chrome driver download về rồi thì để ở đâu?
Để ở bất kỳ thư viện nào trong ổ đĩa C, tạm thời có thể ở thư mục Download

- beautifulsoup4 : tách dữ liệu từ website
- time : để delay thời gian giữa các thao tác, tránh cho website nhận diện là bot cào dữ liệu
- csv : để đọc và ghi dữ liệu ra file csv