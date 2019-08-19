#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
MYSTR=$(dpkg -s nginx)
if [[ $MYSTR != *"install ok installed"* ]]; then
    apt-get -y update
    apt-get -y install nginx
fi
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Test content of web_static" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/server_name _;/a location /hbnb_static {\nalias /data/web_static/current;\nautoindex off;\n}' /etc/nginx/sites-available/default
service nginx restart
