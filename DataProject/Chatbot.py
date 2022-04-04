import nltk
import re
from nltk.corpus import wordnet
#Chatbot scaffolding and psuedocode
#re is a package for regular expressions
#Helps with a dictionary of synonyms for keywords

#Dependencies that need to be imported

class Chatbot():
    #List of keywords to respond to
    #Hello, order, stock, shipping
    list_words = ['Hello', 'Order', 'Stock', 'Shipping']

    list_syn = {}

    for word in list_words:
        synonyms = []
        
        for syn in wordnet.synsets(word):

            for lem in syn.lemmas():
                #Remove any special characters from synonym strings
                lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
                synonyms.append(lem_name)

        list_syn[word] = set(synonyms)
    
    print(list_syn)

