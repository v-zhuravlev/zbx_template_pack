
# Template Module HOST-RESOURCES-MIB storage SNMPv1

## Overview

For Zabbix version: 3.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$VFS.FS.PUSED.MAX.CRIT}|<p>-</p>|90|
|{$VFS.FS.PUSED.MAX.WARN}|<p>-</p>|80|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Storage Discovery|<p>HOST-RESOURCES-MIB::hrStorage discovery with storage filter</p>|SNMP|storage.discovery<p>**Filter**:</p>OR <p>- B: {#STORAGE_TYPE} MATCHES_REGEX `.+(4|9)`</p><p>- A: {#STORAGE_TYPE} MATCHES_REGEX `.+(hrStorageFixedDisk|hrStorageFlashMemory)`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Storage|{#SNMPVALUE}: Used space|<p>Used storage in Bytes</p>|CALCULATED|vfs.fs.used[storageUsed.{#SNMPINDEX}]<p>**Expression**:</p>`(last("vfs.fs.units.used[hrStorageUsed.{#SNMPINDEX}]")*last("vfs.fs.units[hrStorageAllocationUnits.{#SNMPINDEX}]"))`|
|Storage|{#SNMPVALUE}: Total space|<p>Total space in Bytes</p>|CALCULATED|vfs.fs.total[storageTotal.{#SNMPINDEX}]<p>**Expression**:</p>`(last("vfs.fs.units.total[hrStorageSize.{#SNMPINDEX}]")*last("vfs.fs.units[hrStorageAllocationUnits.{#SNMPINDEX}]"))`|
|Storage|{#SNMPVALUE}: Space utilization|<p>Space utilization in % for {#SNMPVALUE}</p>|CALCULATED|vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}]<p>**Expression**:</p>`(last("vfs.fs.units.used[hrStorageUsed.{#SNMPINDEX}]")/last("vfs.fs.units.total[hrStorageSize.{#SNMPINDEX}]"))*100`|
|Zabbix_raw_items|{#SNMPVALUE}: Storage units|<p>MIB: HOST-RESOURCES-MIB</p><p>The size, in bytes, of the data objects allocated from this pool.</p><p>If this entry is monitoring sectors, blocks, buffers, or packets, for example,</p><p>this number will commonly be greater than one.  Otherwise this number will typically be one.</p>|SNMP|vfs.fs.units[hrStorageAllocationUnits.{#SNMPINDEX}]|
|Zabbix_raw_items|{#SNMPVALUE}: Used storage in units|<p>MIB: HOST-RESOURCES-MIB</p><p>The amount of the storage represented by this entry that is allocated, in units of hrStorageAllocationUnits.</p>|SNMP|vfs.fs.units.used[hrStorageUsed.{#SNMPINDEX}]|
|Zabbix_raw_items|{#SNMPVALUE}: Total space in units|<p>MIB: HOST-RESOURCES-MIB</p><p>The size of the storage represented by this entry, in units of hrStorageAllocationUnits.</p><p>This object is writable to allow remote configuration of the size of the storage area in those cases where such an operation makes sense and is possible on the underlying system.</p><p>For example, the amount of main storage allocated to a buffer pool might be modified or the amount of disk space allocated to virtual storage might be modified.</p>|SNMP|vfs.fs.units.total[hrStorageSize.{#SNMPINDEX}]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|{#SNMPVALUE}: Disk space is critically low (used > {$VFS.FS.PUSED.MAX.CRIT:"{#SNMPVALUE}"}%)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</p><p>Two conditions should match: First, space utilization should be above {$VFS.FS.PUSED.MAX.CRIT:"{#SNMPVALUE}"}.</p><p> Second condition should be one of the following:</p><p> - The disk free space is less than 5G.</p><p> - The disk will be full in less than 24hours.</p>|`{TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].last()}>{$VFS.FS.PUSED.MAX.CRIT:"{#SNMPVALUE}"} and (({Template Module HOST-RESOURCES-MIB storage SNMPv1:vfs.fs.total[storageTotal.{#SNMPINDEX}].last()}-{Template Module HOST-RESOURCES-MIB storage SNMPv1:vfs.fs.used[storageUsed.{#SNMPINDEX}].last()})<5G or {TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].timeleft(1h,,100)}<1d)`|AVERAGE|<p>Manual close: YES</p>|
|{#SNMPVALUE}: Disk space is low (used > {$VFS.FS.PUSED.MAX.WARN:"{#SNMPVALUE}"}%)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</p><p>Two conditions should match: First, space utilization should be above {$VFS.FS.PUSED.MAX.CRIT:"{#SNMPVALUE}"}.</p><p> Second condition should be one of the following:</p><p> - The disk free space is less than 10G.</p><p> - The disk will be full in less than 24hours.</p>|`{TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].last()}>{$VFS.FS.PUSED.MAX.WARN:"{#SNMPVALUE}"} and (({Template Module HOST-RESOURCES-MIB storage SNMPv1:vfs.fs.total[storageTotal.{#SNMPINDEX}].last()}-{Template Module HOST-RESOURCES-MIB storage SNMPv1:vfs.fs.used[storageUsed.{#SNMPINDEX}].last()})<10G or {TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].timeleft(1h,,100)}<1d)`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- {#SNMPVALUE}: Disk space is critically low (used > {$VFS.FS.PUSED.MAX.CRIT:"{#SNMPVALUE}"}%)</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template Module HOST-RESOURCES-MIB memory SNMPv1

## Overview

For Zabbix version: 3.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$MEMORY.UTIL.MAX}|<p>-</p>|90|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Memory Discovery|<p>HOST-RESOURCES-MIB::hrStorage discovery with memory filter</p>|SNMP|memory.discovery<p>**Filter**:</p>OR <p>- B: {#STORAGE_TYPE} MATCHES_REGEX `.+2$`</p><p>- A: {#STORAGE_TYPE} MATCHES_REGEX `.+hrStorageRam`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Memory|#{#SNMPINDEX}: Used memory|<p>Used memory in Bytes</p>|CALCULATED|vm.memory.used[memoryUsed.{#SNMPINDEX}]<p>**Expression**:</p>`(last("vm.memory.units.used[hrStorageUsed.{#SNMPINDEX}]")*last("vm.memory.units[hrStorageAllocationUnits.{#SNMPINDEX}]"))`|
|Memory|#{#SNMPINDEX}: Total memory|<p>Total memory in Bytes</p>|CALCULATED|vm.memory.total[memoryTotal.{#SNMPINDEX}]<p>**Expression**:</p>`(last("vm.memory.units.total[hrStorageSize.{#SNMPINDEX}]")*last("vm.memory.units[hrStorageAllocationUnits.{#SNMPINDEX}]"))`|
|Memory|#{#SNMPINDEX}: Memory utilization|<p>Memory utilization in %</p>|CALCULATED|vm.memory.pused[memoryUsedPercentage.{#SNMPINDEX}]<p>**Expression**:</p>`(last("vm.memory.used[memoryUsed.{#SNMPINDEX}]")/last("vm.memory.total[memoryTotal.{#SNMPINDEX}]"))*100`|
|Zabbix_raw_items|#{#SNMPINDEX}: Memory units|<p>MIB: HOST-RESOURCES-MIB</p><p>The size, in bytes, of the data objects allocated from this pool.</p><p>If this entry is monitoring sectors, blocks, buffers, or packets, for example,</p><p>this number will commonly be greater than one. Otherwise this number will typically be one.</p>|SNMP|vm.memory.units[hrStorageAllocationUnits.{#SNMPINDEX}]|
|Zabbix_raw_items|#{#SNMPINDEX}: Used memory in units|<p>MIB: HOST-RESOURCES-MIB</p><p>The amount of the storage represented by this entry that is allocated, in units of hrStorageAllocationUnits.</p>|SNMP|vm.memory.units.used[hrStorageUsed.{#SNMPINDEX}]|
|Zabbix_raw_items|#{#SNMPINDEX}: Total memory in units|<p>MIB: HOST-RESOURCES-MIB</p><p>The size of the storage represented by this entry, in units of hrStorageAllocationUnits.</p><p>This object is writable to allow remote configuration of the size of the storage area in those cases where such an operation makes sense and is possible on the underlying system.</p><p>For example, the amount of main memory allocated to a buffer pool might be modified or the amount of disk space allocated to virtual memory might be modified.</p>|SNMP|vm.memory.units.total[hrStorageSize.{#SNMPINDEX}]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|#{#SNMPINDEX}: High memory utilization ( >{$MEMORY.UTIL.MAX}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:vm.memory.pused[memoryUsedPercentage.{#SNMPINDEX}].min(5m)}>{$MEMORY.UTIL.MAX}`|AVERAGE||

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template Module HOST-RESOURCES-MIB CPU SNMPv1

## Overview

For Zabbix version: 3.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU.UTIL.CRIT}|<p>-</p>|90|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|CPU Discovery|<p>HOST-RESOURCES-MIB::hrProcessorTable discovery</p>|SNMP|hrProcessorLoad.discovery|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|#{#SNMPINDEX}: CPU utilization|<p>MIB: HOST-RESOURCES-MIB</p><p>The average, over the last minute, of the percentage of time that this processor was not idle.</p><p>Implementations may approximate this one minute smoothing period if necessary.</p>|SNMP|system.cpu.util[hrProcessorLoad.{#SNMPINDEX}]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|#{#SNMPINDEX}: High CPU utilization (over {$CPU.UTIL.CRIT}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:system.cpu.util[hrProcessorLoad.{#SNMPINDEX}].min(5m)}>{$CPU.UTIL.CRIT}`|WARNING||

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template Module HOST-RESOURCES-MIB SNMPv1

## Overview

For Zabbix version: 3.2  

## Setup


## Zabbix configuration



## Template links

|Name|
|----|
|Template Module HOST-RESOURCES-MIB CPU SNMPv1|
|Template Module HOST-RESOURCES-MIB memory SNMPv1|
|Template Module HOST-RESOURCES-MIB storage SNMPv1|

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|

## Feedback

Please report any issues with the template at https://support.zabbix.com

