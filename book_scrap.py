import requests
from bs4 import BeautifulSoup
import csv

req=requests.get('https://thegreatestbooks.org/')

html=req.text
soup=BeautifulSoup(html,'html.parser')

with open('books_data.csv','w',encoding='utf-8',newline='') as csvfile:
	writer=csv.DictWriter(csvfile,fieldnames=['Book_name','Author_name'])
	writer.writeheader

def Append_Csv(book,author):
	with open('books_data.csv','a',encoding='utf-8',newline='') as file:
		writer=csv.DictWriter(file,fieldnames=['Book_name','Author_name'])
		writer.writerow({f'Book_name':book,'Author_name':author})


for li in soup.find_all('li',{'class':'item pb-3 pt-3 border-bottom'}):
	for h4 in li.find_all('h4'):
		dt={}
		n=0
		for a in h4.find_all('a'):
			if n==0:
				dt['book']=a['href']
				n+=1
			else:
				dt['author']=a['href']

	
		book_name=li.find('a',href=dt['book']).string
		author=li.find('a',href=dt['author']).string
		
		Append_Csv(book=book_name,author=author)

