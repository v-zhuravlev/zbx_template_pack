
# Template OS Linux Prom

## Overview

For Zabbix version: 4.2  
This template collects Linux metrics from node_exporter 0.16 and above. Support for older node_exporter versions is provided as 'best effort'.

This template was tested on:

- node_exporter, version 0.17.0
- node_exporter, version 0.18.1

## Setup

Please refer to the node_exporter docs. Use node_exporter v0.16.0 or above

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$INODE_PFREE_CRIT}|-|10|
|{$INODE_PFREE_WARN}|-|20|
|{$LOAD_AVG_CRIT}|-|1.5|
|{$MEMORY_AVAILABLE_MIN}|-|20M|
|{$NODE_EXPORTER_PORT}|TCP Port node_exporter is listening on.|9100|
|{$STORAGE_UTIL_CRIT}|-|90|
|{$STORAGE_UTIL_WARN}|-|80|
|{$SWAP_PFREE_WARN}|-|50|
|{$VFS.DEV.READ.AWAIT.WARN}|Disk read average response time (in ms) before the trigger would fire|20|
|{$VFS.DEV.WRITE.AWAIT.WARN}|Disk write average response time (in ms) before the trigger would fire|20|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|CPU discovery|-|DEPENDENT|node_exporter.cpu.discovery</br>**Preprocessing**:</br> - PROMETHEUS_TO_JSON: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu=~".+",mode="idle"}`|
|Mounted filesystem discovery|Discovery of file systems of different types as defined in global regular expression "File systems for discovery".|DEPENDENT|node_exporter.vfs.fs.discovery</br>**Preprocessing**:</br> - PROMETHEUS_TO_JSON: `{__name__=~"^node_filesystem_size(?:_bytes)?$", mountpoint=~".+"}`</br>**Filter**: AND </br> - A: {#FSTYPE} MATCHES_REGEX `@File systems for discovery`|
|Block devices discovery|-|DEPENDENT|node_exporter.vfs.dev.discovery</br>**Preprocessing**:</br> - PROMETHEUS_TO_JSON: `node_disk_io_now{device=~".+"}`|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|Load average (1m avg)|-|DEPENDENT|node_exporter.node_load1</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `node_load1 `|
|CPU|Load average (5m avg)|-|DEPENDENT|node_exporter.node_load5</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `node_load5 `|
|CPU|Load average (15m avg)|-|DEPENDENT|node_exporter.node_load15</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `node_load15 `|
|CPU|Number of CPUs|-|DEPENDENT|node_exporter.system.cpu.num</br>**Preprocessing**:</br> - PROMETHEUS_TO_JSON: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu=~".+",mode="idle"}`</br> - JAVASCRIPT: `//count the number of cores return JSON.parse(value).length `</br> - DISCARD_UNCHANGED_HEARTBEAT: `1d`|
|CPU|Interrupts per second|-|DEPENDENT|node_exporter.system.cpu.intr</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"node_intr"} `</br> - CHANGE_PER_SECOND|
|CPU|Context switches per second|-|DEPENDENT|node_exporter.system.cpu.switches</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"node_context_switches"} `</br> - CHANGE_PER_SECOND|
|CPU|#{#CPUNUM}: CPU utilization|CPU utilization in %|DEPENDENT|node_exporter.system.cpu.util[{#CPUNUM}]</br>**Preprocessing**:</br> - JAVASCRIPT: `//Calculate utilization return (100 - value)`|
|CPU|#{#CPUNUM}: CPU idle time|The time the CPU has spent doing nothing.|DEPENDENT|node_exporter.system.cpu.idle[{#CPUNUM}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="idle"} `</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `100`|
|CPU|#{#CPUNUM}: CPU system time|The time the CPU has spent running the kernel and its processes.|DEPENDENT|node_exporter.system.cpu.system[{#CPUNUM}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="system"} `</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `100`|
|CPU|#{#CPUNUM}: CPU user time|The time the CPU has spent running users' processes that are not niced.|DEPENDENT|node_exporter.system.cpu.user[{#CPUNUM}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="user"} `</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `100`|
|CPU|#{#CPUNUM}: CPU steal time|The amount of CPU 'stolen' from this virtual machine by the hypervisor for other tasks (such as running another virtual machine).|DEPENDENT|node_exporter.system.cpu.steal[{#CPUNUM}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="steal"} `</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `100`|
|CPU|#{#CPUNUM}: CPU softirq time|The amount of time the CPU has been servicing software interrupts.|DEPENDENT|node_exporter.system.cpu.softirq[{#CPUNUM}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="softirq"} `</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `100`|
|CPU|#{#CPUNUM}: CPU nice time|The time the CPU has spent running users' processes that have been niced.|DEPENDENT|node_exporter.system.cpu.nice[{#CPUNUM}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="nice"} `</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `100`|
|CPU|#{#CPUNUM}: CPU iowait time|Amount of time the CPU has been waiting for I/O to complete.|DEPENDENT|node_exporter.system.cpu.iowait[{#CPUNUM}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="iowait"} `</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `100`|
|CPU|#{#CPUNUM}: CPU interrupt time|The amount of time the CPU has been servicing hardware interrupts.|DEPENDENT|node_exporter.system.cpu.interrupt[{#CPUNUM}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="irq"} `</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `100`|
|CPU|#{#CPUNUM}: CPU guest time|Guest  time (time  spent  running  a  virtual  CPU  for  a  guest  operating  system)|DEPENDENT|node_exporter.system.cpu.guest[{#CPUNUM}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_guest_seconds_total)?$",cpu="{#CPUNUM}",mode=~"^(?:user|guest)$"} `</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `100`|
|CPU|#{#CPUNUM}: CPU guest nice time|Time spent running a niced guest (virtual CPU for guest operating systems under the control of the Linux kernel)|DEPENDENT|node_exporter.system.cpu.guest_nice[{#CPUNUM}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_guest_seconds_total)?$",cpu="{#CPUNUM}",mode=~"^(?:nice|guest_nice)$"} `</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `100`|
|Memory|Total memory|Total memory in Bytes|DEPENDENT|node_exporter.node_memory_memtotal_bytes</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"node_memory_MemTotal"} `|
|Memory|Available memory|Available memory, in Linux, available = free + buffers + cache. On other platforms calculation may vary. See also: https://www.zabbix.com/documentation/current/manual/appendix/items/vm.memory.size_params|DEPENDENT|node_exporter.node_memory_memavailable_bytes</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"node_memory_MemAvailable"} `|
|Memory|Total swap space|-|DEPENDENT|node_exporter.node_memory_swaptotal_bytes</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"node_memory_SwapTotal"} `|
|Memory|Free swap space|-|DEPENDENT|node_exporter.node_memory_swapfree_bytes</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"node_memory_SwapFree"} `|
|Memory|Free swap space in %|-|CALCULATED|node_exporter.system.swap.pfree</br>**Expression**:</br>`((last(node_exporter.node_memory_swapfree_bytes))/last(node_exporter.node_memory_swaptotal_bytes))*100`|
|Storage|{#FSNAME}: Free space|-|DEPENDENT|node_exporter.vfs.fs.free[{#FSNAME}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_filesystem_avail(?:_bytes)?$", mountpoint="{#FSNAME}"} `|
|Storage|{#FSNAME}: Total space|Total space in Bytes|DEPENDENT|node_exporter.vfs.fs.total[{#FSNAME}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `{__name__=~"^node_filesystem_size(?:_bytes)?$", mountpoint="{#FSNAME}"} `|
|Storage|{#FSNAME}: Used space|Used storage in Bytes|CALCULATED|node_exporter.vfs.fs.used[{#FSNAME}]</br>**Expression**:</br>`(last(node_exporter.vfs.fs.total[{#FSNAME}])-last(node_exporter.vfs.fs.free[{#FSNAME}]))`|
|Storage|{#FSNAME}: Space utilization|Space utilization in % for {#FSNAME}|CALCULATED|node_exporter.vfs.fs.pused[{#FSNAME}]</br>**Expression**:</br>`(last(node_exporter.vfs.fs.used[{#FSNAME}])/(last(node_exporter.vfs.fs.free[{#FSNAME}])+last(node_exporter.vfs.fs.used[{#FSNAME}])))*100`|
|Storage|{#FSNAME}: Free inodes in %|-|DEPENDENT|node_exporter.vfs.fs.inode.pfree[{#FSNAME}]</br>**Preprocessing**:</br> - PROMETHEUS_TO_JSON: `{__name__=~"node_filesystem_files.*",mountpoint="{#FSNAME}"}`</br> - JAVASCRIPT: `//count vfs.fs.inode.pfree var inode_free; var inode_total; JSON.parse(value).forEach(function(metric) {   if (metric['name'] == 'node_filesystem_files'){       inode_total = metric['value'];   } else if (metric['name'] == 'node_filesystem_files_free'){       inode_free = metric['value'];   } }); return (inode_free/inode_total)*100;`|
|Storage|{#DEVNAME}: Disk read rate|r/s. The number (after merges) of read requests completed per second for the device.|DEPENDENT|node_exporter.vfs.dev.read.rate[{#DEVNAME}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `node_disk_reads_completed_total{device="{#DEVNAME}"} `</br> - CHANGE_PER_SECOND|
|Storage|{#DEVNAME}: Disk write rate|w/s. The number (after merges) of write requests completed per second for the device.|DEPENDENT|node_exporter.vfs.dev.write.rate[{#DEVNAME}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `node_disk_writes_completed_total{device="{#DEVNAME}"} `</br> - CHANGE_PER_SECOND|
|Storage|{#DEVNAME}: Disk read request avg waiting time (r_await)|This formula contains two boolean expressions that evaluates to 1 or 0 in order to set calculated metric to zero and to avoid division by zero exception.|CALCULATED|node_exporter.vfs.dev.read.await[{#DEVNAME}]</br>**Expression**:</br>`(last(node_exporter.vfs.dev.read.time.rate[{#DEVNAME}])/(last(node_exporter.vfs.dev.read.rate[{#DEVNAME}])+(last(node_exporter.vfs.dev.read.rate[{#DEVNAME}])=0)))*1000*(last(node_exporter.vfs.dev.read.rate[{#DEVNAME}]) > 0)`|
|Storage|{#DEVNAME}: Disk write request avg waiting time (w_await)|This formula contains two boolean expressions that evaluates to 1 or 0 in order to set calculated metric to zero and to avoid division by zero exception.|CALCULATED|node_exporter.vfs.dev.write.await[{#DEVNAME}]</br>**Expression**:</br>`(last(node_exporter.vfs.dev.write.time.rate[{#DEVNAME}])/(last(node_exporter.vfs.dev.write.rate[{#DEVNAME}])+(last(node_exporter.vfs.dev.write.rate[{#DEVNAME}])=0)))*1000*(last(node_exporter.vfs.dev.write.rate[{#DEVNAME}]) > 0)`|
|Storage|{#DEVNAME}: Disk average queue size (avgqu-sz)|-|DEPENDENT|node_exporter.vfs.dev.queue_size[{#DEVNAME}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `node_disk_io_time_weighted_seconds_total{device="{#DEVNAME}"} `</br> - CHANGE_PER_SECOND|
|Storage|{#DEVNAME}: Disk utilization|-|DEPENDENT|node_exporter.vfs.dev.util[{#DEVNAME}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `node_disk_io_time_seconds_total{device="{#DEVNAME}"} `</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `100`|
|Zabbix_raw_items|Get node_exporter metrics|-|HTTP_AGENT|node_exporter.get|
|Zabbix_raw_items|{#DEVNAME}: Disk read time (rate)|Rate of total read time counter. Used in r_await calculation|DEPENDENT|node_exporter.vfs.dev.read.time.rate[{#DEVNAME}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `node_disk_read_time_seconds_total{device="{#DEVNAME}"} `</br> - CHANGE_PER_SECOND|
|Zabbix_raw_items|{#DEVNAME}: Disk write time (rate)|Rate of total write time counter. Used in w_await calculation|DEPENDENT|node_exporter.vfs.dev.write.time.rate[{#DEVNAME}]</br>**Preprocessing**:</br> - PROMETHEUS_PATTERN: `node_disk_write_time_seconds_total{device="{#DEVNAME}"} `</br> - CHANGE_PER_SECOND|

## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|Load average is too high|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:node_exporter.node_load1.avg(5m)}/{Template OS Linux Prom:node_exporter.system.cpu.num.last()}>{$LOAD_AVG_CRIT}`|AVERAGE|
|Lack of available memory ({ITEM.VALUE1} of {ITEM.VALUE2})|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:node_exporter.node_memory_memavailable_bytes.last(0)}<{$MEMORY_AVAILABLE_MIN} and {Template OS Linux Prom:node_exporter.node_memory_memtotal_bytes.last(0)}>0`|AVERAGE|
|High swap space usage (free: {ITEM.VALUE1}, total: {ITEM.VALUE2})|Last value: {ITEM.LASTVALUE1}.</br>This trigger is ignored, if there is no swap configured|`{TEMPLATE_NAME:node_exporter.system.swap.pfree.last()}<{$SWAP_PFREE_WARN} and {Template OS Linux Prom:node_exporter.node_memory_swaptotal_bytes.last()}>0`|WARNING|
|{#FSNAME}: Disk space critical status|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#FSNAME}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 5G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].last()}>{$STORAGE_UTIL_CRIT:"{#FSNAME}"} and (({Template OS Linux Prom:node_exporter.vfs.fs.total[{#FSNAME}].last()}-{Template OS Linux Prom:node_exporter.vfs.fs.used[{#FSNAME}].last()})<5G or {TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].timeleft(1h,,100)}<1d)`|AVERAGE|
|{#FSNAME}: Disk space warning|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#FSNAME}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 10G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].last()}>{$STORAGE_UTIL_WARN:"{#FSNAME}"} and (({Template OS Linux Prom:node_exporter.vfs.fs.total[{#FSNAME}].last()}-{Template OS Linux Prom:node_exporter.vfs.fs.used[{#FSNAME}].last()})<10G or {TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].timeleft(1h,,100)}<1d)`|WARNING|
|{#FSNAME}: Free inodes is critically low, below {$INODE_PFREE_CRIT:"{#FSNAME}"}%|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:node_exporter.vfs.fs.inode.pfree[{#FSNAME}].last()}<{$INODE_PFREE_CRIT:"{#FSNAME}"}`|AVERAGE|
|{#FSNAME}: Free inodes is below {$INODE_PFREE_WARN:"{#FSNAME}"}%|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:node_exporter.vfs.fs.inode.pfree[{#FSNAME}].last()}<{$INODE_PFREE_WARN:"{#FSNAME}"}`|WARNING|
|{#DEVNAME}: Disk read request response are too high (read > {$VFS.DEV.READ.AWAIT.WARN:"{#DEVNAME}"} ms for 5m or write > {$VFS.DEV.WRITE.AWAIT.WARN:"{#DEVNAME}"} ms for 5m)|Last value: {ITEM.LASTVALUE1}.</br>This trigger might indicate disk {#DEVNAME} saturation.|`{TEMPLATE_NAME:node_exporter.vfs.dev.read.await[{#DEVNAME}].min(5m)} > {$VFS.DEV.READ.AWAIT.WARN:"{#DEVNAME}"} or {TEMPLATE_NAME:node_exporter.vfs.dev.read.await[{#DEVNAME}].min(5m)} > {$VFS.DEV.WRITE.AWAIT.WARN:"{#DEVNAME}"}`|WARNING|

## Feedback

Please report any issues with the template at https://support.zabbix.com

## References

https://github.com/prometheus/node_exporter
