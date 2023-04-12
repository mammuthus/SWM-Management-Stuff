from __future__ import print_function
import orionsdk
import urllib3

from sws import user, swis

urllib3.disable_warnings()

parent_group_id = '524'
child_group_description = ' Clear child description'
node_role = 'AppTest'

sites_list = [
#
]

# Creating children
for site in sites_list:
    child_group_id = swis.invoke(
        'Orion.Container',
        'CreateContainerWithParent',
        parent_group_id,
        site + child_group_description,
        'Core',  # Child owner, must be 'Core'
        60,  # Refresh frequency in seconds
        0,  # 0 = Mixed status shows warning; 1 = Show worst; 2 = Show best
        site + child_group_description,
        True,  # Polling enabled/disabled = true/false
        # Child group members
        [
            {
                'Name': site + ' ' + child_group_description + ' query',
                'Definition': f"filter:/Orion.Nodes[CustomProperties.City='{site}' AND CustomProperties.NodeRole='{node_role}']",
            },
        ]
    )
    print(f'Created filled child group with id {child_group_id}')
    print(f'    Filled with: {site + child_group_description} query (Site={site}, AND NodeRole={node_role})')
