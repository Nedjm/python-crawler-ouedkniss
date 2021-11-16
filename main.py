import requests
from bs4 import BeautifulSoup, SoupStrainer
import re

proxy = {"http": "socks5://192.111.129.145:16894", "https": "socks5://192.111.129.145:16894"} 
url = 'https://www.ouedkniss.com/automobiles/'

if __name__ == "__main__":
    open('linksFile', 'w')
    pageNumber = 1
    while True :        
        linksFile = open("linksFile.txt", 'a') 
        try:
            r = requests.get(url+str(pageNumber))
        except :
            print("last page number is: ", pageNumber)
            break

        links = []
        soup = BeautifulSoup(r.text, 'html.parser')
        soups = soup('li', class_="annonce_titre")
        for item in soups:
            itemPage = requests.get(url + item.find('a').attrs['href'])
            page = BeautifulSoup(itemPage.text, 'html.parser')
            phone = page.find_all('p', class_="Phone")
            for item in phone:
                phoneNumber = item.find('a').attrs['href']
                linksFile.write(phoneNumber+'\n')






        print(pageNumber)
        pageNumber += 1
        linksFile.close()