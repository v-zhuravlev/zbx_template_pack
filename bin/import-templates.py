#!/usr/bin/env python
import argparse

from zabbix.api import ZabbixAPI
import zabbix_cli

template_parser = zabbix_cli.zabbix_default_args()
parser = argparse.ArgumentParser(parents=[template_parser], add_help=False)
parser.add_argument('--filter', '-f', dest="filter",
                    help="Imports only files that contain filter specified in their filenames.",
                    required=False)
parser.add_argument('filename|dirname', nargs=1, help='filename|dirname')
args = parser.parse_args()


