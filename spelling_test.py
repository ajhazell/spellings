import pyttsx
import random
import json
child = 'bethany'
with open('wordlists.json','r') as f:
    all_spellings = json.load(f)[child]
    
praise = ["Well done!", "Nice!", "That""s right!", "Great!", "Bonza!", "Fab!"]
commiseration = ["oops!", "nevermind!", "better luck next time!", "boo hoo"]
 
engine = pyttsx.init()

def say(phrase):
    engine.say(phrase)
    engine.runAndWait()

def pick(list_to_pick_from):
    return random.choice(list_to_pick_from)

say("Hello {}, this is your spelling test - please follow the on screen prompts".format(child))
print("These are the spelling lists I know about:")
for key in all_spellings.keys():
    print(key)
list_name = raw_input("What list would you like to be tested on?")
if list_name.lower() not in all_spellings:
    raise(Exception("I don''t know about that list!"))
num_right = 0
word_list = all_spellings[list_name]
random.shuffle(word_list)
for word in word_list:
    phrase = "How do you spell... {}?".format(word)    
    answer = None    
    while not answer:
        say(phrase)
        answer= raw_input("Type the word or just press enter to hear it again>")
    
    if answer.lower()==word.lower():
        response = pick(praise) 
        num_right +=1
    else:
        response = pick(commiseration)
        print("The right answer was: {}".format(word))
    print(response) 
    say(response)
       

print("You got {} right out of {}".format(num_right,len(all_spellings[list_name])))