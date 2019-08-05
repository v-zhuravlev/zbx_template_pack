
# Template Net Mellanox SNMPv2

## Overview

For Zabbix version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$FAN_CRIT_STATUS}|-|3|
|{$PSU_CRIT_STATUS}|-|2|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN_STATUS}|-|3|
|{$TEMP_WARN}|-|50|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|
|Template Module HOST-RESOURCES-MIB SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Temperature Discovery|ENTITY-SENSORS-MIB::EntitySensorDataType discovery with celsius filter|SNMP|
|Fan Discovery|ENTITY-SENSORS-MIB::EntitySensorDataType discovery with rpm filter|SNMP|
|Entity Discovery|-|SNMP|
|PSU Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|{#SENSOR_INFO}: Temperature|MIB: ENTITY-SENSORS-MIB</br>The most recent measurement obtained by the agent for this sensor.</br>To correctly interpret the value of this object, the associated entPhySensorType,</br>entPhySensorScale, and entPhySensorPrecision objects must also be examined.|SNMP|
|{#SENSOR_INFO}: Temperature status|MIB: ENTITY-SENSORS-MIB</br>The operational status of the sensor {#SENSOR_INFO}|SNMP|
|{#SENSOR_INFO}: Fan speed|MIB: ENTITY-SENSORS-MIB</br>The most recent measurement obtained by the agent for this sensor.</br>To correctly interpret the value of this object, the associated entPhySensorType,</br>entPhySensorScale, and entPhySensorPrecision objects must also be examined.|SNMP|
|{#SENSOR_INFO}: Fan status|MIB: ENTITY-SENSORS-MIB</br>The operational status of the sensor {#SENSOR_INFO}|SNMP|
|{#ENT_NAME}: Hardware model name|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Hardware serial number|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Power supply status|MIB: ENTITY-STATE-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|{#SENSOR_INFO}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""} or {Template Net Mellanox SNMPv2:sensor.temp.status[entPhySensorOperStatus.{#SNMPINDEX}].last(0)}={$TEMP_WARN_STATUS}`|WARNING|
|{#SENSOR_INFO}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|HIGH|
|{#SENSOR_INFO}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|AVERAGE|
|{#SENSOR_INFO}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[entPhySensorOperStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE|
|{#ENT_NAME}: Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].strlen()}>0`|INFO|
|{#ENT_NAME}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[entStateOper.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE|


