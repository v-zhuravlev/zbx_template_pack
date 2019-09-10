
# Template OS Linux Zabbix agent

## Overview

For Zabbix version: 4.2  
New official Linux template. Requires agent of Zabbix 3.0.14, 3.4.5 and 4.0.0 or newer.

## Setup

Install Zabbix agent to Linux OS according to Zabbix documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|<p>-</p>|90|
|{$IFCONTROL}|<p>-</p>|1|
|{$IF_ERRORS_WARN}|<p>-</p>|2|
|{$IF_UTIL_MAX}|<p>-</p>|90|
|{$LOAD_AVG_CRIT}|<p>-</p>|1.5|
|{$MEMORY_AVAILABLE_MIN}|<p>-</p>|20M|
|{$SWAP_PFREE_WARN}|<p>-</p>|50|
|{$VFS.DEV.DEVNAME.MATCHES}|<p>This macro is used in block devices discovery. Can be overriden on the host or linked template level</p>|.+|
|{$VFS.DEV.DEVNAME.NOT_MATCHES}|<p>This macro is used in block devices discovery. Can be overriden on the host or linked template level</p>|(loop[0-9]*|sd[a-z][0-9]+|nbd[0-9]+|sr[0-9]+|fd[0-9]+)|
|{$VFS.DEV.READ.AWAIT.WARN}|<p>Disk read average response time (in ms) before the trigger would fire</p>|20|
|{$VFS.DEV.WRITE.AWAIT.WARN}|<p>Disk write average response time (in ms) before the trigger would fire</p>|20|
|{$VFS.FS.FSNAME.MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level</p>|.+|
|{$VFS.FS.FSNAME.NOT_MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level</p>|^(/dev|/sys|/run|/proc|.+/shm$)|
|{$VFS.FS.FSTYPE.MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level</p>|^(btrfs|ext2|ext3|ext4|reiser|xfs|ffs|ufs|jfs|jfs2|vxfs|hfs|apfs|refs|ntfs|fat32|zfs)$|
|{$VFS.FS.FSTYPE.NOT_MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level</p>|^\s$|
|{$VFS.FS.INODE.PFREE.MIN.CRIT}|<p>-</p>|10|
|{$VFS.FS.INODE.PFREE.MIN.WARN}|<p>-</p>|20|
|{$VFS.FS.PUSED.MAX.CRIT}|<p>-</p>|90|
|{$VFS.FS.PUSED.MAX.WARN}|<p>-</p>|80|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Network interface discovery|<p>Discovery of network interfaces as defined in global regular expression "Network interfaces for discovery".</p><p>Filtering veth interfaces automatically created by Docker.</p>|ZABBIX_PASSIVE|net.if.discovery<p>**Filter**:</p>AND <p>- A: {#IFNAME} MATCHES_REGEX `@Network interfaces for discovery`</p><p>- B: {#IFNAME} NOT_MATCHES_REGEX `^veth[0-9a-z]+$`</p>|
|Mounted filesystem discovery|<p>Discovery of file systems of different types.</p>|ZABBIX_PASSIVE|vfs.fs.discovery<p>**Filter**:</p>AND <p>- A: {#FSTYPE} MATCHES_REGEX `{$VFS.FS.FSTYPE.MATCHES}`</p><p>- B: {#FSTYPE} NOT_MATCHES_REGEX `{$VFS.FS.FSTYPE.NOT_MATCHES}`</p><p>- C: {#FSNAME} MATCHES_REGEX `{$VFS.FS.FSNAME.MATCHES}`</p><p>- D: {#FSNAME} NOT_MATCHES_REGEX `{$VFS.FS.FSNAME.NOT_MATCHES}`</p>|
|Block devices discovery|<p>-</p>|DEPENDENT|vfs.dev.discovery<p>**Preprocessing**:</p><p>- JSONPATH: `$.lld`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1h`</p><p>**Filter**:</p>AND <p>- A: {#DEVNAME} MATCHES_REGEX `{$VFS.DEV.DEVNAME.MATCHES}`</p><p>- B: {#DEVNAME} NOT_MATCHES_REGEX `{$VFS.DEV.DEVNAME.NOT_MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|Load average (1m avg per core)|<p>The load average is calculated as system CPU load divided by number of CPU cores.</p>|ZABBIX_PASSIVE|system.cpu.load[percpu,avg1]|
|CPU|Load average (5m avg per core)|<p>The load average is calculated as system CPU load divided by number of CPU cores.</p>|ZABBIX_PASSIVE|system.cpu.load[percpu,avg5]|
|CPU|Load average (15m avg per core)|<p>The load average is calculated as system CPU load divided by number of CPU cores.</p>|ZABBIX_PASSIVE|system.cpu.load[percpu,avg15]|
|CPU|CPU utilization|<p>CPU utilization in %</p>|DEPENDENT|system.cpu.util<p>**Preprocessing**:</p><p>- JAVASCRIPT: `//Calculate utilization return (100 - value)`</p>|
|CPU|CPU idle time|<p>The time the CPU has spent doing nothing.</p>|ZABBIX_PASSIVE|system.cpu.util[,idle]|
|CPU|CPU system time|<p>The time the CPU has spent running the kernel and its processes.</p>|ZABBIX_PASSIVE|system.cpu.util[,system]|
|CPU|CPU user time|<p>The time the CPU has spent running users' processes that are not niced.</p>|ZABBIX_PASSIVE|system.cpu.util[,user]|
|CPU|CPU nice time|<p>The time the CPU has spent running users' processes that have been niced.</p>|ZABBIX_PASSIVE|system.cpu.util[,nice]|
|CPU|CPU iowait time|<p>Amount of time the CPU has been waiting for I/O to complete.</p>|ZABBIX_PASSIVE|system.cpu.util[,iowait]|
|CPU|CPU steal time|<p>The amount of CPU 'stolen' from this virtual machine by the hypervisor for other tasks (such as running another virtual machine).</p>|ZABBIX_PASSIVE|system.cpu.util[,steal]|
|CPU|CPU interrupt time|<p>The amount of time the CPU has been servicing hardware interrupts.</p>|ZABBIX_PASSIVE|system.cpu.util[,interrupt]|
|CPU|CPU softirq time|<p>The amount of time the CPU has been servicing software interrupts.</p>|ZABBIX_PASSIVE|system.cpu.util[,softirq]|
|CPU|CPU guest time|<p>Guest  time (time  spent  running  a  virtual  CPU  for  a  guest  operating  system)</p>|ZABBIX_PASSIVE|system.cpu.util[,guest]|
|CPU|CPU guest nice time|<p>Time spent running a niced guest (virtual CPU for guest operating systems under the control of the Linux kernel)</p>|ZABBIX_PASSIVE|system.cpu.util[,guest_nice]|
|CPU|Context switches per second|<p>-</p>|ZABBIX_PASSIVE|system.cpu.switches<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|CPU|Interrupts per second|<p>-</p>|ZABBIX_PASSIVE|system.cpu.intr<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Filesystems|{#FSNAME}: Used space|<p>Used storage in Bytes</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},used]<p>**Expression**:</p>`(last(vfs.fs.size[{#FSNAME},total])-last(vfs.fs.size[{#FSNAME},free]))`|
|Filesystems|{#FSNAME}: Free space|<p>-</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},free]|
|Filesystems|{#FSNAME}: Total space|<p>Total space in Bytes</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},total]|
|Filesystems|{#FSNAME}: Space utilization|<p>Space utilization in % for {#FSNAME}</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},pused]<p>**Expression**:</p>`(last(vfs.fs.size[{#FSNAME},used])/(last(vfs.fs.size[{#FSNAME},free])+last(vfs.fs.size[{#FSNAME},used])))*100`|
|Filesystems|{#FSNAME}: Free inodes in %|<p>-</p>|ZABBIX_PASSIVE|vfs.fs.inode[{#FSNAME},pfree]|
|Memory|Total memory|<p>Total memory in Bytes</p>|ZABBIX_PASSIVE|vm.memory.size[total]|
|Memory|Available memory|<p>Available memory, in Linux, available = free + buffers + cache. On other platforms calculation may vary. See also: https://www.zabbix.com/documentation/current/manual/appendix/items/vm.memory.size_params</p>|ZABBIX_PASSIVE|vm.memory.size[available]|
|Memory|Total swap space|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,total]|
|Memory|Free swap space|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,free]|
|Memory|Free swap space in %|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,pfree]<p>**Expression**:</p>`((last(system.swap.size[,free]))/last(system.swap.size[,total]))*100`|
|Network_interfaces|Interface {#IFNAME}: Bits received||ZABBIX_PASSIVE|net.if.in["{#IFNAME}"]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `8`</p>|
|Network_interfaces|Interface {#IFNAME}: Bits sent||ZABBIX_PASSIVE|net.if.out["{#IFNAME}"]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `8`</p>|
|Network_interfaces|Interface {#IFNAME}: Outbound packets with errors||ZABBIX_PASSIVE|net.if.out["{#IFNAME}",errors]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Inbound packets with errors||ZABBIX_PASSIVE|net.if.in["{#IFNAME}",errors]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Outbound packets discarded||ZABBIX_PASSIVE|net.if.out["{#IFNAME}",dropped]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Inbound packets discarded||ZABBIX_PASSIVE|net.if.in["{#IFNAME}",dropped]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}: Operational status|<p>Indicates the interface RFC2863 operational state as a string.</p><p>Possible values are:"unknown", "notpresent", "down", "lowerlayerdown", "testing","dormant", "up".</p><p>Reference: https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net</p>|ZABBIX_PASSIVE|vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"]<p>**Preprocessing**:</p><p>- JAVASCRIPT: `var newvalue; switch(value) {   case "up":     newvalue = 1;     break;   case "down":     newvalue = 2;     break;   case "testing":     newvalue = 4;     break;   case "unknown":     newvalue = 5;     break;   case "dormant":     newvalue = 6;     break;   case "notPresent":     newvalue = 7;     break;   default:     newvalue = "Problem parsing interface operstate in JS"; } return newvalue;`</p>|
|Network_interfaces|Interface {#IFNAME}: Interface type|<p>Indicates the interface protocol type as a decimal value.</p><p>See include/uapi/linux/if_arp.h for all possible values.</p><p>Reference: https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net</p>|ZABBIX_PASSIVE|vfs.file.contents["/sys/class/net/{#IFNAME}/type"]|
|Status|System uptime|<p>-</p>|ZABBIX_PASSIVE|system.uptime|
|Storage|{#DEVNAME}: Disk read rate|<p>r/s. The number (after merges) of read requests completed per second for the device.</p>|DEPENDENT|vfs.dev.read.rate[{#DEVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.values['{#DEVNAME}'][3]`</p><p>- CHANGE_PER_SECOND|
|Storage|{#DEVNAME}: Disk write rate|<p>w/s. The number (after merges) of write requests completed per second for the device.</p>|DEPENDENT|vfs.dev.write.rate[{#DEVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.values['{#DEVNAME}'][7]`</p><p>- CHANGE_PER_SECOND|
|Storage|{#DEVNAME}: Disk read request avg waiting time (r_await)|<p>This formula contains two boolean expressions that evaluates to 1 or 0 in order to set calculated metric to zero and to avoid division by zero exception.</p>|CALCULATED|vfs.dev.read.await[{#DEVNAME}]<p>**Expression**:</p>`(last(vfs.dev.read.time.rate[{#DEVNAME}])/(last(vfs.dev.read.rate[{#DEVNAME}])+(last(vfs.dev.read.rate[{#DEVNAME}])=0)))*1000*(last(vfs.dev.read.rate[{#DEVNAME}]) > 0)`|
|Storage|{#DEVNAME}: Disk write request avg waiting time (w_await)|<p>This formula contains two boolean expressions that evaluates to 1 or 0 in order to set calculated metric to zero and to avoid division by zero exception.</p>|CALCULATED|vfs.dev.write.await[{#DEVNAME}]<p>**Expression**:</p>`(last(vfs.dev.write.time.rate[{#DEVNAME}])/(last(vfs.dev.write.rate[{#DEVNAME}])+(last(vfs.dev.write.rate[{#DEVNAME}])=0)))*1000*(last(vfs.dev.write.rate[{#DEVNAME}]) > 0)`|
|Storage|{#DEVNAME}: Disk average queue size (avgqu-sz)|<p>-</p>|DEPENDENT|vfs.dev.queue_size[{#DEVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.values['{#DEVNAME}'][13]`</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `0.001`</p>|
|Storage|{#DEVNAME}: Disk utilization|<p>-</p>|DEPENDENT|vfs.dev.util[{#DEVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.values['{#DEVNAME}'][12]`</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `0.1`</p>|
|Zabbix_raw_items|Get /proc/diskstats|<p>-</p>|ZABBIX_PASSIVE|vfs.file.contents[/proc/diskstats]<p>**Preprocessing**:</p><p>- JAVASCRIPT: `var parsed = value.split("\n").reduce(function(acc, x, i) {   acc["values"][x.split(/ +/)[3]] = x.split(/ +/).slice(1)   acc["lld"].push({"{#DEVNAME}":x.split(/ +/)[3]});   return acc; }, {"values":{}, "lld": []}); return JSON.stringify(parsed);`</p>|
|Zabbix_raw_items|{#DEVNAME}: Disk read time (rate)|<p>Rate of total read time counter. Used in r_await calculation</p>|DEPENDENT|vfs.dev.read.time.rate[{#DEVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.values['{#DEVNAME}'][6]`</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `0.001`</p>|
|Zabbix_raw_items|{#DEVNAME}: Disk write time (rate)|<p>Rate of total write time counter. Used in w_await calculation</p>|DEPENDENT|vfs.dev.write.time.rate[{#DEVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.values['{#DEVNAME}'][10]`</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `0.001`</p>|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Load average is too high|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:system.cpu.load[percpu,avg1].avg(5m)}>{$LOAD_AVG_CRIT}`|AVERAGE||
|{#FSNAME}: Disk space is critically low (used > {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"})|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</p><p>Two conditions should match: First, space utilization should be above {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"}.</p><p> Second condition should be one of the following:</p><p> - The disk free space is less than 5G.</p><p> - The disk will be full in less than 24hours.</p>|`{TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].last()}>{$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"} and (({Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},total].last()}-{Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},used].last()})<5G or {TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].timeleft(1h,,100)}<1d)`|AVERAGE|<p>Manual close: YES</p>|
|{#FSNAME}: Disk space is low (used > {$VFS.FS.PUSED.MAX.WARN:"{#FSNAME}"})|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</p><p>Two conditions should match: First, space utilization should be above {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"}.</p><p> Second condition should be one of the following:</p><p> - The disk free space is less than 10G.</p><p> - The disk will be full in less than 24hours.</p>|`{TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].last()}>{$VFS.FS.PUSED.MAX.WARN:"{#FSNAME}"} and (({Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},total].last()}-{Template OS Linux Zabbix agent:vfs.fs.size[{#FSNAME},used].last()})<10G or {TEMPLATE_NAME:vfs.fs.size[{#FSNAME},pused].timeleft(1h,,100)}<1d)`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- {#FSNAME}: Disk space is critically low (used > {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"})</p>|
|{#FSNAME}: Running out of free inodes (free < {$VFS.FS.INODE.PFREE.MIN.CRIT:"{#FSNAME}"}%)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>It may become impossible to write to disk if there are no index nodes left.</p><p>As symptoms, 'No space left on device' or 'Disk is full' errors may be seen even though free space is available.</p>|`{TEMPLATE_NAME:vfs.fs.inode[{#FSNAME},pfree].min(5m)}<{$VFS.FS.INODE.PFREE.MIN.CRIT:"{#FSNAME}"}`|AVERAGE||
|{#FSNAME}: Running out of free inodes (free < {$VFS.FS.INODE.PFREE.MIN.WARN:"{#FSNAME}"}%)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>It may become impossible to write to disk if there are no index nodes left.</p><p>As symptoms, 'No space left on device' or 'Disk is full' errors may be seen even though free space is available.</p>|`{TEMPLATE_NAME:vfs.fs.inode[{#FSNAME},pfree].min(5m)}<{$VFS.FS.INODE.PFREE.MIN.WARN:"{#FSNAME}"}`|WARNING|<p>**Depends on**:</p><p>- {#FSNAME}: Running out of free inodes (free < {$VFS.FS.INODE.PFREE.MIN.CRIT:"{#FSNAME}"}%)</p>|
|Lack of available memory ({ITEM.VALUE1} of {ITEM.VALUE2})|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:vm.memory.size[available].last(0)}<{$MEMORY_AVAILABLE_MIN} and {Template OS Linux Zabbix agent:vm.memory.size[total].last(0)}>0`|AVERAGE||
|High swap space usage (free: {ITEM.VALUE1}, total: {ITEM.VALUE2})|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This trigger is ignored, if there is no swap configured</p>|`{TEMPLATE_NAME:system.swap.size[,pfree].last()}<{$SWAP_PFREE_WARN} and {Template OS Linux Zabbix agent:system.swap.size[,total].last()}>0`|WARNING||
|Interface {#IFNAME}: High error rate|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Recovers when below 80% of {$IF_ERRORS_WARN:"{#IFNAME}"} threshold</p>|`{TEMPLATE_NAME:net.if.in["{#IFNAME}",errors].avg(5m)}>{$IF_ERRORS_WARN:"{#IFNAME}"} or {Template OS Linux Zabbix agent:net.if.out["{#IFNAME}",errors].avg(5m)}>{$IF_ERRORS_WARN:"{#IFNAME}"}`<p>Recovery expression:</p>`{TEMPLATE_NAME:net.if.in["{#IFNAME}",errors].avg(5m)}<{$IF_ERRORS_WARN:"{#IFNAME}"}*0.8 and {Template OS Linux Zabbix agent:net.if.out["{#IFNAME}",errors].avg(5m)}<{$IF_ERRORS_WARN:"{#IFNAME}"}*0.8`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}: Link down</p>|
|Interface {#IFNAME}: Link down|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Interface is down</p>|`{$IFCONTROL:"{#IFNAME}"}=1 and ({TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"].last()}=2 and {TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"].diff()}=1)`<p>Recovery expression:</p>`{TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"].last()}<>2`|AVERAGE||
|Interface {#IFNAME}: Ethernet has changed to lower speed than it was before|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of autonegotiation issues. Ack to close.</p>|`{TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].change()}<0 and {TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].last()}>0 and ({Template OS Linux Zabbix agent:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].last()}=6 or {Template OS Linux Zabbix agent:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].last()}=1) and ({Template OS Linux Zabbix agent:vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"].last()}<>2)`<p>Recovery expression:</p>`({TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].change()}>0 and {TEMPLATE_NAME:vfs.file.contents["/sys/class/net/{#IFNAME}/type"].prev()}>0) or ({Template OS Linux Zabbix agent:vfs.file.contents["/sys/class/net/{#IFNAME}/operstate"].last()}=2)`|INFO|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}: Link down</p>|
|{HOST.NAME} has been restarted (uptime < 10m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The device uptime is less than 10 minutes</p>|`{TEMPLATE_NAME:system.uptime.last()}<10m`|WARNING|<p>Manual close: YES</p>|
|{#DEVNAME}: Disk read request response are too high (read > {$VFS.DEV.READ.AWAIT.WARN:"{#DEVNAME}"} ms for 5m or write > {$VFS.DEV.WRITE.AWAIT.WARN:"{#DEVNAME}"} ms for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This trigger might indicate disk {#DEVNAME} saturation.</p>|`{TEMPLATE_NAME:vfs.dev.read.await[{#DEVNAME}].min(5m)} > {$VFS.DEV.READ.AWAIT.WARN:"{#DEVNAME}"} or {TEMPLATE_NAME:vfs.dev.read.await[{#DEVNAME}].min(5m)} > {$VFS.DEV.WRITE.AWAIT.WARN:"{#DEVNAME}"}`|WARNING|<p>Manual close: YES</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

## Known Issues

- Description: Network discovery. Zabbix agent as of 4.2 doesn't support items such as net.if.status, net.if.speed.
