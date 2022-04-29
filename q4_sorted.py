from urllib.parse import urlparse, urldefrag
from collections import defaultdict
import re

def subdomain_counter():
    '''
    Write to a file all subdomains of ics.uci.edu (domain)
    ordered alphabetically and the number of unique pages
    detected in each subdomain.
    '''
    with open('report_q4.txt', 'r') as q1f:
        d = defaultdict(lambda : [None, 0])
        for url in q1f:
            unfragmented = urldefrag(url)[0]
            parsed_url = urlparse(unfragmented)
            netloc = parsed_url.netloc.strip("www.")
            subdomain = re.split(r"(\.ics\.uci\.edu)", netloc)[0]
            if 'ics.uci.edu' not in subdomain:
                d[subdomain][0] = unfragmented
                d[subdomain][1] += 1
        sorted_q3 = sorted(d.items(), key=lambda x : x[0][0])

    with open('report_q44.txt', 'w') as wq1:
        for value in sorted_q3:
            t = str(value[1][0]).strip('\n')
            tt = str(value[1][1])
            wq1.write(f"{t}, {tt}\n")

if __name__ == "__main__":
    subdomain_counter()