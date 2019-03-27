# template_app_apache

Template App Apache2 for Zabbix 3.4 that works without any external scripts.  
You can poll Apache2 using Zabbix agent locally(Template App Apache2 Zabbix agent) or poll it directly from Zabbix server/proxy(Template App Apache2 HTTP). Choose template that better suits you. Tune URL with user macros if required.  

## Setup

see https://httpd.apache.org/docs/current/mod/mod_status.html

## Tuning

Change those macros on host level if needed:

|Macro|Description|Default(agent)|Default(HTTP)|
|---|----|---|---|
|{$STUB_STATUS_HOST}| | localhost | n/a |
|{$STUB_STATUS_PATH}| | server-status?auto | server-status?auto|
|{$STUB_STATUS_PORT}| | 80 | 80 |
|{$APACHE_PROC}| | apache2 | n/a |

## Items

See in template

## Triggers

See in template

## Demo

![image](https://user-images.githubusercontent.com/14870891/47022436-299fad80-d166-11e8-934a-0c9cee4c694d.png)

## Next steps

TBD

## References

