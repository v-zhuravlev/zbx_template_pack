
# Template Net Huawei VRP SNMPv2

## Overview

For Zabbix version: 3.4  
Reference: https://www.slideshare.net/Huanetwork/huawei-s5700-naming-conventions-and-port-numbering-conventions
Reference: http://support.huawei.com/enterprise/KnowledgebaseReadAction.action?contentId=KB1000090234

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU.UTIL.CRIT}|<p>-</p>|`90`|
|{$FAN_CRIT_STATUS}|<p>-</p>|`2`|
|{$MEMORY.UTIL.MAX}|<p>-</p>|`90`|
|{$TEMP_CRIT_LOW}|<p>-</p>|`5`|
|{$TEMP_CRIT}|<p>-</p>|`60`|
|{$TEMP_WARN}|<p>-</p>|`50`|

## Template links

|Name|
|----|
|Template Module EtherLike-MIB SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|MPU Discovery|<p>http://support.huawei.com/enterprise/KnowledgebaseReadAction.action?contentId=KB1000090234. Filter limits results to Main Processing Units</p>|SNMP|mpu.discovery<p>**Filter**:</p>AND_OR <p>- A: {#ENT_NAME} MATCHES_REGEX `MPU.*`</p>|
|Entity Discovery|<p>-</p>|SNMP|entity.discovery<p>**Filter**:</p>AND_OR <p>- A: {#ENT_CLASS} MATCHES_REGEX `3`</p>|
|FAN Discovery|<p>-</p>|SNMP|discovery.fans|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|{#ENT_NAME}: Загрузка процессора|<p>MIB: HUAWEI-ENTITY-EXTENT-MIB</p><p>The CPU usage for this entity. Generally, the CPU usage will calculate the overall CPU usage on the entity, and itis not sensible with the number of CPU on the entity.</p><p>Reference: http://support.huawei.com/enterprise/KnowledgebaseReadAction.action?contentId=KB1000090234</p>|SNMP|system.cpu.util[hwEntityCpuUsage.{#SNMPINDEX}]|
|Fans|#{#SNMPVALUE}: Статус вентилятора|<p>MIB: HUAWEI-ENTITY-EXTENT-MIB</p>|SNMP|sensor.fan.status[hwEntityFanState.{#SNMPINDEX}]|
|Inventory|{#ENT_NAME}: Серийный номер|<p>MIB: ENTITY-MIB</p>|SNMP|system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Inventory|{#ENT_NAME}: Версия аппаратной ревизии|<p>MIB: ENTITY-MIB</p>|SNMP|system.hw.version[entPhysicalHardwareRev.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Inventory|{#ENT_NAME}: Operating system|<p>MIB: ENTITY-MIB</p>|SNMP|system.sw.os[entPhysicalSoftwareRev.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Inventory|{#ENT_NAME}: Модель|<p>MIB: ENTITY-MIB</p>|SNMP|system.hw.model[entPhysicalDescr.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Memory|{#ENT_NAME}: Memory utilization|<p>MIB: HUAWEI-ENTITY-EXTENT-MIB</p><p>The memory usage for the entity. This object indicates what percent of memory are used.</p><p>Reference: http://support.huawei.com/enterprise/KnowledgebaseReadAction.action?contentId=KB1000090234</p>|SNMP|vm.memory.util[hwEntityMemUsage.{#SNMPINDEX}]|
|Temperature|{#ENT_NAME}: Температура|<p>MIB: HUAWEI-ENTITY-EXTENT-MIB</p><p>The temperature for the {#SNMPVALUE}.</p>|SNMP|sensor.temp.value[hwEntityTemperature.{#SNMPINDEX}]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|{#ENT_NAME}: Высокая загрузка процессора ( > {$CPU.UTIL.CRIT}% за 5m)|<p>CPU utilization is too high. The system might be slow to respond.</p>|`{TEMPLATE_NAME:system.cpu.util[hwEntityCpuUsage.{#SNMPINDEX}].min(5m)}>{$CPU.UTIL.CRIT}`|WARNING||
|#{#SNMPVALUE}: Статус вентилятора: сбой|<p>Проверьте вентилятор</p>|`{TEMPLATE_NAME:sensor.fan.status[hwEntityFanState.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE||
|{#ENT_NAME}: Возможно замена устройства (получен новый серийный номер)|<p>Изменился серийный номер устройства. Подтвердите и закройте.</p>|`{TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].strlen()}>0`|INFO|<p>Manual close: YES</p>|
|{#ENT_NAME}: Operating system description has changed|<p>Operating system description has changed. Possible reasons that system has been updated or replaced. Ack to close.</p>|`{TEMPLATE_NAME:system.sw.os[entPhysicalSoftwareRev.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.sw.os[entPhysicalSoftwareRev.{#SNMPINDEX}].strlen()}>0`|INFO|<p>Manual close: YES</p>|
|{#ENT_NAME}: Мало свободной памяти ОЗУ ( >{$MEMORY.UTIL.MAX}% for 5m)|<p>The system is running out of free memory.</p>|`{TEMPLATE_NAME:vm.memory.util[hwEntityMemUsage.{#SNMPINDEX}].min(5m)}>{$MEMORY.UTIL.MAX}`|AVERAGE||
|{#ENT_NAME}: Температура выше нормы: >{$TEMP_WARN:""}|<p>This trigger uses temperature sensor values as well as temperature sensor status if available</p>|`{TEMPLATE_NAME:sensor.temp.value[hwEntityTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[hwEntityTemperature.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:""}-3`|WARNING|<p>**Depends on**:</p><p>- {#ENT_NAME}: Температура очень высокая: >{$TEMP_CRIT:""}</p>|
|{#ENT_NAME}: Температура очень высокая: >{$TEMP_CRIT:""}|<p>This trigger uses temperature sensor values as well as temperature sensor status if available</p>|`{TEMPLATE_NAME:sensor.temp.value[hwEntityTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[hwEntityTemperature.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:""}-3`|HIGH||
|{#ENT_NAME}: Температура слишком низкая: <{$TEMP_CRIT_LOW:""}|<p>-</p>|`{TEMPLATE_NAME:sensor.temp.value[hwEntityTemperature.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`<p>Recovery expression:</p>`{TEMPLATE_NAME:sensor.temp.value[hwEntityTemperature.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:""}+3`|AVERAGE||

## Feedback

Please report any issues with the template at https://support.zabbix.com

