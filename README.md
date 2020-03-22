# Using Oauth with Python, Nginx and Docker
### Python app using some methods of Instagram API using Docker, Nginx, Python and Bottle

##### Useful links
Bottle https://bottlepy.org/
Nginx https://hub.docker.com/_/nginx

### Steps to Install and Run

#### Setup your server Mac users
1. You want to edit your /etc/hosts file and add the entry 
```
my_redirect_uri_host  127.0.0.1
```
2. For this example I use Nginx as my server, you can follow instructions in README of nginx directory in this project or you can use your own setup with Docker or not using Nginx, Apache, Haproxy, etc.

3. Create your own local_settings.py file that has the following
```
CLIENT_ID = 'MY_IG_APP_CLIENT_ID'
CLIENT_SECRET = 'MY_IG_APP_CLIENT_SECRET'
REDIRECT_URI = 'MY_IG_APP_REDIRECT_URI'
``` 

4. You can setup your python part of this project by following commands below running on command line (Terminal app of Mac or bash application of choice)

````
python3 -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/bin/activate
pip install -r requirements.txt
python app.py
visit browser http://localhost:8080 or the host you have set up in your server configuration.
````