import json
from difflib import get_close_matches

data=json.load(open('data.json','r'))

def definition(word):
    w=word.lower()
    if w in data:
        return data[w]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        match=get_close_matches(w,data.keys())[0]
        ans=input("Did you mean "+match+" instead? If yes, type Y otherwise type N: ")
        if ans=='Y':
            return data[match]
        elif ans=='N':        
            return "The word doesn't exist in the dictionary. Please double-check the word you have entered."
        else:
            return "Invalid input"
    else:
        return "The word doesn't exist in the dictionary. Please double-check the word you have entered."
          
word=input("Enter a word: ")
meanings=definition(word)
if type(meanings)==list:
    for item in meanings:
        print(item)
else:
    print(meanings)