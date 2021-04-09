FROM httpd:latest

RUN apt-get -qq update
RUN apt-get install --yes apache2-dev
RUN apt-get install --yes python3
RUN apt-get install --yes python3-pip
# RUN apt-get install --yes libapache2-mod-wsgi-py3

RUN pip3 install mod_wsgi

COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf

WORKDIR /usr/local/apache2/htdocs/

COPY ./api/requirements.txt /usr/local/apache2/htdocs/

RUN pip3 install -r /usr/local/apache2/htdocs/requirements.txt

ENV FLASK_ENV=prod
COPY ./api/ /var/www/api/
