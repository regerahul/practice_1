import os
import sys

def generate_index():	
    dirs = os.listdir("../_data")
    inverted_index = {}
    for fx in dirs:
        p = open("../_data/"+str(fx))
        for line in p:
	    words = line.split(" ")
            for word in words:
                key = str(word).strip(',.!').lower()
	        if not key in inverted_index:
		    docs = []
                    docs.append(fx)
                    inverted_index[key] = docs
		else:
		    docs = inverted_index[key]
	            docs.append(fx)
    #print inverted_index
    return inverted_index       

def get_documents(tokens):
    #check if the index exists, if not, write it
#    index_dump = "_invertedIndexDump"
#    inverted_index = {}
#    if os.path.isFile(index_dump):
#         inverted_index = open(index_dump)
#    else:
     inverted_index = generate_index()
     allLists = []
     for token in tokens:
        token_key = token.strip(',.!').lower()
        if token_key in inverted_index:
            allLists.append(set(inverted_index[token_key]))
     return set.intersection(*allLists)     
     

def get_user_input():
    print "Enter list of words separated by space"
    ip = raw_input()
    tokens = str(ip).split(" ")
    print "Appears in following docs"
    for doc in get_documents(tokens):
        print doc 


get_user_input()

