from dagster import solid, Field, String
import requests
from datetime import datetime
import json
import os
from dagster.utils import file_relative_path


@solid(config={'auto_discovery_url': Field(String)})
def query_gbfs_auto_discovery_url(context):

    root_url = context.solid_config['auto_discovery_url']

    r = requests.get(root_url)
    if not r.status_code == 200:
        raise Exception("Non 200-status code")

    response = r.json()
    return response['data']['en']['feeds']


@solid
def get_feeds(_, feeds):
    data = {}

    for feed in feeds:
        r = requests.get(feed['url'])
        if not r.status_code == 200:
            raise Exception("Non 200-status code")

        data[feed['name']] = r.json()

    return data


@solid
def store_data(_, feed_data):
    date_accessed = datetime.now()
    for feed_name, data in feed_data.items():
        filename = "{}.json".format(date_accessed.strftime("%Y%m%d-%H%M%S"))
        file_dir = file_relative_path(__file__, os.path.join("logs", feed_name))
        os.makedirs(file_dir, exist_ok=True)

        with open(os.path.join(file_dir, filename), 'w') as out:
            out.write(json.dumps(data))
