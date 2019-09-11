
# Template OS Windows CPU by Zabbix agent

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU.MATCHES}|<p>.</p>|.*|
|{$CPU.NOT_MATCHES}|<p>.</p>|\s|
|{$CPU_UTIL_MAX}|<p>-</p>|90|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|CPU core discovery|<p>Discovery of CPU cores as defined in {$CPU.MATCHES} and {$CPU.NOT_MATCHES}</p>|ZABBIX_PASSIVE|system.cpu.discovery<p>**Filter**:</p>AND <p>- A: {#CPU.NUMBER} MATCHES_REGEX `{$CPU.MATCHES}`</p><p>- B: {#CPU.NUMBER} NOT_MATCHES_REGEX `{$CPU.NOT_MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|Interrupt Time, %|<p>-</p>|ZABBIX_PASSIVE|perf_counter_en["\Processor Information(_total)\% Interrupt Time"]|
|CPU|Load, %|<p>The Processor Information(_total)\% Processor Time shows how much the processor(s) is being utilized.</p>|ZABBIX_PASSIVE|perf_counter_en["\Processor Information(_total)\% Processor Time"]|
|CPU|Privileged time, %|<p>The Processor(_total)\% Privileged Time counter shows the percent of time that the processor is spent </p><p>executing in Kernel (or Privileged) mode. Privileged mode includes services interrupts inside Interrupt </p><p>Service Routines (ISRs), executing Deferred Procedure Calls (DPCs), Device Driver calls and other kernel-mode </p><p>functions of the Windows® Operating System.</p>|ZABBIX_PASSIVE|perf_counter_en["\Processor Information(_total)\% Privileged Time"]|
|CPU|User time, %|<p>The Processor(_total)\% User Time counter shows the percent of time that the processor(s) is spent executing </p><p>in User mode.</p>|ZABBIX_PASSIVE|perf_counter_en["\Processor Information(_total)\% User Time"]|
|CPU|Queue Length|<p>The Processor Queue Length shows the number of threads that are observed as delayed in the processor Ready Queue </p><p>and are waiting to be executed.</p>|ZABBIX_PASSIVE|perf_counter_en["\System\Processor Queue Length"]|
|CPU|CPU utilization|<p>CPU utilization in %</p>|ZABBIX_PASSIVE|system.cpu.util|
|CPU|#{#CPU.NUMBER}: CPU utilization|<p>CPU core #{#CPU.NUMBER} utilization in %</p>|ZABBIX_PASSIVE|system.cpu.util[{#CPU.NUMBER}]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|High CPU utilization|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:system.cpu.util.avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE||
|#{#CPU.NUMBER}: High CPU utilization|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:system.cpu.util[{#CPU.NUMBER}].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE||

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template OS Windows Filesystems by Zabbix agent

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$VFS.FS.FSDRIVETYPE.MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|fixed|
|{$VFS.FS.FSDRIVETYPE.NOT_MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|^\s$|
|{$VFS.FS.FSNAME.MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|.*|
|{$VFS.FS.FSNAME.NOT_MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|^(/dev|/sys|/run|/proc|.+/shm$)|
|{$VFS.FS.FSTYPE.MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|.*|
|{$VFS.FS.FSTYPE.NOT_MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level.</p>|^\s$|
|{$VFS.FS.PUSED.MAX.CRIT}|<p>-</p>|90|
|{$VFS.FS.PUSED.MAX.WARN}|<p>-</p>|80|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Mounted filesystem discovery|<p>Discovery of file systems of different types.</p>|ZABBIX_PASSIVE|vfs.fs.discovery<p>**Filter**:</p>AND <p>- A: {#FSTYPE} MATCHES_REGEX `{$VFS.FS.FSTYPE.MATCHES}`</p><p>- B: {#FSTYPE} NOT_MATCHES_REGEX `{$VFS.FS.FSTYPE.NOT_MATCHES}`</p><p>- C: {#FSNAME} MATCHES_REGEX `{$VFS.FS.FSNAME.MATCHES}`</p><p>- D: {#FSNAME} NOT_MATCHES_REGEX `{$VFS.FS.FSNAME.NOT_MATCHES}`</p><p>- E: {#FSDRIVETYPE} MATCHES_REGEX `{$VFS.FS.FSDRIVETYPE.MATCHES}`</p><p>- F: {#FSDRIVETYPE} NOT_MATCHES_REGEX `{$VFS.FS.FSDRIVETYPE.NOT_MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Filesystems|{#FSNAME}: Used space|<p>Used storage in Bytes</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},used]<p>**Expression**:</p>`(last(vfs.fs.size[{#FSNAME},total])-last(vfs.fs.size[{#FSNAME},free]))`|
|Filesystems|{#FSNAME}: Free space|<p>-</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},free]|
|Filesystems|{#FSNAME}: Total space|<p>Total space in Bytes</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},total]|
|Filesystems|{#FSNAME}: Space utilization|<p>Space utilization in % for {#FSNAME}</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},pused]<p>**Expression**:</p>`(last(vfs.fs.size[{#FSNAME},used])/(last(vfs.fs.size[{#FSNAME},free])+last(vfs.fs.size[{#FSNAME},used])))*100`|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|{#FSNAME}: Disk space critical status|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</p><p>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#FSNAME}"}.</p><p> Second condition should be one of the following:</p><p> - Disk free space is less than 5G.</p><p> - Disk will be full in less than 24hours.</p>|`{TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].last()}>{$STORAGE_UTIL_CRIT:"{#FSNAME}"} and (({Template OS Windows Filesystems by Zabbix agent:vfs.fs.size[{#FSNAME},total].last()}-{Template OS Windows Filesystems by Zabbix agent:vfs.fs.size[{#FSNAME},used].last()})<5G or {TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].timeleft(1h,,100)}<1d)`|AVERAGE||
|{#FSNAME}: Disk space warning|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</p><p>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#FSNAME}"}.</p><p> Second condition should be one of the following:</p><p> - Disk free space is less than 10G.</p><p> - Disk will be full in less than 24hours.</p>|`{TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].last()}>{$STORAGE_UTIL_WARN:"{#FSNAME}"} and (({Template OS Windows Filesystems by Zabbix agent:vfs.fs.size[{#FSNAME},total].last()}-{Template OS Windows Filesystems by Zabbix agent:vfs.fs.size[{#FSNAME},used].last()})<10G or {TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].timeleft(1h,,100)}<1d)`|WARNING|<p>**Depends on**:</p><p>- {#FSNAME}: Disk space critical status</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template OS Windows Inventory by Zabbix agent

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration



## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|General|System uptime|<p>The time (in hundredths of a second) since the network management portion of the system was last re-initialized.</p>|ZABBIX_PASSIVE|system.uptime<p>**Preprocessing**:</p><p>- MULTIPLIER: `0.01`</p>|
|General|System information|<p>-</p>|ZABBIX_PASSIVE|system.uname|
|General|Number of processes|<p>-</p>|ZABBIX_PASSIVE|proc.num[]|
|General|Number of threads|<p>The number of threads used by all running processes.</p>|ZABBIX_PASSIVE|perf_counter_en["\System\Threads"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Host has been restarted (uptime < 10m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The device uptime is less than 10 minutes.</p>|`{TEMPLATE_NAME:system.uptime.last()}<10m`|WARNING|<p>Manual close: YES</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template OS Windows Memory by Zabbix agent

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$MEMORY_AVAILABLE_MIN}|<p>-</p>|20M|
|{$MEMORY_UTIL_MAX}|<p>-</p>|90|
|{$SWAP_PFREE_WARN}|<p>-</p>|50|

## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Memory|Total memory|<p>Total memory in Bytes</p>|ZABBIX_PASSIVE|vm.memory.size[total]|
|Memory|Available memory|<p>Available memory, in Linux, available = free + buffers + cache. On other platforms calculation may vary. See also: https://www.zabbix.com/documentation/current/manual/appendix/items/vm.memory.size_params</p>|ZABBIX_PASSIVE|vm.memory.size[available]|
|Memory|Used memory|<p>Used memory in Bytes</p>|ZABBIX_PASSIVE|vm.memory.size[used]|
|Memory|Memory utilization|<p>Memory utilization in %</p>|ZABBIX_PASSIVE|vm.memory.size[pused]<p>**Expression**:</p>`(last(vm.memory.size[used])/last(vm.memory.size[total]))*100`|
|Memory|Total swap space|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,total]|
|Memory|Free swap space|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,free]|
|Memory|Free swap space in %|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,pfree]<p>**Expression**:</p>`((last(system.swap.size[,free]))/last(system.swap.size[,total]))*100`|
|Memory|Memory: Available|<p>Performance counter measures the amount of physical memory (RAM), in megabytes, that is immediately </p><p>available for allocation either to a process or for system use. It is the sum of the Zero, Free, </p><p>and Standby page lists discussed earlier. When the Available MBytes counter is low, it is a primary </p><p>indicator of a low RAM condition. This is when aggressive working set trims will occur which may or </p><p>may not result in a hard page fault where the pages on the Modified list are written to disk.</p><p>The \Memory\Pages/sec counter measures hard page faults, but it does not distinguish between hard </p><p>page faults that result from normal file reads or writes and page file reads or writes. Therefore, </p><p>use Pages/sec together with the Available MBytes counter, and do not use Pages/sec by itself.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Available Bytes"]|
|Memory|Memory: Cache bytes|<p>Cache Bytes is the sum of the Memory\\System Cache Resident Bytes, Memory\\System Driver Resident Bytes, </p><p>Memory\\System Code Resident Bytes, and Memory\\Pool Paged Resident Bytes counters. This counter displays </p><p>the last observed value only; it is not an average.</p><p>The Memory performance object consists of counters that describe the behavior of physical and virtual </p><p>memory on the computer. Physical memory is the amount of random access memory on the computer. Virtual </p><p>memory consists of the space in physical memory and on disk. Many of the memory counters monitor paging, </p><p>which is the movement of pages of code and data between disk and physical memory. Excessive paging, </p><p>a symptom of a memory shortage, can cause delays which interfere with all system processes.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Cache Bytes"]|
|Memory|Memory: Commit limit|<p>Commit Limit is the amount of virtual memory that can be committed without having to extend </p><p>the paging file(s). It is measured in bytes. Committed memory is the physical memory which </p><p>has space reserved on the disk paging files. There can be one paging file on each logical drive). </p><p>If the paging file(s) are be expanded, this limit increases accordingly. This counter displays </p><p>the last observed value only; it is not an average.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Commit Limit"]|
|Memory|Memory: Committed|<p>The system commit charge is the total amount of committed memory that is in use by all processes </p><p>and by the kernel. This memory might have been guaranteed or written to by a process or by the kernel.</p><p>Memory Available Megabytes in Use This measures the ratio of Committed Bytes to the Commit Limit—in other </p><p>words, the amount of virtual memory in use. This indicates insufficient memory if the number is greater </p><p>than 80 percent. The obvious solution for this is to add more memory.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Committed Bytes"]|
|Memory|Memory: Committed in use, %|<p>The \Memory\% Committed Bytes In Use counter calculates the ratio of committed bytes (system commit charge) </p><p>to the system commit limit, and the system can perform poorly when the system commit limit is reached. </p><p>Therefore, when % Committed Bytes In Use is greater than 80%, use the \Process(*)\Private Bytes counter </p><p>to identify the processes that are consuming the most committed memory.</p><p>The Debug Diagnostic Tool (DebugDiag) is designed to assist in troubleshooting issues such as hangs,  </p><p>slow performance, memory leaks or fragmentation, and crashes in any user-mode process. The tool includes </p><p>additional debugging scripts focused on Internet Information Services (IIS) applications, web data access </p><p>components, COM+ and related Microsoft technologies.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\% Committed Bytes In Use"]|
|Memory|Memory: Free system page table entries|<p>This indicates the number of page table entries not currently in use by the system. If the number is less </p><p>than 5,000, there may well be a memory leak.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Free System Page Table Entries"]|
|Memory|Memory: Page file usage, %|<p>The peak usage of the Page File instance in percent. </p><p>The Paging File performance object consists of counters that monitor the paging file(s) on the computer. </p><p>The paging file is a reserved space on disk that backs up committed physical memory on the computer.</p>|ZABBIX_PASSIVE|perf_counter_en["\Paging File(_total)\% Usage Peak"]|
|Memory|Memory: Pages faults per/sec|<p>Page Faults/sec is the average number of pages faulted per second. It is measured in number of pages </p><p>faulted per second because only one page is faulted in each fault operation, hence this is also equal </p><p>to the number of page fault operations. This counter includes both hard faults (those that require </p><p>disk access) and soft faults (where the faulted page is found elsewhere in physical memory.) Most </p><p>processors can handle large numbers of soft faults without significant consequence. However, hard faults, </p><p>which require disk access, can cause significant delays.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Page Faults/sec"]|
|Memory|Memory: Pages per/sec|<p>This measures the rate at which pages are read from or written to disk to resolve hard page faults. </p><p>If the value is greater than 1,000, as a result of excessive paging, there may be a memory leak.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Pages/sec"]|
|Memory|Memory: Pool non-paged|<p>This measures the size, in bytes, of the non-paged pool. This is an area of system memory for objects </p><p>that cannot be written to disk but instead must remain in physical memory as long as they are allocated. </p><p>There is a possible memory leak if the value is greater than 175MB (or 100MB with the /3GB switch). </p><p>A typical Event ID 2019 is recorded in the system event log.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Pool Nonpaged Bytes"]|
|Memory|Memory: Pool paged|<p>This measures the size, in bytes, of the paged pool. This is an area of system memory used for objects </p><p>that can be written to disk when they are not being used. There may be a memory leak if this value is </p><p>greater than 250MB (or 170MB with the /3GB switch). A typical Event ID 2020 is recorded in the system event log.</p>|ZABBIX_PASSIVE|perf_counter_en["\Memory\Pool Paged Bytes"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Lack of available memory ({ITEM.VALUE1} of {ITEM.VALUE2})|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:vm.memory.size[available].last(0)}<{$MEMORY_AVAILABLE_MIN} and {Template OS Windows Memory by Zabbix agent:vm.memory.size[total].last(0)}>0`|AVERAGE||
|High memory utilization|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:vm.memory.size[pused].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE||
|High swap space usage (free: {ITEM.VALUE1}, total: {ITEM.VALUE2})|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This trigger is ignored, if there is no swap configured</p>|`{TEMPLATE_NAME:system.swap.size[,pfree].last()}<{$SWAP_PFREE_WARN} and {Template OS Windows Memory by Zabbix agent:system.swap.size[,total].last()}>0`|WARNING||

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template OS Windows Network by Zabbix agent

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$NET.IFNAME.MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|.*|
|{$NET.IFNAME.NOT_MATCHES}|<p>This macro is used in Network interface discovery. Can be overriden on the host or linked template level.</p>|Miniport|Virtual|Teredo|Kernel|Loopback|Bluetooth|HTTPS|6to4|QoS|Layer|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Network interface discovery|<p>Discovery of network interfaces as defined in {$NET.IFNAME.MATCHES} and {$NET.IFNAME.NOT_MATCHES}.</p>|ZABBIX_PASSIVE|net.if.discovery<p>**Filter**:</p>AND <p>- A: {#IFNAME} MATCHES_REGEX `{$NET.IFNAME.MATCHES}`</p><p>- B: {#IFNAME} NOT_MATCHES_REGEX `{$NET.IFNAME.NOT_MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Network_interfaces|Interface {#IFNAME}: Bits received|<p>-</p>|ZABBIX_PASSIVE|net.if.in["{#IFNAME}"]|
|Network_interfaces|Interface {#IFNAME}: Bits sent|<p>-</p>|ZABBIX_PASSIVE|net.if.out["{#IFNAME}"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template OS Windows by Zabbix agent

## Overview

For Zabbix version: 3.4  
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
|Template OS Windows CPU by Zabbix agent|
|Template OS Windows Filesystems by Zabbix agent|
|Template OS Windows Inventory by Zabbix agent|
|Template OS Windows Memory by Zabbix agent|
|Template OS Windows Network by Zabbix agent|

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

