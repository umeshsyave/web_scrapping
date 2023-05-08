import requests
from bs4 import BeautifulSoup
import csv

req= requests.get('https://www.holidify.com/')
html= req.text
soup= BeautifulSoup(html,'html.parser')
print(soup.find('h2',{'class':'heading2 w-100'}))