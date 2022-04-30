# adding stop words as a constant global variable because reading it from a file is expensive i think?
# finding a stop word in a set is O(1) on average
STOPWORDS = set([
"a",
"about",
"above",
"after",
"again",
"against",
"all",
"am",
"an",
"and",
"any",
"are",
"aren",
"as",
"at",
"be",
"because",
"been",
"before",
"being",
"below",
"between",
"both",
"but",
"by",
"can",
"cannot",
"could",
"couldn",
"did",
"didn",
"do",
"does",
"doesn",
"doing",
"don",
"down",
"during",
"each",
"few",
"for",
"from",
"further",
"had",
"hadn",
"has",
"hasn",
"have",
"haven",
"having",
"he",
"her",
"here",
"hers",
"herself",
"him",
"himself",
"his",
"how",
"how",
"i",
"if",
"in",
"into",
"is",
"isn",
"it",
"its",
"itself",
"let",
"me",
"more",
"most",
"mustn",
"my",
"myself",
"no",
"nor",
"not",
"of",
"off",
"on",
"once",
"only",
"or",
"other",
"ought",
"our",
"ours",
"ourselves",
"out",
"over",
"own",
"same",
"shan",
"she",
"should",
"shouldn",
"so",
"some",
"such",
"than",
"that",
"that",
"the",
"their",
"theirs",
"them",
"themselves",
"then",
"there",
"these",
"they",
"this",
"those",
"through",
"to",
"too",
"under",
"until",
"up",
"very",
"was",
"wasn",
"we",
"were",
"weren",
"what",
"when",
"where",
"which",
"while",
"who",
"whom",
"why",
"with",
"won",
"would",
"wouldn",
"you",
"your",
"yours",
"yourself",
"yourselves",
"t",
"s",
"ve",
"re",
"ll",
"d",
])

''' returns a list of tokens that do not have stopwords'''

def tokenize(content):
    global STOPWORDS
    tokens = []
    matchString = "abcdefghijklmnopqrstuvwxyzABCDEDFGHIJKLMNOPQRSTUVWXYZ0123456789"

    content_list = content.split('\n')
    for line in content_list:
        finStr = ""
        i = 0
        for chars in line:
            if not(chars in matchString):
                chars = ' '
                if finStr and i and finStr[i-1] == ' ':
                    chars = ''
                    i -= 1
            finStr += chars
            i += 1
        if finStr:
            for strings in [s.lower() for s in finStr.split()]: #lowrcase strings in split
                if strings not in STOPWORDS:
                    tokens.append(strings)
    return tokens

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