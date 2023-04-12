from __future__ import print_function
import orionsdk
import urllib3

from sws import user, swis

urllib3.disable_warnings()

node_role = 'DNS DMZ (Linux)'

find_empty = f"""
    SELECT NCP.NodeID, NCP.NodeOwner, NCP.NodeRole, NCP.Uri, N.Caption
    FROM Orion.NodesCustomProperties as [NCP]
    INNER JOIN Orion.Nodes as [N] ON N.NodeID = NCP.NodeID
    WHERE NCP.City IS NULL AND NCP.NodeRole = '{node_role}'
"""
fe_results = swis.query(find_empty)['results']

for item in fe_results:
    node_id_db = item['NodeID']
    node_owner_db = item['NodeOwner']
    node_role_db = item['NodeRole']
    uri = item['Uri']
    caption_db = item['Caption']
    cropped = caption_db[:3].upper()

    swis.update(uri, City=cropped)
    print(f'{caption_db} node with id {node_id_db} was updated! New City is {cropped}')
