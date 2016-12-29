import sys

class findWord:
    name = ""
    length = 0
    count = 0
    lineNumber = 0

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

    print "DONE"

    #for each word in the header, find its attributes
    for word in wordList:
        with open(input, 'r') as input_file:
            for count,line in enumerate(input_file):
                #print count,word
                if count<4:
                    elements = line.split()
                    for element in elements:
                        fw = findWord
                        fw.name = element
                        print element
                        fw.length = len(element)
                        fw.lineNumber = count
                        counter = 0
                        for characterCount,character in enumerate(line):
                            if character == list(word)[counter]:
                                #print str(characterCount) + str(character) + str(list(find)[counter])
                                counter +=1
                                if counter == 3:
                                    fw.count = characterCount-2
                                    #print str(fw.count) + "WOW"
                                    instanceList.append(fw)
                                    counter = 0
        #print wordList
        for instance in instanceList:
            print instance.name
            print instance.length
            print instance.count
            print instance.lineNumber


if __name__ == '__main__':
    openFile("alt_2004_09.dat")
