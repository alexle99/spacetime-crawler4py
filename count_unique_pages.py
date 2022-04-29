import urllib.request

def count_unique_pages():
    with open('/home/rtighiou/121-clone/spacetime-crawler4py/report_q1.txt', 'r') as uf:
        count = 0
        url_set = set()
        for url in uf:
            #try:
            #response = urllib.request.urlopen(url)
            
            url_set.add(url)
            count += 1
            if count % 100 == 0:
                print(f"Current count: {count}")
            #except Exception as err:
                #print("Error: ", err)
    print(len(url_set))

if __name__ == "__main__":
    count_unique_pages()