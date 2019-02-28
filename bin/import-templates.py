#!/usr/bin/env python
import argparse
import json
import os
import sys
import logging

from pyzabbix.api import ZabbixAPIException, ZabbixAPI
from zabbix_cli import zabbix_default_args


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
        logger.error(err.data)
        sys.exit(1)


def import_single_template(filename):
    """This imports single template"""

    logger.info("Importing {}...".format(filename))
    import_configuration_from_file(zapi, filename)


def import_dir_with_templates(dirname):
    """This imports all templates found in the dir. .xml extension hardcoded"""
    import glob

    templates = []
    for file in glob.glob(dirname + '/*' + args.filter_str + "*.xml"):
        templates.append(file)
    if len(templates) == 0:
        logger.error("No templates found in directory '{}' with filter: {}".format(
            dirname, args.filter_str))
        sys.exit(1)
    templates.sort()
    for template in templates:
        import_single_template(template)


if __name__ == "__main__":

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    template_parser = zabbix_default_args()
    parser = argparse.ArgumentParser(parents=[template_parser], add_help=False)
    parser.add_argument('--trace',
                        help='Trace Zabbix API calls',
                        required=False, action='store_true', default=False)
    parser.add_argument('--filter', '-f', dest='filter_str',
                        help='imports only files in directory that contain chars in the filenames.',
                        required=False, type=str, default='')
    parser.add_argument(dest='arg1', nargs=1,
                        help='provide file or directory name', metavar='path')
    args = parser.parse_args()

    if args.trace:
        zapi_logger = logging.getLogger("pyzabbix.api")
        zapi_logger.setLevel(logging.DEBUG)

    try:
        zapi = ZabbixAPI(url=args.api_url,
                         user=args.username,
                         password=args.password)
    except ZabbixAPIException as err:
        logger.error(err.data)
    else:
        path = args.arg1[0]
        if os.path.isdir(path):
            import_dir_with_templates(path)
        elif os.path.isfile(path):
            import_single_template(path)
        else:
            logger.error("{0} is not a valid template or directory".format(path))
            sys.exit(1)
        zapi.user.logout()
