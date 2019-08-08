
# Template App Apache Zabbix agent

## Overview

For Zabbix version: 4.0  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$APACHE_PROC_NAME}|-|httpd|
|{$APACHE_STATUS_HOST}|-|localhost|
|{$APACHE_STATUS_PATH}|-|server-status?auto|
|{$APACHE_STATUS_PORT}|-|80|

## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Name|Description|Type|
|----|-----------|----|
|Apache: Get Apache HTTP status|-|ZABBIX_PASSIVE|
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
|Apache: Number of processes running|-|ZABBIX_PASSIVE|
|Apache: Memory usage (rss)|Resident set size memory used by process in bytes.|ZABBIX_PASSIVE|
|Apache: Memory usage (vsize)|Virtual memory size used by process in bytes.|ZABBIX_PASSIVE|
|Apache: CPU utilization|Process CPU utilization percentage.|ZABBIX_PASSIVE|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|Apache: Failed to fetch Apache stub status page|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:web.page.get[{$APACHE_STATUS_HOST},{$APACHE_STATUS_PATH},{$APACHE_STATUS_PORT}].str("HTTP/1.1 200")}=0 or  {TEMPLATE_NAME:web.page.get[{$APACHE_STATUS_HOST},{$APACHE_STATUS_PATH},{$APACHE_STATUS_PORT}].nodata(30m)}=1`|WARNING|
|Apache: not running|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:proc.num[{$APACHE_PROC_NAME}].last()}=0`|HIGH|


