import re

def tokenize(html):
    print(type(str(html)))
    print(str(html))
    t_list = list()
    #textFile = open(textFilePath, 'r')
    new_list = str(html).split("\n")
    for line in new_list:
        t_list += [w.lower() for w in re.findall(r'[a-zA-Z0-9]+', line)]
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