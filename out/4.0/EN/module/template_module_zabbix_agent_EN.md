
# Template Module Zabbix agent

## Overview

For Zabbix version: 4.0  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$AGENT.TIMEOUT}|<p>-</p>|`5m`|

## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Monitoring_agent|Version of Zabbix agent running|<p>-</p>|ZABBIX_PASSIVE|agent.version<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Monitoring_agent|Host name of Zabbix agent running|<p>-</p>|ZABBIX_PASSIVE|agent.hostname<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Status|Zabbix agent availability|<p>Monitoring agent availability status</p>|INTERNAL|zabbix[host,agent,available]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Zabbix agent is not available|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Zabbix agent is not available.</p>|`{TEMPLATE_NAME:zabbix[host,agent,available].max({$AGENT.TIMEOUT})}=0`|AVERAGE|<p>Manual close: YES</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

