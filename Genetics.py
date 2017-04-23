import requests
import random
import json

from Genetics import *
from MyRequests import *
from Graph import *

def applySelection(population):
    selectionThreshold = len(population)/2
    selectedPopulation = []
    for i in range(0, int(selectionThreshold)):
        tournament = random.sample(population, 3)
        best = 1000
        bestInx = -1 
        for i in range (0, len(tournament)):
            if tournament[i][len(tournament[i])-1] < best:
                bestInx = i
                best = tournament[i][len(tournament[i])-1]
        selectedPopulation.append(tournament[bestInx])
    return selectedPopulation

def applyCrossover(population, graph):
    partB = []
    for i in range(0, len(population)):
        objectA = list(random.choice(population)[:-1])
        objectB = list(random.choice(population)[:-1])

        lengthOfWalk = len(objectA)
        start = random.randrange(0, lengthOfWalk//2)
        newWalk = []
        
        for i in range(0, lengthOfWalk//2):
            newWalk.append(objectA[start+i])
        for i in range(0, (len(objectB))):
            if(objectB[i] not in newWalk):
                newWalk.append(objectB[i])
        newWalk.append(evaluateWalk(newWalk, graph))
        partB.append(newWalk)
    return partB

def applyMutation(population, graph):
    for i in range(0, len(population)):
        if(random.random() < 0.5):
            population[i] = mutate(population[i][:-1], graph)
    return population

def mutate(walk, graph):
    newWalk = walk[1:]
    newWalk.append(walk[0])
    newWalk.append(evaluateWalk(newWalk, graph))
    return newWalk

def applyGenetics(population, graph):
    newPopA = applySelection(population)
    newPopB = applyCrossover(newPopA, graph)
    newPopulation = newPopA + newPopB
    newPopulation = applyMutation(newPopulation, graph)
    return newPopulation

def sortWalks(walks):
    returnList = []
    while(len(walks) > 0):
        bestInx = -1;
        bestScore = 1000
        for i in range(0, len(walks)):
            score = walks[i][len(walks[i])-1]
            if(score < bestScore):
                bestScore = score
                bestInx = i
        returnList.append(list(walks[bestInx]))
        del walks[bestInx]
    return returnList

def initPopulation(playlistGraph, numbDNA):
    population = []
    for i in range(0, numbDNA):
        walk = getWalk(playlistGraph)
        population.append(walk)
    population = sortWalks(population)
    return population
