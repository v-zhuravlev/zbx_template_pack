
# Template Net Huawei VRP SNMPv2

## Overview

For Zabbix version: 4.0  
Reference: https://www.slideshare.net/Huanetwork/huawei-s5700-naming-conventions-and-port-numbering-conventions
Reference: http://support.huawei.com/enterprise/KnowledgebaseReadAction.action?contentId=KB1000090234

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS}|-|2|
|{$MEMORY_UTIL_MAX}|-|90|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN}|-|50|

## Template links

|Name|
|----|
|Template Module EtherLike-MIB SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|MPU Discovery|http://support.huawei.com/enterprise/KnowledgebaseReadAction.action?contentId=KB1000090234. Filter limits results to Main Processing Units|SNMP|
|Entity Discovery|-|SNMP|
|FAN Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|{#ENT_NAME}: CPU utilization|MIB: HUAWEI-ENTITY-EXTENT-MIB</br>The CPU usage for this entity. Generally, the CPU usage will calculate the overall CPU usage on the entity, and itis not sensible with the number of CPU on the entity.</br>Reference: http://support.huawei.com/enterprise/KnowledgebaseReadAction.action?contentId=KB1000090234|SNMP|
|{#ENT_NAME}: Memory utilization|MIB: HUAWEI-ENTITY-EXTENT-MIB</br>The memory usage for the entity. This object indicates what percent of memory are used.</br>Reference: http://support.huawei.com/enterprise/KnowledgebaseReadAction.action?contentId=KB1000090234|SNMP|
|{#ENT_NAME}: Temperature|MIB: HUAWEI-ENTITY-EXTENT-MIB</br>The temperature for the {#SNMPVALUE}.|SNMP|
|{#ENT_NAME}: Hardware serial number|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Hardware version(revision)|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Operating system|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Hardware model name|MIB: ENTITY-MIB</br>|SNMP|
|#{#SNMPVALUE}: Fan status|MIB: HUAWEI-ENTITY-EXTENT-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|{#ENT_NAME}: High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[hwEntityCpuUsage.{#SNMPINDEX}].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|{#ENT_NAME}: High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[hwEntityMemUsage.{#SNMPINDEX}].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|
|{#ENT_NAME}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[hwEntityTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`|WARNING|
|{#ENT_NAME}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[hwEntityTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|HIGH|
|{#ENT_NAME}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[hwEntityTemperature.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|AVERAGE|
|{#ENT_NAME}: Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].strlen()}>0`|INFO|
|#{#SNMPVALUE}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[hwEntityFanState.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE|

## References

