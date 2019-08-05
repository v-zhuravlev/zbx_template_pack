
# Template Server Supermicro Aten SNMPv2

## Overview

For Zabbix version: 3.2  
for BMC ATEN IPMI controllers of Supermicro servers</br>https://www.supermicro.com/solutions/IPMI.cfm

This template was tested on:

- Supermicro X10DRI, version 

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN}|-|50|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Temperature Discovery|Scanning ATEN-IPMI-MIB::sensorTable with filter: not connected temp sensors (Value = 0)|SNMP|
|FAN Discovery|Scanning ATEN-IPMI-MIB::sensorTable with filter: not connected FAN sensors (Value = 0)|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|{#SENSOR_DESCR}: Temperature|MIB: ATEN-IPMI-MIB</br>A textual string containing information about the interface.</br>This string should include the name of the manufacturer, the product name and the version of the interface hardware/software.|SNMP|
|{#SENSOR_DESCR}: Fan speed, %|MIB: ATEN-IPMI-MIB</br>A textual string containing information about the interface.</br>This string should include the name of the manufacturer, the product name and the version of the interface hardware/software.|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|{#SENSOR_DESCR}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[sensorReading.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[sensorReading.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:""}-3`|WARNING|
|{#SENSOR_DESCR}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[sensorReading.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[sensorReading.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:""}-3`|HIGH|
|{#SENSOR_DESCR}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[sensorReading.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[sensorReading.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:""}+3`|AVERAGE|


