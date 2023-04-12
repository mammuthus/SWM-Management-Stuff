from __future__ import print_function
import orionsdk
import urllib3

from sws import user, swis

urllib3.disable_warnings()

status_mode = 0  # 0 = Mixed status shows warning; 1 = Show worst; 2 = Show best

group_list = [
#
]

child_name = 'Internal group'
child_description = 'Child group'

for group in group_list:
    child_group_id = swis.invoke(
        'Orion.Container',
        'CreateContainerWithParent',
        group,
        child_name,
        'Core',  # Child owner, must be 'Core'
        60,  # Refresh frequency in seconds
        status_mode,
        child_description,
        True,  # Polling enabled/disabled = true/false
        []
    )
    print(f'Group was created with id {child_group_id} inside parent {group}')
