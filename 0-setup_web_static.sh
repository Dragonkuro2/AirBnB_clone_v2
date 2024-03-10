#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p data/web_static/shared data/web_static/releases/test
echo 'Hello World!' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
