# Things I Learned
Adding user-agent to headers for a BeautifulSoup (BS) request solves a 403 access blocked error

Lots of style tags in the BS output that I couldn't see in the inspect element tab, which mucked up everything and made it hard to parse. I made sure the required text was still there by performing a results.text.strip() and CTRL+F searching. At first I explored by starting broad and iterating through direct children tags [obtained with find_all(recursive=False)] then picking the right one to keep narrowing down and repeating. Then, I learned I could do 
for tag in soup("style"):
    tag.decompose() 
which gets rid of all style tags. This did not get rid of any important data.

find() returns the first tag matching the parameters. Similarly, .section.ol finds the first section tag and then the first ol tag within it.

find('tag_type', class_='XXX', id='XXX', attrs={'Atr1':'XXX', 'Atr2':'XXX', etc})

Practiced working with files and command line arguments. Created a variable `out` that served as either a print or f.write depending on if output was command line or output.txt, but didn't account for the fact that f.write doesn't automatically add \n to each line. Tried to then have print for all but have a parameter out which equals "end='\n'" if cmd line (which is default setting) and "file=f" if output.txt (specifying a file output). However, couldn't get Python to view `out` as code and not a string (tried stripping of quotes, tried using exec(), etc). Settled with leaving `out` as a flag for selecting between two different print statements.

Input in format: python FINAL.py [URL, courselist.txt] [-f]
The optional [-f] must go after the optional [URL, courselist.txt]

Realized that all the links we use in DU are when we're logged into DU, which when not signed in, gives a sign-in screen and doesn't display necessary info. Checking link format and changing if necessary from https://app.datacamp.com/learn/courses/course-title to https://datacamp.com/courses/course-title solves this issue, making this program much more convenient to use.