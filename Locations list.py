import orionsdk
import urllib3

from sws import user, swis

urllib3.disable_warnings()

exception_list = [
#
]

parent_query = """
    SELECT DISTINCT Value
    FROM Orion.CustomPropertyValues
    WHERE Field='City'
    """
results = swis.query(parent_query)['results']

locations = [dict['Value'] for dict in results if dict['Value'] not in set(exception_list)]
print(locations)
