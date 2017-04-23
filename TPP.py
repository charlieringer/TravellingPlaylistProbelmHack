import requests
import random
import json
import spotipy

import spotipy.util as util
from Genetics import *
from MyRequests import *
from Graph import *
from User import username

def main():
    scope  = 'user-library-read playlist-read-private playlist-modify-public playlist-modify-private'
    token = util.prompt_for_user_token(username, scope, client_id='f248c8c713ea4c199e40cea4eae1bea4',client_secret='be9b3c6a8e1d4c98b66a09f89111e7ee',redirect_uri='http://localhost:8888')
    playlists = getPlaylists(token, username)
    if playlists == {u'error': {u'status': 401, u'message': u'The access token expired'}}:
        print('Token expired')
        return
    print("Your playlists:")
    for i in range(len(playlists)):
        print(i, ": ", playlists[i][0])
    print("")
    playlistSelection = int(input("Select playlist: "))
    playlistURI = playlists[playlistSelection][1]
    print("Gettings Tracks...")
    urlSearchResults = getPlaylistTracks(playlistURI,username, token)
    if urlSearchResults == {u'error': {u'status': 401, u'message': u'The access token expired'}}:
        print('Token expired')
        return

    items = urlSearchResults['items']
    print("Gettings Audio Features...")
    playlistData = getAudioFeaturesForList(items, token)
    print("Building Graph...")
    playlistGraph = makeGraph(playlistData)
    out = "Inital playlist distance: " + str(getInitWalkDist(playlistGraph))
    print(out)
    
    print("Building population...")
    population = initPopulation(playlistGraph, 20)
    print("Searching for best playlist...")

    for i in range(0, 50):
        population = applyGenetics(population,playlistGraph)
        population = sortWalks(population)
        bestWalk = population[0]
        print("Best playlist for this population: ", bestWalk[len(bestWalk)-1])
    print("Building playlist")
    makePlaylist(population[0][:-1],playlists[playlistSelection][0], token, username)
    print("Done!")

main()




