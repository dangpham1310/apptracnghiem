# a = {
# "username":"0899996922",
# "password_field_random":"thiendang2001",
# "name":"Phạm Thiên Đăng",
# "class":"0",
# "userType":"Admin"
# }
import requests
from time import sleep
payload = [
                "Tiếng Việt",
                "Toán",
                "Ngoại ngữ",
                "Đạo đức",
                "Tự nhiên và xã hội",
                "Lịch sử và Địa lý",
                "Khoa học",
                "Tin học và Công nghệ",
                "Giáo dục thể chất",
                "Nghệ thuật",
                "Hoạt động trải nghiệm"
            ]

for j in payload:
    for i in range (1,6):
        requests.post(url="http://127.0.0.1:5000/addSubject",data={"nameSubject":j,"grade":i})



    
