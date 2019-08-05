
# Template Net QTech QSW SNMPv2

## Overview

For Zabbix version: 3.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS}|-|1|
|{$MEMORY_UTIL_MAX}|-|90|
|{$PSU_CRIT_STATUS}|-|1|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|75|
|{$TEMP_WARN}|-|65|

## Template links

|Name|
|----|
|Template Module EtherLike-MIB SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|PSU Discovery|-|SNMP|
|FAN Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|CPU utilization|MIB: QTECH-MIB</br>CPU utilization in %|SNMP|
|Used memory|MIB: QTECH-MIB</br>Used memory in Bytes|SNMP|
|Total memory|MIB: QTECH-MIB</br>Total memory in Bytes|SNMP|
|Memory utilization|Memory utilization in %|CALCULATED|
|Hardware model name|MIB: ENTITY-MIB</br>|SNMP|
|Hardware serial number|MIB: ENTITY-MIB</br>|SNMP|
|Firmware version|MIB: ENTITY-MIB</br>|SNMP|
|Hardware version(revision)|MIB: ENTITY-MIB</br>|SNMP|
|Operating system|MIB: QTECH-MIB</br>|SNMP|
|Temperature|MIB: QTECH-MIB</br>Temperature readings of testpoint: __RESOURCE__|SNMP|
|{#SNMPINDEX}: Power supply status|MIB: QTECH-MIB</br>|SNMP|
|{#SNMPINDEX}: Fan status|MIB: QTECH-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[switchCpuUsage.0].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[vm.memory.pused.0].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|INFO|
|Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[switchTemperature.0].avg(5m)}>{$TEMP_WARN:""}`|WARNING|
|Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[switchTemperature.0].avg(5m)}>{$TEMP_CRIT:""}`|HIGH|
|Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[switchTemperature.0].avg(5m)}<{$TEMP_CRIT_LOW:""}`|AVERAGE|
|{#SNMPINDEX}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[sysPowerStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE|
|{#SNMPINDEX}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[sysFanStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE|

## References

