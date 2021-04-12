import requests
from bs4 import BeautifulSoup
class LocationRequest:
    re = requests.get("https://mylocation.org/")
    bs = BeautifulSoup(re.text,"html.parser")
    res = bs.find_all("td")
    if res:
        print(res)
    else:
        print("no results found")