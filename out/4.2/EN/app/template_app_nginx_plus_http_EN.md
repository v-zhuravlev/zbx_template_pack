
# Template App Nginx Plus HTTP

## Overview

For Zabbix version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$NGINX_API_URL}|-|http://demo.nginx.com/api/3|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Nginx Plus server zones discovery|Discover NginxHTTP virtual servers|DEPENDENT|nginx.plus.get_server_zones.discovery</br>**Preprocessing**:</br> - JAVASCRIPT: `//parsing NGINX plus output like in footer: output = Object.keys(JSON.parse(value)).map(function(zone){     return {"{#NGINX_ZONE}": zone} }) return JSON.stringify({"data": output}) /* http://demo.nginx.com/api/3/http/server_zones {   "hg.nginx.org": {     "processing": 0,     "requests": 175276,     "responses": {       "1xx": 0,       "2xx": 162948,       "3xx": 10117,       "4xx": 2125,       "5xx": 8,       "total": 175198     },     "discarded": 78,     "received": 50484208,     "sent": 7356417338   },   "trac.nginx.org": {     "processing": 7,     "requests": 448613,     "responses": {       "1xx": 0,       "2xx": 305562,       "3xx": 87065,       "4xx": 23136,       "5xx": 5127,       "total": 420890     },     "discarded": 27716,     "received": 137307886,     "sent": 3989556941   },   "lxr.nginx.org": {     "processing": 0,     "requests": 48743,     "responses": {       "1xx": 0,       "2xx": 47132,       "3xx": 97,       "4xx": 792,       "5xx": 719,       "total": 48740     },     "discarded": 3,     "received": 14502895,     "sent": 6756762274   } } */ `</br> - DISCARD_UNCHANGED_HEARTBEAT: `1h`|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Nginx|Nginx: Get server zones|Display information about HTTP virtual servers|HTTP_AGENT|nginx.plus.get_server_zones|
|Nginx|{#NGINX_ZONE}: Discarded|-|DEPENDENT|nginx.plus.discarded[{#NGINX_ZONE}]</br>**Preprocessing**:</br> - JSONPATH: `$["{#NGINX_ZONE}"].discarded`|
|Nginx|{#NGINX_ZONE}: Processing|-|DEPENDENT|nginx.plus.processing[{#NGINX_ZONE}]</br>**Preprocessing**:</br> - JSONPATH: `$["{#NGINX_ZONE}"].processing`|
|Nginx|{#NGINX_ZONE}: Received|-|DEPENDENT|nginx.plus.received[{#NGINX_ZONE}]</br>**Preprocessing**:</br> - JSONPATH: `$["{#NGINX_ZONE}"].received`|
|Nginx|{#NGINX_ZONE}: Requests|-|DEPENDENT|nginx.plus.requests[{#NGINX_ZONE}]</br>**Preprocessing**:</br> - JSONPATH: `$["{#NGINX_ZONE}"].requests`|
|Nginx|{#NGINX_ZONE}: Responses 1xx|-|DEPENDENT|nginx.plus.responses.1xx[{#NGINX_ZONE}]</br>**Preprocessing**:</br> - JSONPATH: `$["{#NGINX_ZONE}"].responses.1xx`|
|Nginx|{#NGINX_ZONE}: Responses 2xx|-|DEPENDENT|nginx.plus.responses.2xx[{#NGINX_ZONE}]</br>**Preprocessing**:</br> - JSONPATH: `$["{#NGINX_ZONE}"].responses.2xx`|
|Nginx|{#NGINX_ZONE}: Responses 3xx|-|DEPENDENT|nginx.plus.responses.3xx[{#NGINX_ZONE}]</br>**Preprocessing**:</br> - JSONPATH: `$["{#NGINX_ZONE}"].responses.3xx`|
|Nginx|{#NGINX_ZONE}: Responses 4xx|-|DEPENDENT|nginx.plus.responses.4xx[{#NGINX_ZONE}]</br>**Preprocessing**:</br> - JSONPATH: `$["{#NGINX_ZONE}"].responses.4xx`|
|Nginx|{#NGINX_ZONE}: Responses 5xx|-|DEPENDENT|nginx.plus.responses.5xx[{#NGINX_ZONE}]</br>**Preprocessing**:</br> - JSONPATH: `$["{#NGINX_ZONE}"].responses.5xx`|
|Nginx|{#NGINX_ZONE}: Responses total|-|DEPENDENT|nginx.plus.responses.total[{#NGINX_ZONE}]</br>**Preprocessing**:</br> - JSONPATH: `$["{#NGINX_ZONE}"].responses.total`|
|Nginx|{#NGINX_ZONE}: Sent|-|DEPENDENT|nginx.plus.sent[{#NGINX_ZONE}]</br>**Preprocessing**:</br> - JSONPATH: `$["{#NGINX_ZONE}"].sent`|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|

## Feedback

Please report any issues with the template at https://support.zabbix.com

