import requests
import csv

qoute_list=[]
author_list=[]
for i in range(1,11):
    qoutes=requests.get(f'https://quotes.toscrape.com/page/{i}/')
    for line in qoutes.text.split('\n'):
        if '<span class="text" itemprop="text">' in line:
            line=line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '').strip()
            qoute_list.append(line)
    for line in qoutes.text.split('\n'):
        if '<span>by <small class="author" itemprop="author">' in line:
            line=line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>','').strip()
            author_list.append(line)
zipped=zip(author_list,qoute_list)

head=['author','qoute']
# with open('qoutes_doc.csv','w',encoding='utf-8') as csvfile:
#     csvwriter= csv.writer(csvfile)
#     csvwriter.writerow(head)
for row in list(zipped):
    print(list(row))
        # csvwriter.writerow(list(row))




