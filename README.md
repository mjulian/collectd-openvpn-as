collectd-openvpn-as
===================

A collectd plugin for collecting metrics from OpenVPN Access Server 2.0

This plugin is designed with [Librato](https://librato.com) in mind but will probably work with normal collectd too.

## Installation

1. Put `sacli.py` at `/opt/sacli.py`. You can change the location by editing the plugin file.
2. Put `collectd-openvpn-as.py` at `/opt/collectd/share/collectd/collectd-openvpn-as.py`.
3. Configuration file goes at `/opt/collectd/etc/collectd.conf.d/openvpn-as.conf`. There are no configurable parameters.
4. Restart collectd.

## Metrics available
* `librato.openvpn_as.users.current`: Current users on the VPN
* `librato.openvpn_as.users.license_max`: Max license count available
* `librato.openvpn_as.vpn_connections.bytes.in`: Bytes rx, per user
* `librato.openvpn_as.vpn_connections.bytes.out`: Bytes tx, per user
* `librato.openvpn_as.vpn_connections.duration.seconds`: Session duration in seconds, per user
