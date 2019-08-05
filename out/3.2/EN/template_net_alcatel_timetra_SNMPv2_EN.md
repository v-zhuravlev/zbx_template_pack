
# Template Net Alcatel Timetra TiMOS SNMPv2

## Overview

For Zabbix version: 3.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS}|-|4|
|{$MEMORY_UTIL_MAX}|-|90|
|{$PSU_CRIT_STATUS}|-|4|
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
|Temperature Discovery|-|SNMP|
|FAN Discovery|-|SNMP|
|PSU Discovery|-|SNMP|
|Entity Serial Numbers Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|CPU utilization|MIB: TIMETRA-SYSTEM-MIB</br>The value of sgiCpuUsage indicates the current CPU utilization for the system.|SNMP|
|Used memory|MIB: TIMETRA-SYSTEM-MIB</br>The value of sgiKbMemoryUsed indicates the total pre-allocated pool memory, in kilobytes, currently in use on the system.|SNMP|
|Free memory|MIB: TIMETRA-SYSTEM-MIB</br>The value of sgiKbMemoryAvailable indicates the amount of free memory, in kilobytes, in the overall system that is not allocated to memory pools, but is available in case a memory pool needs to grow.|SNMP|
|Memory utilization|Memory utilization in %|CALCULATED|
|{#SNMPVALUE}: Temperature|MIB: TIMETRA-SYSTEM-MIB</br>The current temperature reading in degrees celsius from this hardware component's temperature sensor.  If this component does not contain a temperature sensor, then the value -1 is returned.|SNMP|
|#{#SNMPINDEX}: Fan status|MIB: TIMETRA-SYSTEM-MIB</br>Current status of the Fan tray.|SNMP|
|#{#SNMPINDEX}: Power supply status|MIB: TIMETRA-SYSTEM-MIB</br>The overall status of an equipped power supply. </br>For AC multiple powersupplies, this represents the overall status of the first power supplyin the tray (or shelf).</br>For any other type, this represents the overall status of the power supply.</br>If tmnxChassisPowerSupply1Status is'deviceStateOk', then all monitored statuses are 'deviceStateOk'.</br>A value of 'deviceStateFailed' represents a condition where at least one monitored status is in a failed state.</br>|SNMP|
|#{#SNMPINDEX}: Power supply status|MIB: TIMETRA-SYSTEM-MIB</br>The overall status of an equipped power supply.</br>For AC multiple powersupplies, this represents the overall status of the second power supplyin the tray (or shelf).</br>For any other type, this field is unused and set to 'deviceNotEquipped'.</br>If tmnxChassisPowerSupply2Status is 'deviceStateOk', then all monitored statuses are 'deviceStateOk'.</br>A value of 'deviceStateFailed' represents a condition where at least one monitored status is in a failed state.</br>|SNMP|
|{#ENT_NAME}: Hardware serial number|MIB: TIMETRA-CHASSIS-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[sgiCpuUsage.0].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[vm.memory.pused.0].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|
|{#SNMPVALUE}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[tmnxHwTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`|WARNING|
|{#SNMPVALUE}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[tmnxHwTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|HIGH|
|{#SNMPVALUE}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[tmnxHwTemperature.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|AVERAGE|
|#{#SNMPINDEX}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[tmnxChassisFanOperStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE|
|#{#SNMPINDEX}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[tmnxChassisPowerSupply1Status.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE|
|#{#SNMPINDEX}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[tmnxChassisPowerSupply2Status.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE|
|{#ENT_NAME}: Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber[tmnxHwSerialNumber.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[tmnxHwSerialNumber.{#SNMPINDEX}].strlen()}>0`|INFO|


