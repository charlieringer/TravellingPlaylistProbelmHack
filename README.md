# TravellingPlaylistProbelmHack
A command line tool to mix your Sportify playlists. How? Using a genetic algortim! 

The tool models all of the songs in the playlist as a graph with the distance between tracks being related to how different the audio tracks are (using Spotifys Track Audio Features).

Then it is a case of finding the best path through the graph (which is the Travelling Salesman Problem) using a genetic  algorithm and then making a playlist with the new orderings. Your ears will thanks me!

To use download this + spotipy and set your username in the User.py file. Then run main file (TPP.py) and when prompted authenticate the app. Paste the redirect page into your terminal (it will look like a broken link but it should work). 

You will be shown all of the playlists you one. Select the one you want and the algorithm will analyse the track info, build it as a graph, find a good route through it and build a new playlist with the new ordering (it will be have the same name with _TPP at the end).

Selected as a winner of the Spotify prize at Anvil Hack 3.
