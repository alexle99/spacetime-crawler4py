with open('output.txt') as f:
    from collections import defaultdict
    d = defaultdict(int)

    for i in f:
        d[i] += 1

for j in d:
    if d[j] > 3:
        print(j, d[j])