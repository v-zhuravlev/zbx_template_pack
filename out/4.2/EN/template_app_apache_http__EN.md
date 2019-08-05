
# Template App Apache HTTP

## Overview

For Zabbix version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$APACHE_STATUS_PATH}|-|server-status?auto|
|{$APACHE_STATUS_PORT}|-|80|


## Discovery rules


## Items collected

|Name|Description|Type|
|----|-----------|----|
|Apache: Get Apache HTTP status|-|HTTP_AGENT|
|Apache: Bytes per second|-|DEPENDENT|
|Apache: Connections async closing|-|DEPENDENT|
|Apache: Connections async keep alive|-|DEPENDENT|
|Apache: Connections async writing|-|DEPENDENT|
|Apache: Connections total|-|DEPENDENT|
|Apache: Requests per second|Calculated as change rate for 'Total Accesses' stat.</br>ReqPerSec is not used, as it counts average since last Apache server start.|DEPENDENT|
|Apache: Total accesses (requests)|-|DEPENDENT|
|Apache: Uptime|-|DEPENDENT|
|Apache: Version|-|DEPENDENT|
|Apache: Workers busy|-|DEPENDENT|
|Apache: Workers idle|-|DEPENDENT|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|Apache: Failed to fetch Apache stub status page|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:apache.get_stub_status.str("HTTP/1.1 200")}=0 or  {TEMPLATE_NAME:apache.get_stub_status.nodata(30m)}=1`|WARNING|


