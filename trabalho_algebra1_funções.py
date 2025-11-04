# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 17:18:21 2025

@author: User
"""
from math import sqrt, acos, degrees
from nltk.corpus import stopwords


def cleanup(sample):
    stopset = set(stopwords.words(input("language: ")))
    episode = sample.read().splitlines()
    while '' in episode:
        episode.remove('')
    for i,lines in enumerate(episode):
        lines = lines.split()
        for a,word in enumerate(lines):
            if word in stopset:
                lines.remove(word)
            elif word == "-":
                lines.remove(word)
            elif word.isupper():
                lines[a] = word.lower()
        episode[i] = lines
    return episode


def create_wordbank(samples):
    wordbank = []
    for string in samples:
        for word in string:
            if word not in wordbank:
                wordbank.append(word)
    return wordbank        

def create_vectors(samples,wordbank,interest):
    search = []
    for word in interest:
        if word not in wordbank:
            wordbank.append(word)
            
    vectors = []
    
    for string in samples:
        vector = []
        separated = [i for i in string]
        for word in wordbank:
            number = 0
            while word in separated:
                number += 1
                separated.remove(word)
            vector.append(number)
        vectors.append(vector)
    alterable = interest
    
    for word in wordbank:
        number = 0
        while word in alterable:
            number += 1
            alterable.remove(word)
        search.append(number)
    
    return vectors, search

def get_numbers(vectors,search):
    size_ser = 0
    for i in search:
        square = i*i
        size_ser += square
    roots = []
    for vector in vectors:
        size = 0
        for i in vector:
            square = i*i
            size += square
        roots.append(sqrt(size))    
    ser_root = sqrt(size_ser)
    return roots,ser_root

def cosine_similarity(vectors,roots,search,ser_root,samples):
    results = []
    for i,vector in enumerate(vectors):
        summ = 0
        root = roots[i]
        for i,x in enumerate(vector):
            mult = x*search[i]
            summ += mult
        cos = round(summ/(root*ser_root),5)
        degree = degrees(acos(cos))
        results.append(degree)
    print(results)
    
    looks_for = max(abs(90-i) for i in results)
    
    for i,x in enumerate(results):
        if 90 - x == looks_for:
            if 90 - x != 0:
                winner = " ".join(samples[i])
            else:
                winner = "couldn't find a match"
    return winner
 
    
    