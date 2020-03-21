# Docker and Nginx

### Requirements
1. Make sure you have Docker installed, this project is setup on a Mac with Docker Desktop for Mac https://www.docker.com/products/docker-desktop

### Steps to setup
```
docker build -t custom-nginx .
docker run --name my-custom-nginx-container -d -p 80:80 custom-nginx
```