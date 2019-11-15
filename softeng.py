import sys
import requests
from collections import Counter 

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=a8a1a5ea66c04f1488210e7b0016b948')
response = requests.get(url)
#print (response.json())

words = ''

for i in response.json()['articles']:
    words += i['title'] + ' '

    #print(i['title'])

print(words)

words2 = words.split()

Counter = Counter(words2)

most_occur = Counter.most_common(4)

print(most_occur)
