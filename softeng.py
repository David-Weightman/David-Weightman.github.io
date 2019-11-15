import sys
import requests
from collections import Counter 

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=a8a1a5ea66c04f1488210e7b0016b948')
response = requests.get(url)
print (response.json())
