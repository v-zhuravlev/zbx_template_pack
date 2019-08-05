
# Template Module ICMP Ping

## Overview

For Zabbix version: 3.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$ICMP_LOSS_WARN}|-|20|
|{$ICMP_RESPONSE_TIME_WARN}|-|0.15|


## Discovery rules


## Items collected

|Name|Description|Type|
|----|-----------|----|
|ICMP ping|-|SIMPLE|
|ICMP loss|-|SIMPLE|
|ICMP response time|-|SIMPLE|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|Unavailable by ICMP ping|Last value: {ITEM.LASTVALUE1}.</br>Last three attempts returned timeout.  Please check device connectivity.|`{TEMPLATE_NAME:icmpping.max(#3)}=0`|HIGH|
|High ICMP ping loss|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:icmppingloss.min(5m)}>{$ICMP_LOSS_WARN} and {TEMPLATE_NAME:icmppingloss.min(5m)}<100`|WARNING|
|High ICMP ping response time|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:icmppingsec.avg(5m)}>{$ICMP_RESPONSE_TIME_WARN}`|WARNING|


