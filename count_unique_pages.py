''' counts the number of unique links that are in a text file'''


def count_unique_pages():
    with open('/home/alexanvl/cs121/assignment2/spacetime-crawler4py/second-reports/report_q1.txt', 'r') as uf:
        count = 0
        url_set = set()
        for url in uf:
            url_set.add(url)
            count += 1
            if count % 100 == 0:
                print(f"Current count: {count}")
    print(len(url_set))

if __name__ == "__main__":
    count_unique_pages()