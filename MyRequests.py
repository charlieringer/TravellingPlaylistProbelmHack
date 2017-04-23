import requests
import random
import json

from Genetics import *
from MyRequests import *
from Graph import *

#playlistURI = '5Pa5jw42sPQ9SEKu4dEuZN'
userID = "21nnwwsdm2vvacv2jgbwbhkly"
headers = {'Accept': 'application/json','Authorization': 'Bearer BQCDi_fPb_43-4ThvnrQrah03KNMmPUuD003TqDWG_mc-DqDQ5xN55p0PzRNT7BDmq2P2yU4shXR6YPzvwVDga7YTQPIORn71uoMUyQy_tjAXqKKL2JzGH6BR17f82BKqz8ZT5pLQoOOZsxHeHnyKl8I3C3UvAkpTjmk0yXV3P3GYlsGAbaOzmCNM5D78ReoSpaqSS21BSdeiMncdGIWmTpzZxHKm1de9I4Z7tHet8xOlOFJT2rAY8UfNrjA4ODm-0ve2jw_sCgTfnWE1FIOoclJDa9yUm2dAmE'}

GET_USERS_PLAYLIST_ENDPOINT = 'https://api.spotify.com/v1/users/{user_id}/playlists?'
GET_PLAYLIST_ENDPOINT = 'https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}'
GET_PLAYLIST_TRACKS_ENDPOINT = 'https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks'
GET_AUDIO_FEATURES = 'https://api.spotify.com/v1/audio-features/{id}'
MAKE_PLAYLIST_ENDPOINT = 'https://api.spotify.com/v1/users/{user_id}/playlists'
ADD_TRACK_TO_PLAYLIST_ENDPOINT =  "https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks"

def getPlaylists():
	headers = {'Accept': 'application/json','Authorization': 'Bearer BQCDi_fPb_43-4ThvnrQrah03KNMmPUuD003TqDWG_mc-DqDQ5xN55p0PzRNT7BDmq2P2yU4shXR6YPzvwVDga7YTQPIORn71uoMUyQy_tjAXqKKL2JzGH6BR17f82BKqz8ZT5pLQoOOZsxHeHnyKl8I3C3UvAkpTjmk0yXV3P3GYlsGAbaOzmCNM5D78ReoSpaqSS21BSdeiMncdGIWmTpzZxHKm1de9I4Z7tHet8xOlOFJT2rAY8UfNrjA4ODm-0ve2jw_sCgTfnWE1FIOoclJDa9yUm2dAmE'}
	url = GET_USERS_PLAYLIST_ENDPOINT.format(user_id=userID)
	resp = requests.get(url, headers=headers)
	print(resp.json())
	items = resp.json()['items']
	playlists = []
	for item in items:
		playlist = []
		playlist.append(item['name'])
		playlist.append(item['id'])
		playlists.append(playlist)
	return playlists

def getPlaylistTracks(playlistID, userID, token):
	headers = {'Accept': 'application/json','Authorization': 'Bearer '+token}
	url = GET_PLAYLIST_TRACKS_ENDPOINT.format(user_id=userID, playlist_id=playlistID)
	resp = requests.get(url, headers=headers)
	return resp.json()

def getAudioFeatures(trackID, token):
	headers = {'Accept': 'application/json','Authorization': 'Bearer '+token}
	url = GET_AUDIO_FEATURES.format(id=trackID)
	resp = requests.get(url, headers=headers)
	return resp.json()

def makePlaylist(playlistIDS, oldName, token):
	headers = {'Accept': 'application/json','Authorization': 'Bearer '+token}
	url = MAKE_PLAYLIST_ENDPOINT.format(user_id=userID)
	name = oldName + '_TPP'
	data = {"name": name, "public":False}
	resp = requests.post(url, headers=headers, data=json.dumps(data))
	playlistID = resp.json()['id']
	url2 = ADD_TRACK_TO_PLAYLIST_ENDPOINT.format(user_id=userID, playlist_id=playlistID)
	for trackID in playlistIDS:
	    trackstring = []
	    trackstring.append("spotify:track:{}".format(trackID))
	    data = {"uris": trackstring}
	    resp = requests.post(url2, headers=headers, data=json.dumps(data))

def getAudioFeaturesForList(items, token):
	headers = {'Accept': 'application/json','Authorization': 'Bearer '+token}
	playlistData = []
	for item in items:
	    data = []
	    data.append(item['track']['id'])
	    results = getAudioFeatures(item['track']['id'], token)
	    data.append(results)
	    playlistData.append(data)
	return playlistData