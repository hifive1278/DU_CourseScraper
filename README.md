# DU_CourseScraper

Web scraping program created for Digital University Labs, using BeautifulSoup. The CourseScraper takes as input the URL to a DataCamp course (or .txt file containing a list of DataCamp courses) and returns the course title, description, and assignment titles (i.e. skills). Output can go to either the terminal or to the output.txt file.

To run in terminal, use: `python FINAL.py [URL, courselist.txt] [-f]`

The `-f` flag directs results to output.txt and must go after [URL, courselist.txt], which can be either a link, .txt file, or blank (in which case the program prompts the user for a URL). The URL may be in either a https://www.app.datacamp.com/... format or a https://www.datacamp.com/... format.