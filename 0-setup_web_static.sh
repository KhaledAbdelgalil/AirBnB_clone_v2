#!/usr/bin/env bash
#  Bash script that sets up the web servers for the deployment of web_static
sudo su
apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
chmod 777 /data/web_static/releases/test
echo "<html><head></head><body>Hello World2!</body></html>"> /data/web_static/releases/test/index.html

ln -fs /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/
sed -i '26i\	location /hbnb_static {\n\t alias /data/web_static/current/;\n} ' /etc/nginx/sites-available/default
service nginx start
exit
