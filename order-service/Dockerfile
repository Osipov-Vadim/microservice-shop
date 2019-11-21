FROM python:buster
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /home/docker/code/
RUN pip3 install -r /home/docker/code/requirements.txt
COPY . /home/docker/code/
WORKDIR /home/docker/code/

RUN python3 ./manage.py makemigrations && python3 ./manage.py migrate
# RUN python3 ./manage.py collectstatic

CMD python3 ./manage.py runserver 0.0.0.0:80
EXPOSE 80
