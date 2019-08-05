
# Template App Nginx Zabbix agent

## Overview

For Zabbix version: 4.2  
Test availability of http_stub_status module with 'nginx -V 2>&1 | grep -o with-http_stub_status_module'

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$NGINX_STUB_STATUS_HOST}|-|localhost|
|{$NGINX_STUB_STATUS_PATH}|-|basic_status|
|{$NGINX_STUB_STATUS_PORT}|-|80|


## Discovery rules


## Items collected

|Name|Description|Type|
|----|-----------|----|
|Nginx: Get stub status page|The following status information is provided:</br>Active connections</br>The current number of active client connections including Waiting connections.</br>accepts</br>The total number of accepted client connections.</br>handled</br>The total number of handled connections. Generally, the parameter value is the same as accepts unless some resource limits have been reached (for example, the worker_connections limit).</br>requests</br>The total number of client requests.</br>Reading</br>The current number of connections where nginx is reading the request header.</br>Writing</br>The current number of connections where nginx is writing the response back to the client.</br>Waiting</br>The current number of idle client connections waiting for a request.|ZABBIX_PASSIVE|
|Nginx: Requests total|The total number of client requests.|DEPENDENT|
|Nginx: Requests per second|The total number of client requests.|DEPENDENT|
|Nginx: Connections accepted per second|The total number of accepted client connections.|DEPENDENT|
|Nginx: Connections handled per second|The total number of handled connections. Generally, the parameter value is the same as accepts unless some resource limits have been reached (for example, the worker_connections limit).|DEPENDENT|
|Nginx: Connections active|The current number of active client connections including Waiting connections.|DEPENDENT|
|Nginx: Connections reading|The current number of connections where nginx is reading the request header.|DEPENDENT|
|Nginx: Connections waiting|The current number of idle client connections waiting for a request.|DEPENDENT|
|Nginx: Connectinos writing|The current number of connections where nginx is writing the response back to the client.|DEPENDENT|
|Nginx: Number of processes running|-|ZABBIX_PASSIVE|
|Nginx: Memory usage (vsize)|Virtual memory size used by process in bytes.|ZABBIX_PASSIVE|
|Nginx: Memory usage (rss)|Resident set size memory used by process in bytes.|ZABBIX_PASSIVE|
|Nginx: CPU utilization|Process CPU utilization percentage.|ZABBIX_PASSIVE|
|Nginx: Version|-|DEPENDENT|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|Nginx: Failed to fetch nginx stub status page|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:web.page.get[{$NGINX_STUB_STATUS_HOST},{$NGINX_STUB_STATUS_PATH},{$NGINX_STUB_STATUS_PORT}].str("HTTP/1.1 200")}=0 or  {TEMPLATE_NAME:web.page.get[{$NGINX_STUB_STATUS_HOST},{$NGINX_STUB_STATUS_PATH},{$NGINX_STUB_STATUS_PORT}].nodata(30m)}=1`|WARNING|
|Nginx: not running|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:proc.num[nginx].last()}=0`|HIGH|


