import argparse

def zabbix_arg_parse():
    "This parses arguments coming from command line"

    args = zabbix_default_args().parse_args()
    return args

    
def zabbix_default_args():
    "This returns default arguments parser used to connect to Zabbix API"
    parser = argparse.ArgumentParser(description='Zabbix API')
    parser.add_argument('--username', dest="username",
                        default="Admin",
                        help="Zabbix API username",
                        metavar="your_username")
    parser.add_argument('--password', dest="password", default="zabbix",
                        help="Zabbix API password",
                        metavar="your_password")
    parser.add_argument('--api_url', dest="api_url", default="http://localhost/api_jsonrpc.php",
                        help="Zabbix API endpoint",
                        metavar="http://localhost/api_jsonrpc.php")
    parser.epilog = "Have a nice day."

    return parser