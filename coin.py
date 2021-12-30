from bs4 import BeautifulSoup
import requests
import re
url = "https://www.tgju.org/profile/sekeb"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
def get_coin():
    price2=0
    for link in soup.find_all(class_="value",limit=1):
    # price=link.get("data-col")
        price= BeautifulSoup(link.text , "html.parser")
        price2=price.text.split('\n')[1]
        break
    return price2
    
