

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