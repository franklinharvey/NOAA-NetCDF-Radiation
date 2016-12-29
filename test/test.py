import sys

class findWord:
    name = ""
    length = 0
    count = 0

def openFile(input):
    with open(input, 'r') as input_file:
        count = 0
        content = ""
        find = "ALT_RAD2"

        for count, line in enumerate(input_file):
            fw = findWord
            if count < 1:
                print line
                elements = line.split()
                for element in elements:
                    fw.name = element
                    fw.length = len(element)
                    for characterCount,character in enumerate(line):
                        for j in range(0,wordLength):
                            if character == list(find)[0]:
                                print str(characterCount) + "FOUND"

if __name__ == '__main__':
    openFile("alt_2004_09.dat")
