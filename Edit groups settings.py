from __future__ import print_function
import orionsdk
import urllib3

from sws import user, swis

urllib3.disable_warnings()

container_props_query = """
    SELECT ContainerID, Name, Owner, Frequency, StatusCalculator, Description, PollingEnabled
    FROM Orion.Container
    WHERE name like 'SPB - %'
"""
results = swis.query(container_props_query)['results']

for item in results:
    group_id = item['ContainerID']
    group_name = item['Name']
    group_owner = item['Owner']
    group_freq = item['Frequency']
    group_status_calc = item['StatusCalculator']
    group_desc = item['Description']
    group_enabled = item['PollingEnabled']

    child_group_id = swis.invoke(
        'Orion.Container',
        'UpdateContainer',
        group_id,
        group_name,
        group_owner,
        '30',  # group_freq
        group_status_calc,
        group_desc,
        group_enabled
    )
    print(f'Group {group_name} was updated ({group_id})')
