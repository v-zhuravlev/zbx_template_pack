
# Template Net Brocade FC SNMPv2

## Overview

For Zabbix version: 4.2  
https://community.brocade.com/dtscp75322/attachments/dtscp75322/fibre/25235/1/FOS_MIB_Reference_v740.pdf

This template was tested on:

- Brocade 6520, version v7.4.1c
- Brocade 300, version v7.0.0c
- Brocade BL 5480, version v6.3.1c

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU.UTIL.CRIT}|<p>-</p>|`90`|
|{$FAN_CRIT_STATUS}|<p>-</p>|`2`|
|{$FAN_OK_STATUS}|<p>-</p>|`4`|
|{$HEALTH_CRIT_STATUS}|<p>-</p>|`4`|
|{$HEALTH_WARN_STATUS:"offline"}|<p>-</p>|`2`|
|{$HEALTH_WARN_STATUS:"testing"}|<p>-</p>|`3`|
|{$MEMORY.UTIL.MAX}|<p>-</p>|`90`|
|{$PSU_CRIT_STATUS}|<p>-</p>|`2`|
|{$PSU_OK_STATUS}|<p>-</p>|`4`|
|{$TEMP_CRIT_LOW}|<p>-</p>|`5`|
|{$TEMP_CRIT}|<p>-</p>|`75`|
|{$TEMP_WARN_STATUS}|<p>-</p>|`5`|
|{$TEMP_WARN}|<p>-</p>|`65`|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Temperature Discovery|<p>-</p>|SNMP|temperature.discovery<p>**Filter**:</p>AND_OR <p>- A: {#SENSOR_TYPE} MATCHES_REGEX `1`</p>|
|PSU Discovery|<p>-</p>|SNMP|psu.discovery<p>**Filter**:</p>AND_OR <p>- A: {#SENSOR_TYPE} MATCHES_REGEX `3`</p>|
|FAN Discovery|<p>-</p>|SNMP|fan.discovery<p>**Filter**:</p>AND_OR <p>- A: {#SENSOR_TYPE} MATCHES_REGEX `2`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|Загрузка процессора|<p>MIB: SW-MIB</p><p>System's CPU usage.</p>|SNMP|system.cpu.util[swCpuUsage.0]|
|Fans|{#SENSOR_INFO}: Статус вентилятора|<p>MIB: SW-MIB</p>|SNMP|sensor.fan.status[swSensorStatus.{#SNMPINDEX}]|
|Fans|{#SENSOR_INFO}: Скорость вращения вентилятора|<p>MIB: SW-MIB</p><p>The current value (reading) of the sensor.</p><p>The value, -2147483648, represents an unknown quantity.</p><p>The fan value will be in RPM(revolution per minute)</p>|SNMP|sensor.fan.speed[swSensorValue.{#SNMPINDEX}]|
|Inventory|Серийный номер|<p>MIB: SW-MIB</p>|SNMP|system.hw.serialnumber<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Inventory|Версия прошивки|<p>MIB: SW-MIB</p>|SNMP|system.hw.firmware<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Memory|Memory utilization|<p>MIB: SW-MIB</p><p>Memory utilization in %</p>|SNMP|vm.memory.util[swMemUsage.0]|
|Power_supply|{#SENSOR_INFO}: Статус блока питания|<p>MIB: SW-MIB</p>|SNMP|sensor.psu.status[swSensorStatus.{#SNMPINDEX}]|
|Status|Общий статус системы|<p>MIB: SW-MIB</p><p>The current operational status of the switch.The states are as follow:</p><p>online(1) means the switch is accessible by an external Fibre Channel port</p><p>offline(2) means the switch is not accessible</p><p>testing(3) means the switch is in a built-in test mode and is not accessible by an external Fibre Channel port</p><p>faulty(4) means the switch is not operational.</p>|SNMP|system.status[swOperStatus.0]|
|Temperature|{#SENSOR_INFO}: Температура|<p>MIB: SW-MIB</p><p>Temperature readings of testpoint: {#SENSOR_INFO}</p>|SNMP|sensor.temp.value[swSensorValue.{#SNMPINDEX}]|
|Temperature|{#SENSOR_INFO}: Temperature status|<p>MIB: SW-MIB</p><p>Temperature status of testpoint: {#SENSOR_INFO}</p>|SNMP|sensor.temp.status[swSensorStatus.{#SNMPINDEX}]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Высокая загрузка процессора ( > {$CPU.UTIL.CRIT}% за 5m)|<p>CPU utilization is too high. The system might be slow to respond.</p>|`{TEMPLATE_NAME:system.cpu.util[swCpuUsage.0].min(5m)}>{$CPU.UTIL.CRIT}`|WARNING||
|{#SENSOR_INFO}: Статус вентилятора: сбой|<p>Проверьте вентилятор</p>|`{TEMPLATE_NAME:sensor.fan.status[swSensorStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE||
|{#SENSOR_INFO}: Статус вентилятора: не норма|<p>Проверьте вентилятор</p>|`{TEMPLATE_NAME:sensor.fan.status[swSensorStatus.{#SNMPINDEX}].count(#1,{$FAN_OK_STATUS},ne)}=1`|INFO|<p>**Depends on**:</p><p>- {#SENSOR_INFO}: Статус вентилятора: сбой</p>|
|Возможно замена устройства (получен новый серийный номер)|<p>Изменился серийный номер устройства. Подтвердите и закройте.</p>|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|<p>Manual close: YES</p>|
|Версия прошивки изменилась|<p>Версия прошивки изменилась. Подтвердите и закройте.</p>|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|INFO|<p>Manual close: YES</p>|
|Мало свободной памяти ОЗУ ( >{$MEMORY.UTIL.MAX}% for 5m)|<p>The system is running out of free memory.</p>|`{TEMPLATE_NAME:vm.memory.util[swMemUsage.0].min(5m)}>{$MEMORY.UTIL.MAX}`|AVERAGE||
|{#SENSOR_INFO}: Статус блока питания: авария|<p>Проверьте блок питания</p>|`{TEMPLATE_NAME:sensor.psu.status[swSensorStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE||
|{#SENSOR_INFO}: Статус блока питания: не норма|<p>Проверьте блок питания</p>|`{TEMPLATE_NAME:sensor.psu.status[swSensorStatus.{#SNMPINDEX}].count(#1,{$PSU_OK_STATUS},ne)}=1`|INFO|<p>**Depends on**:</p><p>- {#SENSOR_INFO}: Статус блока питания: авария</p>|
|Статус системы: авария|<p>Проверьте устройство</p>|`{TEMPLATE_NAME:system.status[swOperStatus.0].count(#1,{$HEALTH_CRIT_STATUS},eq)}=1`|HIGH||
|Статус системы: предупреждение|<p>Проверьте устройство</p>|`{TEMPLATE_NAME:system.status[swOperStatus.0].count(#1,{$HEALTH_WARN_STATUS:"offline"},eq)}=1 or {TEMPLATE_NAME:system.status[swOperStatus.0].count(#1,{$HEALTH_WARN_STATUS:"testing"},eq)}=1`|WARNING|<p>**Depends on**:</p><p>- Статус системы: авария</p>|
|{#SENSOR_INFO}: Температура выше нормы: >{$TEMP_WARN:""}|<p>This trigger uses temperature sensor values as well as temperature sensor status if available</p>|`{TEMPLATE_NAME:sensor.temp.value[swSensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""} or {Template Net Brocade FC SNMPv2:sensor.temp.status[swSensorStatus.{#SNMPINDEX}].last(0)}={$TEMP_WARN_STATUS}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[swSensorValue.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:""}-3`|WARNING|<p>**Depends on**:</p><p>- {#SENSOR_INFO}: Температура очень высокая: >{$TEMP_CRIT:""}</p>|
|{#SENSOR_INFO}: Температура очень высокая: >{$TEMP_CRIT:""}|<p>This trigger uses temperature sensor values as well as temperature sensor status if available</p>|`{TEMPLATE_NAME:sensor.temp.value[swSensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[swSensorValue.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:""}-3`|HIGH||
|{#SENSOR_INFO}: Температура слишком низкая: <{$TEMP_CRIT_LOW:""}|<p>-</p>|`{TEMPLATE_NAME:sensor.temp.value[swSensorValue.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[swSensorValue.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:""}+3`|AVERAGE||

## Feedback

Please report any issues with the template at https://support.zabbix.com

## Known Issues

- Description: no IF-MIB::ifAlias is available
  - Version: v6.3.1c, v7.0.0c,  v7.4.1c
  - Device: all

