# practice_1

Problem 1 : Creating inverted index 

Inverted index - Inverted index is usually used in fast text search engines. In our practice problem, it'd be just used on few data files. Lets consider there are 3 documents with their one line content as below :

D1 - "Hi this is practice"
D2 - "practice makes you perfect"
D3 - "Perfect example !"

What we need to build is an index structure which backwords stores this information in below data structure. So for above example --

'hi' - 1 -> [(1,D1)]
'this' - 1 -> [(1,D1)]
.
.
.
'practice' - 2 -> [(1,D1),(1,D2)]
'perfect' - 2 -> [(1,D2),(1,D3)]

So, for each word, we store - its overall frequency, alongwith the its line number and the document in which it appears. E.g. word 'practice' above appears total twice, on first line in document D2 and on first line in document D1

Our task is to build this index when the programme starts and then search the list of keywords passed through the commandline and outputting only the documents which contain all those keywords. E.g. in above example, if the keywords are 'practice perfect' you'd output only D2
Moreover, when the program ends, it stores this index in a file. During the next run if the file is present, it would load the index in memory through that file instead of building it again

(optional) - You can also provide a 'ignore' file which has common verbs and english constructs such as 'of,this,are' and so on for which index building doesn't help much
----------------------------------------------

INPUT :

- list of keywords. 
The programme is supposed to scan all the files in 'data' directory, name of file is considered as document ID.
Example : 

python practice_1.py  


------------------------------------------------

OUTPUT :

List of document ids which contain all of the keywords




PS : You are supposed to use arrays, lists, dictionaries and stuff, don't write a code to run grep through python ;)
