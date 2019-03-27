# template_app_nginx

Template App Nginx for Zabbix 3.4+ that works without any external scripts.  
You can poll Nginx using Zabbix agent locally(Template App Nginx Zabbix agent) or poll it directly from Zabbix server/proxy(Template App Nginx HTTP). Choose template that better suits you. Tune URL with user macros if required.  

## Setup

see https://nginx.ru/en/docs/http/ngx_http_stub_status_module.html

## Tuning

Change those macros on host level if needed:

|Macro|Description|Default(agent)|Default(HTTP)|
|---|----|---|---|
|{$STUB_STATUS_HOST}| | localhost | n/a |
|{$STUB_STATUS_PATH}| | basic_status | basic_status|
|{$STUB_STATUS_PORT}| | 80 | 80 |

## Items

See in template

## Triggers

See in template

## Demo

![image](https://user-images.githubusercontent.com/14870891/40243447-ee32cc5a-5ac8-11e8-9a9f-7bb101f088df.png)

![image](https://user-images.githubusercontent.com/14870891/40243215-5c5d3018-5ac8-11e8-8a48-8d6fece9a890.png)

## Next steps

- access.log parsing
- Nginx plus template

## References

https://github.com/strannick-ru/nginx-plus-zabbix  
https://github.com/AlexGluck/ZBX_NGINX  
https://github.com/adubkov/zbx_nginx_template  
https://github.com/goldenclone/nginx-sla  