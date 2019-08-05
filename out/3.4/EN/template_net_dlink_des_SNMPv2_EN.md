
# Template Net D-Link DES_DGS Switch SNMPv2

## Overview

For Zabbix version: 3.4  

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS}|-|2|
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
|Memory Discovery|-|SNMP|
|Temperature Discovery|-|SNMP|
|PSU Discovery|swPowerID of EQUIPMENT-MIB::swPowerTable|SNMP|
|FAN Discovery|swFanID of EQUIPMENT-MIB::swFanTable|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|CPU utilization|MIB: DLINK-AGENT-MIB</br>The unit of time is 1 minute. The value will be between 0% (idle) and 100%(very busy).|SNMP|
|Hardware model name|MIB: SNMPv2-MIB</br>A textual description of the entity.  This value should</br>include the full name and version identification of the system's hardware type, software operating-system, and</br>networking software.|SNMP|
|Hardware serial number|MIB: DLINK-AGENT-MIB</br>A text string containing the serial number of this device.|SNMP|
|Firmware version|MIB: ENTITY-MIB</br>|SNMP|
|Hardware version(revision)|MIB: ENTITY-MIB</br>|SNMP|
|#{#SNMPVALUE}: Memory utilization|MIB: DLINK-AGENT-MIB</br>The percentage of used DRAM memory of the total DRAM memory available.The value will be between 0%(idle) and 100%(very busy)|SNMP|
|#{#SNMPVALUE}: Temperature|MIB: EQUIPMENT-MIB</br>The shelf current temperature.|SNMP|
|#{#SNMPVALUE}: Power supply status|MIB: EQUIPMENT-MIB</br>Indicates the current power status.</br>lowVoltage : The voltage of the power unit is too low.</br>overCurrent: The current of the power unit is too high.</br>working    : The power unit is working normally.</br>fail       : The power unit has failed.</br>connect    : The power unit is connected but not powered on.</br>disconnect : The power unit is not connected.|SNMP|
|#{#SNMPVALUE}: Fan status|MIB: EQUIPMENT-MIB</br>Indicates the current fan status.</br>speed-0     : If the fan function is normal and the fan does not spin            due to the temperature not  reaching the threshold, the status of the fan is speed 0.</br>speed-low   : Fan spin using the lowest speed.</br>speed-middle: Fan spin using the middle speed.</br>speed-high  : Fan spin using the highest speed.|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[agentCPUutilizationIn1min.0].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|INFO|
|#{#SNMPVALUE}: High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[agentDRAMutilization.{#SNMPINDEX}].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|
|#{#SNMPVALUE}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[swTemperatureCurrent.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`|WARNING|
|#{#SNMPVALUE}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[swTemperatureCurrent.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|HIGH|
|#{#SNMPVALUE}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[swTemperatureCurrent.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|AVERAGE|
|#{#SNMPVALUE}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[swPowerStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE|
|#{#SNMPVALUE}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[swFanStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE|

## References

