
# Template Net Extreme EXOS SNMPv2

## Overview

For Zabbix version: 3.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS}|-|2|
|{$MEMORY_UTIL_MAX}|-|90|
|{$PSU_CRIT_STATUS}|-|3|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT_STATUS}|-|1|
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
|Memory Discovery|-|SNMP|
|PSU Discovery|Table of status of all power supplies in the system.|SNMP|
|FAN Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|CPU utilization|MIB: EXTREME-SOFTWARE-MONITOR-MIB</br>Total CPU utlization (percentage) as of last sampling.|SNMP|
|Device: Temperature|MIB: EXTREME-SYSTEM-MIB</br>Temperature readings of testpoint: Device</br>Reference: https://gtacknowledge.extremenetworks.com/articles/Q_A/Does-EXOS-support-temperature-polling-via-SNMP-on-all-nodes-in-a-stack|SNMP|
|Device: Temperature status|MIB: EXTREME-SYSTEM-MIB</br>Temperature status of testpoint: Device|SNMP|
|Hardware model name|MIB: ENTITY-MIB</br>|SNMP|
|Hardware serial number|MIB: ENTITY-MIB</br>|SNMP|
|Firmware version|MIB: ENTITY-MIB</br>|SNMP|
|Hardware version(revision)|MIB: ENTITY-MIB</br>|SNMP|
|Operating system|MIB: EXTREME-SYSTEM-MIB</br>The software revision of the primary image stored in this device.</br>This string will have a zero length if the revision is unknown, invalid or not present.</br>This will also be reported in RMON2 probeSoftwareRev if this is the software image currently running in the device.</br>|SNMP|
|#{#SNMPVALUE}: Free memory|MIB: EXTREME-SOFTWARE-MONITOR-MIB</br>Total amount of free memory in Kbytes in the system.|SNMP|
|#{#SNMPVALUE}: Total memory|MIB: EXTREME-SOFTWARE-MONITOR-MIB</br>Total amount of DRAM in Kbytes in the system.|SNMP|
|#{#SNMPVALUE}: Memory utilization|Memory utilization in %|CALCULATED|
|PSU {#SNMPVALUE}: Power supply status|MIB: EXTREME-SYSTEM-MIB</br>Status of the power supply {#SNMPVALUE}|SNMP|
|Fan {#SNMPVALUE}: Fan status|MIB: EXTREME-SYSTEM-MIB</br>Operational status of a cooling fan.|SNMP|
|Fan {#SNMPVALUE}: Fan speed|MIB: EXTREME-SYSTEM-MIB</br>The speed (RPM) of a cooling fan in the fantray {#SNMPVALUE}|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[extremeCpuMonitorTotalUtilization.0].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|Device: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[extremeCurrentTemperature.0].avg(5m)}>{$TEMP_WARN:""}`|WARNING|
|Device: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[extremeCurrentTemperature.0].avg(5m)}>{$TEMP_CRIT:""} or {Template Net Extreme EXOS SNMPv2:sensor.temp.status[extremeOverTemperatureAlarm.0].last(0)}={$TEMP_CRIT_STATUS}`|HIGH|
|Device: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[extremeCurrentTemperature.0].avg(5m)}<{$TEMP_CRIT_LOW:""}`|AVERAGE|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|INFO|
|#{#SNMPVALUE}: High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[{#SNMPVALUE}].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|
|PSU {#SNMPVALUE}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[extremePowerSupplyStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE|
|Fan {#SNMPVALUE}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[extremeFanOperational.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE|

## References

