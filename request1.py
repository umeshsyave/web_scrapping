import requests
with open('qoutesnew.txt','w') as file:
    n=0
    for i in range(1,11):
        data=requests.get(f'https://quotes.toscrape.com/page/{i}/')
        html=data.text
        with open('qoutesnew.txt', 'a',encoding='utf-8') as file:
            for line in html.split('\n'):
                if '<span class="text" itemprop="text">' in line:
                    output=line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '').strip()
                    n=n+1
                    file.write(f'{n}:{output}')
                    file.write('\n')

