import sys


def openFile(string):
    letterCount = len(string) - len(string.lstrip())
    print letterCount



if __name__ == '__main__':
    openFile(sys.argv[1])
