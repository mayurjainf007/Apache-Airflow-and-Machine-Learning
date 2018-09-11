import oauth2 as oauth
import urllib.request as urllib
import json
from pathlib import Path

def twitterreq(url, method, parameters):
	req = oauth.Request.from_consumer_and_token(oauth_consumer, token=oauth_token, http_method=http_method, http_url=url, parameters=parameters)
	req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
	headers = req.to_header()
	if http_method == "POST":
		encoded_post_data = req.to_postdata()
	else:
		encoded_post_data = None
		url = req.to_url()
	opener = urllib.OpenerDirector()
	opener.add_handler(http_handler)
	opener.add_handler(https_handler)
	response = opener.open(url, encoded_post_data)
	return response

def fetchsamples():
	urlx = "https://api.twitter.com/1.1/statuses/home_timeline.json"
	urly = "https://api.twitter.com/1.1/trends/closest.json"
	url = "https://api.twitter.com/1.1/trends/available.json"
	parameters = []
	response = twitterreq(url, "GET", parameters)
	f = open("txts/geo.txt",'w+')
	line = []
	for line in response:
		line = line.decode('utf8').replace("'", '"').strip()
	data = json.loads(line)
	s = json.dumps(data, indent=4, sort_keys=True)
	f.write(s)

api_key = "xxxxx"
api_secret = "xxxxx"
access_token_key = "xxxxx"
access_token_secret = "xxxxx"
lists = [api_key,api_secret,access_token_key,access_token_secret]
	with open('txts/twitter_oauth.txt', 'w') as f:
	    pickle.dump(lists, f)
_debug = 0
oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)
signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()
http_method = "GET"
http_handler = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)
fetchsamples()
