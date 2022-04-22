from collections import defaultdict

filename = "output.txt"

with open(filename, 'r') as f:
    d = defaultdict(int)
    for i in f:
        d[i] += 1

for i in d:
    if d[i] > 3:
        print(i, d[i])