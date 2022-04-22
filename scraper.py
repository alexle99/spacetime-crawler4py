from collections import defaultdict
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urldefrag
from tokenizer_split import tokenize
import ssimhash
""" 
DECISIONS & DOCUMENTATION:

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#parser-installation
- using LXML because faster and C dependend 

pip3 install simhash
https://leons.im/posts/a-python-implementation-of-simhash-algorithm/

<scheme>://<netloc>/<path>;<params>?<query>#<fragment>

LET all_urls_so_far be a set
if not(f"<scheme>://<netloc>/<path>" exists in all_urls_so_far):
    add current url to set

"""
previous_content = ""
previous_tokens = list()

token_counter = 0

def scraper(url, resp):
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
    global visited
    global previous_content
    result = [url]
    visited = defaultdict(int)
    THRESHOLD = 3

    #check if response is not 2XX (invalid)
    if resp.status not in range(200, 300): 
        return result

    # check to make sure the site has good content
    # check if site is too big
    # check if site lacks valuable information
    # check if site is similar to prevous url

    # additional requirements
    # keep track of how many unique urls we go through
    # What is the longest page in terms of the number of words? HTML markup doesn't count
    

    if (resp.raw_response):
        content = BeautifulSoup(resp.raw_response.content, "lxml").get_text()
        token_list = tokenize(content)
        print(len(token_list))


        for link in BeautifulSoup(resp.raw_response.content, parse_only=SoupStrainer('a'), features="html.parser"):
            if link.has_attr('href'):
                t = link['href']
                unfragmented = urldefrag(t)[0]
                # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
                parsed = urlparse(unfragmented)
                
                # This compares the current URL to a previous URL based on their
                # netloc & path, in which a dynamic trap will differ solely on their
                # params...
                
                if (previous_content):
                    
                    hash1 = ssimhash.simhash(tokenize(content))
                    hash2 = ssimhash.simhash(tokenize(previous_content))
                    if (visited[(parsed.netloc, parsed.path)] < THRESHOLD) and (hash1.similarity(hash2) < .98):
                        visited[(parsed.netloc, parsed.path)] += 1
                        print(f"Scheme: {parsed.scheme} & Netloc: {parsed.netloc} & Path: {parsed.path} & Params: {parsed.params}")
                        print(f"ADDING {parsed.path}")
                        result.append(unfragmented)
                else:
                    pass
            previous_content = content

    return result


# def dynamic_trap():


#     return

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
