auth_url_base = 'https://api.instagram.com/oauth/authorize/'

CLIENT_ID = ''
REDIRECT_URI = ''
GET_TOKEN_URL = ''

try:
    from local_settings import *
except ImportError as error:
    print('local_settings not found')