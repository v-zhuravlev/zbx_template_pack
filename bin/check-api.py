#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from zabbix.api import ZabbixAPI
import zabbix_cli

args = zabbix_cli.zabbix_arg_parse()
# Create ZabbixAPI class instance
try:
    zapi = ZabbixAPI(url=args.api_url,
                 user=args.username,
                 password=args.password)
except:
    print "Zabbix API is not available"    
else:
    print "Zabbix API is ready"
    zapi.do_request("user.logout",{})
