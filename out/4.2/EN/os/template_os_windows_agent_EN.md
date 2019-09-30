
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
|CPU|CPU interrupt time|<p>The Processor Information\% Interrupt Time is the time the processor spends receiving and servicing </p><p>hardware interrupts during sample intervals. This value is an indirect indicator of the activity of </p><p>devices that generate interrupts, such as the system clock, the mouse, disk drivers, data communication </p><p>lines, network interface cards and other peripheral devices. This is an easy way to identify a potential </p><p>hardware failure. This should never be higher than 20%.</p>|ZABBIX_PASSIVE|perf_counter_en["\Processor Information(_total)\% Interrupt Time"]|
|CPU|CPU privileged time|<p>The Processor Information\% Privileged Time counter shows the percent of time that the processor is spent </p><p>executing in Kernel (or Privileged) mode. Privileged mode includes services interrupts inside Interrupt </p><p>Service Routines (ISRs), executing Deferred Procedure Calls (DPCs), Device Driver calls and other kernel-mode </p><p>functions of the Windows® Operating System.</p>|ZABBIX_PASSIVE|perf_counter_en["\Processor Information(_total)\% Privileged Time"]|
|CPU|CPU user time|<p>The Processor Information\% User Time counter shows the percent of time that the processor(s) is spent executing </p><p>in User mode.</p>|ZABBIX_PASSIVE|perf_counter_en["\Processor Information(_total)\% User Time"]|
|CPU|CPU queue length|<p>The Processor Queue Length shows the number of threads that are observed as delayed in the processor Ready Queue </p><p>and are waiting to be executed.</p>|ZABBIX_PASSIVE|perf_counter_en["\System\Processor Queue Length"]|
|CPU|CPU utilization|<p>CPU utilization in %</p>|ZABBIX_PASSIVE|system.cpu.util|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|CPU Interrupt Time is too high (over {$CPU.INTERRUPT.CRIT.MAX}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>"The CPU Interrupt Time in the last 5 minutes exceeds {$CPU.INTERRUPT.CRIT.MAX}%."</p><p>The Processor Information\% Interrupt Time is the time the processor spends receiving and servicing </p><p>hardware interrupts during sample intervals. This value is an indirect indicator of the activity of </p><p>devices that generate interrupts, such as the system clock, the mouse, disk drivers, data communication </p><p>lines, network interface cards and other peripheral devices. This is an easy way to identify a potential </p><p>hardware failure. This should never be higher than 20%.</p>|`{TEMPLATE_NAME:perf_counter_en["\Processor Information(_total)\% Interrupt Time"].min(5m)}>{$CPU.INTERRUPT.CRIT.MAX}`|HIGH|<p>**Depends on**:</p><p>- High CPU utilization (over {$CPU.UTIL.CRIT}% for 5m)</p>|
|CPU privileged time is too high (over {$CPU.PRIV.CRIT.MAX}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The CPU privileged time in the last 5 minutes exceeds {$CPU.PRIV.CRIT.MAX}%.</p>|`{TEMPLATE_NAME:perf_counter_en["\Processor Information(_total)\% Privileged Time"].min(5m)}>{$CPU.PRIV.CRIT.MAX}`|WARNING|<p>**Depends on**:</p><p>- CPU Interrupt Time is too high (over {$CPU.INTERRUPT.CRIT.MAX}% for 5m)</p><p>- High CPU utilization (over {$CPU.UTIL.CRIT}% for 5m)</p>|
|CPU Queue Length is too high (over {$CPU.QUEUE.CRIT.MAX}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The CPU Queue Length in the last 5 minutes exceeds {$CPU.QUEUE.CRIT.MAX}%.</p>|`{TEMPLATE_NAME:perf_counter_en["\System\Processor Queue Length"].min(5m)}>{$CPU.QUEUE.CRIT.MAX}`|WARNING|<p>**Depends on**:</p><p>- High CPU utilization (over {$CPU.UTIL.CRIT}% for 5m)</p>|
|High CPU utilization (over {$CPU.UTIL.CRIT}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:system.cpu.util.min(5m)}>{$CPU.UTIL.CRIT}`|WARNING||

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

# Template Module Windows inventory by Zabbix agent

## Overview

For Zabbix version: 4.2  

## Setup


## Zabbix configuration



## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|General|System uptime|<p>-</p>|ZABBIX_PASSIVE|system.uptime|
|General|System information|<p>-</p>|ZABBIX_PASSIVE|system.uname|
|General|Number of processes|<p>-</p>|ZABBIX_PASSIVE|proc.num[]|
|General|Number of threads|<p>The number of threads used by all running processes.</p>|ZABBIX_PASSIVE|perf_counter_en["\System\Threads"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Host has been restarted (uptime < 10m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The device uptime is less than 10 minutes.</p>|`{TEMPLATE_NAME:system.uptime.last()}<10m`|WARNING|<p>Manual close: YES</p>|

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
|{$MEM.COMMITED.CRIT.MAX}|<p>The warning threshold of the % Committed Bytes In Use counter.</p>|`80`|
|{$MEM.PAGE_SEC.CRIT.MAX}|<p>The warning threshold of the Memory Pages/sec counter.</p>|`1000`|
|{$MEM.PAGE_TABLE.CRIT.MAX}|<p>The warning threshold of the Free System Page Table Entries counter.</p>|`5000`|
|{$MEMORY.UTIL.MAX}|<p>The warning threshold of the Memory util item.</p>|`90`|
|{$SWAP.PFREE.MIN.WARN}|<p>-</p>|`50`|

## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Memory|Used memory|<p>Used memory in Bytes</p>|ZABBIX_PASSIVE|vm.memory.size[used]|
|Memory|Memory utilization|<p>Memory utilization in %</p>|CALCULATED|vm.memory.util<p>**Expression**:</p>`last("vm.memory.size[used]") / last("vm.memory.size[total]") * 100`|
|Memory|Total memory|<p>Total memory in Bytes</p>|ZABBIX_PASSIVE|vm.memory.size[total]|
|Memory|Free swap space|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,free]|
|Memory|Free swap space in %|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,pfree]|
|Memory|Total swap space|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,total]|
|Memory|Cache bytes|<p>Cache Bytes is the sum of the Memory\\System Cache Resident Bytes, Memory\\System Driver Resident Bytes, </p><p>Memory\\System Code Resident Bytes, and Memory\\Pool Paged Resident Bytes counters. This counter displays </p><p>the last observed value only; it is not an average.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Cache Bytes"]|
|Memory|Committed in use, %|<p>The \Memory\% Committed Bytes In Use counter calculates the ratio of committed bytes (system commit charge) </p><p>to the system commit limit, and the system can perform poorly when the system commit limit is reached. </p><p>Therefore, when % Committed Bytes In Use is greater than 80%, use the \Process(*)\Private Bytes counter </p><p>to identify the processes that are consuming the most committed memory.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\% Committed Bytes In Use"]|
|Memory|Free system page table entries|<p>This indicates the number of page table entries not currently in use by the system. If the number is less </p><p>than 5,000, there may well be a memory leak.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Free System Page Table Entries"]|
|Memory|Page file usage, %|<p>The peak usage of the Page File instance in percent. </p><p>The Paging File performance object consists of counters that monitor the paging file(s) on the computer. </p><p>The paging file is a reserved space on disk that backs up committed physical memory on the computer.</p>|ZABBIX_PASSIVE|perf_counter_en["\Paging File(_total)\% Usage Peak"]|
|Memory|Pages faults per/sec|<p>Page Faults/sec is the average number of pages faulted per second. It is measured in number of pages </p><p>faulted per second because only one page is faulted in each fault operation, hence this is also equal </p><p>to the number of page fault operations. This counter includes both hard faults (those that require </p><p>disk access) and soft faults (where the faulted page is found elsewhere in physical memory.) Most </p><p>processors can handle large numbers of soft faults without significant consequence. However, hard faults, </p><p>which require disk access, can cause significant delays.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Page Faults/sec"]|
|Memory|Pages per/sec|<p>This measures the rate at which pages are read from or written to disk to resolve hard page faults. </p><p>If the value is greater than 1,000, as a result of excessive paging, there may be a memory leak.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Pages/sec"]|
|Memory|Pool non-paged|<p>This measures the size, in bytes, of the non-paged pool. This is an area of system memory for objects </p><p>that cannot be written to disk but instead must remain in physical memory as long as they are allocated. </p><p>There is a possible memory leak if the value is greater than 175MB (or 100MB with the /3GB switch). </p><p>A typical Event ID 2019 is recorded in the system event log.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Pool Nonpaged Bytes"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|High memory utilization ( >{$MEMORY.UTIL.MAX}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:vm.memory.util.min(5m)}>{$MEMORY.UTIL.MAX}`|AVERAGE||
|High swap space usage ( less than {$SWAP.PFREE.MIN.WARN}% free)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This trigger is ignored, if there is no swap configured</p>|`{TEMPLATE_NAME:system.swap.size[,pfree].min(5m)}<{$SWAP.PFREE.MIN.WARN} and {Template Module Windows memory by Zabbix agent:system.swap.size[,total].last()}>0`|WARNING|<p>**Depends on**:</p><p>- High memory utilization ( >{$MEMORY.UTIL.MAX}% for 5m)</p>|
|Memory Committed Bytes is too high (over {$MEM.COMMITED.CRIT.MAX}% for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The Memory\% Committed Bytes in the last 5 minutes exceeds {$MEM.COMMITED.CRIT.MAX}%. If you see this counter remaining over 80% for an extended time, you have a memory leak, or you need to upgrade your RAM.</p>|`{TEMPLATE_NAME:perf_counter_en["\Memory\% Committed Bytes In Use"].min(5m)}>{$MEM.COMMITED.CRIT.MAX}`|HIGH||
|Free System Page Table Entries is too low (less {$MEM.PAGE_TABLE.CRIT.MAX} for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The Memory Free System Page Table Entries is less than {$MEM.PAGE_TABLE.CRIT.MAX} for 5 minutes. If the number is less than 5,000, there may well be a memory leak.</p>|`{TEMPLATE_NAME:perf_counter_en["\Memory\Free System Page Table Entries"].max(5m)}<{$MEM.PAGE_TABLE.CRIT.MAX}`|HIGH||
|The Memory Pages/sec is too high (over {$MEM.PAGE_SEC.CRIT.MAX} for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The Memory Pages/sec in the last 5 minutes exceeds {$MEM.PAGE_SEC.CRIT.MAX}. If the value is greater than 1,000, as a result of excessive paging, there may be a memory leak.</p>|`{TEMPLATE_NAME:perf_counter_en["\Memory\Pages/sec"].min(5m)}>{$MEM.PAGE_SEC.CRIT.MAX}`|HIGH||

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
|{$NET.IFNAME.MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`.*`|
|{$NET.IFNAME.NOT_MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|`Miniport|Virtual|Teredo|Kernel|Loopback|Bluetooth|HTTPS|6to4|QoS|Layer`|
|{$NET.PHYSICALADAPTER.MATCHES}|<p>-</p>|`True`|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Network interface discovery|<p>Discovery of network interfaces as defined in MACRO.</p>|DEPENDENT|net.if.discovery<p>**Filter**:</p>AND <p>- A: {#IFPHYSICALADAPTER} MATCHES_REGEX `{$NET.PHYSICALADAPTER.MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Network_interfaces|Interface {#IFNAME}: Bits received|<p>The total number of octets received on the interface, including framing characters. This object is a 64-bit version of ifInOctets. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.in["{#IFNAME}"]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `8`</p>|
|Network_interfaces|Interface {#IFNAME}: Bits sent|<p>The total number of octets transmitted out of the interface, including framing characters. This object is a 64-bit version of ifOutOctets.Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.out["{#IFNAME}"]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `8`</p>|
|Network_interfaces|Interface {#IFNAME}: Inbound packets discarded|<p>The number of inbound packets which were chosen to be discarded</p><p>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.</p><p>One possible reason for discarding such a packet could be to free up buffer space.</p><p>Discontinuities in the value of this counter can occur at re-initialization of the management system,</p><p>and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.in["{#IFNAME}",dropped]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Outbound packets discarded|<p>The number of outbound packets which were chosen to be discarded</p><p>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.</p><p>One possible reason for discarding such a packet could be to free up buffer space.</p><p>Discontinuities in the value of this counter can occur at re-initialization of the management system,</p><p>and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.out["{#IFNAME}",dropped]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Inbound packets with errors|<p>For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.in["{#IFNAME}",errors]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Outbound packets with errors|<p>For packet-oriented interfaces, the number of outbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of outbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|ZABBIX_PASSIVE|net.if.out["{#IFNAME}",errors]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Speed|<p>An estimate of the interface's current bandwidth in units of 1,000,000 bits per second. If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n-500,000' to`n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. For a sub-layer which has no concept of bandwidth, this object should be zero.</p>|DEPENDENT|net.if.speed["{#IFNAME}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.Name == "{#IFNAME}")].Speed.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|Network_interfaces|Interface {#IFNAME}: net.if.type|<p>-</p>|DEPENDENT|net.if.type["{#IFNAME}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.Name == "{#IFNAME}")].AdapterType.first()`</p>|
|Network_interfaces|Interface {#IFNAME}: net.if.status|<p>-</p>|DEPENDENT|net.if.status["{#IFNAME}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.Name == "{#IFNAME}")].NetConnectionStatus.first()`</p>|
|Zabbix_raw_items|Interface {#IFNAME}: Network interface get|<p>-</p>|ZABBIX_PASSIVE|wmi.getall[root\cimv2,"select * from win32_networkadapter"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Interface {#IFNAME}: High error rate ( > {$IF.ERRORS.WARN:"{#IFNAME}"} for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Recovers when below 80% of {$IF.ERRORS.WARN:"{#IFNAME}"} threshold</p>|`{TEMPLATE_NAME:net.if.in["{#IFNAME}",errors].min(5m)}>{$IF.ERRORS.WARN:"{#IFNAME}"} or {Template Module Windows network by Zabbix agent:net.if.out["{#IFNAME}",errors].min(5m)}>{$IF.ERRORS.WARN:"{#IFNAME}"}`<p>Recovery expression:</p>`{TEMPLATE_NAME:net.if.in["{#IFNAME}",errors].max(5m)}<{$IF.ERRORS.WARN:"{#IFNAME}"}*0.8 and {Template Module Windows network by Zabbix agent:net.if.out["{#IFNAME}",errors].max(5m)}<{$IF.ERRORS.WARN:"{#IFNAME}"}*0.8`|WARNING|<p>Manual close: YES</p>|
|Interface {#IFNAME}: Ethernet has changed to lower speed than it was before|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of autonegotiation issues. Ack to close.</p>|`{TEMPLATE_NAME:net.if.speed["{#IFNAME}"].change()}<0 and {TEMPLATE_NAME:net.if.speed["{#IFNAME}"].last()}>0 and ( {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=6 or {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=7 or {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=11 or {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=62 or {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=69 or {Template Module Windows network by Zabbix agent:net.if.type["{#IFNAME}"].last()}=117 ) and ({Template Module Windows network by Zabbix agent:net.if.status["{#IFNAME}"].last()}<>2)`<p>Recovery expression:</p>`({TEMPLATE_NAME:net.if.speed["{#IFNAME}"].change()}>0 and {TEMPLATE_NAME:net.if.speed["{#IFNAME}"].prev()}>0) or ({Template Module Windows network by Zabbix agent:net.if.status["{#IFNAME}"].last()}=2)`|INFO|<p>Manual close: YES</p>|

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
|Template Module Windows inventory by Zabbix agent|
|Template Module Windows memory by Zabbix agent|
|Template Module Windows network by Zabbix agent|
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

