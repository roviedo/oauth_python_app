import json
import ssl
import urllib.request
from bottle import route, post, run, template, request, response
from settings import *

@route('/')
def index():
    auth_url = '%s?client_id=%s&redirect_uri=%s&response_type=code' % (auth_url_base, CLIENT_ID, REDIRECT_URI)
    return template('<b>Hello, let\'s do oauth <a href="{{auth_url}}">Authorize</a></b>!', auth_url=auth_url)

@route('/oauth/complete/')
def step2():
    gcontext = ssl.SSLContext()
    code = request.query['code']

    url = GET_TOKEN_URL
    values = {
        'client_id' : CLIENT_ID,
        'client_secret' : CLIENT_SECRET,
        'grant_type' : 'authorization_code',
        'redirect_uri': REDIRECT_URI,
        'code': code
    }

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req, context=gcontext) as response:
        data = json.load(response)

    '''
    Now at this point you have the access_token and
    user simple user data. Now you can store the access token
    in your preferred DB and build your app fetching data with it
    and using it following the third parties guidelines.
    '''
    return {'user': data.get('user')}


run(host='localhost', port=8080)
