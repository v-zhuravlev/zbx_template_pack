
# Template Net Arista SNMPv2

## Overview

For Zabbix version: 3.4  

This template was tested on:

- Arista DCS-7050Q-16, version EOS version 4.12.6

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$FAN_CRIT_STATUS}|<p>-</p>|`3`|
|{$MEMORY.NAME.NOT_MATCHES}|<p>Filter is overriden to ignore RAM(Cache) and RAM(Buffers) memory objects.</p>|`(Buffer|Cache)`|
|{$PSU_CRIT_STATUS}|<p>-</p>|`2`|
|{$TEMP_CRIT_LOW}|<p>-</p>|`5`|
|{$TEMP_CRIT}|<p>-</p>|`60`|
|{$TEMP_WARN_STATUS}|<p>-</p>|`3`|
|{$TEMP_WARN}|<p>-</p>|`50`|
|{$VFS.FS.PUSED.MAX.CRIT}|<p>-</p>|`95`|
|{$VFS.FS.PUSED.MAX.WARN}|<p>-</p>|`90`|

## Template links

|Name|
|----|
|Template Module EtherLike-MIB SNMPv2|
|Template Module Generic SNMPv2|
|Template Module HOST-RESOURCES-MIB SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Temperature discovery|<p>ENTITY-SENSORS-MIB::EntitySensorDataType discovery with celsius filter</p>|SNMP|temp.discovery<p>**Filter**:</p>AND <p>- B: {#SENSOR_TYPE} MATCHES_REGEX `8`</p><p>- B: {#SENSOR_PRECISION} MATCHES_REGEX `1`</p>|
|Fan discovery|<p>ENTITY-SENSORS-MIB::EntitySensorDataType discovery with rpm filter</p>|SNMP|fan.discovery<p>**Filter**:</p>OR <p>- B: {#SNMPVALUE} MATCHES_REGEX `10`</p>|
|Entity discovery|<p>-</p>|SNMP|entity.discovery<p>**Filter**:</p>AND_OR <p>- A: {#ENT_CLASS} MATCHES_REGEX `3`</p>|
|PSU discovery|<p>-</p>|SNMP|psu.discovery<p>**Filter**:</p>AND_OR <p>- A: {#ENT_CLASS} MATCHES_REGEX `6`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Fans|{#SENSOR_INFO}: Скорость вращения вентилятора|<p>MIB: ENTITY-SENSORS-MIB</p><p>The most recent measurement obtained by the agent for this sensor.</p><p>To correctly interpret the value of this object, the associated entPhySensorType,</p><p>entPhySensorScale, and entPhySensorPrecision objects must also be examined.</p>|SNMP|sensor.fan.speed[entPhySensorValue.{#SNMPINDEX}]|
|Fans|{#SENSOR_INFO}: Статус вентилятора|<p>MIB: ENTITY-SENSORS-MIB</p><p>The operational status of the sensor {#SENSOR_INFO}</p>|SNMP|sensor.fan.status[entPhySensorOperStatus.{#SNMPINDEX}]|
|Inventory|{#ENT_NAME}: Модель|<p>MIB: ENTITY-MIB</p>|SNMP|system.hw.model[entPhysicalModelName.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Inventory|{#ENT_NAME}: Серийный номер|<p>MIB: ENTITY-MIB</p>|SNMP|system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Power_supply|{#ENT_NAME}: Статус блока питания|<p>MIB: ENTITY-STATE-MIB</p>|SNMP|sensor.psu.status[entStateOper.{#SNMPINDEX}]|
|Temperature|{#SENSOR_INFO}: Температура|<p>MIB: ENTITY-SENSORS-MIB</p><p>The most recent measurement obtained by the agent for this sensor.</p><p>To correctly interpret the value of this object, the associated entPhySensorType,</p><p>entPhySensorScale, and entPhySensorPrecision objects must also be examined.</p>|SNMP|sensor.temp.value[entPhySensorValue.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- MULTIPLIER: `0.1`</p>|
|Temperature|{#SENSOR_INFO}: Temperature status|<p>MIB: ENTITY-SENSORS-MIB</p><p>The operational status of the sensor {#SENSOR_INFO}</p>|SNMP|sensor.temp.status[entPhySensorOperStatus.{#SNMPINDEX}]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|{#SENSOR_INFO}: Статус вентилятора: сбой|<p>Проверьте вентилятор</p>|`{TEMPLATE_NAME:sensor.fan.status[entPhySensorOperStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE||
|{#ENT_NAME}: Возможно замена устройства (получен новый серийный номер)|<p>Изменился серийный номер устройства. Подтвердите и закройте.</p>|`{TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].strlen()}>0`|INFO|<p>Manual close: YES</p>|
|{#ENT_NAME}: Статус блока питания: авария|<p>Проверьте блок питания</p>|`{TEMPLATE_NAME:sensor.psu.status[entStateOper.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE||
|{#SENSOR_INFO}: Температура выше нормы: >{$TEMP_WARN:""}|<p>This trigger uses temperature sensor values as well as temperature sensor status if available</p>|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""} or {Template Net Arista SNMPv2:sensor.temp.status[entPhySensorOperStatus.{#SNMPINDEX}].last(0)}={$TEMP_WARN_STATUS}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:""}-3`|WARNING|<p>**Depends on**:</p><p>- {#SENSOR_INFO}: Температура очень высокая: >{$TEMP_CRIT:""}</p>|
|{#SENSOR_INFO}: Температура очень высокая: >{$TEMP_CRIT:""}|<p>This trigger uses temperature sensor values as well as temperature sensor status if available</p>|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:""}-3`|HIGH||
|{#SENSOR_INFO}: Температура слишком низкая: <{$TEMP_CRIT_LOW:""}|<p>-</p>|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:""}+3`|AVERAGE||

## Feedback

Please report any issues with the template at https://support.zabbix.com

