from dagster import schedules, ScheduleDefinition
from dagster_cron import SystemCronScheduler

query_gbfs_schedule = ScheduleDefinition(
    name='query_gbfs_schedule',
    cron_schedule='* * * * *',
    pipeline_name='query_gbfs_pieline',
    environment_dict={
        'storage': {'filesystem': None},
        'solids': {
            'query_gbfs_auto_discovery_url': {
                'config': {'auto_discovery_url': 'https://gbfs.baywheels.com/gbfs/gbfs.json'}
            }
        },
    },
)


@schedules(scheduler=SystemCronScheduler)
def def_scheduler():
    return [query_gbfs_schedule]
