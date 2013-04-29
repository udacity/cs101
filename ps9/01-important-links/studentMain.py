# Use the BeautifulSoup module to define a bold_links(page) procedure
# that takes as input a string representing the contents of a web page,
# and returns a set containing all the important links on that page.
# An important link is a link that is inside a bold (<b>...</b>) element
# or that contains a bold element inside the link text.
# For example, the string in the following page variable contains 2 bold links:
# 'http://www.cs.virginia.edu/evans/' and 'http://davedavefind.appspot.com/'.
page = """
        <a href="http://duckduckgo.com">DuckDuckGo</a> is pretty good, but it isn't
<b><a href="http://www.cs.virginia.edu/evans/">Dave</a></b>'s
<a href="http://davedavefind.appspot.com/"><b>favorite</b> search engine</a> or
<a href="http://www.cs.cmu.edu/~rgs/alice-X.html"><em>soup</em></a>!
"""
important = set(['http://www.cs.virginia.edu/evans/', 'http://davedavefind.appspot.com/'])

from bs4 import BeautifulSoup

# This is an example of how to work with Beautiful Soup
# For more information see the documentation at
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree
def get_all_links(page):
    soup = BeautifulSoup(page)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def bold_links(page):
    links = get_all_links(page)
    return links

# test
print bold_links(page) == important
