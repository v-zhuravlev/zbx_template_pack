# template_app_nginx

Template App Nginx for Zabbix 3.4+ that works without any external scripts.  
You can poll Nginx using Zabbix agent locally(Template App Nginx Zabbix agent) or poll it directly from Zabbix server/proxy(Template App Nginx HTTP). Choose template that better suits you. Tune URL with user macros if required.  


## Setup

see https://nginx.ru/en/docs/http/ngx_http_stub_status_module.html

```
Active connections: 1 
server accepts handled requests
3 3 3 
Reading: 0 Writing: 1 Waiting: 0
```

## Tuning

Change those macros on host level if needed:

|Macro|Description|Default(agent)|Default(HTTP)|
|---|----|---|---|
|{$NGINX_STUB_STATUS_HOST}| | localhost | n/a |
|{$NGINX_STUB_STATUS_PATH}| | basic_status | basic_status|
|{$NGINX_STUB_STATUS_PORT}| | 80 | 80 |
|{$NGINX_ACCESS_LOG}| | /var/log/nginx/access.log | n/a |
|{$NGINX_4XX_RATE_WARN}| | 2 | n/a |
|{$NGINX_5XX_RATE_CRIT}| | 2 | n/a |

## Items

See details in templates.

|Item|Triggers|Graphs|in Template App Nginx HTTP|in Template App Nginx Agent|
|---|---|---|---|---|
|nginx.get_stub_status|x| |x|x|
|nginx.requests.total| | |x|x|
|nginx.requests.total.rate| | |x|x|
|nginx.connections.accepted.rate| | |x|x|
|nginx.connections.handled.rate| | |x|x|
|nginx.connections.active| |x|x|x|
|nginx.connections.reading| |x|x|x|
|nginx.connections.waiting| |x|x|x|
|nginx.connections.writing| |x|x|x|
|nginx.responses.1xx.rate| |x| |x|
|nginx.responses.2xx.rate| |x| |x|
|nginx.responses.3xx.rate| |x| |x|
|nginx.responses.4xx.rate|x|x| |x|
|nginx.responses.5xx.rate|x|x| |x|
|nginx.proc.num|x| | |x|

## Triggers

See in template

## Demo

![image](https://user-images.githubusercontent.com/14870891/40243447-ee32cc5a-5ac8-11e8-9a9f-7bb101f088df.png)

![image](https://user-images.githubusercontent.com/14870891/40243215-5c5d3018-5ac8-11e8-8a48-8d6fece9a890.png)

![image](https://user-images.githubusercontent.com/14870891/56141847-48acba00-5fa6-11e9-92d8-2ac13db6c391.png)

![image](https://user-images.githubusercontent.com/14870891/56146598-23707980-5faf-11e9-84f9-f00bbdf468fc.png)


## Next steps

- new demo screens
- update doc
- trigger on 5xx and 4xx
- access.log parsing (risky)
- Nginx plus template

## References
https://nginx.org/en/docs/http/ngx_http_stub_status_module.html
https://github.com/strannick-ru/nginx-plus-zabbix  
https://github.com/AlexGluck/ZBX_NGINX  
https://github.com/adubkov/zbx_nginx_template  
https://github.com/goldenclone/nginx-sla  
http://servermonitoringhq.com/blog/how_to_quickly_stress_test_a_web_server
https://github.com/lebinh/ngxtop