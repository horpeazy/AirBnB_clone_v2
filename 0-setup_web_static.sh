#!/usr/bin/env bash
# Shell script to setup a new server to serve web static
sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p /data/web_static/
mkdir /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
echo "Hello world!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/server_name _/a\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
