
# Template App Nginx by HTTP

## Overview

For Zabbix version: 4.2  
The template to monitor Nginx by Zabbix that work without any external scripts.

Most of the metrics are collected in one go, thanks to Zabbix bulk data collection.  
`Template App Nginx by HTTP` collects metrics by polling [ngx_http_stub_status_module](https://nginx.ru/en/docs/http/ngx_http_stub_status_module.html) with HTTP agent remotely

```text
Active connections: 291 
server accepts handled requests
16630948 16630948 31070465 
Reading: 6 Writing: 179 Waiting: 106 
```

Note that this solution supports https and redirects.


This template was tested on:

- Nginx, version 1.17.2

## Setup

Setup [ngx_http_stub_status_module](https://nginx.ru/en/docs/http/ngx_http_stub_status_module.html).  
Test availability of http_stub_status module with `nginx -V 2>&1 | grep -o with-http_stub_status_module`.

Example configuration of Nginx:

```text
location = /basic_status {
    stub_status;
    allow <IP of your Zabbix server/proxy>;
    deny all;
}
```

If you use another location, don't forget to change {$NGINX.STUB_STATUS_PATH} macro.


## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$NGINX.RESPONSE_TIME.MAX.WARN}|The Nginx maximum response time in seconds for trigger expression.|10|
|{$NGINX.STUB_STATUS_PATH}|The path of Nginx stub_status page.|basic_status|
|{$NGINX.STUB_STATUS_PORT}|The port of Nginx stub_status host or container.|80|
|{$NGINX.STUB_STATUS_PROTOCOL}|The protocol http or https of Nginx stub_status host or container.|http|

## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Nginx|Nginx: Service status|-|SIMPLE|net.tcp.service.perf[{$NGINX.STUB_STATUS_PROTOCOL},{HOST.CONN},{$NGINX.STUB_STATUS_PORT}]|
|Nginx|Nginx: Requests total|The total number of client requests.|DEPENDENT|nginx.requests.total</br>**Preprocessing**:</br> - REGEX: `server accepts handled requests\s+([0-9]+) ([0-9]+) ([0-9]+) \3`|
|Nginx|Nginx: Requests per second|The total number of client requests.|DEPENDENT|nginx.requests.total.rate</br>**Preprocessing**:</br> - REGEX: `server accepts handled requests\s+([0-9]+) ([0-9]+) ([0-9]+) \3`</br> - CHANGE_PER_SECOND|
|Nginx|Nginx: Connections accepted per second|The total number of accepted client connections.|DEPENDENT|nginx.connections.accepted.rate</br>**Preprocessing**:</br> - REGEX: `server accepts handled requests\s+([0-9]+) ([0-9]+) ([0-9]+) \1`</br> - CHANGE_PER_SECOND|
|Nginx|Nginx: Connections handled per second|The total number of handled connections. Generally, the parameter value is the same as accepts unless some resource limits have been reached (for example, the worker_connections limit).|DEPENDENT|nginx.connections.handled.rate</br>**Preprocessing**:</br> - REGEX: `server accepts handled requests\s+([0-9]+) ([0-9]+) ([0-9]+) \2`</br> - CHANGE_PER_SECOND|
|Nginx|Nginx: Connections active|The current number of active client connections including Waiting connections.|DEPENDENT|nginx.connections.active</br>**Preprocessing**:</br> - REGEX: `Active connections: ([0-9]+) \1`|
|Nginx|Nginx: Connections reading|The current number of connections where nginx is reading the request header.|DEPENDENT|nginx.connections.reading</br>**Preprocessing**:</br> - REGEX: `Reading: ([0-9]+) Writing: ([0-9]+) Waiting: ([0-9]+) \1`|
|Nginx|Nginx: Connections waiting|The current number of idle client connections waiting for a request.|DEPENDENT|nginx.connections.waiting</br>**Preprocessing**:</br> - REGEX: `Reading: ([0-9]+) Writing: ([0-9]+) Waiting: ([0-9]+) \3`|
|Nginx|Nginx: Connectinos writing|The current number of connections where nginx is writing the response back to the client.|DEPENDENT|nginx.connections.writing</br>**Preprocessing**:</br> - REGEX: `Reading: ([0-9]+) Writing: ([0-9]+) Waiting: ([0-9]+) \2`|
|Nginx|Nginx: Version|-|DEPENDENT|nginx.version</br>**Preprocessing**:</br> - REGEX: `Server: nginx/(.+) \1`</br> - DISCARD_UNCHANGED_HEARTBEAT: `1d`|
|Zabbix_raw_items|Nginx: Get stub status page|The following status information is provided:</br>Active connections - the current number of active client connections including Waiting connections.</br>Accepts - the total number of accepted client connections.</br>Handled - the total number of handled connections. Generally, the parameter value is the same as accepts unless some resource limits have been reached (for example, the worker_connections limit).</br>Requests - the total number of client requests.</br>Reading - the current number of connections where nginx is reading the request header.</br>Writing - the current number of connections where nginx is writing the response back to the client.</br>Waiting - the current number of idle client connections waiting for a request.|HTTP_AGENT|nginx.get_stub_status|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Nginx: Service is down|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:net.tcp.service.perf[{$NGINX.STUB_STATUS_PROTOCOL},{HOST.CONN},{$NGINX.STUB_STATUS_PORT}].last()}=0`|HIGH|Manual close: YES</br>|
|Nginx: Service response time is too high (over {$NGINX.RESPONSE_TIME.MAX.WARN}s for 5m)|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:net.tcp.service.perf[{$NGINX.STUB_STATUS_PROTOCOL},{HOST.CONN},{$NGINX.STUB_STATUS_PORT}].min(5m)}>{$NGINX.RESPONSE_TIME.MAX.WARN}`|WARNING|Manual close: YES</br>|
|Nginx: Version has changed (new version: {ITEM.VALUE})|Last value: {ITEM.LASTVALUE1}.</br>Nginx version has changed. Ack to close.|`{TEMPLATE_NAME:nginx.version.diff()}=1 and {TEMPLATE_NAME:nginx.version.strlen()}>0`|INFO|Manual close: YES</br>|
|Nginx: Failed to fetch stub status page (no data for 30m)|Last value: {ITEM.LASTVALUE1}.</br>Zabbix has not received data for items for the last 30 minutes.|`{TEMPLATE_NAME:nginx.get_stub_status.str("HTTP/1.1 200")}=0 or  {TEMPLATE_NAME:nginx.get_stub_status.nodata(30m)}=1`|WARNING|Manual close: YES</br>**Depends on**:</br> - Nginx: Service is down</br>|

## Feedback

Please report any issues with the template at https://support.zabbix.com
