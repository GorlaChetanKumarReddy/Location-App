from app1.Dummy2 import Requests

CITY_NAME = ""
class LocatoinCostroctor:
    def __init__(self,get_responce):
        self.get_responce = get_responce
        print('im constructor')

    def __call__(self,request, *args, **kwargs):
        responce = self.get_responce(request)
        re = requests.get("https://mylocation.org/")
        bs = BeautifulSoup(re.text, "html.parser")
        res = bs.find_all("td")
        global CITY_NAME
        CITY_NAME = res[10].text
        print(CITY_NAME)
        print('im call')
        return responce
