import requests
import spotipy
import sys
import re
import spotipy.util as util
from collections import Counter

#Gets most used key term used in US news headlines
def getKeyWords(Counter, num):
    # Gets the news data from the news api website
    news_url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=a8a1a5ea66c04f1488210e7b0016b948')
    response = requests.get(news_url)

    # List of stop words that are to be removed from our list of words
    stopwords = ["I", "Me", "My", "Myself", "We", "Our", "Ours", "Ourselves", "You",
                 "Your", "Yours", "Yourself", "Yourselves", "He", "Him", "His",
                 "Himself", "She", "Her", "hers", "herself", "it", "its", "itself",
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
                 "Mail", "Online", "don't", "Mirror", "After", "NPR", "Washington", "Post", "", "new"]

    # Variable to store the list of headlines
    words = ''
    # Store the headlines in the declared variable
    for i in response.json()['articles']:
        words +=  i['title'] + ' '

    # Splits the headlines into an array where each word is its own value
    words2 = words.split()
    # Removes special characters
    words2 = [re.sub('[^a-zA-Z]+', '', x) for x in words2]
    # Counts the occurence of each word
    Counter = Counter(words2)

    # Removes the words in the stop word array from the list
    for i in stopwords:
        del Counter[i[:1].upper() + i[1:]]
        del Counter[i[:1].lower() + i[1:]]
        del Counter[i.upper()]
        del Counter[i.lower()]
    # Returns list of most common words
    return Counter.most_common(num)


    # Empties playlist
def empty(sp, un, pl_id):
    #Identifies URIs of songs in playlist
    tracks = sp.user_playlist_tracks(un, pl_id, fields='', limit=100, offset=0, market=None)
    track_ids = [item['track']['uri'] for item in tracks['items']]
    #Removes them of playlist
    sp.user_playlist_remove_all_occurrences_of_tracks(un, pl_id, track_ids)

    # Searches songs with keyword and adds them to playlist
def search(sp, keyword, limit):
    # Searches spotify with most common term
    res = sp.search(keyword, limit , 0, 'track', None)
    tracks = res['tracks']
    # Gets track uris for search_results
    track_ids = [item['uri'] for item in tracks['items']]
    # Adds tracks to playlist
    sp.user_playlist_add_tracks(username, playlist_id, track_ids)

# Key Terms
username = "75ag8jyj355b1cshmfjd5vj3l"
playlist_id = "37j7Yf18t5qXwa21qfNgef"
client_id = '364b5081d9e14ae38dccf9a353c5b827'
client_secret = '98993b5baf324f59917f4069a6747c65'
redirect_uri = 'http://localhost:8000/'
scope = 'user-library-read playlist-modify-public playlist-modify-private user-library-modify'


# Asks user how many key terms they want to use. Capped at 10 as 'empty' command can only do 100 songs per call
num = 0
while (num < 1):
    try:
        num = int(input("How many keyterms would you like to consider?(Cannot exceed 10)\n"))
        if (num < 1):
            print("Sorry! Please enter an positive integer greater than 0\n")
            num = 0
        elif (num > 10):
            print("Sorry! Please enter an positive integer less than 10\n")
            num = 0
    except ValueError:
        print("Sorry! You didn't enter a valid integer.\n")
    
# Gets the most commonly occuring words
keywords = getKeyWords(Counter, num)
# Prints most common words and their occurrence
words = []
for i in keywords:
    print("Word:", i[0], " Appears:", i[1], "times")
    words.append(i[0])

# Asks user how many songs per term they would like to add. Capped at 10 for above stated reason
numSongs = 0
while (numSongs < 1):
    try:
        numSongs = int(input("How many songs from each term would you like to add? (Cannot exceed 10)\n"))
        if (numSongs < 1):
            print("Sorry! Please enter an positive integer greater than 0\n")
            numSongs = 0
        elif (numSongs > 10):
            print("Sorry! Please enter an positive integer less than 10\n")
            numSongs = 0
    except ValueError:
        print("Sorry! You didn't enter a valid integer.\n")


# Gets authentication
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)

    empty(sp, username, playlist_id)
    
    for i in words:
        search(sp, i, numSongs)

    print("Find your playlist here: open.spotify.com/playlist/" + playlist_id)
    
else:
    print ("Can't get token for", username)
