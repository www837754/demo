import requests

# 登录url
url_dl = 'http://127.0.0.1:5000/login'

# 发帖url
url_ft ='http://127.0.0.1:5000/user/232399401'

# 退出url
url_tc = 'http://127.0.0.1:5000/logout'

# 重新验证能否发帖
url_ft01 ='http://127.0.0.1:5000/user/232399401'

# 登录参数
data_dl = {'csrf_token':'1572227149##f364e57b530b4c5b91ed7127aad59a9732835b2d',
        'email':'232399401@qq.com','password':'123'
        }

# 发帖参数
data_ft ={'csrf_token':'1572228871##32d1eed9dded786c4829976ad3e38ecf086eb0a8,',
          'id':'0','title':'ce','slug':'ce','body':'cececececece'}

# 登录
dl = requests.post(url=url_dl,data=data_dl)
print(dl.status_code)
# print(dl.text)



# 发帖
ft = requests.post(url=url_ft,data=data_ft)
print(ft.status_code)
# print(ft.text)

# 退出
cook = dl.cookies.get_dict()
print(cook)

tc = requests.get(url=url_tc,cookies = cook)
print(tc.status_code)

# 退出后再次验证能否发帖，如不能证明退出成功
ft_01 = requests.get(url=url_ft01,data=data_ft)
print(tc.status_code)