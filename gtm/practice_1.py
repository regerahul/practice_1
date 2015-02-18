from os import listdir
from os.path import isfile, join

index = {}

mypath = '_data'
txtFiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for fileName in txtFiles:
  openFile = open("_data/" + fileName, "rU")
  for line in openFile:
    splitLine = line.split(" ")
    for word in splitLine:
      if word in index:
      	index[word]['count'] += 1
      	index[word]['files'].append(fileName)
      else:
        index[word] = {}
        index[word]['count'] = 1
        index[word]['files'] = [fileName]

print(index)
