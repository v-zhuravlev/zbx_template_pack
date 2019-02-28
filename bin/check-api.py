#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from zabbix.api import ZabbixAPI
from zabbix_cli import zabbix_arg_parse

args = zabbix_arg_parse()
# Create ZabbixAPI class instance
try:
    zapi = ZabbixAPI(url=args.api_url,
                     user=args.username,
                     password=args.password)
except:
    sys.exit("Zabbix API is not available")
else:
    print("Zabbix API is ready")
    zapi.user.logout()
