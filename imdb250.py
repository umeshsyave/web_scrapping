import requests
from bs4 import BeautifulSoup
import csv


#create a file and writing header
with open('imdb_top250.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['movie','year','rating'])
    writer.writeheader()

#function to write row in csv file
def csv_input(name,year,rating):
    with open('imdb_top250.csv','a',newline='',encoding='utf-8') as file:
        writer=csv.DictWriter(file,fieldnames=['movie','year','rating'])
        writer.writerow({f'movie':name,'year':year,'rating':rating})

req= requests.get('https://www.imdb.com/chart/top/')
html=req.text

soup=BeautifulSoup(html,'html.parser')
table=soup.find('tbody',{'class':'lister-list'})
for items in table.find_all('tr'):                  #iterating the line start with tag tr
    title=items.find('td',{'class':'titleColumn'})                      #title is present in td tag, class=titlecolumn
    rating=items.find('td',{'class':'ratingColumn imdbRating'})         #getting rating  tag
    movie_name=title.a.string                                   #movie title in subtag a
    movie_year=title.span.string                                #movie year in sub tag span
    movie_rating=rating.strong.string                              #movie rating in subtag strong
    csv_input(movie_name,movie_year,movie_rating)



