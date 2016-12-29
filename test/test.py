import sys

class findWord:
    name = ""
    length = 0
    position = 0
    lineNumber = 0

def printInstance(fw):
    string = "Name: %s | Length: %d | Position: %d | Line Number: %d"  % (fw.name,fw.length,fw.position,fw.lineNumber)
    print string

def openFile(input):
    wordList = [] #list of all words found in header
    instanceList = [] #list of all word objects

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
                                if len(word)<3: #like "Mn" or "Dy"
                                    if counter == 1:
                                        fw.position = characterCount-counter
                                        return fw
                                else:
                                    if counter == 3:
                                        fw.position = characterCount-counter
                                        return fw
                                counter += 1

                            #if non consecutive, reset
                            elif counter > 0:
                                counter = 0
                                pass


if __name__ == '__main__':
    openFile(sys.argv[1])
