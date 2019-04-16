# template_app_nginx_plus

Template App Nginx Plus for Zabbix 4.2 that works without any external scripts.  
Tune URL with user macros if required.  

Sample dashboard of [Nginx Plus](https://www.nginx.com/products/nginx/) can be found [here](http://demo.nginx.com/dashboard.htm):  


## Setup

see https://www.nginx.com/products/nginx/live-activity-monitoring

## Tuning

Change those macros on host level if needed:

|Macro|Description|Default(agent)|Default(HTTP)|
|---|----|---|---|
|{$NGINX_STUB_STATUS_HOST}| | localhost | n/a |
|{$NGINX_API_URL}| | basic_status | basic_status|
|{$NGINX_STUB_STATUS_PORT}| | 80 | 80 |

## Items

See in template

## Triggers

See in template

## Demo



## Next steps



## References

- https://www.nginx.com/blog/nginx-plus-r13-released#r13-api
- http://demo.nginx.com/dashboard.htm
- http://demo.nginx.com/api/3
- API documentation https://nginx.org/en/docs/http/ngx_http_api_module.html
- old status module(not used here) https://nginx.org/en/docs/http/ngx_http_status_module.html