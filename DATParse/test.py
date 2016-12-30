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

def getInstanceList(input):
    """
    Initial function; this is called to create a list of all the headers.

    Argument: Total .dat file which needs parsing of headers.
    Return: Unsorted list of instances.

    The output will not be filtered, it will include all words found in the first four lines of the input.
    """
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
        fw = getInstance(word,input)
        instanceList.append(copy.deepcopy(fw))

    return instanceList

def getInstance(word,input):
    """Compares the list of all the headers to the first 4 lines of a file and determines how many characters appear before each header. This is used to determine left-to-right order."""
    # Called by getInstanceList, do not access directly.
    with open(input, 'r') as input_file:
        for count,line in enumerate(input_file):
            if count<4:
                elements = line.split() #split the line into words
                for element in elements: #iterate through every word in a line
                    if word == element:
                        fw1 = findWord()
                        fw1.set_variable('name', element)
                        fw1.set_variable('length', len(element))
                        fw1.set_variable('lineNumber', count)
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

                            elif counter > 0:
                                counter = 0
                                pass
                            #if non consecutive, reset. This is very important because otherwise words can be found early. For instance, "U_IR" can be found long before all four characters of "U_IR" are found consecutively. "U" can be found in "DIFFUSE" and then "_IR" can be picked up from "D_IR". Besides, consecutive letters is a better practice for finding matches.

def sortInstanceList(instanceList):
    """Returns a sorted list of all the headers."""
    return sorted(instanceList, key=lambda instance: instance.get_variable('position'))

def printList(instanceList):
    """Prints a list of headers with its position. Used for testing."""
    for instance in instanceList:
        print "%s: %d" % (instance.get_variable('name'),instance.get_variable('position'))

def getCSVHeaders(instanceList):
    """Returns a string formatted for .csv files"""
    csvHeaderString = ""
    for count,instance in enumerate(instanceList):
        temp = instance.get_variable('name')
        if count!=len(instanceList)-1:
            csvHeaderString += temp + ","
        else:
            csvHeaderString += temp
            return csvHeaderString

def filterInstanceList(instanceList):
    filterList = ["ALT_RAD","ALT_RAD2","BAO0_RAD","BAO_RAD","BER_RAD","BRW_RAD","BRW_RAD2","KWA_RAD","MLO_RAD","SMO_RAD","SPO_RAD","SUM_RAD2","THD_RAD"]
    for count,instance in enumerate(instanceList):
        for word in filterList:
            if instance.get_variable('name') == word:
                del instanceList[count]

    return instanceList

if __name__ == '__main__':
    instanceList = getInstanceList(sys.argv[1])
    sortedInstanceList = sortInstanceList(instanceList)
    sortedInstanceList = filterInstanceList(sortedInstanceList)
    printList(sortedInstanceList)
