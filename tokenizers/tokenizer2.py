from bs4 import BeautifulSoup
from urllib import request


def get_content(url):
    response = request.urlopen(url)
    html = response.read().decode('utf-8')
    content = BeautifulSoup(html, "lxml").get_text()
    with open("test.txt", "w") as f:
        for lines in content:
            if lines:
                print("CURRENT LINE", lines)
                f.write(lines)
    return "test.txt"


if __name__ == "__main__":
    # url="https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
    url="https://github.com/alexle99/spacetime-crawler4py"
    get_content(url)