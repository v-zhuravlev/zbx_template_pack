
# Template Net Dell Force S-Series SNMPv2

## Overview

For Zabbix version: 4.0  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS}|-|2|
|{$FAN_OK_STATUS}|-|1|
|{$MEMORY_UTIL_MAX}|-|90|
|{$PSU_CRIT_STATUS}|-|2|
|{$PSU_OK_STATUS}|-|1|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|65|
|{$TEMP_WARN}|-|55|

## Template links

|Name|
|----|
|Template Module EtherLike-MIB SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|CPU and Memory and Flash Discovery|-|SNMP|
|PSU Discovery|A list of power supply residents in the S-series chassis.|SNMP|
|FAN Discovery|-|SNMP|
|Stack Unit Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|#{#SNMPINDEX}: CPU utilization|MIB: F10-S-SERIES-CHASSIS-MIB</br>CPU utilization in percentage for last 1 minute.|SNMP|
|#{#SNMPINDEX}: Memory utilization|MIB: F10-S-SERIES-CHASSIS-MIB</br>Total memory usage in percentage.|SNMP|
|PSU {#SNMPVALUE}: Power supply status|MIB: F10-S-SERIES-CHASSIS-MIB</br>The status of the power supply {#SNMPVALUE}|SNMP|
|Fan {#SNMPVALUE}: Fan status|MIB: F10-S-SERIES-CHASSIS-MIB</br>The status of the fan tray {#SNMPVALUE}.|SNMP|
|Device {#SNMPVALUE}: Temperature|MIB: F10-S-SERIES-CHASSIS-MIB</br>The temperature of the unit.|SNMP|
|#{#SNMPVALUE}: Hardware model name|MIB: F10-S-SERIES-CHASSIS-MIB</br>The plugged-in model ID for this unit.|SNMP|
|#{#SNMPVALUE}: Hardware serial number|MIB: F10-S-SERIES-CHASSIS-MIB</br>The unit's serial number.|SNMP|
|#{#SNMPVALUE}: Hardware version(revision)|MIB: F10-S-SERIES-CHASSIS-MIB</br>The unit manufacturer's product revision|SNMP|
|#{#SNMPVALUE}: Operating system|MIB: F10-S-SERIES-CHASSIS-MIB</br>Current code version of this unit.|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|#{#SNMPINDEX}: High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[chStackUnitCpuUtil1Min.{#SNMPINDEX}].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|#{#SNMPINDEX}: High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[chStackUnitMemUsageUtil.{#SNMPINDEX}].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|
|PSU {#SNMPVALUE}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[chSysPowerSupplyOperStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE|
|PSU {#SNMPVALUE}: Power supply is not in normal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[chSysPowerSupplyOperStatus.{#SNMPINDEX}].count(#1,{$PSU_OK_STATUS},ne)}=1`|INFO|
|Fan {#SNMPVALUE}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[chSysFanTrayOperStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE|
|Fan {#SNMPVALUE}: Fan is not in normal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[chSysFanTrayOperStatus.{#SNMPINDEX}].count(#1,{$FAN_OK_STATUS},ne)}=1`|INFO|
|Device {#SNMPVALUE}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[chStackUnitTemp.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`|WARNING|
|Device {#SNMPVALUE}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[chStackUnitTemp.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|HIGH|
|Device {#SNMPVALUE}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[chStackUnitTemp.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|AVERAGE|
|#{#SNMPVALUE}: Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber[chStackUnitSerialNumber.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[chStackUnitSerialNumber.{#SNMPINDEX}].strlen()}>0`|INFO|

## References

