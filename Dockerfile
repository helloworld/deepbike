FROM dagster/dagster-py37:latest

RUN apt-get update
RUN apt-get -y install cron
RUN apt-get -y install vim

RUN mkdir '/dagster_home'

COPY ./entrypoint.sh /
COPY ./app /app

WORKDIR /app

EXPOSE 3000

RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh
