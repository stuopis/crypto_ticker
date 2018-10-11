import requests
from bs4 import BeautifulSoup

data = requests.get('https://coinmarketcap.com/')
soup = BeautifulSoup(data.text, 'html.parser')
tbody = soup.find('tbody')

for tr in tbody.find_all('tr'):
    place = tr.find_all('td')[0].text.strip()
    name = tr.find_all('td')[1].find_all('a')[0].text.strip()
    price = tr.find_all('td')[3].text.strip()
    marketcap =  tr.find_all('td')[2].text.strip()
    print(place + " " + name + " " + price + " " + marketcap)
