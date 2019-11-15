import sys
import requests
from collections import Counter 

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=a8a1a5ea66c04f1488210e7b0016b948')
response = requests.get(url)
print (response.json())

stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
             "your", "yours", "yourself", "yourselves", "he", "him", "his",
             "himself", "she", "her", "hers", "herself", "it", "its", "itself",
             "they", "them", "their", "theirs", "themselves", "what", "which",
             "who", "whom", "this", "that", "these", "those", "am", "is", "are",
             "was", "were", "be", "been", "being", "have", "has", "had",
             "having", "do", "does", "did", "doing", "a", "an", "the", "and",
             "but", "if", "or", "because", "as", "until", "while", "of", "at",
             "by", "for", "with", "about", "against", "between", "into",
             "through", "during", "before", "after", "above", "below", "to",
             "from", "up", "down", "in", "out", "on", "off", "over", "under",
             "again", "further", "then", "once", "here", "there", "when",
             "where", "why", "how", "all", "any", "both", "each", "few",
             "more", "most", "other", "some", "such", "no", "nor", "not",
             "only", "own", "same", "so", "than", "too", "very", "s", "t",
             "can", "will", "just", "don", "should", "now", "-", "News", "The",
             "|", "CNN", "CBS", "BBC"]

words = ''

for i in response.json()['articles']:
    words +=  i['title'] + ' '

words2 = words.split()

Counter = Counter(words2)

for i in stopwords:
    del Counter[i]

most_occur = Counter.most_common(4)

print(most_occur)
