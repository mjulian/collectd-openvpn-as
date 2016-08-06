#!/usr/local/openvpn_as/bin/python
import os
import sys
path = sys.path
sys.path = ['/usr/local/openvpn_as/scripts', '/usr/local/openvpn_as/bin', '/usr/local/openvpn_as/sbin'] + path

if 'LD_LIBRARY_PATH' not in os.environ:
    os.environ['LD_LIBRARY_PATH'] = '/usr/local/openvpn_as/lib'
    os.environ['PYTHONHOME'] = '/usr/local/openvpn_as'
    os.environ['PYOVPN_VERSION'] = '2.0.25'
    os.environ['OPENVPN_AS_BASE'] = '/usr/local/openvpn_as'
    os.environ['OPENVPN_AS_CONFIG'] = '/usr/local/openvpn_as/etc/as.conf'
    try:
        os.execv(sys.argv[0], sys.argv)
    except Exception, exc:
        print 'Failed re-exec:', exc
        sys.exit(1)

os.environ['PYOVPN_CMDNAME'] = 'sacli'

from pyovpn.sagent.sagent_entry import sacli

sacli()
