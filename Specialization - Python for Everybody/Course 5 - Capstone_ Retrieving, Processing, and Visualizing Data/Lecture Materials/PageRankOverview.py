'Page Rank'
#Write a simple web crawler
#Compute a simple version of Google's Page Rank algorithm
#Visualize the resulting network

'Search Engine Architecture'
#Web Crawling
#Index Building
#Searching

'Web Crawler'
#A Web crawler is a computer program that browses the World Wide Web in a methodical, automated manner.
#Web crawlers are mainly used to create a copy of all the visited web pages for later processing by a seach
#engine that will index the downloaded pages to provide fast searches.

#Retrieve a page
#Look through the page for links
# Add the links to a list of "to be retrieved" sites
#Repeat...

'Web Crawling Policy'
#*a selection policy that states which pages to download.
#a re-visit policy that staes when to check for changes to the pages,
#!a politeness policy that states how to avoid overloading Web sites, and
#?a parallelization policy that states how to coordinate distributed Web crawlers

'robots.txt'
#A way for a web site to communicate with web crawlers
#An informal and voluntary standard
#Sometimes folks make a "Spider Trap" to catch "bad" spiders
'''
User-agent: *
Disallow: /cgi-bin/
Disallow: /images/
Disallow: /tmp/
Disallow: /private/
'''

'Searching Indexing'
#Search engine indexing collects, parses, and stores data to faciliate fast and accurate information retrieval.
#The purpose of storing an index is to optimize speed and performance in finding relevant documents for a search
#query. Without an index, the search engine would scan every document in the corpus, which would require considerable
#time and computing power.
