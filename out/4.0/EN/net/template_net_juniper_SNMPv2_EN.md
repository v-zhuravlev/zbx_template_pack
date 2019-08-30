
# Template Net Juniper SNMPv2

## Overview

For Zabbix version: 4.0  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS}|-|6|
|{$HEALTH_CRIT_STATUS}|-|3|
|{$MEMORY_UTIL_MAX}|-|90|
|{$PSU_CRIT_STATUS}|-|6|
|{$TEMP_CRIT:"Routing Engine"}|-|80|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN:"Routing Engine"}|-|70|
|{$TEMP_WARN}|-|50|

## Template links

|Name|
|----|
|Template Module EtherLike-MIB SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|CPU and Memory Discovery|Scanning JUNIPER-MIB::jnxOperatingTable for CPU and Memory</br>http://kb.juniper.net/InfoCenter/index?page=content&id=KB17526&actp=search. Filter limits results to Routing Engines|SNMP|jnxOperatingTable.discovery</br>**Filter**: AND_OR </br> - A: {#SNMPVALUE} MATCHES_REGEX `Routing Engine.*`|
|Temperature discovery|Scanning JUNIPER-MIB::jnxOperatingTable for Temperature</br>http://kb.juniper.net/InfoCenter/index?page=content&id=KB17526&actp=search. Filter limits results to Routing Engines|SNMP|jnxOperatingTable.discovery.temp</br>**Filter**: AND_OR </br> - A: {#SNMPVALUE} MATCHES_REGEX `[^0]+`|
|FAN Discovery|Scanning JUNIPER-MIB::jnxOperatingTable for Fans|SNMP|jnxOperatingTable.discovery.fans|
|PSU Discovery|Scanning JUNIPER-MIB::jnxOperatingTable for Power Supplies|SNMP|jnxOperatingTable.discovery.psu|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|{#SNMPVALUE}: CPU utilization|MIB: JUNIPER-MIB</br>The CPU Load Average over the last 5 minutes Here it will be shown as percentage valueZero if unavailable or inapplicable.</br>Reference: http://kb.juniper.net/library/CUSTOMERSERVICE/GLOBAL_JTAC/BK26199/SRX%20SNMP%20Monitoring%20Guide_v1.1.pdf|SNMP|system.cpu.util[jnxOperatingCPU.{#SNMPINDEX}]|
|Fans|{#SNMPVALUE}: Fan status|MIB: JUNIPER-MIB</br>|SNMP|sensor.fan.status[jnxOperatingState.4.{#SNMPINDEX}]|
|Inventory|Hardware serial number|MIB: JUNIPER-MIB</br>The serial number of this subject, blank if unknown or unavailable.|SNMP|system.hw.serialnumber</br>**Preprocessing**:</br> - DISCARD_UNCHANGED_HEARTBEAT: `1d`|
|Inventory|Hardware model name|MIB: JUNIPER-MIB</br>The name, model, or detailed description of the box,indicating which product the box is about, for example 'M40'.|SNMP|system.hw.model</br>**Preprocessing**:</br> - DISCARD_UNCHANGED_HEARTBEAT: `1d`|
|Inventory|Operating system|MIB: SNMPv2-MIB</br>|SNMP|system.sw.os</br>**Preprocessing**:</br> - REGEX: `kernel (JUNOS [0-9a-zA-Z\.\-]+) \1`</br> - DISCARD_UNCHANGED_HEARTBEAT: `1d`|
|Memory|{#SNMPVALUE}: Memory utilization|MIB: JUNIPER-MIB</br>The buffer pool utilization in percentage of this subject.  Zero if unavailable or inapplicable.</br>Reference: http://kb.juniper.net/library/CUSTOMERSERVICE/GLOBAL_JTAC/BK26199/SRX%20SNMP%20Monitoring%20Guide_v1.1.pdf|SNMP|vm.memory.pused[jnxOperatingBuffer.{#SNMPINDEX}]|
|Power_supply|{#SNMPVALUE}: Power supply status|MIB: JUNIPER-MIB</br>If they are using DC power supplies there is a known issue on PR 1064039 where the fans do not detect the temperature correctly and fail to cool the power supply causing the shutdown to occur.</br>This is fixed in Junos 13.3R7 https://forums.juniper.net/t5/Routing/PEM-0-not-OK-MX104/m-p/289644#M14122|SNMP|sensor.psu.status[jnxOperatingState.2.{#SNMPINDEX}]|
|Status|Overall system health status|MIB: JUNIPER-ALARM-MIB</br>The red alarm indication on the craft interface panel.</br>The red alarm is on when there is some system</br>failure or power supply failure or the system</br>is experiencing a hardware malfunction or some</br>threshold is being exceeded.</br>This red alarm state could be turned off by the</br>ACO/LT (Alarm Cut Off / Lamp Test) button on the</br>front panel module.|SNMP|system.status[jnxRedAlarmState.0]|
|Temperature|{#SENSOR_INFO}: Temperature|MIB: JUNIPER-MIB</br>The temperature in Celsius (degrees C) of {#SENSOR_INFO}|SNMP|sensor.temp.value[jnxOperatingTemp.{#SNMPINDEX}]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|{#SNMPVALUE}: High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[jnxOperatingCPU.{#SNMPINDEX}].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE||
|{#SNMPVALUE}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[jnxOperatingState.4.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE||
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|Manual close: YES</br>|
|{#SNMPVALUE}: High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[jnxOperatingBuffer.{#SNMPINDEX}].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE||
|{#SNMPVALUE}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[jnxOperatingState.2.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE||
|System status is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for errors|`{TEMPLATE_NAME:system.status[jnxRedAlarmState.0].count(#1,{$HEALTH_CRIT_STATUS},eq)}=1`|HIGH||
|{#SENSOR_INFO}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[jnxOperatingTemp.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[jnxOperatingTemp.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:""}-3`|WARNING|**Depends on**:</br> - {#SENSOR_INFO}: Temperature is above critical threshold: >{$TEMP_CRIT:""}</br>|
|{#SENSOR_INFO}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[jnxOperatingTemp.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[jnxOperatingTemp.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:""}-3`|HIGH||
|{#SENSOR_INFO}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[jnxOperatingTemp.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[jnxOperatingTemp.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:""}+3`|AVERAGE||

## Feedback

Please report any issues with the template at https://support.zabbix.com

