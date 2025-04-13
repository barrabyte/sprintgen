#
# Using the list of words in words.json, generate a sprint/branch name using
# two randomly picked words. Separate the 2 words with an underscore to create
# the sprint/branch name.
#
# The wordlist is generated using getraw.py
#

import random
import json

with open('words.json','r') as wl:
    wordlist = json.load(wl)
start = 0
stop = len(wordlist) -1

first = random.randrange(start,stop)
second = random.randrange(start,stop)

print(f"{wordlist[first]}_{wordlist[second]}")
