
# Template Net Brocade FC SNMPv2

## Overview

Minimum version: 4.0  
https://community.brocade.com/dtscp75322/attachments/dtscp75322/fibre/25235/1/FOS_MIB_Reference_v740.pdf
This template was tested on:

- Brocade 6520, version v7.4.1c
- Brocade 300, version v7.0.0c
- Brocade BL 5480, version v6.3.1c

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS}|-|2|
|{$FAN_OK_STATUS}|-|4|
|{$HEALTH_CRIT_STATUS}|-|4|
|{$HEALTH_WARN_STATUS:"offline"}|-|2|
|{$HEALTH_WARN_STATUS:"testing"}|-|3|
|{$MEMORY_UTIL_MAX}|-|90|
|{$PSU_CRIT_STATUS}|-|2|
|{$PSU_OK_STATUS}|-|4|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|75|
|{$TEMP_WARN_STATUS}|-|5|
|{$TEMP_WARN}|-|65|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Temperature Discovery|-|SNMP|
|PSU Discovery|-|SNMP|
|FAN Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|CPU utilization|MIB: SW-MIB</br>System's CPU usage.|SNMP|
|Memory utilization|MIB: SW-MIB</br>Memory utilization in %|SNMP|
|Overall system health status|MIB: SW-MIB</br>The current operational status of the switch.The states are as follow:</br>online(1) means the switch is accessible by an external Fibre Channel port</br>offline(2) means the switch is not accessible</br>testing(3) means the switch is in a built-in test mode and is not accessible by an external Fibre Channel port</br>faulty(4) means the switch is not operational.|SNMP|
|Hardware serial number|MIB: SW-MIB</br>|SNMP|
|Firmware version|MIB: SW-MIB</br>|SNMP|
|{#SENSOR_INFO}: Temperature|MIB: SW-MIB</br>Temperature readings of testpoint: {#SENSOR_INFO}|SNMP|
|{#SENSOR_INFO}: Temperature status|MIB: SW-MIB</br>Temperature status of testpoint: {#SENSOR_INFO}|SNMP|
|{#SENSOR_INFO}: Power supply status|MIB: SW-MIB</br>|SNMP|
|{#SENSOR_INFO}: Fan status|MIB: SW-MIB</br>|SNMP|
|{#SENSOR_INFO}: Fan speed|MIB: SW-MIB</br>The current value (reading) of the sensor.</br>The value, -2147483648, represents an unknown quantity.</br>The fan value will be in RPM(revolution per minute)</br>|SNMP|


## Triggers

|Name|Description|Expression|
|----|-----------|----|
|High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[swCpuUsage.0].avg(5m)}>{$CPU_UTIL_MAX}`|
|High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[swMemUsage.0].avg(5m)}>{$MEMORY_UTIL_MAX}`|
|System status is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for errors|`{TEMPLATE_NAME:system.status[swOperStatus.0].count(#1,{$HEALTH_CRIT_STATUS},eq)}=1`|
|System status is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for warnings|`{TEMPLATE_NAME:system.status[swOperStatus.0].count(#1,{$HEALTH_WARN_STATUS:"offline"},eq)}=1 or {TEMPLATE_NAME:system.status[swOperStatus.0].count(#1,{$HEALTH_WARN_STATUS:"testing"},eq)}=1`|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|
|{#SENSOR_INFO}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[swSensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""} or {Template Net Brocade FC SNMPv2:sensor.temp.status[swSensorStatus.{#SNMPINDEX}].last(0)}={$TEMP_WARN_STATUS}`|
|{#SENSOR_INFO}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[swSensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|
|{#SENSOR_INFO}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[swSensorValue.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|
|{#SENSOR_INFO}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[swSensorStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|
|{#SENSOR_INFO}: Power supply is not in normal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[swSensorStatus.{#SNMPINDEX}].count(#1,{$PSU_OK_STATUS},ne)}=1`|
|{#SENSOR_INFO}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[swSensorStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|
|{#SENSOR_INFO}: Fan is not in normal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[swSensorStatus.{#SNMPINDEX}].count(#1,{$FAN_OK_STATUS},ne)}=1`|

## References

