'What is Web Scraping?'
#When a program or script pretends to be a browser and retrieves web apges, looks at those web pages, extracts information, and then looks at more web pages
#Search engines scrape web pages - we call this "spidering the web" or "web crawling"

'Why Scrape?' #might not be legal lmaooo
#Pull data - particularly social data - who links to who?
#Get your own data out of some system that has no "export capability"
#Monitor a site for new information
#Spider the web to make a database for a search engine

'Scraping Web Pages'
#There is some controversy about web page scraping and some sites are a bit snippy about it.
#Republishing copyright information is not allowed
#Violating terms of service is not allowed

'The Easy Way - Beautiful Soup'
#You could do string searches the hard way
#Or use the free software library called BeautifulSoup (aka HTML superparser) from www.crummy.com

'BeautifulSoup Installation'
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read() #.read() = read it all, not a for loop. whole blob with \n's at the end and it comes into one big string
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a') #give me a list of all the anchor tags in the document
for tag in tags:
    print(tag.get('href', None)) #get the href key (link) or none.

'Summary'
#The TCP/IP gives up pipes/sockets between applications
#We designed application protocols to make use of these pipes
#HyperText Transfer Protocol (HTTP) is a simple yet powerful protocol
#Python has good support for sockets, HTTP, and HTML parsing
