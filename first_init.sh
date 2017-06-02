sudo rm /etc/nginx/sites-enabled/default

sudo /etc/init.d/mysql start
mysql -uroot -e "create database db_web"
