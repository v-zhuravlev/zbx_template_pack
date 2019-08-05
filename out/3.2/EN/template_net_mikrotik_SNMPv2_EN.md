
# Template Net Mikrotik SNMPv2

## Overview

For Zabbix version: 3.2  

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$MEMORY_UTIL_MAX}|-|90|
|{$STORAGE_UTIL_CRIT}|-|90|
|{$STORAGE_UTIL_WARN}|-|80|
|{$TEMP_CRIT:"CPU"}|-|75|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN:"CPU"}|-|70|
|{$TEMP_WARN}|-|50|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|CPU Discovery|HOST-RESOURCES-MIB::hrProcessorTable discovery|SNMP|
|Temperature Discovery CPU|MIKROTIK-MIB::mtxrHlProcessorTemperature</br>Since temperature of CPU is not available on all Mikrotik hardware, this is done to avoid unsupported items.|SNMP|
|Storage Discovery|HOST-RESOURCES-MIB::hrStorage discovery with storage filter|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Used memory|MIB: HOST-RESOURCES-MIB</br>The amount of the storage represented by this entry that is allocated, in units of hrStorageAllocationUnits.|SNMP|
|Total memory|MIB: HOST-RESOURCES-MIB</br>The size of the storage represented by this entry, in</br>units of hrStorageAllocationUnits. This object is</br>writable to allow remote configuration of the size of</br>the storage area in those cases where such an</br>operation makes sense and is possible on the</br>underlying system. For example, the amount of main</br>memory allocated to a buffer pool might be modified or</br>the amount of disk space allocated to virtual memory</br>might be modified.</br>|SNMP|
|Memory utilization|Memory utilization in %|CALCULATED|
|Device: Temperature|MIB: MIKROTIK-MIB</br>(mtxrHlTemperature) Device temperature in Celsius (degrees C). Might be missing in entry models (RB750, RB450G..)</br>Reference: http://wiki.mikrotik.com/wiki/Manual:SNMP|SNMP|
|Operating system|MIB: MIKROTIK-MIB</br>Software version|SNMP|
|Hardware model name|-|SNMP|
|Hardware serial number|MIB: MIKROTIK-MIB</br>RouterBOARD serial number|SNMP|
|Firmware version|MIB: MIKROTIK-MIB</br>Current firmware version|SNMP|
|#{#SNMPINDEX}: CPU utilization|MIB: HOST-RESOURCES-MIB</br>The average, over the last minute, of the percentage of time that this processor was not idle. Implementations may approximate this one minute smoothing period if necessary.|SNMP|
|CPU: Temperature|MIB: MIKROTIK-MIB</br>(mtxrHlProcessorTemperature) Processor temperature in Celsius (degrees C). Might be missing in entry models (RB750, RB450G..)|SNMP|
|Disk-{#SNMPINDEX}: Used space|MIB: HOST-RESOURCES-MIB</br>The amount of the storage represented by this entry that is allocated, in units of hrStorageAllocationUnits.|SNMP|
|Disk-{#SNMPINDEX}: Total space|MIB: HOST-RESOURCES-MIB</br>The size of the storage represented by this entry, in</br>units of hrStorageAllocationUnits. This object is</br>writable to allow remote configuration of the size of</br>the storage area in those cases where such an</br>operation makes sense and is possible on the</br>underlying system. For example, the amount of main</br>memory allocated to a buffer pool might be modified or</br>the amount of disk space allocated to virtual memory</br>might be modified.</br>|SNMP|
|Disk-{#SNMPINDEX}: Space utilization|Space utilization in % for Disk-{#SNMPINDEX}|CALCULATED|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[memoryUsedPercentage.Memory].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|
|Device: Temperature is above warning threshold: >{$TEMP_WARN:"Device"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[mtxrHlTemperature].avg(5m)}>{$TEMP_WARN:"Device"}`|WARNING|
|Device: Temperature is above critical threshold: >{$TEMP_CRIT:"Device"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[mtxrHlTemperature].avg(5m)}>{$TEMP_CRIT:"Device"}`|HIGH|
|Device: Temperature is too low: <{$TEMP_CRIT_LOW:"Device"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[mtxrHlTemperature].avg(5m)}<{$TEMP_CRIT_LOW:"Device"}`|AVERAGE|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|INFO|
|#{#SNMPINDEX}: High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[hrProcessorLoad.{#SNMPINDEX}].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|CPU: Temperature is above warning threshold: >{$TEMP_WARN:"CPU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"CPU"}`|WARNING|
|CPU: Temperature is above critical threshold: >{$TEMP_CRIT:"CPU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"CPU"}`|HIGH|
|CPU: Temperature is too low: <{$TEMP_CRIT_LOW:"CPU"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"CPU"}`|AVERAGE|
|Disk-{#SNMPINDEX}: Disk space critical status|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"Disk-{#SNMPINDEX}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 5G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.pused[hrStorageSize.{#SNMPINDEX}].last()}>{$STORAGE_UTIL_CRIT:"Disk-{#SNMPINDEX}"} and (({Template Net Mikrotik SNMPv2:vfs.fs.total[hrStorageSize.{#SNMPINDEX}].last()}-{Template Net Mikrotik SNMPv2:vfs.fs.used[hrStorageSize.{#SNMPINDEX}].last()})<5G or {TEMPLATE_NAME:vfs.fs.pused[hrStorageSize.{#SNMPINDEX}].timeleft(1h,,100)}<1d)`|AVERAGE|
|Disk-{#SNMPINDEX}: Disk space warning|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"Disk-{#SNMPINDEX}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 10G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.pused[hrStorageSize.{#SNMPINDEX}].last()}>{$STORAGE_UTIL_WARN:"Disk-{#SNMPINDEX}"} and (({Template Net Mikrotik SNMPv2:vfs.fs.total[hrStorageSize.{#SNMPINDEX}].last()}-{Template Net Mikrotik SNMPv2:vfs.fs.used[hrStorageSize.{#SNMPINDEX}].last()})<10G or {TEMPLATE_NAME:vfs.fs.pused[hrStorageSize.{#SNMPINDEX}].timeleft(1h,,100)}<1d)`|WARNING|

## References

