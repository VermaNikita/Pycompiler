FROM centos:latest 

MAINTAINER NikitaVerma <nikita.shimpy0911@gmail.com>

RUN yum -y install httpd python36

COPY dp.py /var/www/cgi-bin/

EXPOSE 80

CMD ["/usr/sbin/httpd", "-D" , "FOREGROUND"]
