from __future__ import print_function
import orionsdk
import urllib3

from sws import user, swis

urllib3.disable_warnings()

counter = 0

print('N', 'ID', 'Caption', 'DNS', 'IP', 'Status', 'Status Description', 'Polling Method', 'Owner', 'Role', 'City',
      'Agent Status', 'Is Active', 'Agent Version', 'Min Since Sync', 'EngineID', sep=',')

with open(r"IP_list") as file:
    for line in file:
        line = line.strip()  # preprocess line

        ip_var = line
        nodes_q = f"""
                    SELECT 
                        N.NodeID, N.Caption, N.DNS, N.IPAddress, 
                        N.Status, N.StatusDescription, N.ObjectSubType,
                        CP.NodeOwner, CP.NodeRole, CP.City, 
                        A.AgentStatus, A.IsActiveAgent, A.AgentVersion,
                        N.MinutesSinceLastSync, N.EngineID
                    FROM Orion.NodesCustomProperties AS [CP]
                    INNER JOIN (
                        SELECT NodeID, ObjectSubType, IPAddress, 
                        Caption, DNS, Status, StatusDescription, AgentPort, EngineID, MinutesSinceLastSync
                        FROM Orion.Nodes
                        WHERE NodeID IS NOT NULL 
                    ) N ON N.NodeID = CP.NodeID
                    LEFT JOIN (
                        SELECT NodeID, AgentStatus, IsActiveAgent, AgentVersion
                        FROM Orion.AgentManagement.Agent
                        WHERE NodeID IS NOT NULL 
                    ) A ON A.NodeID = N.NodeID

                    WHERE IPAddress = '{ip_var}'
            """

        fe_results = swis.query(nodes_q)['results']

        for item in fe_results:
            counter += 1
            row = [counter] + [item[field] for field in ('NodeID', 'Caption', 'DNS', 'IPAddress', 'Status', 'StatusDescription',
                                                         'ObjectSubType', 'NodeOwner', 'NodeRole', 'City', 'AgentStatus',
                                                         'IsActiveAgent', 'AgentVersion', 'MinutesSinceLastSync', 'EngineID')]
            print(*row, sep=',')
