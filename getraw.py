# READ A LIST OF WORDS FROM A TEXT FILE (THE FILE MUST CONTAIN A SINGLE WORD ON EACH LINE)
# IF THE WORD IS BETWEEN 4 AND 8 CHARACTER IN LENGTH, CHECK FOR PROFANIES AND IF THE WORD IS CLEAN
# INCLUDE IT IN AN APPROVED LIST
# WRITE THE APPROVED LIST TO A FILE AS A JSON OBJECT
#

import json
from profanity_check import predict, predict_prob

approved_list = []
with open('wordlist.txt','r') as input:
    for line in input:
        word = line.strip()
        wlen = len(word)
        if  4 <= wlen <= 8:
          check_word = predict_prob([word])
          if check_word < 0.89:
             approved_list.append(word)

with open('words.json','w') as output:
  json.dump(approved_list,output)
print(len(approved_list))