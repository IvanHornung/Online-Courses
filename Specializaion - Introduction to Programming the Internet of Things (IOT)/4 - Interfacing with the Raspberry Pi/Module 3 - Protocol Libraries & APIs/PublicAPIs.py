#Public APIs

'Example API for Sentiment Analysis'
#Sentiment analysis analyzes text to determine if it is positive or negative
#   -"I hate cats" score = -1
#   -"I love cats" score = +1
#AlchemyAPI (owned by IBM) does this
#Can download their SDK and use their API
#   -May not work on Raspberry Pi

'AlchemyAPI SDK'
#Want to scan a web page and check its sentiment
#Webpage is written in HTML

from alchemyapi import AlchemyAPI

demo_html = '<html><body>AlchemyAPI works on HTML</body></html>'

response = alchemyapi.sentiment('html', demo_html)

if 'score' in response['docSentiment']:
    print('score: ', response['docSentiment']['score'])
