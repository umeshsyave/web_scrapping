import requests
import json


url='https://www.espncricinfo.com/cricket-news?page=1'
req=requests.get(url)
data=req.text
print(type(data))