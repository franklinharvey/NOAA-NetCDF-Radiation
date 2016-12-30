import sys

class findWord(object):
    def __init__(self, **kwargs):
        self.variables = kwargs

    def set_variable(self, k, v):
        self.variables[k]=v

    def get_variable(self, k):
        return self.variables.get(k, None)

    def print_info(self):
        for k in self.variables:
            print k + ": " + str(self.variables[k])

    # name = ""
    # length = 0
    # position = 0
    # lineNumber = 0

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
    index = 0
    for word in wordList:
        fw = findWordFunc(word,input)
        printInstance(fw)
        instanceList[index].name = fw.name
        instanceList[index].position = fw.position
        index += 1
    for instance in instanceList:
        print instance

def findWordFunc(word,input):
    with open(input, 'r') as input_file:
        for count,line in enumerate(input_file):
            if count<4:
                elements = line.split() #split the line into words
                for element in elements: #iterate through every word in a line
                    if word == element:
                        fw = findWord
                        fw.set_variable('name',element)
                        fw.set_variable('length', len(element))
                        fw.set_variable('lineNumber',count)
                        fw.print_info
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
