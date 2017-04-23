import requests
import random
import json
from Genetics import *
from MyRequests import *
from Graph import *

def makeGraph(rawData):
    playlistGraph = []
    for trackdata in rawData:
        thisGraphEntry = []
        thisGraphEntry.append(trackdata[0])
        edges = {}
        for otherTrackdata in rawData:
            if(otherTrackdata[0] == trackdata[0]):
                continue
            dist = getDistance(trackdata, otherTrackdata)
            edges[otherTrackdata[0]] = dist
        thisGraphEntry.append(edges)
        playlistGraph.append(thisGraphEntry)
    return playlistGraph

def evaluateWalk(walk, graph):
    start = walk[0]
    dist = 0.0
    for i in range(1, len(walk)-1):
        # dist between walk[i] and walk[i-1]. both ids.
        for element in graph:
            if element[0] == walk[i]:
                dist += (element[1][walk[i-1]])
                break
    return dist

def getWalk(inGraph):
    graph = cloneGraph(inGraph)
    walk = []
    distance = 0.0
    while(len(graph) > 0):
        if(len(graph) == 1):
            #distance between this node and this last point
            distance+=(graph[0][1][walk[len(walk)-1]])
            walk.append(graph[0][0])
            break
        if(len(walk) == 0):
            element = random.randrange(0,len(graph))
            walk.append(graph[element][0])
            del (graph[element])
        else:
            element = random.randrange(0,len(graph))
            distance+=(graph[element][1][walk[len(walk)-1]])
            walk.append(graph[element][0])
            del (graph[element])
    walk.append(distance)
    return(walk)

def cloneGraph(oldGraph):
    returnList = []
    for node in oldGraph:
        newNode = []
        newNode.append(node[0])
        newNode.append(dict(node[1]))
        returnList.append(newNode)
    return returnList

def getDistance(trackData,otherTrackdata):
    dist = 0.0
    dist+= abs(trackData[1]['acousticness']-otherTrackdata[1]['acousticness'])
    dist+= abs(trackData[1]['danceability']-otherTrackdata[1]['danceability'])
    dist+= abs(trackData[1]['energy']-otherTrackdata[1]['energy'])
    dist+= abs(trackData[1]['speechiness']-otherTrackdata[1]['speechiness'])
    dist+= abs(trackData[1]['valence']-otherTrackdata[1]['valence'])
    dist+= abs(trackData[1]['instrumentalness']-otherTrackdata[1]['instrumentalness'])
    dist+= abs((trackData[1]['loudness']/10)-(otherTrackdata[1]['loudness']/10))
    #dist+= abs(trackData[1]['tempo']-otherTrackdata[1]['tempo'])
    #"loudness" : -11.840,
    #"tempo" : 98.002,
    return dist;