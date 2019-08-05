
# Template OS Linux Zabbix agent

## Overview

Minimum version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$INODE_PFREE_CRIT}|-|10|
|{$INODE_PFREE_WARN}|-|20|
|{$LOAD_AVG_CRIT}|-|1.5|
|{$MEMORY_AVAILABLE_MIN}|-|20M|
|{$STORAGE_UTIL_CRIT}|-|90|
|{$STORAGE_UTIL_WARN}|-|80|
|{$SWAP_PFREE_WARN}|-|50|


## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Mounted filesystem discovery|Discovery of file systems of different types as defined in global regular expression "File systems for discovery".|ZABBIX_PASSIVE|
|Block devices discovery|-|DEPENDENT|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Get /proc/diskstats|-|ZABBIX_PASSIVE|
|Load average (1m avg per core)|The load average is calculated as system CPU load divided by number of CPU cores.|ZABBIX_PASSIVE|
|Load average (5m avg per core)|The load average is calculated as system CPU load divided by number of CPU cores.|ZABBIX_PASSIVE|
|Load average (15m avg per core)|The load average is calculated as system CPU load divided by number of CPU cores.|ZABBIX_PASSIVE|
|CPU utilization|CPU utilization in %|DEPENDENT|
|CPU idle time|The time the CPU has spent doing nothing.|ZABBIX_PASSIVE|
|CPU system time|The time the CPU has spent running the kernel and its processes.|ZABBIX_PASSIVE|
|CPU user time|The time the CPU has spent running users' processes that are not niced.|ZABBIX_PASSIVE|
|CPU nice time|The time the CPU has spent running users' processes that have been niced.|ZABBIX_PASSIVE|
|CPU iowait time|Amount of time the CPU has been waiting for I/O to complete.|ZABBIX_PASSIVE|
|CPU steal time|The amount of CPU 'stolen' from this virtual machine by the hypervisor for other tasks (such as running another virtual machine).|ZABBIX_PASSIVE|
|CPU interrupt time|The amount of time the CPU has been servicing hardware interrupts.|ZABBIX_PASSIVE|
|CPU softirq time|The amount of time the CPU has been servicing software interrupts.|ZABBIX_PASSIVE|
|CPU guest time|Guest  time (time  spent  running  a  virtual  CPU  for  a  guest  operating  system)|ZABBIX_PASSIVE|
|CPU guest nice time|Time spent running a niced guest (virtual CPU for guest operating systems under the control of the Linux kernel)|ZABBIX_PASSIVE|
|Context switches per second|-|ZABBIX_PASSIVE|
|Interrupts per second|-|ZABBIX_PASSIVE|
|Total memory|Total memory in Bytes|ZABBIX_PASSIVE|
|Available memory|Available memory, in Linux, available = free + buffers + cache. On other platforms calculation may vary. See also: https://www.zabbix.com/documentation/current/manual/appendix/items/vm.memory.size_params|ZABBIX_PASSIVE|
|Total swap space|-|ZABBIX_PASSIVE|
|Free swap space|-|ZABBIX_PASSIVE|
|Free swap space in %|-|ZABBIX_PASSIVE|
|{#FSNAME}: Used space|Used storage in Bytes|ZABBIX_PASSIVE|
|{#FSNAME}: Free space|-|ZABBIX_PASSIVE|
|{#FSNAME}: Total space|Total space in Bytes|ZABBIX_PASSIVE|
|{#FSNAME}: Space utilization|Space utilization in % for {#FSNAME}|ZABBIX_PASSIVE|
|{#FSNAME}: Free inodes in %|-|ZABBIX_PASSIVE|
|{#DEVNAME}: Disk read rate|r/s. The number (after merges) of read requests completed per second for the device.|DEPENDENT|
|{#DEVNAME}: Disk write rate|w/s. The number (after merges) of write requests completed per second for the device.|DEPENDENT|
|{#DEVNAME}: Disk read time (rate)|Rate of total read time counter. Used in r_await calculation|DEPENDENT|
|{#DEVNAME}: Disk write time (rate)|Rate of total write time counter. Used in w_await calculation|DEPENDENT|
|{#DEVNAME}: Disk read request avg waiting time (r_await)|This formula contains two boolean expressions that evaluates to 1 or 0 in order to set calculated metric to zero and to avoid division by zero exception.|CALCULATED|
|{#DEVNAME}: Disk write request avg waiting time (w_await)|This formula contains two boolean expressions that evaluates to 1 or 0 in order to set calculated metric to zero and to avoid division by zero exception.|CALCULATED|
|{#DEVNAME}: Disk average queue size (avgqu-sz)|-|DEPENDENT|
|{#DEVNAME}: Disk utilization|-|DEPENDENT|


## Triggers

|Name|Description|Expression|
|----|-----------|----|
|Load average is too high|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.load[percpu,avg1].avg(5m)}>{$LOAD_AVG_CRIT}`|
|Lack of available memory ({ITEM.VALUE1} of {ITEM.VALUE2})|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.size[available].last(0)}<{$MEMORY_AVAILABLE_MIN} and {Template OS Linux Zabbix agent:vm.memory.size[total].last(0)}>0`|
|High swap space usage (free: {ITEM.VALUE1}, total: {ITEM.VALUE2})|Last value: {ITEM.LASTVALUE1}.</br>This trigger is ignored, if there is no swap configured|`{TEMPLATE_NAME:system.swap.size[,pfree].last()}<{$SWAP_PFREE_WARN} and {Template OS Linux Zabbix agent:system.swap.size[,total].last()}>0`|
|{#FSNAME}: Disk space critical status|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#FSNAME}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 5G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].last()}>{$STORAGE_UTIL_CRIT:"{#FSNAME}"} and (({Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},total].last()}-{Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},used].last()})<5G or {TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].timeleft(1h,,100)}<1d)`|
|{#FSNAME}: Disk space warning|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#FSNAME}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 10G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].last()}>{$STORAGE_UTIL_WARN:"{#FSNAME}"} and (({Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},total].last()}-{Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},used].last()})<10G or {TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].timeleft(1h,,100)}<1d)`|
|{#FSNAME}: Free inodes is critically low, below {$INODE_PFREE_CRIT:"{#FSNAME}"}%|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vfs.fs.inode[{#FSNAME},pfree].last()}<{$INODE_PFREE_CRIT:"{#FSNAME}"}`|
|{#FSNAME}: Free inodes is below {$INODE_PFREE_WARN:"{#FSNAME}"}%|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vfs.fs.inode[{#FSNAME},pfree].last()}<{$INODE_PFREE_WARN:"{#FSNAME}"}`|

## References

