"""
Very simple chatbot.
Feel free do modify and come up with improvements!!!
Copyright (c) 2017 Laurence Some Rights Reserved.
# ADD YOUR NAMES UP TOP, IF YOU CONTRIBUTE!
"""

import random       # Used for making choices

def chatbot():
    """This is the chatbot function"""

    def stringToList(userString):
        """Converts user input into lowercase list"""
        userString = userString.lower()
        userList = userString.split()
        return userList
    
    def compareLists(userInput,conditionList):
        """See if words in user's input are in another list"""
        for word in userInput:
            if word in conditionList:
                return True     # Statement is true if word is found
                break


    # Possible greetings
    greetings = ["hello","hi","good","howdy","hey"]

    # Possible salutations
    bye = ["goodbye","bye","see you"]

    # Possible verb tenses of verb "to be"
    verbToBe = ["am","are","is","aren't","isn't"]

    # While user didn't say bye!:
    while True:
        user_input = input("User: ")            # get user input
        mod_input = stringToList(user_input)    # input as list
        try:                                    # try:
            if mod_input[0] in greetings:       # if user says hello:
                print("Hello back!")
            if compareLists(mod_input,bye) == True:   # if user says goodbye:
                print("Bye")
                break                           # Break the loop
            elif compareLists(mod_input,verbToBe):      # if 'to be' in the sentence
                for word in mod_input:
                    if word in verbToBe:
                        to_be_index = mod_input.index(word)
                # sentence structure:
                predicate = mod_input[(to_be_index+1):] # everything after the 'to be'
                subject = mod_input[:to_be_index]       # everything before the 'to be'
                verb = mod_input[to_be_index]           # 'to be'
                choice = random.randint(0,1)            # randomness between 0 or 1
                if choice == 0:                         # if choice is 0:
                    # initialize new sentence
                    adverb = "why"
                    new_sentence = []
                    sentence = []
                    new_sentence.append(adverb)
                    new_sentence.append(verb)
                    for word in subject:
                        new_sentence.append(word)
                    for word in predicate:
                        new_sentence.append(word)
                    sentence = (' '.join(new_sentence)) # create a new sentence
                    print(sentence+'?')
                else:                           # if choice is 1:
                    predicate = (' '.join(predicate))
                    print("I like", predicate)
            else:           # otherwise:
                print("That is interesting")
        except IndexError:  # If user doesn't return anything:
            print("Stop ignoring me!!!")

  
if __name__ == "__main__":
    chatbot()
