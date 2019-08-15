
# Template OS Linux Zabbix agent

## Overview

For Zabbix version: 4.2  
New official Linux template. Requires agent of Zabbix 3.0.14, 3.4.5 and 4.0.0 or newer.

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$IFCONTROL}|-|1|
|{$IF_ERRORS_WARN}|-|2|
|{$IF_UTIL_MAX}|-|90|
|{$INODE_PFREE_CRIT}|-|10|
|{$INODE_PFREE_WARN}|-|20|
|{$LOAD_AVG_CRIT}|-|1.5|
|{$MEMORY_AVAILABLE_MIN}|-|20M|
|{$STORAGE_UTIL_CRIT}|-|90|
|{$STORAGE_UTIL_WARN}|-|80|
|{$SWAP_PFREE_WARN}|-|50|
|{$VFS.DEV.READ.AWAIT.WARN}|Disk read average response time (in ms) before the trigger would fire|20|
|{$VFS.DEV.WRITE.AWAIT.WARN}|Disk write average response time (in ms) before the trigger would fire|20|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Network interface discovery|Discovery of network interfaces as defined in global regular expression "Network interfaces for discovery".</br>Filtering veth interfaces automatically created by Docker.|ZABBIX_PASSIVE|
|Mounted filesystem discovery|Discovery of file systems of different types as defined in global regular expression "File systems for discovery".|ZABBIX_PASSIVE|
|Block devices discovery|-|DEPENDENT|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|Load average (1m avg per core)|The load average is calculated as system CPU load divided by number of CPU cores.|ZABBIX_PASSIVE|system.cpu.load[percpu,avg1] |
|CPU|Load average (5m avg per core)|The load average is calculated as system CPU load divided by number of CPU cores.|ZABBIX_PASSIVE|system.cpu.load[percpu,avg5] |
|CPU|Load average (15m avg per core)|The load average is calculated as system CPU load divided by number of CPU cores.|ZABBIX_PASSIVE|system.cpu.load[percpu,avg15] |
|CPU|CPU utilization|CPU utilization in %|DEPENDENT|system.cpu.util </br>**Preprocessing**:</br> - JAVASCRIPT: `//Calculate utilization return (100 - value)`|
|CPU|CPU idle time|The time the CPU has spent doing nothing.|ZABBIX_PASSIVE|system.cpu.util[,idle] |
|CPU|CPU system time|The time the CPU has spent running the kernel and its processes.|ZABBIX_PASSIVE|system.cpu.util[,system] |
|CPU|CPU user time|The time the CPU has spent running users' processes that are not niced.|ZABBIX_PASSIVE|system.cpu.util[,user] |
|CPU|CPU nice time|The time the CPU has spent running users' processes that have been niced.|ZABBIX_PASSIVE|system.cpu.util[,nice] |
|CPU|CPU iowait time|Amount of time the CPU has been waiting for I/O to complete.|ZABBIX_PASSIVE|system.cpu.util[,iowait] |
|CPU|CPU steal time|The amount of CPU 'stolen' from this virtual machine by the hypervisor for other tasks (such as running another virtual machine).|ZABBIX_PASSIVE|system.cpu.util[,steal] |
|CPU|CPU interrupt time|The amount of time the CPU has been servicing hardware interrupts.|ZABBIX_PASSIVE|system.cpu.util[,interrupt] |
|CPU|CPU softirq time|The amount of time the CPU has been servicing software interrupts.|ZABBIX_PASSIVE|system.cpu.util[,softirq] |
|CPU|CPU guest time|Guest  time (time  spent  running  a  virtual  CPU  for  a  guest  operating  system)|ZABBIX_PASSIVE|system.cpu.util[,guest] |
|CPU|CPU guest nice time|Time spent running a niced guest (virtual CPU for guest operating systems under the control of the Linux kernel)|ZABBIX_PASSIVE|system.cpu.util[,guest_nice] |
|CPU|Context switches per second|-|ZABBIX_PASSIVE|system.cpu.switches </br>**Preprocessing**:</br> - CHANGE_PER_SECOND|
|CPU|Interrupts per second|-|ZABBIX_PASSIVE|system.cpu.intr </br>**Preprocessing**:</br> - CHANGE_PER_SECOND|
|Filesystems|{#FSNAME}: Used space|Used storage in Bytes|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},used] </br>**Expression**:</br>`(last(vfs.fs.size[{#FSNAME},total])-last(vfs.fs.size[{#FSNAME},free]))`|
|Filesystems|{#FSNAME}: Free space|-|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},free] |
|Filesystems|{#FSNAME}: Total space|Total space in Bytes|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},total] |
|Filesystems|{#FSNAME}: Space utilization|Space utilization in % for {#FSNAME}|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},pused] </br>**Expression**:</br>`(last(vfs.fs.size[{#FSNAME},used])/(last(vfs.fs.size[{#FSNAME},free])+last(vfs.fs.size[{#FSNAME},used])))*100`|
|Filesystems|{#FSNAME}: Free inodes in %|-|ZABBIX_PASSIVE|vfs.fs.inode[{#FSNAME},pfree] |
|Memory|Total memory|Total memory in Bytes|ZABBIX_PASSIVE|vm.memory.size[total] |
|Memory|Available memory|Available memory, in Linux, available = free + buffers + cache. On other platforms calculation may vary. See also: https://www.zabbix.com/documentation/current/manual/appendix/items/vm.memory.size_params|ZABBIX_PASSIVE|vm.memory.size[available] |
|Memory|Total swap space|-|ZABBIX_PASSIVE|system.swap.size[,total] |
|Memory|Free swap space|-|ZABBIX_PASSIVE|system.swap.size[,free] |
|Memory|Free swap space in %|-|ZABBIX_PASSIVE|system.swap.size[,pfree] </br>**Expression**:</br>`((last(system.swap.size[,free]))/last(system.swap.size[,total]))*100`|
|Network_interfaces|Interface {#IFNAME}: Bits received||ZABBIX_PASSIVE|net.if.in["{#IFNAME}"] </br>**Preprocessing**:</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `8`|
|Network_interfaces|Interface {#IFNAME}: Bits sent||ZABBIX_PASSIVE|net.if.out["{#IFNAME}"] </br>**Preprocessing**:</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `8`|
|Network_interfaces|Interface {#IFNAME}: Outbound packets with errors||ZABBIX_PASSIVE|net.if.out["{#IFNAME}",errors] </br>**Preprocessing**:</br> - CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Inbound packets with errors||ZABBIX_PASSIVE|net.if.in["{#IFNAME}",errors] </br>**Preprocessing**:</br> - CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Outbound packets discarded||ZABBIX_PASSIVE|net.if.out["{#IFNAME}",dropped] </br>**Preprocessing**:</br> - CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Inbound packets discarded||ZABBIX_PASSIVE|net.if.in["{#IFNAME}",dropped] </br>**Preprocessing**:</br> - CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Operational status|Indicates the interface RFC2863 operational state as a string.</br>Possible values are:"unknown", "notpresent", "down", "lowerlayerdown", "testing","dormant", "up".</br>Reference: https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net|ZABBIX_PASSIVE|vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"] </br>**Preprocessing**:</br> - JAVASCRIPT: `var newvalue; switch(value) {   case "up":     newvalue = 1;     break;   case "down":     newvalue = 2;     break;   case "testing":     newvalue = 4;     break;   case "unknown":     newvalue = 5;     break;   case "dormant":     newvalue = 6;     break;   case "notPresent":     newvalue = 7;     break;   default:     newvalue = "Problem parsing interface operstate in JS"; } return newvalue;`|
|Network_interfaces|Interface {#IFNAME}: Interface type|Indicates the interface protocol type as a decimal value.</br>See include/uapi/linux/if_arp.h for all possible values.</br>Reference: https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net|ZABBIX_PASSIVE|vfs.file.contents["/sys/class/net/{#IFNAME}/type"] |
|Storage|{#DEVNAME}: Disk read rate|r/s. The number (after merges) of read requests completed per second for the device.|DEPENDENT|vfs.dev.read.rate[{#DEVNAME}] </br>**Preprocessing**:</br> - JSONPATH: `$.values['{#DEVNAME}'][3]`</br> - CHANGE_PER_SECOND|
|Storage|{#DEVNAME}: Disk write rate|w/s. The number (after merges) of write requests completed per second for the device.|DEPENDENT|vfs.dev.write.rate[{#DEVNAME}] </br>**Preprocessing**:</br> - JSONPATH: `$.values['{#DEVNAME}'][7]`</br> - CHANGE_PER_SECOND|
|Storage|{#DEVNAME}: Disk read request avg waiting time (r_await)|This formula contains two boolean expressions that evaluates to 1 or 0 in order to set calculated metric to zero and to avoid division by zero exception.|CALCULATED|vfs.dev.read.await[{#DEVNAME}] </br>**Expression**:</br>`(last(vfs.dev.read.time.rate[{#DEVNAME}])/(last(vfs.dev.read.rate[{#DEVNAME}])+(last(vfs.dev.read.rate[{#DEVNAME}])=0)))*1000*(last(vfs.dev.read.rate[{#DEVNAME}]) > 0)`|
|Storage|{#DEVNAME}: Disk write request avg waiting time (w_await)|This formula contains two boolean expressions that evaluates to 1 or 0 in order to set calculated metric to zero and to avoid division by zero exception.|CALCULATED|vfs.dev.write.await[{#DEVNAME}] </br>**Expression**:</br>`(last(vfs.dev.write.time.rate[{#DEVNAME}])/(last(vfs.dev.write.rate[{#DEVNAME}])+(last(vfs.dev.write.rate[{#DEVNAME}])=0)))*1000*(last(vfs.dev.write.rate[{#DEVNAME}]) > 0)`|
|Storage|{#DEVNAME}: Disk average queue size (avgqu-sz)|-|DEPENDENT|vfs.dev.queue_size[{#DEVNAME}] </br>**Preprocessing**:</br> - JSONPATH: `$.values['{#DEVNAME}'][13]`</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `0.001`|
|Storage|{#DEVNAME}: Disk utilization|-|DEPENDENT|vfs.dev.util[{#DEVNAME}] </br>**Preprocessing**:</br> - JSONPATH: `$.values['{#DEVNAME}'][12]`</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `0.1`|
|Zabbix_raw_items|Get /proc/diskstats|-|ZABBIX_PASSIVE|vfs.file.contents[/proc/diskstats] </br>**Preprocessing**:</br> - JAVASCRIPT: `var parsed = value.split("\n").reduce(function(acc, x, i) {   acc["values"][x.split(/ +/)[3]] = x.split(/ +/).slice(1)   acc["lld"].push({"{#DEVNAME}":x.split(/ +/)[3]});   return acc; }, {"values":{}, "lld": []}); return JSON.stringify(parsed);`|
|Zabbix_raw_items|{#DEVNAME}: Disk read time (rate)|Rate of total read time counter. Used in r_await calculation|DEPENDENT|vfs.dev.read.time.rate[{#DEVNAME}] </br>**Preprocessing**:</br> - JSONPATH: `$.values['{#DEVNAME}'][6]`</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `0.001`|
|Zabbix_raw_items|{#DEVNAME}: Disk write time (rate)|Rate of total write time counter. Used in w_await calculation|DEPENDENT|vfs.dev.write.time.rate[{#DEVNAME}] </br>**Preprocessing**:</br> - JSONPATH: `$.values['{#DEVNAME}'][10]`</br> - CHANGE_PER_SECOND</br> - MULTIPLIER: `0.001`|

## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|Load average is too high|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.load[percpu,avg1].avg(5m)}>{$LOAD_AVG_CRIT}`|AVERAGE|
|{#FSNAME}: Disk space critical status|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#FSNAME}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 5G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].last()}>{$STORAGE_UTIL_CRIT:"{#FSNAME}"} and (({Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},total].last()}-{Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},used].last()})<5G or {TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].timeleft(1h,,100)}<1d)`|AVERAGE|
|{#FSNAME}: Disk space warning|Last value: {ITEM.LASTVALUE1}.</br>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</br>Two conditions should match: First, space utilization should be above {$STORAGE_UTIL_CRIT:"{#FSNAME}"}.</br> Second condition should be one of the following:</br> - Disk free space is less than 10G.</br> - Disk will be full in less than 24hours.|`{TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].last()}>{$STORAGE_UTIL_WARN:"{#FSNAME}"} and (({Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},total].last()}-{Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},used].last()})<10G or {TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].timeleft(1h,,100)}<1d)`|WARNING|
|{#FSNAME}: Free inodes is critically low, below {$INODE_PFREE_CRIT:"{#FSNAME}"}%|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vfs.fs.inode[{#FSNAME},pfree].last()}<{$INODE_PFREE_CRIT:"{#FSNAME}"}`|AVERAGE|
|{#FSNAME}: Free inodes is below {$INODE_PFREE_WARN:"{#FSNAME}"}%|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vfs.fs.inode[{#FSNAME},pfree].last()}<{$INODE_PFREE_WARN:"{#FSNAME}"}`|WARNING|
|Lack of available memory ({ITEM.VALUE1} of {ITEM.VALUE2})|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.size[available].last(0)}<{$MEMORY_AVAILABLE_MIN} and {Template OS Linux Zabbix agent:vm.memory.size[total].last(0)}>0`|AVERAGE|
|High swap space usage (free: {ITEM.VALUE1}, total: {ITEM.VALUE2})|Last value: {ITEM.LASTVALUE1}.</br>This trigger is ignored, if there is no swap configured|`{TEMPLATE_NAME:system.swap.size[,pfree].last()}<{$SWAP_PFREE_WARN} and {Template OS Linux Zabbix agent:system.swap.size[,total].last()}>0`|WARNING|
|Interface {#IFNAME}: High error rate|Last value: {ITEM.LASTVALUE1}.</br>Recovers when below 80% of {$IF_ERRORS_WARN:"{#IFNAME}"} threshold|`{TEMPLATE_NAME:net.if.in["{#IFNAME}",errors].avg(5m)}>{$IF_ERRORS_WARN:"{#IFNAME}"} or {Template OS Linux Zabbix agent:net.if.out["{#IFNAME}",errors].avg(5m)}>{$IF_ERRORS_WARN:"{#IFNAME}"}`</br>Recovery expression: `{TEMPLATE_NAME:net.if.in["{#IFNAME}",errors].avg(5m)}<{$IF_ERRORS_WARN:"{#IFNAME}"}*0.8 and {Template OS Linux Zabbix agent:net.if.out["{#IFNAME}",errors].avg(5m)}<{$IF_ERRORS_WARN:"{#IFNAME}"}*0.8`|WARNING|
|Interface {#IFNAME}: Link down|Last value: {ITEM.LASTVALUE1}.</br>Interface is down|`{$IFCONTROL:"{#IFNAME}"}=1 and ({TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"].last()}=2 and {TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"].diff()}=1)`</br>Recovery expression: `{TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"].last()}<>2`|AVERAGE|
|Interface {#IFNAME}: Ethernet has changed to lower speed than it was before|Last value: {ITEM.LASTVALUE1}.</br>This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of autonegotiation issues. Ack to close.|`{TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].change()}<0 and {TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].last()}>0 and ({Template OS Linux Zabbix agent:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].last()}=6 or {Template OS Linux Zabbix agent:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].last()}=1) and ({Template OS Linux Zabbix agent:vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"].last()}<>2)`</br>Recovery expression: `({TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].change()}>0 and {TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].prev()}>0) or ({Template OS Linux Zabbix agent:vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"].last()}=2)`|INFO|
|{#DEVNAME}: Disk read request response are too high (read > {$VFS.DEV.READ.AWAIT.WARN:"{#DEVNAME}"} ms for 5m or write > {$VFS.DEV.WRITE.AWAIT.WARN:"{#DEVNAME}"} ms for 5m)|Last value: {ITEM.LASTVALUE1}.</br>This trigger might indicate disk {#DEVNAME} saturation.|`{TEMPLATE_NAME:vfs.dev.read.await[{#DEVNAME}].min(5m)} > {$VFS.DEV.READ.AWAIT.WARN:"{#DEVNAME}"} or {TEMPLATE_NAME:vfs.dev.read.await[{#DEVNAME}].min(5m)} > {$VFS.DEV.WRITE.AWAIT.WARN:"{#DEVNAME}"}`|WARNING|

## Feedback

Please report any issues with the template at https://support.zabbix.com

