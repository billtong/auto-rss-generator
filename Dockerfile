FROM selenium/standalone-firefox
EXPOSE 4444

RUN

ADD . /usr/app
