
# Template Server IBM IMM SNMPv2

## Overview

Minimum version: 3.4  
for IMM2 and IMM1 IBM serverX hardware
This template was tested on:

- IBM System x3550 M2 with IMM1, version 
- IBM x3250M3 with IMM1, version 
- IBM x3550M5 with IMM2, version 
- System x3550 M3 with IMM1, version 

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$DISK_OK_STATUS}|-|Normal|
|{$FAN_OK_STATUS}|-|Normal|
|{$HEALTH_CRIT_STATUS}|-|2|
|{$HEALTH_DISASTER_STATUS}|-|0|
|{$HEALTH_WARN_STATUS}|-|4|
|{$PSU_OK_STATUS}|-|Normal|
|{$TEMP_CRIT:"Ambient"}|-|35|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN:"Ambient"}|-|30|
|{$TEMP_WARN}|-|50|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Temperature Discovery|Scanning IMM-MIB::tempTable|SNMP|
|Temperature Discovery Ambient|Scanning IMM-MIB::tempTable with Ambient filter|SNMP|
|Temperature Discovery CPU|Scanning IMM-MIB::tempTable with CPU filter|SNMP|
|PSU Discovery|IMM-MIB::powerFruName|SNMP|
|FAN Discovery|IMM-MIB::fanDescr|SNMP|
|Physical Disk Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Overall system health status|MIB: IMM-MIB</br>Indicates status of system health for the system in which the IMM resides. Value of 'nonRecoverable' indicates a severe error has occurred and the system may not be functioning. A value of 'critical' indicates that a error has occurred but the system is currently functioning properly. A value of 'nonCritical' indicates that a condition has occurred that may change the state of the system in the future but currently the system is working properly. A value of 'normal' indicates that the system is operating normally.|SNMP|
|Hardware model name|MIB: IMM-MIB</br>|SNMP|
|Hardware serial number|MIB: IMM-MIB</br>Machine serial number VPD information|SNMP|
|{#SNMPVALUE}: Temperature|MIB: IMM-MIB</br>Temperature readings of testpoint: {#SNMPVALUE}|SNMP|
|Ambient: Temperature|MIB: IMM-MIB</br>Temperature readings of testpoint: Ambient|SNMP|
|CPU: Temperature|MIB: IMM-MIB</br>Temperature readings of testpoint: CPU|SNMP|
|{#PSU_DESCR}: Power supply status|MIB: IMM-MIB</br>A description of the power module status.|SNMP|
|{#FAN_DESCR}: Fan status|MIB: IMM-MIB</br>A description of the fan component status.|SNMP|
|{#FAN_DESCR}: Fan speed, %|MIB: IMM-MIB</br>Fan speed expressed in percent(%) of maximum RPM.</br>An octet string expressed as 'ddd% of maximum' where:d is a decimal digit or blank space for a leading zero.</br>If the fan is determined not to be running or the fan speed cannot be determined, the string will indicate 'Offline'.|SNMP|
|{#SNMPINDEX}: Physical disk status|MIB: IMM-MIB</br>|SNMP|
|{#SNMPINDEX}: Physical disk part number|MIB: IMM-MIB</br>disk module FRU name.|SNMP|


## Triggers

|Name|Description|Expression|
|----|-----------|----|
|System is in unrecoverable state!|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.status[systemHealthStat.0].count(#1,{$HEALTH_DISASTER_STATUS},eq)}=1`|
|System status is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for errors|`{TEMPLATE_NAME:system.status[systemHealthStat.0].count(#1,{$HEALTH_CRIT_STATUS},eq)}=1`|
|System status is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for warnings|`{TEMPLATE_NAME:system.status[systemHealthStat.0].count(#1,{$HEALTH_WARN_STATUS},eq)}=1`|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|
|{#SNMPVALUE}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[tempReading.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`|
|{#SNMPVALUE}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[tempReading.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|
|{#SNMPVALUE}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[tempReading.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|
|Ambient: Temperature is above warning threshold: >{$TEMP_WARN:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[tempReading.Ambient.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"Ambient"}`|
|Ambient: Temperature is above critical threshold: >{$TEMP_CRIT:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[tempReading.Ambient.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"Ambient"}`|
|Ambient: Temperature is too low: <{$TEMP_CRIT_LOW:"Ambient"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[tempReading.Ambient.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"Ambient"}`|
|CPU: Temperature is above warning threshold: >{$TEMP_WARN:"CPU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[tempReading.CPU.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"CPU"}`|
|CPU: Temperature is above critical threshold: >{$TEMP_CRIT:"CPU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[tempReading.CPU.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"CPU"}`|
|CPU: Temperature is too low: <{$TEMP_CRIT_LOW:"CPU"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[tempReading.CPU.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"CPU"}`|
|{#PSU_DESCR}: Power supply is not in normal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[powerHealthStatus.{#SNMPINDEX}].count(#1,{$PSU_OK_STATUS},ne)}=1`|
|{#FAN_DESCR}: Fan is not in normal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[fanHealthStatus.{#SNMPINDEX}].count(#1,{$FAN_OK_STATUS},ne)}=1`|
|{#SNMPINDEX}: Physical disk is not in OK state|Last value: {ITEM.LASTVALUE1}.</br>Please check physical disk for warnings or errors|`{TEMPLATE_NAME:system.hw.physicaldisk.status[diskHealthStatus.{#SNMPINDEX}].count(#1,{$DISK_OK_STATUS},ne)}=1`|

## References

