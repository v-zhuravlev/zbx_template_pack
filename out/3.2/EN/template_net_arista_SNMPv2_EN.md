
# Template Net Arista SNMPv2

## Overview

Minimum version: 3.2  
This template was tested on:

- Arista DCS-7050Q-16, version EOS version 4.12.6

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$FAN_CRIT_STATUS}|-|3|
|{$MEMORY_UTIL_MAX}|-|90|
|{$PSU_CRIT_STATUS}|-|2|
|{$STORAGE_UTIL_CRIT}|-|95|
|{$STORAGE_UTIL_WARN}|-|90|
|{$TEMP_CRIT_LOW}|-|5|
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
|CPU Discovery|-|SNMP|
|Memory Discovery|HOST-RESOURCES-MIB::hrStorage discovery with memory filter and description 'RAM'. Do not discover RAM(Buffers) or RAM(Cache)|SNMP|
|Storage Discovery|HOST-RESOURCES-MIB::hrStorage discovery with storage filter|SNMP|
|Temperature Discovery|ENTITY-SENSORS-MIB::EntitySensorDataType discovery with celsius filter|SNMP|
|Fan Discovery|ENTITY-SENSORS-MIB::EntitySensorDataType discovery with rpm filter|SNMP|
|Entity Discovery|-|SNMP|
|PSU Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|{#DEVICE_DESCR}: CPU utilization|MIB: HOST-RESOURCES-MIB</br>The average, over the last minute, of the percentage of time that this processor was not idle.</br>Implementations may approximate this one minute smoothing period if necessary.|SNMP|
|#{#SNMPINDEX}: Memory units|MIB: HOST-RESOURCES-MIB</br>The size, in bytes, of the data objects allocated from this pool.</br>If this entry is monitoring sectors, blocks, buffers, or packets, for example,</br>this number will commonly be greater than one. Otherwise this number will typically be one.|SNMP|
|#{#SNMPINDEX}: Used memory in units|MIB: HOST-RESOURCES-MIB</br>The amount of the storage represented by this entry that is allocated, in units of hrStorageAllocationUnits.|SNMP|
|#{#SNMPINDEX}: Total memory in units|MIB: HOST-RESOURCES-MIB</br>The size of the storage represented by this entry, in units of hrStorageAllocationUnits.</br>This object is writable to allow remote configuration of the size of the storage area in those cases where such an operation makes sense and is possible on the underlying system.</br>For example, the amount of main memory allocated to a buffer pool might be modified or the amount of disk space allocated to virtual memory might be modified.|SNMP|
|#{#SNMPINDEX}: Used memory|Used memory in Bytes|CALCULATED|
|#{#SNMPINDEX}: Total memory|Total memory in Bytes|CALCULATED|
|#{#SNMPINDEX}: Memory utilization|Memory utilization in %|CALCULATED|
|{#SNMPVALUE}: Storage units|MIB: HOST-RESOURCES-MIB</br>The size, in bytes, of the data objects allocated from this pool.</br>If this entry is monitoring sectors, blocks, buffers, or packets, for example,</br>this number will commonly be greater than one.  Otherwise this number will typically be one.|SNMP|
|{#SNMPVALUE}: Used storage in units|MIB: HOST-RESOURCES-MIB</br>The amount of the storage represented by this entry that is allocated, in units of hrStorageAllocationUnits.|SNMP|
|{#SNMPVALUE}: Total space in units|MIB: HOST-RESOURCES-MIB</br>The size of the storage represented by this entry, in units of hrStorageAllocationUnits.</br>This object is writable to allow remote configuration of the size of the storage area in those cases where such an operation makes sense and is possible on the underlying system.</br>For example, the amount of main storage allocated to a buffer pool might be modified or the amount of disk space allocated to virtual storage might be modified.|SNMP|
|{#SNMPVALUE}: Used space|Used storage in Bytes|CALCULATED|
|{#SNMPVALUE}: Total space|Total space in Bytes|CALCULATED|
|{#SNMPVALUE}: Space utilization|Space utilization in % for {#SNMPVALUE}|CALCULATED|
|{#SENSOR_INFO}: Temperature|MIB: ENTITY-SENSORS-MIB</br>The most recent measurement obtained by the agent for this sensor.</br>To correctly interpret the value of this object, the associated entPhySensorType,</br>entPhySensorScale, and entPhySensorPrecision objects must also be examined.|SNMP|
|{#SENSOR_INFO}: Temperature status|MIB: ENTITY-SENSORS-MIB</br>The operational status of the sensor {#SENSOR_INFO}|SNMP|
|{#SENSOR_INFO}: Fan speed|MIB: ENTITY-SENSORS-MIB</br>The most recent measurement obtained by the agent for this sensor.</br>To correctly interpret the value of this object, the associated entPhySensorType,</br>entPhySensorScale, and entPhySensorPrecision objects must also be examined.|SNMP|
|{#SENSOR_INFO}: Fan status|MIB: ENTITY-SENSORS-MIB</br>The operational status of the sensor {#SENSOR_INFO}|SNMP|
|{#ENT_NAME}: Hardware model name|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Hardware serial number|MIB: ENTITY-MIB</br>|SNMP|
|{#ENT_NAME}: Power supply status|MIB: ENTITY-STATE-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|
|----|-----------|----|
|{#DEVICE_DESCR}: High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[hrProcessorLoad.{#SNMPINDEX}].avg(5m)}>{$CPU_UTIL_MAX}`|
|#{#SNMPINDEX}: High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[memoryUsedPercentage.{#SNMPINDEX}].avg(5m)}>{$MEMORY_UTIL_MAX}`|
|{#SNMPVALUE}: Disk space critical status|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#SNMPVALUE}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 5G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].last()}>{$STORAGE_UTIL_CRIT:"{#SNMPVALUE}"} and (({Template Net Arista SNMPv2:vfs.fs.total[storageTotal.{#SNMPINDEX}].last()}-{Template Net Arista SNMPv2:vfs.fs.used[storageUsed.{#SNMPINDEX}].last()})<5G or {TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].timeleft(1h,,100)}<1d)`|
|{#SNMPVALUE}: Disk space warning|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#SNMPVALUE}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 10G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].last()}>{$STORAGE_UTIL_WARN:"{#SNMPVALUE}"} and (({Template Net Arista SNMPv2:vfs.fs.total[storageTotal.{#SNMPINDEX}].last()}-{Template Net Arista SNMPv2:vfs.fs.used[storageUsed.{#SNMPINDEX}].last()})<10G or {TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].timeleft(1h,,100)}<1d)`|
|{#SENSOR_INFO}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""} or {Template Net Arista SNMPv2:sensor.temp.status[entPhySensorOperStatus.{#SNMPINDEX}].last(0)}={$TEMP_WARN_STATUS}`|
|{#SENSOR_INFO}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|
|{#SENSOR_INFO}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[entPhySensorValue.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|
|{#SENSOR_INFO}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[entPhySensorOperStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|
|{#ENT_NAME}: Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].strlen()}>0`|
|{#ENT_NAME}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[entStateOper.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|

## References

