from datetime import datetime, timedelta, timezone
import orionsdk
import urllib3

from sws import user, swis

urllib3.disable_warnings()

site = 'ATL'
function = 'S'
unmanage_duration = 3

get_nodes = f"""
        SELECT NodeID, Caption, Node.CustomProperties.City, Uri 
        FROM Orion.Nodes Node
        WHERE Node.CustomProperties.City = '{site}'
    """

results = swis.query(get_nodes)['results']

unmanage_from = datetime.now(timezone.utc)
unmanage_until = unmanage_from + timedelta(hours=unmanage_duration)

for node in results:
    node_id = f'N:{node["NodeID"]}'
    print(f'Node: {node["Caption"]}')
    print(f'From: {unmanage_from.strftime("%d.%m.%y %H:%M")}')
    print(f'Till: {unmanage_until.strftime("%d.%m.%y %H:%M")}')
    print(node_id)
    print()
    
    uri = node['Uri']
    
    if function == 'S':
        swis.invoke('Orion.Nodes', 'Unmanage', node_id, unmanage_from, unmanage_until, False)
    else:
        swis.invoke('Orion.AlertSuppression', 'SuppressAlerts', [uri], unmanage_from, unmanage_until)
