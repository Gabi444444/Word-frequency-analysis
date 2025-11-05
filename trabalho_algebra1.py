# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 09:55:03 2025

@author: User
"""

from math import sqrt, acos, degrees

respostas = open("respostausar.txt","r")

samples = respostas.read().splitlines()
wordbank = []

pessoas = ["Flávia","Giuu","Adriane","Elisângela","Kenji","Eu","Gustavo","Ganancioso","Cara do marketing","Artista","Programador","Desinteressado"]


for string in samples:
    separated = string.split()
    for word in separated:
        if word not in wordbank:
            wordbank.append(word)   

custom = input("você quer fazer inputs customizados? ")
buscas = []

if custom == "sim":
    tests = int(input("\nquantas procuras? "))
    n = 0
    while n < tests:
        buscas.append(input("\ninsira sua query, sem pontuação: ").split())
        n += 1

else:
    searches = open("querries_usar.txt","r")
    queries = searches.read().splitlines()
    buscas = [i.split() for i in queries]
    
for query in buscas:
    print("\n",query)
    interest = []
    temp_wordbank = [i for i in wordbank]
    for word in query:
        if word not in temp_wordbank:
            temp_wordbank.append(word)
    vectors = []
    
    if len(temp_wordbank) - len(query) == len(wordbank):
        print("\nnenhuma dessas palavras está no dataset, similaridade nula")
        break
    
    for string in samples:
        vector = []
        separated = string.split()
        for word in temp_wordbank:
            number = 0
            while word in separated:
                number += 1
                separated.remove(word)
            vector.append(number)
        vectors.append(vector)
    
    alterable = query
    
    for word in temp_wordbank:
        number = 0
        while word in alterable:
            number += 1
            alterable.remove(word)
        interest.append(number)
    
    size_int = 0
    
    for i in interest:
        square = i*i
        size_int += square
    squares = []
    
    for vector in vectors:
        size = 0
        for i in vector:
            square = i*i
            size += square
        squares.append(size)
        
    results = []
    int_root = sqrt(size_int)
    
    for i,vector in enumerate(vectors):
        summ = 0
        root = sqrt(squares[i])
        for i,x in enumerate(vector):
            mult = x*interest[i]
            summ += mult
            cos = round(summ/(root*int_root),5)
        degree = degrees(acos(cos))
        results.append(degree)
    print(results)
    
    
    for i in range(3):
        looks_for = max(abs(90-i) for i in results)
        for i,x in enumerate(results):
            if 90 - x == looks_for:
                if 90 - x == 0:
                    print("similaridade irrelevante a partir daqui")
                    break
                else:
                    print("\n",f"{pessoas[i]}:",samples[i],"\nângulo:",x)
                    results[i] = 90
    
            




