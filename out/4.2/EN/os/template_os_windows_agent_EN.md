
# Template Module Windows CPU by Zabbix agent

## Overview

For Zabbix version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU.INTERRUPT.CRIT.MAX}|<p>The critical threshold of the % Interrupt Time counter.</p>|`50`|
|{$CPU.PRIV.CRIT.MAX}|<p>The threshold of the % Privileged Time counter.</p>|`30`|
|{$CPU.QUEUE.CRIT.MAX}|<p>The threshold of the Processor Queue Length counter.</p>|`3`|
|{$CPU.UTIL.CRIT}|<p>-</p>|`90`|

## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|CPU utilization|<p>CPU utilization in %</p>|ZABBIX_PASSIVE|system.cpu.util|
|CPU|CPU interrupt time|<p>The Processor Information\% Interrupt Time is the time the processor spends receiving and servicing </p><p>hardware interrupts during sample intervals. This value is an indirect indicator of the activity of </p><p>devices that generate interrupts, such as the system clock, the mouse, disk drivers, data communication </p><p>lines, network interface cards and other peripheral devices. This is an easy way to identify a potential </p><p>hardware failure. This should never be higher than 20%.</p>|ZABBIX_PASSIVE|perf_counter_en["\Processor Information(_total)\% Interrupt Time"]|
|CPU|CPU privileged time|<p>The Processor Information\% Privileged Time counter shows the percent of time that the processor is spent </p><p>executing in Kernel (or Privileged) mode. Privileged mode includes services interrupts inside Interrupt </p><p>Service Routines (ISRs), executing Deferred Procedure Calls (DPCs), Device Driver calls and other kernel-mode </p><p>functions of the Windows® Operating System.</p>|ZABBIX_PASSIVE|perf_counter_en["\Processor Information(_total)\% Privileged Time"]|
|CPU|CPU user time|<p>The Processor Information\% User Time counter shows the percent of time that the processor(s) is spent executing </p><p>in User mode.</p>|ZABBIX_PASSIVE|perf_counter_en["\Processor Information(_total)\% User Time"]|
|CPU|CPU queue length|<p>The Processor Queue Length shows the number of threads that are observed as delayed in the processor Ready Queue </p><p>and are waiting to be executed.</p>|ZABBIX_PASSIVE|perf_counter_en["\System\Processor Queue Length"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|High CPU utilization (over {$CPU.UTIL.CRIT}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:system.cpu.util.min(5m)}>{$CPU.UTIL.CRIT}`|WARNING||
|CPU interrupt time is too high (over {$CPU.INTERRUPT.CRIT.MAX}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>"The CPU Interrupt Time in the last 5 minutes exceeds {$CPU.INTERRUPT.CRIT.MAX}%."</p><p>The Processor Information\% Interrupt Time is the time the processor spends receiving and servicing </p><p>hardware interrupts during sample intervals. This value is an indirect indicator of the activity of </p><p>devices that generate interrupts, such as the system clock, the mouse, disk drivers, data communication </p><p>lines, network interface cards and other peripheral devices. This is an easy way to identify a potential </p><p>hardware failure. This should never be higher than 20%.</p>|`{TEMPLATE_NAME:perf_counter_en["\Processor Information(_total)\% Interrupt Time"].min(5m)}>{$CPU.INTERRUPT.CRIT.MAX}`|WARNING|<p>**Depends on**:</p><p>- High CPU utilization (over {$CPU.UTIL.CRIT}% for 5m)</p>|
|CPU privileged time is too high (over {$CPU.PRIV.CRIT.MAX}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The CPU privileged time in the last 5 minutes exceeds {$CPU.PRIV.CRIT.MAX}%.</p>|`{TEMPLATE_NAME:perf_counter_en["\Processor Information(_total)\% Privileged Time"].min(5m)}>{$CPU.PRIV.CRIT.MAX}`|WARNING|<p>**Depends on**:</p><p>- CPU interrupt time is too high (over {$CPU.INTERRUPT.CRIT.MAX}% for 5m)</p><p>- High CPU utilization (over {$CPU.UTIL.CRIT}% for 5m)</p>|
|CPU queue length is too high (over {$CPU.QUEUE.CRIT.MAX}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The CPU Queue Length in the last 5 minutes exceeds {$CPU.QUEUE.CRIT.MAX}%.</p>|`{TEMPLATE_NAME:perf_counter_en["\System\Processor Queue Length"].min(5m)}>{$CPU.QUEUE.CRIT.MAX}`|WARNING|<p>**Depends on**:</p><p>- High CPU utilization (over {$CPU.UTIL.CRIT}% for 5m)</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template Module Windows memory by Zabbix agent

## Overview

For Zabbix version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$MEM.PAGE_SEC.CRIT.MAX}|<p>The warning threshold of the Memory Pages/sec counter.</p>|`1000`|
|{$MEM.PAGE_TABLE_CRIT.MIN}|<p>The warning threshold of the Free System Page Table Entries counter.</p>|`5000`|
|{$MEMORY.UTIL.MAX}|<p>The warning threshold of the Memory util item.</p>|`90`|
|{$SWAP.PFREE.MIN.WARN}|<p>-</p>|`50`|

## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Memory|Used memory|<p>Used memory in Bytes</p>|ZABBIX_PASSIVE|vm.memory.size[used]|
|Memory|Total memory|<p>Total memory in Bytes</p>|ZABBIX_PASSIVE|vm.memory.size[total]|
|Memory|Memory utilization|<p>Memory utilization in %</p>|CALCULATED|vm.memory.util<p>**Expression**:</p>`last("vm.memory.size[used]") / last("vm.memory.size[total]") * 100`|
|Memory|Cache bytes|<p>Cache Bytes is the sum of the Memory\\System Cache Resident Bytes, Memory\\System Driver Resident Bytes, </p><p>Memory\\System Code Resident Bytes, and Memory\\Pool Paged Resident Bytes counters. This counter displays </p><p>the last observed value only; it is not an average.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Cache Bytes"]|
|Memory|Free swap space|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,free]|
|Memory|Free swap space in %|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,pfree]|
|Memory|Total swap space|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,total]|
|Memory|Free system page table entries|<p>This indicates the number of page table entries not currently in use by the system. If the number is less </p><p>than 5,000, there may well be a memory leak or you running out of memory.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Free System Page Table Entries"]|
|Memory|Memory page faults per second|<p>Page Faults/sec is the average number of pages faulted per second. It is measured in number of pages </p><p>faulted per second because only one page is faulted in each fault operation, hence this is also equal </p><p>to the number of page fault operations. This counter includes both hard faults (those that require </p><p>disk access) and soft faults (where the faulted page is found elsewhere in physical memory.) Most </p><p>processors can handle large numbers of soft faults without significant consequence. However, hard faults, </p><p>which require disk access, can cause significant delays.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Page Faults/sec"]|
|Memory|Memory pages per second|<p>This measures the rate at which pages are read from or written to disk to resolve hard page faults. </p><p>If the value is greater than 1,000, as a result of excessive paging, there may be a memory leak.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Pages/sec"]|
|Memory|Memory pool non-paged|<p>This measures the size, in bytes, of the non-paged pool. This is an area of system memory for objects </p><p>that cannot be written to disk but instead must remain in physical memory as long as they are allocated. </p><p>There is a possible memory leak if the value is greater than 175MB (or 100MB with the /3GB switch). </p><p>A typical Event ID 2019 is recorded in the system event log.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Pool Nonpaged Bytes"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|High memory utilization ( >{$MEMORY.UTIL.MAX}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:vm.memory.util.min(5m)}>{$MEMORY.UTIL.MAX}`|AVERAGE||
|High swap space usage ( less than {$SWAP.PFREE.MIN.WARN}% free)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This trigger is ignored, if there is no swap configured</p>|`{TEMPLATE_NAME:system.swap.size[,pfree].min(5m)}<{$SWAP.PFREE.MIN.WARN} and {Template Module Windows memory by Zabbix agent:system.swap.size[,total].last()}>0`|WARNING|<p>**Depends on**:</p><p>- High memory utilization ( >{$MEMORY.UTIL.MAX}% for 5m)</p>|
|Number of free system page table entries is too low (less {$MEM.PAGE_TABLE_CRIT.MIN} for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The Memory Free System Page Table Entries is less than {$MEM.PAGE_TABLE_CRIT.MIN} for 5 minutes. If the number is less than 5,000, there may well be a memory leak.</p>|`{TEMPLATE_NAME:perf_counter_en["\Memory\Free System Page Table Entries"].max(5m)}<{$MEM.PAGE_TABLE_CRIT.MIN}`|WARNING|<p>**Depends on**:</p><p>- High memory utilization ( >{$MEMORY.UTIL.MAX}% for 5m)</p>|
|The Memory Pages/sec is too high (over {$MEM.PAGE_SEC.CRIT.MAX} for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The Memory Pages/sec in the last 5 minutes exceeds {$MEM.PAGE_SEC.CRIT.MAX}. If the value is greater than 1,000, as a result of excessive paging, there may be a memory leak.</p>|`{TEMPLATE_NAME:perf_counter_en["\Memory\Pages/sec"].min(5m)}>{$MEM.PAGE_SEC.CRIT.MAX}`|WARNING|<p>**Depends on**:</p><p>- High memory utilization ( >{$MEMORY.UTIL.MAX}% for 5m)</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template Module Windows filesystems by Zabbix agent

## Overview

For Zabbix version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$VFS.FS.FSDRIVETYPE.MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|`fixed`|
|{$VFS.FS.FSDRIVETYPE.NOT_MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|`^\s$`|
|{$VFS.FS.FSNAME.MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|`.*`|
|{$VFS.FS.FSNAME.NOT_MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|`^(/dev|/sys|/run|/proc|.+/shm$)`|
|{$VFS.FS.FSTYPE.MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|`.*`|
|{$VFS.FS.FSTYPE.NOT_MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|`^\s$`|
|{$VFS.FS.PUSED.MAX.CRIT}|<p>-</p>|`90`|
|{$VFS.FS.PUSED.MAX.WARN}|<p>-</p>|`80`|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Mounted filesystem discovery|<p>Discovery of file systems of different types.</p>|ZABBIX_PASSIVE|vfs.fs.discovery<p>**Filter**:</p>AND <p>- A: {#FSTYPE} MATCHES_REGEX `{$VFS.FS.FSTYPE.MATCHES}`</p><p>- B: {#FSTYPE} NOT_MATCHES_REGEX `{$VFS.FS.FSTYPE.NOT_MATCHES}`</p><p>- C: {#FSNAME} MATCHES_REGEX `{$VFS.FS.FSNAME.MATCHES}`</p><p>- D: {#FSNAME} NOT_MATCHES_REGEX `{$VFS.FS.FSNAME.NOT_MATCHES}`</p><p>- E: {#FSDRIVETYPE} MATCHES_REGEX `{$VFS.FS.FSDRIVETYPE.MATCHES}`</p><p>- F: {#FSDRIVETYPE} NOT_MATCHES_REGEX `{$VFS.FS.FSDRIVETYPE.NOT_MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Filesystems|{#FSNAME}: Used space|<p>Used storage in Bytes</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},used]|
|Filesystems|{#FSNAME}: Total space|<p>Total space in Bytes</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},total]|
|Filesystems|{#FSNAME}: Space utilization|<p>Space utilization in % for {#FSNAME}</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},pused]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|{#FSNAME}: Disk space is critically low (used > {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"}%)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</p><p>Two conditions should match: First, space utilization should be above {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"}.</p><p> Second condition should be one of the following:</p><p> - The disk free space is less than 5G.</p><p> - The disk will be full in less than 24hours.</p>|`{TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].last()}>{$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"} and (({Template Module Windows filesystems by Zabbix agent:vfs.fs.size[{#FSNAME},total].last()}-{Template Module Windows filesystems by Zabbix agent:vfs.fs.size[{#FSNAME},used].last()})<5G or {TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].timeleft(1h,,100)}<1d)`|AVERAGE|<p>Manual close: YES</p>|
|{#FSNAME}: Disk space is low (used > {$VFS.FS.PUSED.MAX.WARN:"{#FSNAME}"}%)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</p><p>Two conditions should match: First, space utilization should be above {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"}.</p><p> Second condition should be one of the following:</p><p> - The disk free space is less than 10G.</p><p> - The disk will be full in less than 24hours.</p>|`{TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].last()}>{$VFS.FS.PUSED.MAX.WARN:"{#FSNAME}"} and (({Template Module Windows filesystems by Zabbix agent:vfs.fs.size[{#FSNAME},total].last()}-{Template Module Windows filesystems by Zabbix agent:vfs.fs.size[{#FSNAME},used].last()})<10G or {TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].timeleft(1h,,100)}<1d)`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- {#FSNAME}: Disk space is critically low (used > {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"}%)</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template Module Windows physical disks by Zabbix agent

## Overview

For Zabbix version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$VFS.DEV.DEVNAME.MATCHES}|<p>-</p>|`.*`|
|{$VFS.DEV.DEVNAME.NOT_MATCHES}|<p>-</p>|`_Total`|
|{$VFS.DEV.UTIL.MAX.WARN}|<p>-</p>|`95`|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Physical disks discovery|<p>-</p>|DEPENDENT|vfs.dev.discovery<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1h`</p><p>**Filter**:</p>AND <p>- A: {#DEVNAME} MATCHES_REGEX `{$VFS.DEV.DEVNAME.MATCHES}`</p><p>- B: {#DEVNAME} NOT_MATCHES_REGEX `{$VFS.DEV.DEVNAME.NOT_MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Storage|{#DEVNAME}: Disk read rate|<p>-</p>|DEPENDENT|vfs.dev.read.rate[DiskReadsPersec.{#DEVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.Name == "{#DEVNAME}")].DiskReadsPersec.first()`</p>|
|Storage|{#DEVNAME}: Disk write rate|<p>-</p>|DEPENDENT|vfs.dev.write.rate[DiskWritesPersec.{#DEVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.Name == "{#DEVNAME}")].DiskWritesPersec.first()`</p>|
|Storage|{#DEVNAME}: Disk average queue size (avgqu-sz)|<p>-</p>|DEPENDENT|vfs.dev.queue_size[CurrentDiskQueueLength.{#DEVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.Name == "{#DEVNAME}")].CurrentDiskQueueLength.first()`</p>|
|Storage|{#DEVNAME}: Disk utilization|<p>-</p>|DEPENDENT|vfs.dev.util[PercentDiskTime.{#DEVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.Name == "{#DEVNAME}")].PercentDiskTime.first()`</p>|
|Zabbix_raw_items|Physical disks WMI get|<p>-</p>|ZABBIX_PASSIVE|wmi.getall[root\cimv2,"select * from win32_perfformatteddata_perfdisk_physicaldisk"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|{#DEVNAME}: Disk is overloaded (util > {$VFS.DEV.UTIL.MAX.WARN}% for 15m)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:vfs.dev.util[PercentDiskTime.{#DEVNAME}].min(15m)}>{$VFS.DEV.UTIL.MAX.WARN}`|WARNING|<p>Manual close: YES</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template Module Windows generic by Zabbix agent

## Overview

For Zabbix version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$SYSTEM.FUZZYTIME.MAX}|<p>-</p>|`60`|

## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|General|System uptime|<p>-</p>|ZABBIX_PASSIVE|system.uptime|
|General|System local time|<p>-</p>|ZABBIX_PASSIVE|system.localtime|
|General|System name|<p>System host name.</p>|ZABBIX_PASSIVE|system.hostname<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1h`</p>|
|General|System description|<p>-</p>|ZABBIX_PASSIVE|system.uname<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|General|Number of logged in users|<p>Number of users who are currently logged</p>|ZABBIX_PASSIVE|system.users.num|
|General|Number of processes|<p>-</p>|ZABBIX_PASSIVE|proc.num[]|
|General|Number of threads|<p>The number of threads used by all running processes.</p>|ZABBIX_PASSIVE|perf_counter_en["\System\Threads"]|
|Inventory|Operating system architecture|<p>-</p>|ZABBIX_PASSIVE|system.sw.arch<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Inventory|Software installed|<p>-</p>|ZABBIX_PASSIVE|system.sw.packages<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Host has been restarted (uptime < 10m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The device uptime is less than 10 minutes.</p>|`{TEMPLATE_NAME:system.uptime.last()}<10m`|WARNING|<p>Manual close: YES</p>|
|Check system time (diff with Zabbix server > {$SYSTEM.FUZZYTIME.MAX}s)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:system.localtime.fuzzytime({$SYSTEM.FUZZYTIME.MAX})}=0`|WARNING|<p>Manual close: YES</p>|
|Systen name has changed (new name: {ITEM.VALUE})|<p>Last value: {ITEM.LASTVALUE1}.</p><p>System name has changed. Ack to close.</p>|`{TEMPLATE_NAME:system.hostname.diff()}=1 and {TEMPLATE_NAME:system.hostname.strlen()}>0`|INFO|<p>Manual close: YES</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template Module Windows network by Zabbix agent

## Overview

For Zabbix version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$NET.IF.IFALIAS.MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`.*`|
|{$NET.IF.IFALIAS.NOT_MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`CHANGE_THIS`|
|{$NET.IF.IFDESCR.MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`.*`|
|{$NET.IF.IFDESCR.NOT_MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`CHANGE_THIS`|
|{$NET.IF.IFNAME.MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`.*`|
|{$NET.IF.IFNAME.NOT_MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`Miniport|Virtual|Teredo|Kernel|Loopback|Bluetooth|HTTPS|6to4|QoS|Layer`|
|{$NET.IF.IFNETENABLED.MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`True`|
|{$NET.IF.IFNETENABLED.NOT_MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`CHANGE_THIS`|
|{$NET.IF.PHYSICALADAPTER.MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`True`|
|{$NET.IF.PHYSICALADAPTER.NOT_MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`CHANGE_THIS`|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Network interfaces discovery|<p>-</p>|DEPENDENT|net.if.discovery<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1h`</p><p>**Filter**:</p>AND <p>- A: {#IFPHYSICALADAPTER} MATCHES_REGEX `{$NET.IF.PHYSICALADAPTER.MATCHES}`</p><p>- B: {#IFPHYSICALADAPTER} NOT_MATCHES_REGEX `{$NET.IF.PHYSICALADAPTER.NOT_MATCHES}`</p><p>- C: {#IFNAME} MATCHES_REGEX `{$NET.IF.IFNAME.MATCHES}`</p><p>- D: {#IFNAME} NOT_MATCHES_REGEX `{$NET.IF.IFNAME.NOT_MATCHES}`</p><p>- E: {#IFDESCR} MATCHES_REGEX `{$NET.IF.IFDESCR.MATCHES}`</p><p>- F: {#IFDESCR} NOT_MATCHES_REGEX `{$NET.IF.IFDESCR.NOT_MATCHES}`</p><p>- G: {#IFALIAS} MATCHES_REGEX `{$NET.IF.IFALIAS.MATCHES}`</p><p>- H: {#IFALIAS} NOT_MATCHES_REGEX `{$NET.IF.IFALIAS.NOT_MATCHES}`</p><p>- I: {#IFNETENABLED} MATCHES_REGEX `{$NET.IF.IFNETENABLED.MATCHES}`</p><p>- J: {#IFNETENABLED} NOT_MATCHES_REGEX `{$NET.IF.IFNETENABLED.NOT_MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Bits received|<p>The total number of octets received on the interface, including framing characters. This object is a 64-bit version of ifInOctets. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.in["{#IFNAME}"]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `8`</p>|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Bits sent|<p>The total number of octets transmitted out of the interface, including framing characters. This object is a 64-bit version of ifOutOctets.Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.out["{#IFNAME}"]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `8`</p>|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Inbound packets discarded|<p>The number of inbound packets which were chosen to be discarded</p><p>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.</p><p>One possible reason for discarding such a packet could be to free up buffer space.</p><p>Discontinuities in the value of this counter can occur at re-initialization of the management system,</p><p>and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.in["{#IFNAME}",dropped]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Outbound packets discarded|<p>The number of outbound packets which were chosen to be discarded</p><p>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.</p><p>One possible reason for discarding such a packet could be to free up buffer space.</p><p>Discontinuities in the value of this counter can occur at re-initialization of the management system,</p><p>and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.out["{#IFNAME}",dropped]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Inbound packets with errors|<p>For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.in["{#IFNAME}",errors]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Outbound packets with errors|<p>For packet-oriented interfaces, the number of outbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of outbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.out["{#IFNAME}",errors]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Speed|<p>An estimate of the interface's current bandwidth in units of 1,000,000 bits per second. If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n-500,000' to`n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. For a sub-layer which has no concept of bandwidth, this object should be zero.</p>|DEPENDENT|net.if.speed["{#IFNAME}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.Name == "{#IFNAME}")].Speed.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Interface type|<p>The type of interface.</p><p>Additional values for ifType are assigned by the Internet Assigned NumbersAuthority (IANA),</p><p>through updating the syntax of the IANAifType textual convention.</p>|DEPENDENT|net.if.type["{#IFNAME}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.Name == "{#IFNAME}")].AdapterTypeId.first()`</p>|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Operational status|<p>The current operational state of the interface.</p><p>- The testing(3) state indicates that no operational packet scan be passed</p><p>- If ifAdminStatus is down(2) then ifOperStatus should be down(2)</p><p>- If ifAdminStatus is changed to up(1) then ifOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic</p><p>- It should change todormant(5) if the interface is waiting for external actions (such as a serial line waiting for an incoming connection)</p><p>- It should remain in the down(2) state if and only if there is a fault that prevents it from going to the up(1) state</p><p>- It should remain in the notPresent(6) state if the interface has missing(typically, hardware) components.</p>|DEPENDENT|net.if.status["{#IFNAME}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.Name == "{#IFNAME}")].NetConnectionStatus.first()`</p>|
|Zabbix_raw_items|Network interfaces WMI get|<p>-</p>|ZABBIX_PASSIVE|wmi.getall[root\cimv2,"select * from win32_networkadapter"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Interface {#IFNAME}({#IFALIAS}): High bandwidth usage ( > {$IF.UTIL.MAX:"{#IFNAME}"}% )|<p>Last value: {ITEM.LASTVALUE1}.</p>|`({TEMPLATE_NAME:net.if.in["{#IFNAME}"].avg(15m)}>({$IF.UTIL.MAX:"{#IFNAME}"}/100)*{Template Module Windows network by Zabbix agent:net.if.speed["{#IFNAME}"].last()} or {Template Module Windows network by Zabbix agent:net.if.out["{#IFNAME}"].avg(15m)}>({$IF.UTIL.MAX:"{#IFNAME}"}/100)*{Template Module Windows network by Zabbix agent:net.if.speed["{#IFNAME}"].last()}) and {Template Module Windows network by Zabbix agent:net.if.speed["{#IFNAME}"].last()}>0`<p>Recovery expression:</p>`{TEMPLATE_NAME:net.if.in["{#IFNAME}"].avg(15m)}<(({$IF.UTIL.MAX:"{#IFNAME}"}-3)/100)*{Template Module Windows network by Zabbix agent:net.if.speed["{#IFNAME}"].last()} and {Template Module Windows network by Zabbix agent:net.if.out["{#IFNAME}"].avg(15m)}<(({$IF.UTIL.MAX:"{#IFNAME}"}-3)/100)*{Template Module Windows network by Zabbix agent:net.if.speed["{#IFNAME}"].last()}`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}({#IFALIAS}): Link down</p>|
|Interface {#IFNAME}({#IFALIAS}): High error rate ( > {$IF.ERRORS.WARN:"{#IFNAME}"} for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Recovers when below 80% of {$IF.ERRORS.WARN:"{#IFNAME}"} threshold</p>|`{TEMPLATE_NAME:net.if.in["{#IFNAME}",errors].min(5m)}>{$IF.ERRORS.WARN:"{#IFNAME}"} or {Template Module Windows network by Zabbix agent:net.if.out["{#IFNAME}",errors].min(5m)}>{$IF.ERRORS.WARN:"{#IFNAME}"}`<p>Recovery expression:</p>`{TEMPLATE_NAME:net.if.in["{#IFNAME}",errors].max(5m)}<{$IF.ERRORS.WARN:"{#IFNAME}"}*0.8 and {Template Module Windows network by Zabbix agent:net.if.out["{#IFNAME}",errors].max(5m)}<{$IF.ERRORS.WARN:"{#IFNAME}"}*0.8`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}({#IFALIAS}): Link down</p>|
|Interface {#IFNAME}({#IFALIAS}): Ethernet has changed to lower speed than it was before|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of autonegotiation issues. Ack to close.</p>|`{TEMPLATE_NAME:net.if.speed["{#IFNAME}"].change()}<0 and {TEMPLATE_NAME:net.if.speed["{#IFNAME}"].last()}>0 and ( {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=6 or {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=7 or {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=11 or {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=62 or {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=69 or {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=117 ) and ({Template Module Windows network by Zabbix agent:net.if.status["{#IFNAME}"].last()}<>2)`<p>Recovery expression:</p>`({TEMPLATE_NAME:net.if.speed["{#IFNAME}"].change()}>0 and {TEMPLATE_NAME:net.if.speed["{#IFNAME}"].prev()}>0) or ({Template Module Windows network by Zabbix agent:net.if.status["{#IFNAME}"].last()}=2)`|INFO|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}({#IFALIAS}): Link down</p>|
|Interface {#IFNAME}({#IFALIAS}): Link down|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This trigger expression works as follows:</p><p>1. Can be triggered if operations status is down.</p><p>2. {$IFCONTROL:"{#IFNAME}"}=1 - user can redefine Context macro to value - 0. That marks this interface as not important. No new trigger will be fired if this interface is down.</p><p>3. {TEMPLATE_NAME:METRIC.diff()}=1) - trigger fires only if operational status was up(1) sometime before. (So, do not fire 'ethernal off' interfaces.)</p><p>WARNING: if closed manually - won't fire again on next poll, because of .diff.</p>|`{$IFCONTROL:"{#IFNAME}"}=1 and ({TEMPLATE_NAME:net.if.status["{#IFNAME}"].last()}=2 and {TEMPLATE_NAME:net.if.status["{#IFNAME}"].diff()}=1)`<p>Recovery expression:</p>`{TEMPLATE_NAME:net.if.status["{#IFNAME}"].last()}<>2`|AVERAGE|<p>Manual close: YES</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template OS Windows by Zabbix agent

## Overview

For Zabbix version: 4.2  
New official Windows template. Requires agent of Zabbix 3.0.14, 3.4.5 and 4.0.0 or newer.


This template was tested on:

- Windows, version 10

## Setup

Install Zabbix agent to Windows OS according to Zabbix documentation.


## Zabbix configuration

No specific Zabbix configuration is required.


## Template links

|Name|
|----|
|Template Module Windows CPU by Zabbix agent|
|Template Module Windows filesystems by Zabbix agent|
|Template Module Windows generic by Zabbix agent|
|Template Module Windows memory by Zabbix agent|
|Template Module Windows network by Zabbix agent|
|Template Module Windows physical disks by Zabbix agent|
|Template Module Zabbix agent|

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|

## Feedback

Please report any issues with the template at https://support.zabbix.com

You can also provide feedback, discuss the template or ask for help with it at
[ZABBIX forums](https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/384765-discussion-thread-for-official-zabbix-template-nginx).
