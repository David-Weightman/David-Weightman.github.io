import requests
import spotipy
import sys
import spotipy.util as util
from collections import Counter

#gets the news data from the news api website
news_url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=a8a1a5ea66c04f1488210e7b0016b948')
response = requests.get(news_url)

# List of stop words that are to be removed from our list of words
stopwords = ["I", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
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
             "|", "CNN", "CBS", "BBC", "Guardian", "says", "news", "Daily",
             "Mail", "Online", "don't", "Mirror", "After"]

# Variable to store the list of headlines
words = ''

# Store the headlines in the declared variable
for i in response.json()['articles']:
    words +=  i['title'] + ' '

# Split the headlines into an array where each word is its own value
words2 = words.split()

# Count the occurence of each word
Counter = Counter(words2)

# Remove the words in the stop word array from the list
for i in stopwords:
    del Counter[i]

# Gets the most commonly occuring word from the list and prints it to screen
most_occur = Counter.most_common(4)
print("Most common word today: ", most_occur[0][0])


# Key Terms
username = "75ag8jyj355b1cshmfjd5vj3l"
playlist_id = "37j7Yf18t5qXwa21qfNgef"
client_id = '364b5081d9e14ae38dccf9a353c5b827'
client_secret = '98993b5baf324f59917f4069a6747c65'
redirect_uri = 'http://localhost:8000/'
scope = 'user-library-read playlist-modify-public playlist-modify-private user-library-modify'


# Gets authentication
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)

    # Empties playlist
    existing_tracks = sp.user_playlist_tracks(username, playlist_id, fields='', limit=100, offset=0, market=None)
    existing_track_ids = [item['track']['uri'] for item in existing_tracks['items']]
    sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, existing_track_ids)
    
    # Searches spotify with most common term
    res = sp.search(most_occur[0][0], 20 , 0, 'track', None)
    tracks = res['tracks']

    # Gets track uris for search_results
    track_ids = [item['uri'] for item in tracks['items']]

    # Adds tracks tp playlist
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)

    print("Find your playlist here: open.spotify.com/playlist/" + playlist_id)
    
else:
    print ("Can't get token for", username)
