import sys
import copy

class findWord:
    name = ""
    length = 0
    count = 0
    lineNumber = 0

def printInstance(fw):
    print "Name: %s | Length: %d | Count: %d | Line Number: %d"  % (fw.name,fw.length,fw.count,fw.lineNumber)

def openFile(input):
    wordList = []
    instanceList = []
    with open(input, 'r') as input_file:

        #populate list of words in header
        for count, line in enumerate(input_file):
            if count < 4:
                elements = line.split()
                for element in elements:
                    wordList.append(element)

    #for each word in the header, find its attributes
    for word in wordList:
        fw = findWordFunc(word,input)
        printInstance(fw)

def findWordFunc(word,input):
    with open(input, 'r') as input_file:
        for count,line in enumerate(input_file):
            if count<4:
                elements = line.split() #split the line into words
                for element in elements: #iterate through every word in a line
                    if word == element:
                        fw = findWord
                        fw.name = element
                        fw.length = len(element)
                        fw.lineNumber = count
                        counter = 0
                        for characterCount,character in enumerate(line):
                            if character == list(word)[counter]:
                                #print str(characterCount) + str(character) + str(list(find)[counter])
                                if len(word)<3: #like "Mn" or "Dy"
                                    if counter == 1:
                                        fw.count = characterCount-counter
                                        return fw
                                else:
                                    if counter == 3:
                                        fw.count = characterCount-counter
                                        return fw
                                counter += 1


if __name__ == '__main__':
    openFile("alt_2004_09.dat")
