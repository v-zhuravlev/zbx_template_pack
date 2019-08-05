
# Template Net D-Link DES 7200 SNMPv2

## Overview

Minimum version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS}|-|5|
|{$MEMORY_UTIL_MAX}|-|90|
|{$PSU_CRIT_STATUS}|-|5|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|75|
|{$TEMP_WARN}|-|65|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Memory Discovery|-|SNMP|
|Temperature Discovery|-|SNMP|
|PSU Discovery|-|SNMP|
|FAN Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|CPU utilization|MIB: MY-PROCESS-MIB</br>CPU utilization in %|SNMP|
|Hardware model name|MIB: SNMPv2-MIB</br>A textual description of the entity. This value should</br>include the full name and version identification of the system's hardware type, software operating-system, and</br>networking software.|SNMP|
|Firmware version|MIB: ENTITY-MIB</br>|SNMP|
|Hardware version(revision)|MIB: ENTITY-MIB</br>|SNMP|
|Operating system|MIB: MY-SYSTEM-MIB</br>|SNMP|
|Memory utilization|MIB: MY-MEMORY-MIB</br>This is the memory pool utilization currently.|SNMP|
|{#SNMPVALUE}: Temperature|MIB: MY-SYSTEM-MIB</br>Return the current temperature of the FastSwitch.The temperature display is not supported for the current temperature returns to 0.|SNMP|
|{#SNMPVALUE}: Power supply status|MIB: MY-SYSTEM-MIB</br>|SNMP|
|{#SNMPVALUE}: Fan status|MIB: MY-SYSTEM-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|
|----|-----------|----|
|High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[myCPUUtilization5Min.0].avg(5m)}>{$CPU_UTIL_MAX}`|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|
|High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[myMemoryPoolCurrentUtilization.{#SNMPINDEX}].avg(5m)}>{$MEMORY_UTIL_MAX}`|
|{#SNMPVALUE}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[mySystemTemperatureCurrent.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`|
|{#SNMPVALUE}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[mySystemTemperatureCurrent.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|
|{#SNMPVALUE}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[mySystemTemperatureCurrent.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|
|{#SNMPVALUE}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[mySystemElectricalSourceIsNormal.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|
|{#SNMPVALUE}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[mySystemFanIsNormal.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|

## References

