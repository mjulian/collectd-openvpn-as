#
# Plugin to collectd statistics from OpenVPN Access Server
#

import collectd
from subprocess import check_output
import json
from datetime import datetime


class OpenVPNAS(object):

    def __init__(self):
        self.plugin_name = "openvpn_as"

    def submit(self, type, instance, value, host, plugin_instance=None):
        v = collectd.Values()
        v.plugin = self.plugin_name
        if plugin_instance:
            v.plugin_instance = plugin_instance
        v.host = host
        v.type = type
        if instance:
            v.type_instance = instance
        v.values = [value, ]
        v.meta = {'0': True}
        v.dispatch()

    def do_server_status(self):
        vpn_status = check_output(['/opt/sacli.py', 'VPNStatus'])
        lic_usage = check_output(['/opt/sacli.py', 'LicUsage'])
        vpn_config = check_output(['/opt/sacli.py', 'ConfigQuery'])

        vpn_config = json.loads(vpn_config)
        vpn_status = json.loads(vpn_status)

        node_name = vpn_config.get('host.name')
        current_users, license_max = json.loads(lic_usage)

        self.submit('users', 'current', current_users, node_name)
        self.submit('users', 'license_max', license_max, node_name)

        for vpn_server, data in vpn_status.iteritems():
            clients = data.get('client_list')
            for client in clients:
                username = client[0]
                bytes_rx = client[4]
                bytes_tx = client[5]
                connected_at = client[7]
                now = datetime.utcnow()
                then = datetime.utcfromtimestamp(float(connected_at))
                tdelta = now - then
                connection_duration = tdelta.total_seconds() / 60

                self.submit('bytes', 'in', bytes_rx, username, plugin_instance='vpn_connections')
                self.submit('bytes', 'out', bytes_tx, username, plugin_instance='vpn_connections')
                self.submit('duration', None, connection_duration, username, plugin_instance='vpn_connections')


openvpnas = OpenVPNAS()
collectd.register_read(openvpnas.do_server_status)
