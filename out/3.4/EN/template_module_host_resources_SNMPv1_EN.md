
# Template Module HOST-RESOURCES-MIB SNMPv1

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$MEMORY_UTIL_MAX}|-|90|
|{$STORAGE_UTIL_CRIT}|-|90|
|{$STORAGE_UTIL_WARN}|-|80|


## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|CPU Discovery|HOST-RESOURCES-MIB::hrProcessorTable discovery|SNMP|
|Memory Discovery|HOST-RESOURCES-MIB::hrStorage discovery with memory filter|SNMP|
|Storage Discovery|HOST-RESOURCES-MIB::hrStorage discovery with storage filter|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|#{#SNMPINDEX}: CPU utilization|MIB: HOST-RESOURCES-MIB</br>The average, over the last minute, of the percentage of time that this processor was not idle.</br>Implementations may approximate this one minute smoothing period if necessary.</br>|SNMP|
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


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|#{#SNMPINDEX}: High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[hrProcessorLoad.{#SNMPINDEX}].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|#{#SNMPINDEX}: High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[memoryUsedPercentage.{#SNMPINDEX}].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|
|{#SNMPVALUE}: Disk space critical status|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#SNMPVALUE}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 5G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].last()}>{$STORAGE_UTIL_CRIT:"{#SNMPVALUE}"} and (({Template Module HOST-RESOURCES-MIB SNMPv1:vfs.fs.total[storageTotal.{#SNMPINDEX}].last()}-{Template Module HOST-RESOURCES-MIB SNMPv1:vfs.fs.used[storageUsed.{#SNMPINDEX}].last()})<5G or {TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].timeleft(1h,,100)}<1d)`|AVERAGE|
|{#SNMPVALUE}: Disk space warning|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#SNMPVALUE}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 10G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].last()}>{$STORAGE_UTIL_WARN:"{#SNMPVALUE}"} and (({Template Module HOST-RESOURCES-MIB SNMPv1:vfs.fs.total[storageTotal.{#SNMPINDEX}].last()}-{Template Module HOST-RESOURCES-MIB SNMPv1:vfs.fs.used[storageUsed.{#SNMPINDEX}].last()})<10G or {TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].timeleft(1h,,100)}<1d)`|WARNING|


