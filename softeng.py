import requests
import spotipy
import sys
import spotipy.util as util

#url = ('https://newsapi.org/v2/top-headlines?'
#       'country=us&'
#       'apiKey=a8a1a5ea66c04f1488210e7b0016b948')
#response = requests.get(url)
#print (response.json())



scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print ("Can't get token for", username)
