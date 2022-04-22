import re
# import nltk
import sys, time

#Import Modules
# from urllib import request
# from bs4 import BeautifulSoup
# import nltk
# from nltk import *
# from nltk.book import *
# from nltk.corpus import stopwords
#from xml.etree.ElementTree import ElementTree
from lxml import etree
'''

"Natural language processing is an exciting area."

print(sent_tokenize(text))
# output: ['Natural language processing is an exciting area.', 'Huge budget have been allocated for this.']

print(word_tokenize(text))
# output: ['Natural', 'language', 'processing', 'is', 'an', 'exciting', 'area', '.', 'Huge', 'budget', 'have', 'been', 'allocated', 'for', 'this', '.']


print(stopwords.words("english"))


https://www.analyticsvidhya.com/blog/2021/07/nltk-a-beginners-hands-on-guide-to-natural-language-processing/

'''

def tokenize(html):
    print(type(str(html)))
    print(str(html))
    t_list = list()
    #textFile = open(textFilePath, 'r')
    new_list = str(html).split("\n")
    for line in new_list:
        t_list += [w.lower() for w in re.findall(r'[a-zA-Z0-9]+', line)]
        print("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n\n\n")
    #textFile.close()
    return t_list

def computeWordFrequencies(tokenList):
    t_dict = dict()
    for token in tokenList:
        if token in t_dict:
            t_dict[token] += 1
        else:
            t_dict[token] = 1
    return t_dict
    
def printFrequencies(tokenDict):
    for w in sorted(tokenDict, key=lambda t: (-tokenDict[t], t)):
        print(f"{w} -> {tokenDict[w]}")

def tokenization(textFilePath):
    tl = tokenize(textFilePath)
    return computeWordFrequencies(tl)

def intersection(tDict1, tDict2):
    commonTokens = set(tDict1).intersection(set(tDict2))
    return len(commonTokens)


'''
Navigation
index
index
Beautiful Soup 4.9.0 documentation
Beautiful Soup Documentation
Navigation

'''

def tokenize(TextFilePath):
    finList = []
    matchString = "abcdefghijklmnopqrstuvwxyzABCDEDFGHIJKLMNOPQRSTUVWXYZ0123456789"
    with open(TextFilePath, "r") as f:
        lineStr = True
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
    return finList

if __name__ == "__main__":
    import tokenizer2
    # url="https://edstem.org/us/courses/21429/discussion/1425732"
    url="https://github.com/alexle99/spacetime-crawler4py"
    print(tokenize(tokenizer2.get_content(url)))