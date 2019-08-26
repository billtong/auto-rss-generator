FROM aw3i/pip3
EXPOSE 8000
ADD . /usr/rss-collector
WORKDIR /usr/rss-collector
ENTRYPOINT ./deploy.sh