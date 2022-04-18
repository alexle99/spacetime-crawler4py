import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urldefrag


def scraper(url, resp):
    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]


# Implementation required.
# url: the URL that was used to get the page
# resp.url: the actual url of the page
# resp.status: the status code returned by the server. 200 is OK, you got the page. Other numbers mean that there was some kind of problem.
# resp.error: when status is not 200, you can check the error here, if needed.
# resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
#         resp.raw_response.url: the url, again
#         resp.raw_response.content: the content of the page!
# Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content
def extract_next_links(url, resp):
    from collections import defaultdict
    """
    Status responses:
    https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html

    """
    result = list()
    visited = defaultdict(int)
    THRESHOLD = 3

    # print("Entering extraction")
       
    #check if response is not 2XX (invalid)
    if resp.status not in range(200, 300): 
        return result
        
    if (resp.raw_response):
        for link in BeautifulSoup(resp.raw_response.content, parse_only=SoupStrainer('a'), features="html.parser"):
            if link.has_attr('href'):
                t = link['href']
                # print("Type is ", type(t))
                unfragmented = urldefrag(t)[0]
                parsed = urlparse(unfragmented)
                if visited[(parsed.netloc, parsed.path)] < THRESHOLD:
                    visited[(parsed.netloc, parsed.path)] += 1
                    result.append(unfragmented)
    return result

def is_valid(url):
    # Decide whether to crawl this url or not. 
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    #print("Checking validity")

    parsed = urlparse(url)

    #print("Valid checker")
    try:
        result = re.match(r"(.*\.ics.uci.edu/.*|.*\.cs.uci.edu/.*|.*\.informatics.uci.edu/.*|.*\.stat.uci.edu/.*|today.uci.edu/department/information_computer_sciences/.*)$", url)
        if (not result):
            return False

        if parsed.scheme not in {"http", "https"}:
            return False

        result = not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

        return result

    except TypeError:
        print ("TypeError for ", parsed)
        raise
