import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('h3')
for title in titles:
    print(title.a['title'])