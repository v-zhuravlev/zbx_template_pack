
# Template Net Ubiquiti AirOS SNMPv1

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$MEMORY_UTIL_MAX}|-|90|

## Template links

|Name|
|----|
|Template Module Generic SNMPv1|
|Template Module Interfaces Simple SNMPv1|

## Discovery rules


## Items collected

|Name|Description|Type|
|----|-----------|----|
|CPU utilization|MIB: FROGFOOT-RESOURCES-MIB</br>5 minute load average of processor load.|SNMP|
|Free memory|MIB: FROGFOOT-RESOURCES-MIB</br>|SNMP|
|Total memory|MIB: FROGFOOT-RESOURCES-MIB</br>Total memory in Bytes|SNMP|
|Memory utilization|Memory utilization in %|CALCULATED|
|Hardware model name|MIB: IEEE802dot11-MIB</br>A printable string used to identify the manufacturer's product name of the resource. Maximum string length is 128 octets.|SNMP|
|Firmware version|MIB: IEEE802dot11-MIB</br>Printable string used to identify the manufacturer's product version of the resource. Maximum string length is 128 octets.|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[loadValue.2].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[memoryUsedPercentage].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|INFO|

## References

