"""
This file accepts .dat files with offset headers such as the one found here(http://bit.ly/2ipTrbn). It's purpose is to return a sorted list of headers as they appear left to right regardless of line numbers. This assumes all headers appear on lines 0-3 (assuming the first line as line 0).
"""
import sys
import copy

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
        fw.print_info()
        instanceList.append(copy.deepcopy(fw))

def findWordFunc(word,input):
    with open(input, 'r') as input_file:
        for count,line in enumerate(input_file):
            if count<4:
                elements = line.split() #split the line into words
                for element in elements: #iterate through every word in a line
                    if word == element:
                        fw1 = findWord()
                        fw1.set_variable('name',element)
                        fw1.set_variable('length', len(element))
                        fw1.set_variable('lineNumber',count)
                        counter = 0
                        for characterCount,character in enumerate(line):
                            if character == list(word)[counter]:
                                if len(word)<3: #like "Mn" or "Dy"
                                    if counter == 1:
                                        fw1.set_variable('position',characterCount-counter)
                                        return fw1
                                else:
                                    if counter == 3:
                                        fw1.set_variable('position',characterCount-counter)
                                        return fw1
                                counter += 1

                            #if non consecutive, reset
                            elif counter > 0:
                                counter = 0
                                pass

if __name__ == '__main__':
    openFile(sys.argv[1])
