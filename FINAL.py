#https://scrapeops.io/web-scraping-playbook/403-forbidden-error-web-scraping/

import requests
import sys
from bs4 import BeautifulSoup

multiple_links = False
out = "cmd"
if (len(sys.argv) == 1):
    URL = input("Enter URL: ")
elif (len(sys.argv) > 1):
    if sys.argv[1] == "test":
        URL = "https://www.datacamp.com/courses/intro-to-python-for-data-science"
    elif ".txt" in sys.argv[1]:
        URL = open(sys.argv[1], "r").read().split("\n")
        multiple_links = True
    elif sys.argv[1] == "-f":
        out = "file"
        URL = input("Enter URL: ")
    elif ("https" in sys.argv[1]) or ("www" in sys.argv[1]): # "or" or "and"?
        URL = sys.argv[1]
    else:
        print("Invalid input. Please enter a valid URL or file name.")
        quit()

    if len(sys.argv) > 2 and sys.argv[2] == "-f":
        out = "file"

HEADERS = {  # Prevents 403 error of website blocking access to bots (could be fine with just the user-agent component)
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }

if multiple_links:
    for link in URL:
        link = link.replace("app.", "")
        link = link.replace("learn/", "")

        if (len(sys.argv) > 1 and sys.argv[1] == "-f") or (len(sys.argv) > 2 and sys.argv[2] == "-f"):
            f = open("output.txt", "a")

        page = requests.get(link, headers=HEADERS)

        soup = BeautifulSoup(page.content, "html.parser")
        for tag in soup("style"):
            tag.decompose() # Remove all style tags

        course_info = soup.find('body').find('div', id='__next').find('div', id='main').header
        
        if out == "file":
            print("\nCOURSE NAME: " + course_info.h1.text.strip(), file=f)
            print("DESCRIPTION: " + course_info.p.text.strip() + "\n", file=f)
        else:
            print("\nCOURSE NAME: " + course_info.h1.text.strip())
            print("DESCRIPTION: " + course_info.p.text.strip() + "\n")

        results = soup.find('body').find('div', id='__next').find('div', id='main').find('div', attrs={'data-test-id': 'course-description'}).section.ol.find_all("li", recursive=False)

        for section in results: # Each section of the course
            if out == "file":
                print("\n" + "SECTION TITLE: " + section.find("h3").text.strip(), file=f)
            else:
                print("\n" + "SECTION TITLE: " + section.find("h3").text.strip())

            for skill in section.find_all(recursive=False)[0].find_all(recursive=False)[3].find_all(recursive=False):
                if out == "file":
                    print(skill.find_all(recursive=False)[0].text.strip(), file=f)
                else:
                    print(skill.find_all(recursive=False)[0].text.strip()) # [0] here to isolate the Title from the XP
        if out == "file":
            print("-----------------------------------------------------", file=f)
        else:
            print("-----------------------------------------------------")
else:
    URL = URL.replace("app.", "")
    URL = URL.replace("learn/", "")
    
    if (len(sys.argv) > 1 and sys.argv[1] == "-f") or (len(sys.argv) > 2 and sys.argv[2] == "-f"):
        f = open("output.txt", "a")

    page = requests.get(URL, headers=HEADERS)

    soup = BeautifulSoup(page.content, "html.parser")
    for tag in soup("style"):
        tag.decompose() # Remove all style tags

    course_info = soup.find('body').find('div', id='__next').find('div', id='main').header
    if out == "file":
        print("\nCOURSE NAME: " + course_info.h1.text.strip(), file=f)
        print("DESCRIPTION: " + course_info.p.text.strip() + "\n", file=f)
    else:
        print("\nCOURSE NAME: " + course_info.h1.text.strip())
        print("DESCRIPTION: " + course_info.p.text.strip() + "\n")

    results = soup.find('body').find('div', id='__next').find('div', id='main').find('div', attrs={'data-test-id': 'course-description'}).section.ol.find_all("li", recursive=False)

    for section in results: # Each section of the course
        if out == "file":
            print("\n" + "SECTION TITLE: " + section.find("h3").text.strip(), file=f)
        else:
            print("\n" + "SECTION TITLE: " + section.find("h3").text.strip())

        for skill in section.find_all(recursive=False)[0].find_all(recursive=False)[3].find_all(recursive=False):
            if out == "file":
                print(skill.find_all(recursive=False)[0].text.strip(), file=f)
            else:
                print(skill.find_all(recursive=False)[0].text.strip()) # [0] here to isolate the Title from the XP
    
    if out == "file":
        print("-----------------------------------------------------", file=f)
    else:
        print("-----------------------------------------------------")