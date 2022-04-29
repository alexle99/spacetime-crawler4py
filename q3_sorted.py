from collections import defaultdict
import os

def common_words():
    '''
    Write to a file the 50 most common words (excluding stopwords)
    ordered by frequency.
    '''
    # with open('report_q3.txt', 'r') as q1f:
    with open('report_test.txt', 'r') as q1f:
        d = defaultdict(int)
        for words in q1f:
            d[words] += 1
        sorted_q3 = sorted(d.items(), key=lambda x : -x[1])
    with open('report_q33.txt', 'w') as wq1:
        count = 0
        for sorted_word in sorted_q3:
            if count == 40:
                break
            word = str(sorted_word[0]).rstrip('\n')
            wq1.write(f"{word}\n")
            count += 1

if __name__ == "__main__":
    common_words()