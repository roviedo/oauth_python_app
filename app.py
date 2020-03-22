from bottle import route, run, template
import urllib.request
from settings import *

@route('/')
def index():
    auth_url = '%s?client_id=%s&redirect_uri=%s&response_type=code' % (auth_url_base, CLIENT_ID, REDIRECT_URI)
    return template('<b>Hello<a href="{{auth_url}}">Testing</a></b>!', auth_url=auth_url)

@route('/oauth/complete/')
def step2():
    # TODO: here we get the access token with the code we've received
    ## curl -F 'client_id=CLIENT_ID' \
    ## -F 'client_secret=CLIENT_SECRET' \
    ## -F 'grant_type=authorization_code' \
    ## -F 'redirect_uri=AUTHORIZATION_REDIRECT_URI' \
    ## -F 'code=CODE' \
    ## https://api.instagram.com/oauth/access_token
    return template('<div><b>Testing {{name}}</b></div>', name='test')

run(host='localhost', port=8080)
