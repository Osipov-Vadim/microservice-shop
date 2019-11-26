FROM python:buster

RUN apt-get update && \
    apt-get install -y \
    bash curl nano net-tools zip unzip \
    jq dnsutils iputils-ping python-pip


# Python Environment Setup
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Setup Consul and Goreman
RUN mkdir -p /data/db /etc/consul.d /code

ADD https://releases.hashicorp.com/consul/1.6.2/consul_1.6.2_linux_amd64.zip /tmp/consul.zip
RUN cd /bin && unzip /tmp/consul.zip && chmod +x /bin/consul && rm /tmp/consul.zip

ADD https://github.com/mattn/goreman/releases/download/v0.0.10/goreman_linux_amd64.zip /tmp/goreman.zip
RUN cd /bin && unzip /tmp/goreman.zip && chmod +x /bin/goreman && rm /tmp/goreman.zip

ADD ./consul /etc/consul.d
ADD Procfile /root/Procfile

# Setting workdir
ADD consul.sh /opt
COPY . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations && python3 manage.py migrate

RUN chmod +x /code/catalog_service.sh
RUN chmod +x /opt/consul.sh

# Exposing appropriate ports
EXPOSE 80

ENTRYPOINT [ "goreman" ]
CMD [ "-f", "/root/Procfile", "start" ]
