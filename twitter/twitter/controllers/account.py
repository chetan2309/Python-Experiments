import logging

from twitter.lib.base import *
import twitter
import twitter.lib.twittertoken as twittertoken
from pylons.controllers.util import abort, redirect_to, url_for

log = logging.getLogger(__name__)
key = 'yt8R1s4tnN8ZAGXCxBcfnA'
secret = 'F9hr5prV8McjE6CljD3yAzCRUWhHeDPcvoR7g0hk'

class AccountController(BaseController):

	def twitter_auth(self):
		token = twittertoken.GenerateToken(consumer_key=key, consumer_secret=secret)
		request_token = token.getrequestTokenURL()
		#save the token secret it will be used to generate the user's access_token and and access_secret
		session['token_secret'] = request_token['token_secret']
		session.save()
		# redirect to twitter screen
		return redirect_to(url_for(request_token['url']))
	 
	def twitter_preferences(self):
	    params = request.params
	    twittertoken.GenerateToken(consumer_key=key, consumer_secret=secret)
	    auth = twittertoken.authRequest(oauth_token=params.get('oauth_token'),oauth_token_secret=session.get('token_secret'),oauth_verifier=params.get('oauth_verifier'))
	    if auth['access_token'] and auth['access_token_secret']:
	      #save to db or get user friend list
	      for u in api.GetFriends():
	        log.debug(u.name)