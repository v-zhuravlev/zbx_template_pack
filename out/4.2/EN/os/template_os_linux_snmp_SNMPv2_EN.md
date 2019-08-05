
# Template OS Linux SNMPv2

## Overview

For Zabbix version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$INODE_PFREE_CRIT}|-|10|
|{$INODE_PFREE_WARN}|-|20|
|{$MEMORY_AVAILABLE_MIN}|-|20M|
|{$STORAGE_UTIL_CRIT}|-|90|
|{$STORAGE_UTIL_WARN}|-|80|
|{$SWAP_PFREE_WARN}|-|50|

## Template links

|Name|
|----|
|Template Module EtherLike-MIB SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Block devices discovery|-|SNMP|
|CPU discovery|This discovery will create set of per core CPU metrics from UCD-SNMP-MIB, using {#CPUNUM} in preprocessing. That's the only reason why LLD is used.|DEPENDENT|
|Filesystems discovery|HOST-RESOURCES-MIB::hrStorage discovery with storage filter|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Load average (1m avg)|MIB: UCD-SNMP-MIB</br>|SNMP|
|Load average (5m avg)|MIB: UCD-SNMP-MIB</br>|SNMP|
|Load average (15m avg)|MIB: UCD-SNMP-MIB</br>|SNMP|
|Number of CPUs|MIB: HOST-RESOURCES-MIB</br>Count the number of CPU cores by counting number of cores discovered in hrProcessorTable using LLD|SNMP|
|Interrupts per second|-|SNMP|
|Context switches per second|-|SNMP|
|Free memory|MIB: UCD-SNMP-MIB</br>|SNMP|
|Memory (buffers)|MIB: UCD-SNMP-MIB</br>Memory used by kernel buffers (Buffers in /proc/meminfo)|SNMP|
|Memory (cached)|MIB: UCD-SNMP-MIB</br>Memory used by the page cache and slabs (Cached and Slab in /proc/meminfo)|SNMP|
|Total memory|MIB: UCD-SNMP-MIB</br>Total memory in Bytes|SNMP|
|Available memory|Available memory, in Linux, available = free + buffers + cache. On other platforms calculation may vary. See also: https://www.zabbix.com/documentation/current/manual/appendix/items/vm.memory.size_params|CALCULATED|
|Total swap space|MIB: UCD-SNMP-MIB</br>The total amount of swap space configured for this host.|SNMP|
|Free swap space|MIB: UCD-SNMP-MIB</br>The amount of swap space currently unused or available.|SNMP|
|Free swap space in %|-|CALCULATED|
|{#DEVNAME}: Disk read rate|MIB: UCD-DISKIO-MIB</br>The number of read accesses from this device since boot.|SNMP|
|{#DEVNAME}: Disk write rate|MIB: UCD-DISKIO-MIB</br>The number of write accesses from this device since boot.|SNMP|
|{#DEVNAME}: Disk utilization|MIB: UCD-DISKIO-MIB</br>The 1 minute average load of disk (%)|SNMP|
|CPU idle time|MIB: UCD-SNMP-MIB</br>The time the CPU has spent doing nothing.|SNMP|
|CPU system time|MIB: UCD-SNMP-MIB</br>The time the CPU has spent running the kernel and its processes.|SNMP|
|CPU user time|MIB: UCD-SNMP-MIB</br>The time the CPU has spent running users' processes that are not niced.|SNMP|
|CPU steal time|MIB: UCD-SNMP-MIB</br>The amount of CPU 'stolen' from this virtual machine by the hypervisor for other tasks (such as running another virtual machine).|SNMP|
|CPU softirq time|MIB: UCD-SNMP-MIB</br>The amount of time the CPU has been servicing software interrupts.|SNMP|
|CPU nice time|MIB: UCD-SNMP-MIB</br>The time the CPU has spent running users' processes that have been niced.|SNMP|
|CPU iowait time|MIB: UCD-SNMP-MIB</br>Amount of time the CPU has been waiting for I/O to complete.|SNMP|
|CPU interrupt time|MIB: UCD-SNMP-MIB</br>The amount of time the CPU has been servicing hardware interrupts.|SNMP|
|CPU guest time|MIB: UCD-SNMP-MIB</br>Guest  time (time  spent  running  a  virtual  CPU  for  a  guest  operating  system)|SNMP|
|CPU guest nice time|MIB: UCD-SNMP-MIB</br>Time spent running a niced guest (virtual CPU for guest operating systems under the control of the Linux kernel)|SNMP|
|{#STORAGE_DESCR}: Storage units|MIB: HOST-RESOURCES-MIB</br>The size, in bytes, of the data objects allocated from this pool.</br>If this entry is monitoring sectors, blocks, buffers, or packets, for example,</br>this number will commonly be greater than one.  Otherwise this number will typically be one.|SNMP|
|{#STORAGE_DESCR}: Used storage in units|MIB: HOST-RESOURCES-MIB</br>The amount of the storage represented by this entry that is allocated, in units of hrStorageAllocationUnits.|SNMP|
|{#STORAGE_DESCR}: Total space in units|MIB: HOST-RESOURCES-MIB</br>The size of the storage represented by this entry, in units of hrStorageAllocationUnits.</br>This object is writable to allow remote configuration of the size of the storage area in those cases where such an operation makes sense and is possible on the underlying system.</br>For example, the amount of main storage allocated to a buffer pool might be modified or the amount of disk space allocated to virtual storage might be modified.|SNMP|
|{#STORAGE_DESCR}: Used space|Used storage in Bytes|CALCULATED|
|{#STORAGE_DESCR}: Total space|Total space in Bytes|CALCULATED|
|{#STORAGE_DESCR}: Space utilization|Space utilization in % for {#STORAGE_DESCR}|CALCULATED|
|{#STORAGE_DESCR}: Free inodes in %|MIB: UCD-SNMP-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|Load average is too high|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.load.avg1[laLoad.1].avg(5m)}/{Template OS Linux SNMPv2:snmp.system.cpu.num.last()}>{$LOAD_AVG_CRIT}`|AVERAGE|
|Lack of available memory ({ITEM.VALUE1} of {ITEM.VALUE2})|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:snmp.vm.memory.available.last(0)}<{$MEMORY_AVAILABLE_MIN} and {Template OS Linux SNMPv2:vm.memory.total[memTotalReal.0].last(0)}>0`|AVERAGE|
|High swap space usage (free: {ITEM.VALUE1}, total: {ITEM.VALUE2})|Last value: {ITEM.LASTVALUE1}.</br>This trigger is ignored, if there is no swap configured|`{TEMPLATE_NAME:snmp.system.swap.pfree.last()}<{$SWAP_PFREE_WARN} and {Template OS Linux SNMPv2:system.swap.total[memTotalSwap.0].last()}>0`|WARNING|
|{#STORAGE_DESCR}: Disk space critical status|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#STORAGE_DESCR}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 5G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].last()}>{$STORAGE_UTIL_CRIT:"{#STORAGE_DESCR}"} and (({Template OS Linux SNMPv2:vfs.fs.total[storageTotal.{#SNMPINDEX}].last()}-{Template OS Linux SNMPv2:vfs.fs.used[storageUsed.{#SNMPINDEX}].last()})<5G or {TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].timeleft(1h,,100)}<1d)`|AVERAGE|
|{#STORAGE_DESCR}: Disk space warning|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#STORAGE_DESCR}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 10G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].last()}>{$STORAGE_UTIL_WARN:"{#STORAGE_DESCR}"} and (({Template OS Linux SNMPv2:vfs.fs.total[storageTotal.{#SNMPINDEX}].last()}-{Template OS Linux SNMPv2:vfs.fs.used[storageUsed.{#SNMPINDEX}].last()})<10G or {TEMPLATE_NAME:vfs.fs.pused[storageUsedPercentage.{#SNMPINDEX}].timeleft(1h,,100)}<1d)`|WARNING|
|{#STORAGE_DESCR}: Free inodes is critically low, below {$INODE_PFREE_CRIT:"{#STORAGE_DESCR}"}%|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vfs.fs.inode.pfree[dskPercentNode.{#STORAGE_DESCR}].last()}<{$INODE_PFREE_CRIT:"{#STORAGE_DESCR}"}`|AVERAGE|
|{#STORAGE_DESCR}: Free inodes is below {$INODE_PFREE_WARN:"{#STORAGE_DESCR}"}%|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vfs.fs.inode.pfree[dskPercentNode.{#STORAGE_DESCR}].last()}<{$INODE_PFREE_WARN:"{#STORAGE_DESCR}"}`|WARNING|


