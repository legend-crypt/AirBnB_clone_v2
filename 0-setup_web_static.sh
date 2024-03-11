#!/usr/bin/env bash
# a script to install and conf nginx

# script installs nginx
sudo apt-get update
sudo apt-get install nginx -y

#create repositories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#dummy html page created
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#change directory name
sudo chown -R ubuntu:ubuntu /data/

#set up the page to be served
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default

#restart the server
sudo service nginx restart
