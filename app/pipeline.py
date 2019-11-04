from dagster import pipeline

from solid import query_gbfs_auto_discovery_url, get_feeds, store_data


@pipeline
def query_gbfs_pieline():
    store_data(get_feeds(query_gbfs_auto_discovery_url()))
