#!/usr/bin/env bash
#script that sets up your web servers for the deployment

apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/releases/test/
echo '<h1>Hello World</h1>' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '16a\
  location /hbnb_static/ {\
	alias /data/web_static/current/;\
  }' /etc/nginx/sites-available/default
nginx -s reload
