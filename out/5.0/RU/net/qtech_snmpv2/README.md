
# Template Net QTech QSW SNMPv2

## Overview

For Zabbix version: 5.0  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU.UTIL.CRIT}|<p>-</p>|`90`|
|{$FAN_CRIT_STATUS}|<p>-</p>|`1`|
|{$MEMORY.UTIL.MAX}|<p>-</p>|`90`|
|{$PSU_CRIT_STATUS}|<p>-</p>|`1`|
|{$TEMP_CRIT_LOW}|<p>-</p>|`5`|
|{$TEMP_CRIT}|<p>-</p>|`75`|
|{$TEMP_WARN}|<p>-</p>|`65`|

## Template links

|Name|
|----|
|Template Module EtherLike-MIB SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|PSU Discovery|<p>-</p>|SNMP|psu.discovery|
|FAN Discovery|<p>-</p>|SNMP|fan.discovery|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|Загрузка процессора|<p>MIB: QTECH-MIB</p><p>Загрузка процессора в %</p>|SNMP|system.cpu.util[switchCpuUsage.0]|
|Fans|{#SNMPINDEX}: Статус вентилятора|<p>MIB: QTECH-MIB</p>|SNMP|sensor.fan.status[sysFanStatus.{#SNMPINDEX}]|
|Inventory|Модель|<p>MIB: ENTITY-MIB</p>|SNMP|system.hw.model<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Inventory|Серийный номер|<p>MIB: ENTITY-MIB</p>|SNMP|system.hw.serialnumber<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Inventory|Версия прошивки|<p>MIB: ENTITY-MIB</p>|SNMP|system.hw.firmware<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Inventory|Версия аппаратной ревизии|<p>MIB: ENTITY-MIB</p>|SNMP|system.hw.version<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Inventory|Operating system|<p>MIB: QTECH-MIB</p>|SNMP|system.sw.os[sysSoftwareVersion.0]<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Memory|Used memory|<p>MIB: QTECH-MIB</p><p>Used memory in Bytes</p>|SNMP|vm.memory.used[switchMemoryBusy.0]|
|Memory|Total memory|<p>MIB: QTECH-MIB</p><p>Total memory in Bytes</p>|SNMP|vm.memory.total[switchMemorySize.0]|
|Memory|Memory utilization|<p>Memory utilization in %</p>|CALCULATED|vm.memory.util[vm.memory.util.0]<p>**Expression**:</p>`last("vm.memory.used[switchMemoryBusy.0]")/last("vm.memory.total[switchMemorySize.0]")*100`|
|Power_supply|{#SNMPINDEX}: Статус блока питания|<p>MIB: QTECH-MIB</p>|SNMP|sensor.psu.status[sysPowerStatus.{#SNMPINDEX}]|
|Temperature|Температура|<p>MIB: QTECH-MIB</p><p>Temperature readings of testpoint: __RESOURCE__</p>|SNMP|sensor.temp.value[switchTemperature.0]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Высокая загрузка процессора ( > {$CPU.UTIL.CRIT}% за 5m)|<p>CPU utilization is too high. The system might be slow to respond.</p>|`{TEMPLATE_NAME:system.cpu.util[switchCpuUsage.0].min(5m)}>{$CPU.UTIL.CRIT}`|WARNING||
|{#SNMPINDEX}: Статус вентилятора: сбой|<p>Проверьте вентилятор</p>|`{TEMPLATE_NAME:sensor.fan.status[sysFanStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE||
|Возможно замена устройства (получен новый серийный номер)|<p>Изменился серийный номер устройства. Подтвердите и закройте.</p>|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|<p>Manual close: YES</p>|
|Версия прошивки изменилась|<p>Версия прошивки изменилась. Подтвердите и закройте.</p>|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|INFO|<p>Manual close: YES</p>|
|Operating system description has changed|<p>Operating system description has changed. Possible reasons that system has been updated or replaced. Ack to close.</p>|`{TEMPLATE_NAME:system.sw.os[sysSoftwareVersion.0].diff()}=1 and {TEMPLATE_NAME:system.sw.os[sysSoftwareVersion.0].strlen()}>0`|INFO|<p>Manual close: YES</p>|
|Мало свободной памяти ОЗУ ( >{$MEMORY.UTIL.MAX}% for 5m)|<p>The system is running out of free memory.</p>|`{TEMPLATE_NAME:vm.memory.util[vm.memory.util.0].min(5m)}>{$MEMORY.UTIL.MAX}`|AVERAGE||
|{#SNMPINDEX}: Статус блока питания: авария|<p>Проверьте блок питания</p>|`{TEMPLATE_NAME:sensor.psu.status[sysPowerStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE||
|Температура выше нормы: >{$TEMP_WARN:""}|<p>This trigger uses temperature sensor values as well as temperature sensor status if available</p>|`{TEMPLATE_NAME:sensor.temp.value[switchTemperature.0].avg(5m)}>{$TEMP_WARN:""}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[switchTemperature.0].max(5m)}<{$TEMP_WARN:""}-3`|WARNING|<p>**Depends on**:</p><p>- Температура очень высокая: >{$TEMP_CRIT:""}</p>|
|Температура очень высокая: >{$TEMP_CRIT:""}|<p>This trigger uses temperature sensor values as well as temperature sensor status if available</p>|`{TEMPLATE_NAME:sensor.temp.value[switchTemperature.0].avg(5m)}>{$TEMP_CRIT:""}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[switchTemperature.0].max(5m)}<{$TEMP_CRIT:""}-3`|HIGH||
|Температура слишком низкая: <{$TEMP_CRIT_LOW:""}|<p>-</p>|`{TEMPLATE_NAME:sensor.temp.value[switchTemperature.0].avg(5m)}<{$TEMP_CRIT_LOW:""}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[switchTemperature.0].min(5m)}>{$TEMP_CRIT_LOW:""}+3`|AVERAGE||

## Feedback

Please report any issues with the template at https://support.zabbix.com

