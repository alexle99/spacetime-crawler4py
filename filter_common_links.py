'''writes all the unique of a text file to a new text file'''

def count_unique_pages():
    urlSet = set() 
    with open('/home/alexanvl/cs121/assignment2/spacetime-crawler4py/first-reports/report_q1_copy.txt', 'r') as all_links:
        with open('unique_links_file.txt', 'a') as unique_links_file:
            for url in all_links:
                if url not in urlSet:
                    urlSet.add(url)
                    unique_links_file.write(url)
    print("LEN OF UNIQUE LINKS: " + str(len(urlSet)))

if __name__ == "__main__":
    count_unique_pages()