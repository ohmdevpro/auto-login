import requests

username = input("Username ID : ")
password = input("Password ID : ")

headers = {
  "Host": "bypass-xattack.000webhostapp.com",
  "Connection": "keep-alive",
  "Content-Length": "35",
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "X-Requested-With": "XMLHttpRequest",
  "User-Agent": "Apple",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Origin": "http://bypass-xattack.000webhostapp.com",
  "Referer": "http://bypass-xattack.000webhostapp.com/login"
}

data = {
  "username":f"{username}",
  "password":f"{password}"
}

name = requests.post("http://bypass-xattack.000webhostapp.com/api/login.php",data=data, headers=headers)
print(name.text)
