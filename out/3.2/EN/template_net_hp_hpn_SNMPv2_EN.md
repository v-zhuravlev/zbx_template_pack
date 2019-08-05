
# Template Net HP Enterprise Switch SNMPv2

## Overview

Minimum version: 3.2  
This template was tested on:

- HP ProCurve J4900B Switch 2626, version ProCurve J4900B Switch 2626, revision H.10.31, ROM H.08.02 (/sw/code/build/fish(mkfs))
- HP J9728A 2920-48G Switch, version HP J9728A 2920-48G Switch, revision WB.16.03.0003, ROM WB.16.03 (/ws/swbuildm/rel_tacoma_qaoff/code/build/anm(swbuildm_rel_tacoma_qaoff_rel_tacoma)) (Formerly ProCurve)"

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS:"bad"}|-|2|
|{$FAN_WARN_STATUS:"warning"}|-|3|
|{$MEMORY_UTIL_MAX}|-|90|
|{$PSU_CRIT_STATUS:"bad"}|-|2|
|{$PSU_WARN_STATUS:"warning"}|-|3|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT_STATUS}|-|2|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN_STATUS}|-|3|
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
|Temperature Discovery|ENTITY-SENSORS-MIB::EntitySensorDataType discovery with celsius filter|SNMP|
|Memory Discovery|Discovery of NETSWITCH-MIB::hpLocalMemTable, A table that contains information on all the local memory for each slot.|SNMP|
|FAN Discovery|Discovering all entities of hpicfSensorObjectId that ends with: 11.2.3.7.8.3.2 - fans and are present|SNMP|
|PSU Discovery|Discovering all entities of hpicfSensorObjectId that ends with: 11.2.3.7.8.3.1 - power supplies and are present|SNMP|
|Temp Status Discovery|Discovering all entities of hpicfSensorObjectId that ends with: 11.2.3.7.8.3.3 - over temp status and are present|SNMP|
|Entity Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|CPU utilization|MIB: STATISTICS-MIB</br>The CPU utilization in percent(%).</br>Reference: http://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-c02597344&sp4ts.oid=51079|SNMP|
|Hardware serial number|MIB: SEMI-MIB</br>|SNMP|
|Firmware version|MIB: NETSWITCH-MIB</br>Contains the operating code version number (also known as software or firmware).</br>For example, a software version such as A.08.01 is described as follows:</br>A    the function set available in your router</br>08   the common release number</br>01   updates to the current common release|SNMP|
|{#SENSOR_INFO}: Temperature|MIB: ENTITY-SENSORS-MIB</br>The most recent measurement obtained by the agent for this sensor.</br>To correctly interpret the value of this object, the associated entPhySensorType,</br>entPhySensorScale, and entPhySensorPrecision objects must also be examined.|SNMP|
|#{#SNMPVALUE}: Used memory|MIB: NETSWITCH-MIB</br>The number of currently allocated bytes.|SNMP|
|#{#SNMPVALUE}: Free memory|MIB: NETSWITCH-MIB</br>The number of available (unallocated) bytes.|SNMP|
|#{#SNMPVALUE}: Memory utilization|Memory utilization in %|CALCULATED|
|{#ENT_DESCR}: Fan status|MIB: HP-ICF-CHASSIS</br>Actual status indicated by the sensor: {#ENT_DESCR}|SNMP|
|{#ENT_DESCR}: Power supply status|MIB: HP-ICF-CHASSIS</br>Actual status indicated by the sensor: {#ENT_DESCR}|SNMP|
|{#ENT_DESCR}: Temperature status|MIB: HP-ICF-CHASSIS</br>Actual status indicated by the sensor: {#ENT_DESCR}|SNMP|
|{#ENT_NAME}: Hardware model name|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Hardware version(revision)|MIB: ENTITY-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|
|----|-----------|----|
|High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[hpSwitchCpuStat.0].avg(5m)}>{$CPU_UTIL_MAX}`|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|
|{#SENSOR_INFO}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`|
|{#SENSOR_INFO}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|
|{#SENSOR_INFO}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|
|#{#SNMPVALUE}: High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[vm.memory.pused.{#SNMPINDEX}].avg(5m)}>{$MEMORY_UTIL_MAX}`|
|{#ENT_DESCR}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[hpicfSensorStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"bad"},eq)}=1`|
|{#ENT_DESCR}: Fan is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[hpicfSensorStatus.{#SNMPINDEX}].count(#1,{$FAN_WARN_STATUS:"warning"},eq)}=1`|
|{#ENT_DESCR}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[hpicfSensorStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS:"bad"},eq)}=1`|
|{#ENT_DESCR}: Power supply is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[hpicfSensorStatus.{#SNMPINDEX}].count(#1,{$PSU_WARN_STATUS:"warning"},eq)}=1`|

## References

