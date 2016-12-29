import sys


def openFile(string):
    testString = "                    ALT_RAD                                                \n                                                   ALT_RAD2                \n                     DIRECT        D_GLOBAL        U_GLOBAL          Zenith\n   Year Mn Dy Hr Mi        DIFFUSE2            D_IR            U_IR        "
    letterCount = len(string) - len(string.lstrip())
    print letterCount



if __name__ == '__main__':
    openFile(sys.argv[1])
