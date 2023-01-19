from urllib import response
from bs4 import BeautifulSoup as bs
import requests

domain = 'https://cymru.com/$certname/'
url = 'https://cymru.com/$certname/'
username = "User Here"
password = "Pass Here"
filetype = '.txt'

if not os.path.exists("eventos"):
    os.makedirs("eventos")

def get_soup(url):
    return bs(requests.get(url, auth=(username, password)).text, 'html.parser')

for link in get_soup(url).find_all('a'):
    file_link = link.get('href')
    if filetype in file_link:
        print(file_link)
        with open('eventos/' + link.text, 'wb') as file:
            response = requests.get(domain + file_link, auth=(username, password))
            file.write(response.content)

print('Download complete!')
