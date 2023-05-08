import requests
import json
n=0
for i in range(1,10):
    url=f'https://hs-consumer-api.espncricinfo.com/v1/edition/feed?edition=in&lang=en&page={i}&records=10'
    req=requests.get(url)
    data=json.loads(req.text)
    new=data['results']
#print(new[0])
    for item in new:
        print(item['id'])
        print(item['title'])
        print(item['subtitle'])
        print()
    n=n+1
    print('..........',n)


