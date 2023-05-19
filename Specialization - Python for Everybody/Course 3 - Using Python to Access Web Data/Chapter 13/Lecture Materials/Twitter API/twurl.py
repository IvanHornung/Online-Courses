import urllib
import oauth #part of python
import hidden #you have to write, put the four strings in there

def augment(url, parameters) :
  secrets = hidden.oauth()
  consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
  token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])
  oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, token=token, http_method='GET', http_url=url, parameters=parameters) #make request
  oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token) #sign request
  return oauth_request.to_url()
