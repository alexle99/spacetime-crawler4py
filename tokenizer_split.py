def tokenize(content):
    finList = []
    matchString = "abcdefghijklmnopqrstuvwxyzABCDEDFGHIJKLMNOPQRSTUVWXYZ0123456789"

    content_list = content.split('\n')
    for lineStr in content_list:
        finStr = ""
        index = 0
        for chars in lineStr:
            if not(chars in matchString):
                chars = ' '
                if finStr and index and finStr[index-1] == ' ':
                    chars = ''
                    index -= 1
            finStr += chars
            index += 1
        if finStr:
            for strings in finStr.split():
                finList.append(strings.lower())
    return finList

# This function will loop through N elements of the given list and
# determine whether the value has already been seen, if it has, increase
# the number of times (value).
def computeWordFrequencies(tokenList):
    finDict = {}
    for value in tokenList:
        if value not in finDict:
            finDict[value] = 1
        else:
            finDict[value] += 1
    return finDict