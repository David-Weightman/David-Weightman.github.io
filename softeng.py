import requests
import spotipy
import sys
import spotipy.util as util


#config = configparser.ConfigParser()
#config.read('config.cfg')
#client_id = config.get('SPOTIFY', 'CLIENT_ID')
#client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')


#url = ('https://newsapi.org/v2/top-headlines?'
#       'country=us&'
#       'apiKey=a8a1a5ea66c04f1488210e7b0016b948')
#response = requests.get(url)
#print (response.json())


username = "75ag8jyj355b1cshmfjd5vj3l"
playlist_id = "37j7Yf18t5qXwa21qfNgef"
client_id = '364b5081d9e14ae38dccf9a353c5b827'
client_secret = '98993b5baf324f59917f4069a6747c65'
redirect_uri = 'http://localhost:80/callback/'
scope = 'playlist-modify-public'

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)


#if un != "":
#    username = un
#    playlist_id = play_id
#else:
#    print ("Usage: %s username playlist_id" % (un,play_id))
#    sys.exit()

#scope = 'playlist-modify-public'
#token = util.prompt_for_user_token(username, scope)

#if token:
#    sp = spotipy.Spotify(auth=token)
#    results = sp.current_user_saved_tracks()
#    for item in results['items']:
#        track = item['track']
#        print (track['name'] + ' - ' + track['artists'][0]['name'])
#else:
#    print ("Can't get token for", username)
