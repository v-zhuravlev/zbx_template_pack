
# Template App Nginx Plus HTTP

## Overview

Minimum version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$NGINX_API_URL}|-|http://demo.nginx.com/api/3|


## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Nginx Plus server zones discovery|Discover NginxHTTP virtual servers|DEPENDENT|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Nginx: Get server zones|Display information about HTTP virtual servers|HTTP_AGENT|
|{#NGINX_ZONE}: Discarded|-|DEPENDENT|
|{#NGINX_ZONE}: Processing|-|DEPENDENT|
|{#NGINX_ZONE}: Received|-|DEPENDENT|
|{#NGINX_ZONE}: Requests|-|DEPENDENT|
|{#NGINX_ZONE}: Responses 1xx|-|DEPENDENT|
|{#NGINX_ZONE}: Responses 2xx|-|DEPENDENT|
|{#NGINX_ZONE}: Responses 3xx|-|DEPENDENT|
|{#NGINX_ZONE}: Responses 4xx|-|DEPENDENT|
|{#NGINX_ZONE}: Responses 5xx|-|DEPENDENT|
|{#NGINX_ZONE}: Responses total|-|DEPENDENT|
|{#NGINX_ZONE}: Sent|-|DEPENDENT|


## Triggers

|Name|Description|Expression|
|----|-----------|----|

## References

