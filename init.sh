sudo ln -sf etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf etc/hello.py /etc/gunicorn.d/hello.py

sudo /etc/init.d/nginx restart
sudo gunicorn -c etc/hello.py hello
cd ask
sudo gunicorn -c ../etc/django.py ask.wsgi:application
