from bs4 import BeautifulSoup
import requests

html =  requests.get('https://www.python.org')

soup = BeautifulSoup(html.text, 'lxml')

title = soup.find_all('title')
print(title[0].text)

info = soup.find_all('div', {'class': 'introduction'})
print(info)