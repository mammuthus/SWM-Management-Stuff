from __future__ import print_function
import re
import requests
import orionsdk
import urllib3

from sws import user, swis

urllib3.disable_warnings()

counter = 0
target_custom_property = 'Z Decommission 3'

with open(r"Captions_list") as file:
    for line in file:
        line = line.strip()
        ip_var = line
        counter += 1

        find_uri_query = f"""
        SELECT N.NodeID, N.Uri, N.Caption, CP.Grouped_by
        FROM Orion.NodesCustomProperties AS [CP]
        INNER JOIN (
            SELECT Uri, NodeID, Caption
            FROM Orion.Nodes
        ) N ON N.NodeID = CP.NodeID
        WHERE N.Caption = '{ip_var}'
        """

        find_uri_results = swis.query(find_uri_query)['results']

        if not find_uri_results:
            print(f'Invalid input in {counter}: {line}')
        else:
            for node_dict in find_uri_results:
                node_id = node_dict['NodeID']
                node_uri = node_dict['Uri']
                node_caption = node_dict['Caption']
                node_current_custom_property = node_dict['Grouped_by']

            print(f'Node {node_caption} ({node_id}) was changed. Old CP: {node_current_custom_property}')
            swis.update(node_uri + '/CustomProperties', Grouped_by=target_custom_property)
