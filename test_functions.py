# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 09:26:50 2025

@author: User
"""
import trabalho_algebra1_funções as sim

continues = True
sample = []


sample_size = int(input("how many samples: "))
n = 0

while n < sample_size:
    sample.append(input("please type a string with no punctuation: ").split())
    n += 1

wordbank = sim.create_wordbank(sample)

quant = int(input("how many searches? "))
n = 0

search = []
while n < quant:
    search.append(input("what to look for? ").split())
    n += 1
    
for query in search:
    vectors = sim.create_vectors(sample, wordbank, query)
    numbers = sim.get_numbers(vectors[0],vectors[1])
    winner = sim.cosine_similarity(vectors[0],numbers[0],vectors[1],numbers[1],sample)
    print("\n",winner)