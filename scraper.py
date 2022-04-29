from collections import defaultdict
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urldefrag, urljoin
from tokenizer_split import tokenize, computeWordFrequencies
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
    # result = [] #list of next links to return
    resultSet = set()
    visited = defaultdict(int) #keeps track of visited netloc, path tuple to prevent redundancy
    previous_hash = ssimhash.simhash("")
    hash1 = previous_hash
    THRESHOLD = 10

    #check if response is not 200 (invalid)
    if resp.status != 200 and resp.status != 301 and resp.status != 307: 
        return []


    if (resp.raw_response and resp.raw_response.url and resp.raw_response.content): #.url and .content for dead urls preliminary
        content = BeautifulSoup(resp.raw_response.content, "lxml").get_text()
        token_list = tokenize(content)
        token_frequency = sorted(computeWordFrequencies(token_list).items(), key=lambda x : -x[1])
        acc = 0
        with open('report_q3.txt', 'a') as cof:
            for values in token_frequency:
                if acc == 50:
                    break
                cof.write(values[0])
                cof.write('\n')
                acc += 1
        
        unfragmented = urldefrag(url)[0]
        parsed = urlparse(unfragmented)

        # Q1 on the report
        with open('report_q1.txt', 'a') as of:
            of.write(unfragmented)
            of.write('\n')

        # Q2 on the report
        with open('report_q2.txt', 'a') as wf:
            wf.write(str(len(token_list)))
            wf.write('\n')

        simhash_list = []
        url_set = set()

        
        for link in BeautifulSoup(resp.raw_response.content, parse_only=SoupStrainer('a'), features="html.parser"):
            if link.has_attr('href'):
                t = link['href']
                unfragmented = urldefrag(t)[0]
                if link not in url_set:
                    if (unfragmented[0].startswith("/")):
                        baseUrl = url
                        relativeUrl = link.get("href")
                        unfragmented = urljoin(baseUrl, relativeUrl)

                # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
                parsed = urlparse(unfragmented)
                # This compares the current URL to a previous URL based on their
                # netloc & path, in which a dynamic trap will differ solely on their
                # params...

                if parsed.netloc and parsed.path:
                    if f"{parsed.netloc}{parsed.path}" not in visited and (visited[f"{parsed.netloc}{parsed.path}"] < THRESHOLD):
                        visited[f"{parsed.netloc}{parsed.path}"] += 1
                        # result.append(unfragmented)
                        resultSet.add(unfragmented)
                        url_set.add(unfragmented)
                    else:
                        hash1 = ssimhash.simhash(tokenize(content))
                        if (hash1.similarity(previous_hash) < .95) and (visited[f"{parsed.netloc}{parsed.path}"] < THRESHOLD):
                            visited[f"{parsed.netloc}{parsed.path}"] += 1
                            # result.append(unfragmented)
                            resultSet.add(unfragmented)
                            url_set.add(unfragmented)


                    # ics.uci.edu
                    # Q4 on the report
                    if  re.match(r"^(.*ics.uci.edu)$", parsed.netloc):
                        with open('report_q4.txt', 'a') as icsf:
                            icsf.write(unfragmented)
                            icsf.write('\n')

            previous_hash = hash1
            simhash_list.append(hash1)
    return list(resultSet)

def is_valid(url):
    # Decide whether to crawl this url or not. 
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    #print("Checking validity")

    parsed = urlparse(url)

    #print("Valid checker")
    try:
        result = re.match(r"^(.*\.ics.uci.edu/.*|.*\.cs.uci.edu/.*|.*\.informatics.uci.edu/.*|.*\.stat.uci.edu/.*|today.uci.edu/department/information_computer_sciences/.*)$", url)
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
