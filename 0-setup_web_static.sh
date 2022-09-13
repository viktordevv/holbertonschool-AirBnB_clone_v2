#!/usr/bin/env bash
# Prepare your web servers

apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
# symbolic link
ln -sf /data/web_static/releases/test /data/web_static/current
#change permission
chown -R ubuntu:ubuntu /data
# configure nginx
sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default
# restart service
service nginx restart
exit 0
