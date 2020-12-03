"""Settings for the of_l2ls NApp."""
# LLDP Mac Addresses
LLDP_MACS = ['01:80:c2:00:00:0e', '01:80:c2:00:00:03',
             '01:80:c2:00:00:00']

# Flow priority for flows installed by this NApp

# flow_priority = 10
FLOW_PRIORITY = 10
TABLE_ID = 0

FLOW_MANAGER_URL = 'http://localhost:8181/api/kytos/flow_manager/v2'
