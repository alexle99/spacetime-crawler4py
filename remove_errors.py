import urllib.request

def test():
    counter = 0
    with open("/home/alexanvl/cs121/assignment2/spacetime-crawler4py/first-reports/report_q1_copy.txt", "r") as rf:
        for url in rf:
            try:
                response = urllib.request.urlopen(url)
            except urllib.error.HTTPError as err:
                print("ERROR IS ", err)
                print(url)
            finally:
                if counter % 100 == 0:
                    print(f"Counter at: {counter}")
                counter += 1
            


if __name__ == "__main__":
    test()