import pyttsx
import random
import json
import time
    
praise = ["Well done!", "Nice!", "That""s right!", "Great!", "Bonza!", "Fab!"]
commiseration = ["oops!", "nevermind!", "better luck next time!", "boo hoo"]
 
engine = pyttsx.init()
filename = time.asctime().replace(":","-")

logfile = open(filename,'w') 

def ask(prompt):
    ans = raw_input(prompt)
    logfile.write(prompt + "\n")    
    return ans
 
def display(msg):
    logfile.write(msg + "\n")
    print(msg)
    
def logonly(msg):
    logfile.write(msg + "\n")
    
    
def say(phrase):
    logfile.write("The computer said:\"" + phrase + "\"\n")
    engine.say(phrase)
    engine.runAndWait()

def pick(list_to_pick_from):
    return random.choice(list_to_pick_from)

def run_test_on_list(word_list):

    random.shuffle(word_list)
    right = []
    practice = []
    for word in word_list:
        phrase = "How do you spell... {}?".format(word)    
        answer = None    
        while not answer:
            say(phrase)
            answer= ask("Type the word or just press enter to hear it again>")
        
        if answer.lower()==word.lower():
            response = pick(praise)
            right.append(word)
        else:
            response = pick(commiseration)
            practice.append(word)
            display("The right answer was: {}".format(word))
        display(response) 
        say(response)
           
    display("============= Test Summary ===================")
    display("You got {} right out of {}".format(len(right),len(word_list)))
    if len(practice)>0:
        display("These are the words you need to practice:")
        for word in practice:
            display(word)
    else:
        display("Nothing left to practice in this list!")
    
    return practice
############################################################################
if __name__ == "__main__":
    child = "bethany"
    with open("wordlists.json","r") as f:
        all_spellings = json.load(f)[child]
    logonly("This is the written transcript of {}'s spelling test.\nThe spelling questions are spoken by the computer and {} types the answers".format(child,child))
    say("Hello {}, this is your spelling test - please follow the on screen prompts".format(child))
    display("============= {}'s spelling test ==============".format(child))
    display(time.ctime())
    display("")
    display("These are the spelling lists I know about:")
    for key in all_spellings.keys():
        display(key)
    list_name = ask("What list would you like to be tested on?")
    if list_name.lower() not in all_spellings:
        raise(Exception("I don''t know about that list!"))
    
    # keep running test until there is nothing left to practice
    word_list = all_spellings[list_name]
    while word_list:
        word_list = run_test_on_list(word_list)
        if word_list:
            display("Re-running test on just the ones you need to practice")
    
    logfile.close()    
