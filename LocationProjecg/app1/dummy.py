import requests
from bs4 import BeautifulSoup



responce = requests.get("https://mylocation.org/")

bs = BeautifulSoup(responce.text,"html.parser")
res = bs.find("div",{"class":"info"})
print(res)



