sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo gunicorn hello.py
sudo /etc/init.d/nginx restart

