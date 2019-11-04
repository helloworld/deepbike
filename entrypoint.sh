#!/bin/sh

touch /etc/crontab /etc/cron.*/*

service cron start

export DAGSTER_HOME='/dagster_home'

dagster schedule up

for name in `dagster schedule list --name`; do
    echo $name;
    dagster schedule stop $name || true;
    dagster schedule start $name;
done


dagit -h 0.0.0.0 -p 3000