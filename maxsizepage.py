import urllib.request

'''finds the max number from a file that has numbers that show the amount of tokens in a url'''

def maxSizePage():
    with open('/home/alexanvl/cs121/assignment2/spacetime-crawler4py/second-reports/report_q2.txt', 'r') as uf:
        size_set = set()
        for s in uf: 
            size_set.add(int(s.strip()))

    tokenMax = max(size_set)
    print(tokenMax)

if __name__ == "__main__":
     maxSizePage()