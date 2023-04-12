from __future__ import print_function
import re
import requests
import orionsdk
import urllib3

from sws import user, swis

urllib3.disable_warnings()

sites_list = [
#
]

for site in sites_list:
    network_hardware_query = f"""
        SELECT DefinitionID, ContainerID, Name, Definition
        FROM Orion.ContainerMemberDefinition
        WHERE Name like '%{site} IP SLA query%'
    """
    results = swis.query(network_hardware_query)['results']

    for item in results:
        definition_id = item['DefinitionID']
        swis.invoke('Orion.Container', 'DeleteDefinition', definition_id)

        container_id = item['ContainerID']
        swis.invoke('Orion.Container', 'AddDefinition', container_id, {
            'Name': site + ' IP SLA query',
            'Definition': f"filter:/Orion.IpSla.Operations[EndsWith(OperationName,'{site.lower()}swic01') AND DisplaySource!='spbswic01.amust.local']"
        })
