
# Template Net HP Comware HH3C SNMPv2

## Overview

For Zabbix version: 4.2  
http://certifiedgeek.weebly.com/blog/hp-comware-snmp-mib-for-cpu-memory-and-temperature
http://www.h3c.com.hk/products___solutions/technology/system_management/configuration_example/200912/656451_57_0.htm

This template was tested on:

- HP 1910-48, version 1910-48 Switch Software Version 5.20.99, Release 1116 Copyright(c)2010-2016 Hewlett Packard Enterprise Development LP
- HP A5500-24G-4SFP, version HP Comware Platform Software, Software Version 5.20.99 Release 5501P21 HP A5500-24G-4SFP

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS:"fanError"}|-|41|
|{$FAN_CRIT_STATUS:"hardwareFaulty"}|-|91|
|{$MEMORY_UTIL_MAX}|-|90|
|{$PSU_CRIT_STATUS:"hardwareFaulty"}|-|91|
|{$PSU_CRIT_STATUS:"psuError"}|-|51|
|{$PSU_CRIT_STATUS:"rpsError"}|-|61|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN}|-|50|

## Template links

|Name|
|----|
|Template Module EtherLike-MIB SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Module Discovery|Filter limits results to 'Module level1' or Fabric Modules|SNMP|
|Temperature Discovery|Discovering modules temperature (same filter as in Module Discovery) plus and temperature sensors|SNMP|
|FAN Discovery|Discovering all entities of PhysicalClass - 7: fan(7)|SNMP|
|PSU Discovery|Discovering all entities of PhysicalClass - 6: powerSupply(6)|SNMP|
|Entity Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|{#MODULE_NAME}: CPU utilization|MIB: HH3C-ENTITY-EXT-MIB</br>The CPU usage for this entity. Generally, the CPU usage</br>will calculate the overall CPU usage on the entity, and it</br>is not sensible with the number of CPU on the entity</br>|SNMP|
|{#MODULE_NAME}: Memory utilization|MIB: HH3C-ENTITY-EXT-MIB</br>The memory usage for the entity. This object indicates what</br>percent of memory are used.</br>|SNMP|
|{#SNMPVALUE}: Temperature|MIB: HH3C-ENTITY-EXT-MIB</br>The temperature for the {#SNMPVALUE}.|SNMP|
|{#ENT_NAME}: Fan status|MIB: HH3C-ENTITY-EXT-MIB</br>Indicate the error state of this entity object.</br>fanError(41) means that the fan stops working.|SNMP|
|{#ENT_NAME}: Power supply status|MIB: HH3C-ENTITY-EXT-MIB</br>Indicate the error state of this entity object.</br>psuError(51) means that the Power Supply Unit is in the state of fault.</br>rpsError(61) means the Redundant Power Supply is in the state of fault.</br>|SNMP|
|{#ENT_NAME}: Hardware model name|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Hardware serial number|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Firmware version|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Hardware version(revision)|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Operating system|MIB: ENTITY-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|{#MODULE_NAME}: High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[hh3cEntityExtCpuUsage.{#SNMPINDEX}].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|{#MODULE_NAME}: High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[hh3cEntityExtMemUsage.{#SNMPINDEX}].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|
|{#SNMPVALUE}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[hh3cEntityExtTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`|WARNING|
|{#SNMPVALUE}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[hh3cEntityExtTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|HIGH|
|{#SNMPVALUE}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[hh3cEntityExtTemperature.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|AVERAGE|
|{#ENT_NAME}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[hh3cEntityExtErrorStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"fanError"},eq)}=1 or {TEMPLATE_NAME:sensor.fan.status[hh3cEntityExtErrorStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"hardwareFaulty"},eq)}=1`|AVERAGE|
|{#ENT_NAME}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[hh3cEntityExtErrorStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS:"psuError"},eq)}=1 or {TEMPLATE_NAME:sensor.psu.status[hh3cEntityExtErrorStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS:"rpsError"},eq)}=1 or {TEMPLATE_NAME:sensor.psu.status[hh3cEntityExtErrorStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS:"hardwareFaulty"},eq)}=1`|AVERAGE|
|{#ENT_NAME}: Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].strlen()}>0`|INFO|
|{#ENT_NAME}: Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware[entPhysicalFirmwareRev.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.firmware[entPhysicalFirmwareRev.{#SNMPINDEX}].strlen()}>0`|INFO|

## References

