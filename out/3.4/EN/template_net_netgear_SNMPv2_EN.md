
# Template Net Netgear Fastpath SNMPv2

## Overview

For Zabbix version: 3.4  
https://kb.netgear.com/24352/MIBs-for-Smart-switches

This template was tested on:

- Netgear M5300-28G

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS:"failed"}|-|2|
|{$MEMORY_UTIL_MAX}|-|90|
|{$PSU_CRIT_STATUS:"failed"}|-|2|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT_STATUS}|-|3|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN_STATUS}|-|2|
|{$TEMP_WARN}|-|50|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Temperature Discovery|FASTPATH-BOXSERVICES-PRIVATE-MIB::boxServicesTempSensorsTable|SNMP|
|FAN Discovery|FASTPATH-BOXSERVICES-PRIVATE-MIB::1.3.6.1.4.1.4526.10.43.1.6.1.1|SNMP|
|PSU Discovery|FASTPATH-BOXSERVICES-PRIVATE-MIB::boxServicesPowSupplyIndex|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|CPU utilization|MIB: FASTPATH-SWITCHING-MIB</br>CPU utilization in %|SNMP|
|Free memory|MIB: FASTPATH-SWITCHING-MIB</br>The total memory freed for utilization.|SNMP|
|Total memory|MIB: FASTPATH-SWITCHING-MIB</br>The total Memory allocated for the tasks|SNMP|
|Memory utilization|Memory utilization in %|CALCULATED|
|Operating system|MIB: FASTPATH-SWITCHING-MIB</br>Operating System running on this unit|SNMP|
|Hardware model name|MIB: FASTPATH-SWITCHING-MIB</br>|SNMP|
|Hardware serial number|MIB: FASTPATH-SWITCHING-MIB</br>Serial number of the switch|SNMP|
|#{#SNMPVALUE}: Temperature|MIB: FASTPATH-BOXSERVICES-PRIVATE-MIB</br>The temperature value reported by sensor|SNMP|
|#{#SNMPVALUE}: Temperature status|MIB: FASTPATH-BOXSERVICES-PRIVATE-MIB</br>The state of temperature sensor|SNMP|
|#{#SNMPVALUE}: Fan status|MIB: FASTPATH-BOXSERVICES-PRIVATE-MIB</br>The status of fan|SNMP|
|#{#SNMPVALUE}: Power supply status|MIB: FASTPATH-BOXSERVICES-PRIVATE-MIB</br>The status of power supply|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[agentSwitchCpuProcessTotalUtilization.0].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[memoryUsedPercentage.0].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|
|#{#SNMPVALUE}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[boxServicesTempSensorTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""} or {Template Net Netgear Fastpath SNMPv2:sensor.temp.status[boxServicesTempSensorState.{#SNMPINDEX}].last(0)}={$TEMP_WARN_STATUS}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[boxServicesTempSensorTemperature.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:""}-3`|WARNING|
|#{#SNMPVALUE}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[boxServicesTempSensorTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""} or {Template Net Netgear Fastpath SNMPv2:sensor.temp.status[boxServicesTempSensorState.{#SNMPINDEX}].last(0)}={$TEMP_CRIT_STATUS}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[boxServicesTempSensorTemperature.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:""}-3`|HIGH|
|#{#SNMPVALUE}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[boxServicesTempSensorTemperature.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[boxServicesTempSensorTemperature.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:""}+3`|AVERAGE|
|#{#SNMPVALUE}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[boxServicesFanItemState.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"failed"},eq)}=1`|AVERAGE|
|#{#SNMPVALUE}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[boxServicesPowSupplyItemState.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS:"failed"},eq)}=1`|AVERAGE|


