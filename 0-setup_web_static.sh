#!/usr/bin/env bash
# Shell script to setup a new server to serve web static
sudo apt-get update -y
sudo apt-get install nginx -y
sudo service nginx start
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "Hello world!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
