import nltk
#nltk.download() #Empty field to download "wordnet" and "omw-1.4" 
# from ntlk library window, under the second tab corpora, then can be 
# commented out

import re
from nltk.corpus import wordnet
#Chatbot program shows synonyms for selected words thus far
#re is a package for regular expressions
#Helps with a dictionary of synonyms for keywords


class Chatbot():
    #List of keywords to respond to
    #Hello, order, stock, shipping
    list_words = ['Hello', 'Order', 'Inventory', 'Shipping']

    list_syn = {}

    for word in list_words:
        synonyms = []
        
        for syn in wordnet.synsets(word):

            for lem in syn.lemmas():
                #Remove any special characters from synonym strings
                lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
                synonyms.append(lem_name)

        list_syn[word] = set(synonyms)
    
    #print(list_syn)#print to check if works

    #Building dictionary of intents & keywords
    keywords = {}
    keywords_dict = {}

    #Defining a new key in the keywords dictionary
    keywords['greet'] = []

    #Populating the values in the keywords dictionary w/ synonyms of keywords 
    # formatted w/ RegEx metacharacters
    for synonym in list(list_syn['Hello']):
      keywords['greet'].append('.*\\b'+synonym+'\\b.*')

    #Defining a new key in the keywords dictionary
    keywords['Order'] = []

    #Populating the values in the keywords dictionary w/ synonyms of keywords 
    # formatted w/ RegEx metacharacters
    for synonym in list(list_syn['Order']):
        keywords['Order'].append('.*\\b'+synonym+'\\b.*')
    
     #Defining a new key in the keywords dictionary
    keywords['Inventory'] = []

    #Populating the values in the keywords dictionary w/ synonyms of keywords 
    # formatted w/ RegEx metacharacters
    for synonym in list(list_syn['Inventory']):
        keywords['Inventory'].append('.*\\b'+synonym+'\\b.*')

     #Defining a new key in the keywords dictionary
    keywords['Shipping'] = []

    #Populating the values in the keywords dictionary w/ synonyms of keywords
    # formatted w/ RegEx metacharacters
    for synonym in list(list_syn['Shipping']):
        keywords['Shipping'].append('.*\\b'+synonym+'\\b.*')

    for intent, keys in keywords.items():
        #Joining the values in the keywords dictionary w/ the OR (|) operator
        #updating them in keywords_dict dictionary
        keywords_dict[intent]=re.compile('|'.join(keys))
        
    #print(keywords_dict)#Print to check if it works
    
    #Building a dictionary of responses

    responses={
        'greet':'Hello! My name is Lucky the chatbot, how can I help?',
        'Order':'Looks like you are looking for your order, let me search for that.',
        'Inventory':'Let me help you find the inventory for that.',
        'Shipping':'How about we get that shipping information changed?',
        'fallback':'I dont quite understand. Could you repeat that?',
    }

    print("Welcome to TTC!")

    #While loop to run the chatbot indefinitely
    while(True):
        #Takes the user input and converts all characters to lowercase
        user_input = input().lower()

        #Defining the chatbot's exit condition
        if user_input == 'quit':
            print("Thanks for choosing TTC!")
            break
        matched_intent = None

        for intent,pattern in keywords_dict.items():
            #Using the regular expression search function to look for keywords
            # in user input
            if re.search(pattern,user_input):
                #If a keyword matches, select the corresponding intent from 
                # the keywords_dict dictionary
                matched_intent = intent

        #The fallback intent is selected by default
        key='fallback'

        if matched_intent in responses:
            #If a keyword matches, the fallback intent is replaced by the matched
            #intent as the key for the responses dictionary
            key = matched_intent

        #The chatbot prints the response that matches the selected intent
        print(responses[key])