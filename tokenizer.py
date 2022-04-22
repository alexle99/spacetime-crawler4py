from bs4 import BeautifulSoup
from urllib import request


def get_content(url):
    response = request.urlopen(url)
    html = response.read().decode('utf-8')
    content = BeautifulSoup(html, "lxml").get_text()
    return content


# This function will tokenize the given words from the given text file
# as the text file is passed as a path. The path will be either absolute
# or relative. If the given argument is not an existing path, then an error
# will be raised and the program will terminate. We will iterate over the entire
# file line by line instead of reading the entire file all at once in order to
# prevent any program crashes from memory issues. As we grab one line, we iterate
# over that specific line to grab character by character, we "replace" any illegal
# characters with a space, but the way the algorithm works is we are building the same
# line to only include legal characters, e.g., "wate##r 000___     S&&" will end up
# being "stripped" of its illegal characters and become "wate r 000 S", reducing
# what our original line was, after doing so we can split based on whitespace as
# assuming the algorithm works as it should, tokens will be separated by one whitespace.
def tokenize(TextFile):
    finList = []
    matchString = "abcdefghijklmnopqrstuvwxyzABCDEDFGHIJKLMNOPQRSTUVWXYZ0123456789"
    with open(TextFile, "r") as f:
        lineStr = True
        iterations = 0
        while lineStr:
            lineStr = f.readline()
            finStr = ""
            index = 0
            for chars in lineStr:
                if not(chars in matchString):
                    chars = ' '
                    if index and finStr and finStr[index-1] == ' ':
                        chars = ''
                        index -= 1
                finStr += chars
                index += 1
            if finStr:
                for strings in finStr.split():
                    finList.append(strings.lower())
            iterations += 1
        print("Number of iterations: ", iterations)
    return finList