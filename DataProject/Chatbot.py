import nltk
#nltk.download() #Empty field to download "wordnet" and "omw-1.4" from ntlk library window, under the second tab corpora, then can be commented out
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
    
    print(list_syn)

