
# Template OS Linux Prom

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
|{$NODE_EXPORTER_PORT}|-|9100|
|{$STORAGE_UTIL_CRIT}|-|90|
|{$STORAGE_UTIL_WARN}|-|80|
|{$SWAP_PFREE_WARN}|-|50|


## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|CPU discovery|-|DEPENDENT|
|Mounted filesystem discovery|Discovery of file systems of different types as defined in global regular expression "File systems for discovery".|DEPENDENT|
|Block devices discovery|-|DEPENDENT|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Get node_exporter metrics|-|HTTP_AGENT|
|Load average (1m avg)|-|DEPENDENT|
|Load average (5m avg)|-|DEPENDENT|
|Load average (15m avg)|-|DEPENDENT|
|Number of CPUs|-|DEPENDENT|
|Interrupts per second|-|DEPENDENT|
|Context switches per second|-|DEPENDENT|
|Total memory|Total memory in Bytes|DEPENDENT|
|Available memory|Available memory, in Linux, available = free + buffers + cache. On other platforms calculation may vary. See also: https://www.zabbix.com/documentation/current/manual/appendix/items/vm.memory.size_params|DEPENDENT|
|Total swap space|-|DEPENDENT|
|Free swap space|-|DEPENDENT|
|Free swap space in %|-|CALCULATED|
|#{#CPUNUM}: CPU utilization|CPU utilization in %|DEPENDENT|
|#{#CPUNUM}: CPU idle time|The time the CPU has spent doing nothing.|DEPENDENT|
|#{#CPUNUM}: CPU system time|The time the CPU has spent running the kernel and its processes.|DEPENDENT|
|#{#CPUNUM}: CPU user time|The time the CPU has spent running users' processes that are not niced.|DEPENDENT|
|#{#CPUNUM}: CPU steal time|The amount of CPU 'stolen' from this virtual machine by the hypervisor for other tasks (such as running another virtual machine).|DEPENDENT|
|#{#CPUNUM}: CPU softirq time|The amount of time the CPU has been servicing software interrupts.|DEPENDENT|
|#{#CPUNUM}: CPU nice time|The time the CPU has spent running users' processes that have been niced.|DEPENDENT|
|#{#CPUNUM}: CPU iowait time|Amount of time the CPU has been waiting for I/O to complete.|DEPENDENT|
|#{#CPUNUM}: CPU interrupt time|The amount of time the CPU has been servicing hardware interrupts.|DEPENDENT|
|#{#CPUNUM}: CPU guest time|Guest  time (time  spent  running  a  virtual  CPU  for  a  guest  operating  system)|DEPENDENT|
|#{#CPUNUM}: CPU guest nice time|Time spent running a niced guest (virtual CPU for guest operating systems under the control of the Linux kernel)|DEPENDENT|
|{#FSNAME}: Free space|-|DEPENDENT|
|{#FSNAME}: Total space|Total space in Bytes|DEPENDENT|
|{#FSNAME}: Used space|Used storage in Bytes|CALCULATED|
|{#FSNAME}: Space utilization|Space utilization in % for {#FSNAME}|CALCULATED|
|{#FSNAME}: Free inodes in %|-|DEPENDENT|
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
|Load average is too high|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:node_exporter.node_load1.avg(5m)}/{Template OS Linux Prom:node_exporter.system.cpu.num.last()}>{$LOAD_AVG_CRIT}`|
|Lack of available memory ({ITEM.VALUE1} of {ITEM.VALUE2})|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:node_exporter.node_memory_memavailable_bytes.last(0)}<{$MEMORY_AVAILABLE_MIN} and {Template OS Linux Prom:node_exporter.node_memory_memtotal_bytes.last(0)}>0`|
|High swap space usage (free: {ITEM.VALUE1}, total: {ITEM.VALUE2})|Last value: {ITEM.LASTVALUE1}.</br>This trigger is ignored, if there is no swap configured|`{TEMPLATE_NAME:node_exporter.system.swap.pfree.last()}<{$SWAP_PFREE_WARN} and {Template OS Linux Prom:node_exporter.node_memory_swaptotal_bytes.last()}>0`|
|{#FSNAME}: Disk space critical status|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#FSNAME}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 5G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].last()}>{$STORAGE_UTIL_CRIT:"{#FSNAME}"} and (({Template OS Linux Prom:node_exporter.vfs.fs.total[{#FSNAME}].last()}-{Template OS Linux Prom:node_exporter.vfs.fs.used[{#FSNAME}].last()})<5G or {TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].timeleft(1h,,100)}<1d)`|
|{#FSNAME}: Disk space warning|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#FSNAME}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 10G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].last()}>{$STORAGE_UTIL_WARN:"{#FSNAME}"} and (({Template OS Linux Prom:node_exporter.vfs.fs.total[{#FSNAME}].last()}-{Template OS Linux Prom:node_exporter.vfs.fs.used[{#FSNAME}].last()})<10G or {TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].timeleft(1h,,100)}<1d)`|
|{#FSNAME}: Free inodes is critically low, below {$INODE_PFREE_CRIT:"{#FSNAME}"}%|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:node_exporter.vfs.fs.inode.pfree[{#FSNAME}].last()}<{$INODE_PFREE_CRIT:"{#FSNAME}"}`|
|{#FSNAME}: Free inodes is below {$INODE_PFREE_WARN:"{#FSNAME}"}%|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:node_exporter.vfs.fs.inode.pfree[{#FSNAME}].last()}<{$INODE_PFREE_WARN:"{#FSNAME}"}`|

## References

