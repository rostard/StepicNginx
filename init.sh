ph=$(pwd)


sudo ln -sf $ph/etc/nginx.conf  /etc/nginx/sites-enabled/
#sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf etc/hello.py /etc/gunicorn.d/hello.py


#sudo gunicorn -c etc/hello.py hello
cd ask
sudo gunicorn -c ../etc/django.py ask.wsgi:application

sudo /etc/init.d/mysql start
mysql -uroot -e "create database db_web"
