# Template App Nginx *

Templates to monitor Nginx by Zabbix that work without any external scripts.  Most of the metrics are collected in one go, thanks to Zabbix bulk data collection.  
Two templates are available:  
`Template App Nginx Zabbix agent` - (Zabbix version >= 3.4) - collects metrics by polling [ngx_stub_status_module](https://nginx.ru/en/docs/http/ngx_http_stub_status_module.html) locally with Zabbix agent:

```text
Active connections: 1 
server accepts handled requests
3 3 3
Reading: 0 Writing: 1 Waiting: 0
```

It also uses Zabbix agent to collect `nginx` Linux process stats like CPU usage, memory usage and whether process is running or not.

`Template App Nginx HTTP` - (Zabbix version >= 4.0) - collects metrics by polling [ngx_stub_status_module](https://nginx.ru/en/docs/http/ngx_http_stub_status_module.html) with HTTP agent remotely.  

## Setup

- Setup [ngx_http_stub_status_module](https://nginx.ru/en/docs/http/ngx_http_stub_status_module.html)
- (If using `Template App Nginx Zabbix agent`) install and setup [Zabbix agent](https://www.zabbix.com/documentation/current/manual/installation/install_from_packages)

## Zabix configuration

Change those macros on host level if needed:

|Macro|Description|Default(agent)|Default(HTTP)|
|---|----|---|---|
|{$NGINX_STUB_STATUS_HOST}| | localhost | n/a |
|{$NGINX_STUB_STATUS_PATH}| | basic_status | basic_status|
|{$NGINX_STUB_STATUS_PORT}| | 80 | 80 |

## Items

See what items are collected in the templates.

|Item|Triggers|Graphs|HTTP agent template|Zabbix agent template|
|---|---|---|---|---|
|nginx.get_stub_status|x| |x|x|
|nginx.version| | |x|x|
|nginx.requests.total| | |x|x|
|nginx.requests.total.rate| | |x|x|
|nginx.connections.accepted.rate| | |x|x|
|nginx.connections.handled.rate| | |x|x|
|nginx.connections.active| |x|x|x|
|nginx.connections.reading| |x|x|x|
|nginx.connections.waiting| |x|x|x|
|nginx.connections.writing| |x|x|x|
|nginx.proc.num|x| | |x|
|nginx.proc.mem.vsize| |x| |x|
|nginx.proc.mem.rss| |x| |x|
|nginx.proc.cpu.util| | | |x|
|nginx.responses.1xx.rate| |x| | |
|nginx.responses.2xx.rate| |x| | |
|nginx.responses.3xx.rate| |x| | |
|nginx.responses.4xx.rate|x|x| | |
|nginx.responses.5xx.rate|x|x| | |

## Triggers

See in template

## Demo

Available:
![image](https://user-images.githubusercontent.com/14870891/56308681-91a07200-6150-11e9-8ebb-abd5ec58d7ab.png)


![image](https://user-images.githubusercontent.com/14870891/56308529-2b1b5400-6150-11e9-8378-315c43b9206f.png)

![image](https://user-images.githubusercontent.com/14870891/56308912-11c6d780-6151-11e9-9198-4fa2d3c7f311.png)

Work in progress:
![image](https://user-images.githubusercontent.com/14870891/56141847-48acba00-5fa6-11e9-92d8-2ac13db6c391.png)

![image](https://user-images.githubusercontent.com/14870891/56146598-23707980-5faf-11e9-84f9-f00bbdf468fc.png)

## Next steps

- Add triggers on high rate of 5xx and 4xx
- Add access.log parsing
- Add the following new macros:

|Macro|Description|Default(agent)|Default(HTTP)|
|---|----|---|---|
|{$NGINX_ACCESS_LOG}| | /var/log/nginx/access.log | n/a |
|{$NGINX_4XX_RATE_WARN}| | 2 | n/a |
|{$NGINX_5XX_RATE_CRIT}| | 2 | n/a |

## References

https://nginx.org/en/docs/http/ngx_http_stub_status_module.html  
https://github.com/strannick-ru/nginx-plus-zabbix  
https://github.com/AlexGluck/ZBX_NGINX  
https://github.com/adubkov/zbx_nginx_template  
https://github.com/goldenclone/nginx-sla  
http://servermonitoringhq.com/blog/how_to_quickly_stress_test_a_web_server  
https://github.com/lebinh/ngxtop