import os
import sys
 
# parse_qsl moved to urlparse module in v2.6
try:
  from urlparse import parse_qsl
except:
  from cgi import parse_qsl
 
import oauth2 as oauth
 
REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL  = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL        = 'https://api.twitter.com/oauth/authenticate'
 
class GenerateToken(object):
 
  def __init__(self,consumer_key=None,consumer_secret=None):
    if consumer_key is None or consumer_secret is None:
      raise TokenError('please add a consumer key and secret')
    else:
      signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()
      self.oauth_consumer             = oauth.Consumer(key=consumer_key, secret=consumer_secret)
      self.oauth_client               = oauth.Client(self.oauth_consumer)
 
  def getrequestTokenURL(self):
    resp, content = self.oauth_client.request(REQUEST_TOKEN_URL, 'GET')
    if resp['status'] != '200':
      raise TokenError('Invalid response from Twitter')
    else:
      request_token = dict(parse_qsl(content))
      pieces = {
        'url' : "%s?oauth_token=%s" % (AUTHORIZATION_URL, request_token['oauth_token']),
        'token_secret': request_token['oauth_token_secret']
      }
      return pieces
 
  def authRequest(self,oauth_token=None,oauth_token_secret=None,oauth_verifier=None):
      token = oauth.Token(oauth_token,oauth_token_secret)
      token.set_verifier(oauth_verifier)
      oauth_client  = oauth.Client(self.oauth_consumer, token)
      resp, content = oauth_client.request(ACCESS_TOKEN_URL, method='POST', body='oauth_verifier=%s' % oauth_verifier)
      access_token  = dict(parse_qsl(content))
      if resp['status'] != '200':
        raise TokenError('The request for a Token %s did not succeed: %s' % (access_token,resp['status']) )
      else:
        auth = {
          'access_token' : access_token['oauth_token'],
          'access_token_secret' : access_token['oauth_token_secret'],
        }
        return auth
 
class TokenError(Exception):
  '''Base class for Token errors'''
 
  @property
  def message(self):
    '''Returns the first argument used to construct this error.'''
    return self.args[0]