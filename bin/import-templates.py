#!/usr/bin/env python
import argparse
import json
import os
import sys
from zabbix.api import ZabbixAPI
from pyzabbix.api import ZabbixAPIException
import zabbix_cli


def import_configuration_from_file(zapi, filename):
    """This imports configuration into ZabbixAPI from file"""
    with open(filename, 'r') as file:
        contents = file.read()
    params_raw = """
    {
        "format": "xml",
        "rules": {
            "groups": {
                "createMissing": true
            },
            "hosts": {
                "createMissing": true,
                "updateExisting": true
            },
            "templates": {
                "createMissing": true,
                "updateExisting": true
            },            
            "templateLinkage": {
                "createMissing": true
            },                    
            "templateScreens": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            },   
            "applications": {
                "createMissing": true,
                "deleteMissing": true
            },    
            "discoveryRules": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            },            
            "items": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            },
            "triggers": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            },
            "graphs": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            },
            "screens": {
                "createMissing": true,
                "updateExisting": true
            },
            "maps": {
                "createMissing": true,
                "updateExisting": true
            },
            "images": {
                "createMissing": true,
                "updateExisting": true
            },
            "valueMaps": {
                "createMissing": true,
                "updateExisting": true
            }
        },
        "source": ""
        }
    """
    params = json.loads(params_raw)
    params['source'] = contents
    try:
        zapi.do_request('configuration.import', params)
    except ZabbixAPIException as err:
        sys.exit(err.data) #too long: https://github.com/adubkov/py-zabbix/blob/master/pyzabbix/api.py#L256
        #sys.exit("Failed to import the template.")


def import_single_template(filename):
    """This imports single template"""

    print ("Importing {}...".format(filename))
    import_configuration_from_file(zapi, filename)


def import_dir_with_templates(dirname):
    """This imports all templates found in the directory"""
    import glob

    templates = []
    for file in glob.glob(dirname+'/*'+args.filter_str+"*.xml"):
        templates.append(file)
    if len(templates) == 0:
        sys.exit("No templates found in directory '{}' with filter: {}".format(
            dirname, args.filter_str))
    templates.sort()
    for template in templates:
        import_single_template(template)


template_parser = zabbix_cli.zabbix_default_args()
parser = argparse.ArgumentParser(parents=[template_parser], add_help=False)
parser.add_argument('--filter', '-f', dest='filter_str',
                    help="imports only files in directory that contain chars in the filenames.",
                    required=False, type=str, default='')
parser.add_argument(dest='arg1', nargs=1,
                    help='provide file or directory name', metavar='path')
args = parser.parse_args()


try:
    zapi = ZabbixAPI(url=args.api_url,
                     user=args.username,
                     password=args.password)
except ZabbixAPIException as err:
    print (err[0])
else:
    path = args.arg1[0]
    if os.path.isdir(path):
        import_dir_with_templates(path)
    elif os.path.isfile(path):
        import_single_template(path)
    else:
        sys.exit("{0} is not a valid template or directory".format(path))

    zapi.do_request('user.logout')
