import urllib.request

def maxSizePage():
    with open('/home/rtighiou/121-clone/spacetime-crawler4py/report_q2.txt', 'r') as uf:
        count = 0
        size_set = set()
        for s in uf: 
            size_set.add(int(s.strip()))
            #print(s)

    tokenMax = max(size_set)
    print(tokenMax)

if __name__ == "__main__":
     maxSizePage()