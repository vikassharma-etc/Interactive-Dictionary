#"python script for app1"
import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("resources/data.json"))

def translate(word):
    word=word.lower()
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), n=1, cutoff=0.8)) > 0:
        yn = input("Did you mean {0}? Please enter Yfor yes or N for no.".format(get_close_matches(word, data.keys(), n=1, cutoff=0.8)[0]))
        if yn.lower() == "y":
            return data[get_close_matches(word, data.keys(), n=1, cutoff=0.8)[0]]
        elif yn.lower() == "n":
            return "Word doesn't exist. Please double check."
        else:
            return "We didn't understand the input."
    else:
        return "Word doesn't exist. Please double check."

while True:
    word = input("Enter a word: ")
    if word:
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
    else:
        print("No words. Good Bye!")
        break
