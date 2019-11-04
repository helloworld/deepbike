from dagster import RepositoryDefinition
from pipeline import query_gbfs_pieline


def def_repo():
    return RepositoryDefinition(name="deepbike", pipeline_defs=[query_gbfs_pieline])
