
# Template OS Linux Prom

## Overview

For Zabbix version: 4.2  
This template collects Linux metrics from node_exporter 0.18 and above. Support for older node_exporter versions is provided as 'best effort'.

This template was tested on:

- node_exporter, version 0.17.0
- node_exporter, version 0.18.1

## Setup

Please refer to the node_exporter docs. Use node_exporter v0.18.0 or above

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|<p>-</p>|90|
|{$INODE_PFREE_CRIT}|<p>-</p>|10|
|{$INODE_PFREE_WARN}|<p>-</p>|20|
|{$LOAD_AVG_CRIT}|<p>-</p>|1.5|
|{$MEMORY_AVAILABLE_MIN}|<p>-</p>|20M|
|{$NODE_EXPORTER_PORT}|<p>TCP Port node_exporter is listening on.</p>|9100|
|{$SWAP_PFREE_WARN}|<p>-</p>|50|
|{$VFS.DEV.DEVNAME.MATCHES}|<p>This macro is used in block devices discovery. Can be overriden on the host or linked template level</p>|.+|
|{$VFS.DEV.DEVNAME.NOT_MATCHES}|<p>This macro is used in block devices discovery. Can be overriden on the host or linked template level</p>|(loop[0-9]*|sd[a-z][0-9]+|nbd[0-9]+|sr[0-9]+|fd[0-9]+)|
|{$VFS.DEV.READ.AWAIT.WARN}|<p>Disk read average response time (in ms) before the trigger would fire</p>|20|
|{$VFS.DEV.WRITE.AWAIT.WARN}|<p>Disk write average response time (in ms) before the trigger would fire</p>|20|
|{$VFS.FS.FSNAME.MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level</p>|.+|
|{$VFS.FS.FSNAME.NOT_MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level</p>|^(/dev|/sys|/run|/proc|.+/shm$)|
|{$VFS.FS.FSTYPE.MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level</p>|^(btrfs|ext2|ext3|ext4|reiser|xfs|ffs|ufs|jfs|jfs2|vxfs|hfs|apfs|refs|ntfs|fat32|zfs)$|
|{$VFS.FS.FSTYPE.NOT_MATCHES}|<p>This macro is used in filesystems discovery. Can be overriden on the host or linked template level</p>|^\s$|
|{$VFS.FS.PUSED.MAX.CRIT}|<p>-</p>|90|
|{$VFS.FS.PUSED.MAX.WARN}|<p>-</p>|80|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Network interface discovery|<p>Discovery of network interfaces as defined in global regular expression "Network interfaces for discovery".</p><p>Filtering:</p><p> - interfaces with operstate != 'up'.</p><p> - veth interfaces automatically created by Docker.</p>|DEPENDENT|node_exporter.net.if.discovery<p>**Preprocessing**:</p><p>- PROMETHEUS_TO_JSON: `{__name__=~"^node_network_info$"}`</p><p>**Filter**:</p>AND <p>- A: {#IFNAME} MATCHES_REGEX `@Network interfaces for discovery`</p><p>- B: {#IFNAME} NOT_MATCHES_REGEX `^veth[0-9a-z]+$`</p><p>- C: {#IFOPERSTATUS} MATCHES_REGEX `^up$`</p>|
|CPU discovery|<p>-</p>|DEPENDENT|node_exporter.cpu.discovery<p>**Preprocessing**:</p><p>- PROMETHEUS_TO_JSON: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu=~".+",mode="idle"}`</p>|
|Mounted filesystem discovery|<p>Discovery of file systems of different types.</p>|DEPENDENT|node_exporter.vfs.fs.discovery<p>**Preprocessing**:</p><p>- PROMETHEUS_TO_JSON: `{__name__=~"^node_filesystem_size(?:_bytes)?$", mountpoint=~".+"}`</p><p>**Filter**:</p>AND <p>- A: {#FSTYPE} MATCHES_REGEX `{$VFS.FS.FSTYPE.MATCHES}`</p><p>- B: {#FSTYPE} NOT_MATCHES_REGEX `{$VFS.FS.FSTYPE.NOT_MATCHES}`</p><p>- C: {#FSNAME} MATCHES_REGEX `{$VFS.FS.FSNAME.MATCHES}`</p><p>- D: {#FSNAME} NOT_MATCHES_REGEX `{$VFS.FS.FSNAME.NOT_MATCHES}`</p>|
|Block devices discovery|<p>-</p>|DEPENDENT|node_exporter.vfs.dev.discovery<p>**Preprocessing**:</p><p>- PROMETHEUS_TO_JSON: `node_disk_io_now{device=~".+"}`</p><p>**Filter**:</p>AND <p>- A: {#DEVNAME} MATCHES_REGEX `{$VFS.DEV.DEVNAME.MATCHES}`</p><p>- B: {#DEVNAME} NOT_MATCHES_REGEX `{$VFS.DEV.DEVNAME.NOT_MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|Load average (1m avg)|<p>-</p>|DEPENDENT|node_exporter.node_load1<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_load1 `</p>|
|CPU|Load average (5m avg)|<p>-</p>|DEPENDENT|node_exporter.node_load5<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_load5 `</p>|
|CPU|Load average (15m avg)|<p>-</p>|DEPENDENT|node_exporter.node_load15<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_load15 `</p>|
|CPU|Number of CPUs|<p>-</p>|DEPENDENT|node_exporter.system.cpu.num<p>**Preprocessing**:</p><p>- PROMETHEUS_TO_JSON: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu=~".+",mode="idle"}`</p><p>- JAVASCRIPT: `//count the number of cores return JSON.parse(value).length `</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|CPU|Interrupts per second|<p>-</p>|DEPENDENT|node_exporter.system.cpu.intr<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"node_intr"} `</p><p>- CHANGE_PER_SECOND|
|CPU|Context switches per second|<p>-</p>|DEPENDENT|node_exporter.system.cpu.switches<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"node_context_switches"} `</p><p>- CHANGE_PER_SECOND|
|CPU|#{#CPUNUM}: CPU utilization|<p>CPU utilization in %</p>|DEPENDENT|node_exporter.system.cpu.util[{#CPUNUM}]<p>**Preprocessing**:</p><p>- JAVASCRIPT: `//Calculate utilization return (100 - value)`</p>|
|CPU|#{#CPUNUM}: CPU idle time|<p>The time the CPU has spent doing nothing.</p>|DEPENDENT|node_exporter.system.cpu.idle[{#CPUNUM}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="idle"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `100`</p>|
|CPU|#{#CPUNUM}: CPU system time|<p>The time the CPU has spent running the kernel and its processes.</p>|DEPENDENT|node_exporter.system.cpu.system[{#CPUNUM}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="system"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `100`</p>|
|CPU|#{#CPUNUM}: CPU user time|<p>The time the CPU has spent running users' processes that are not niced.</p>|DEPENDENT|node_exporter.system.cpu.user[{#CPUNUM}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="user"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `100`</p>|
|CPU|#{#CPUNUM}: CPU steal time|<p>The amount of CPU 'stolen' from this virtual machine by the hypervisor for other tasks (such as running another virtual machine).</p>|DEPENDENT|node_exporter.system.cpu.steal[{#CPUNUM}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="steal"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `100`</p>|
|CPU|#{#CPUNUM}: CPU softirq time|<p>The amount of time the CPU has been servicing software interrupts.</p>|DEPENDENT|node_exporter.system.cpu.softirq[{#CPUNUM}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="softirq"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `100`</p>|
|CPU|#{#CPUNUM}: CPU nice time|<p>The time the CPU has spent running users' processes that have been niced.</p>|DEPENDENT|node_exporter.system.cpu.nice[{#CPUNUM}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="nice"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `100`</p>|
|CPU|#{#CPUNUM}: CPU iowait time|<p>Amount of time the CPU has been waiting for I/O to complete.</p>|DEPENDENT|node_exporter.system.cpu.iowait[{#CPUNUM}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="iowait"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `100`</p>|
|CPU|#{#CPUNUM}: CPU interrupt time|<p>The amount of time the CPU has been servicing hardware interrupts.</p>|DEPENDENT|node_exporter.system.cpu.interrupt[{#CPUNUM}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_seconds_total)?$",cpu="{#CPUNUM}",mode="irq"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `100`</p>|
|CPU|#{#CPUNUM}: CPU guest time|<p>Guest  time (time  spent  running  a  virtual  CPU  for  a  guest  operating  system)</p>|DEPENDENT|node_exporter.system.cpu.guest[{#CPUNUM}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_guest_seconds_total)?$",cpu="{#CPUNUM}",mode=~"^(?:user|guest)$"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `100`</p>|
|CPU|#{#CPUNUM}: CPU guest nice time|<p>Time spent running a niced guest (virtual CPU for guest operating systems under the control of the Linux kernel)</p>|DEPENDENT|node_exporter.system.cpu.guest_nice[{#CPUNUM}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_cpu(?:_guest_seconds_total)?$",cpu="{#CPUNUM}",mode=~"^(?:nice|guest_nice)$"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `100`</p>|
|Memory|Total memory|<p>Total memory in Bytes</p>|DEPENDENT|node_exporter.node_memory_memtotal_bytes<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"node_memory_MemTotal"} `</p>|
|Memory|Available memory|<p>Available memory, in Linux, available = free + buffers + cache. On other platforms calculation may vary. See also: https://www.zabbix.com/documentation/current/manual/appendix/items/vm.memory.size_params</p>|DEPENDENT|node_exporter.node_memory_memavailable_bytes<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"node_memory_MemAvailable"} `</p>|
|Memory|Total swap space|<p>-</p>|DEPENDENT|node_exporter.node_memory_swaptotal_bytes<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"node_memory_SwapTotal"} `</p>|
|Memory|Free swap space|<p>-</p>|DEPENDENT|node_exporter.node_memory_swapfree_bytes<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"node_memory_SwapFree"} `</p>|
|Memory|Free swap space in %|<p>-</p>|CALCULATED|node_exporter.system.swap.pfree<p>**Expression**:</p>`((last(node_exporter.node_memory_swapfree_bytes))/last(node_exporter.node_memory_swaptotal_bytes))*100`|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Bits received||DEPENDENT|node_exporter.net.if.in["{#IFNAME}"]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_network_receive_bytes_total{device="{#IFNAME}"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `8`</p>|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Bits sent||DEPENDENT|node_exporter.net.if.out["{#IFNAME}"]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_network_transmit_bytes_total{device="{#IFNAME}"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `8`</p>|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Outbound packets with errors||DEPENDENT|node_exporter.net.if.out.errors["{#IFNAME}"]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_network_transmit_errs_total{device="{#IFNAME}"} `</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Inbound packets with errors||DEPENDENT|node_exporter.net.if.in.errors["{#IFNAME}"]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_network_receive_errs_total{device="{#IFNAME}"} `</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Inbound packets discarded||DEPENDENT|node_exporter.net.if.in.discards["{#IFNAME}"]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_network_receive_drop_total{device="{#IFNAME}"} `</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Outbound packets discarded||DEPENDENT|node_exporter.net.if.out.discards["{#IFNAME}"]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_network_transmit_drop_total{device="{#IFNAME}"} `</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Speed||DEPENDENT|node_exporter.net.if.speed["{#IFNAME}"]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_network_speed_bytes{device="{#IFNAME}"} `</p><p>- MULTIPLIER: `8`</p>|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Interface type|<p>node_network_protocol_type protocol_type value of /sys/class/net/<iface>.</p>|DEPENDENT|node_exporter.net.if.type["{#IFNAME}"]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_network_protocol_type{device="{#IFNAME}"} `</p>|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Operational status|<p>Indicates the interface RFC2863 operational state as a string.</p><p>Possible values are:"unknown", "notpresent", "down", "lowerlayerdown", "testing","dormant", "up".</p><p>Reference: https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net</p>|DEPENDENT|node_exporter.net.if.status["{#IFNAME}"]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_network_info{device="{#IFNAME}"} operstate`</p><p>- JAVASCRIPT: `var newvalue; switch(value) {   case "up":     newvalue = 1;     break;   case "down":     newvalue = 2;     break;   case "testing":     newvalue = 4;     break;   case "unknown":     newvalue = 5;     break;   case "dormant":     newvalue = 6;     break;   case "notPresent":     newvalue = 7;     break;   default:     newvalue = "Problem parsing interface operstate in JS"; } return newvalue;`</p>|
|Status|System uptime|<p>-</p>|DEPENDENT|system.uptime<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_boot_time(?:_seconds)?$"} `</p><p>- JAVASCRIPT: `//use boottime to calculate uptime return (Math.floor(Date.now()/1000)-Number(value));`</p>|
|Storage|{#FSNAME}: Free space|<p>-</p>|DEPENDENT|vfs.fs.free[{#FSNAME}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_filesystem_avail(?:_bytes)?$", mountpoint="{#FSNAME}"} `</p>|
|Storage|{#FSNAME}: Total space|<p>Total space in Bytes</p>|DEPENDENT|node_exporter.vfs.fs.total[{#FSNAME}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `{__name__=~"^node_filesystem_size(?:_bytes)?$", mountpoint="{#FSNAME}"} `</p>|
|Storage|{#FSNAME}: Used space|<p>Used storage in Bytes</p>|CALCULATED|node_exporter.vfs.fs.used[{#FSNAME}]<p>**Expression**:</p>`(last(node_exporter.vfs.fs.total[{#FSNAME}])-last(vfs.fs.free[{#FSNAME}]))`|
|Storage|{#FSNAME}: Space utilization|<p>Space utilization in % for {#FSNAME}</p>|CALCULATED|node_exporter.vfs.fs.pused[{#FSNAME}]<p>**Expression**:</p>`(last(node_exporter.vfs.fs.used[{#FSNAME}])/(last(vfs.fs.free[{#FSNAME}])+last(node_exporter.vfs.fs.used[{#FSNAME}])))*100`|
|Storage|{#FSNAME}: Free inodes in %|<p>-</p>|DEPENDENT|node_exporter.vfs.fs.inode.pfree[{#FSNAME}]<p>**Preprocessing**:</p><p>- PROMETHEUS_TO_JSON: `{__name__=~"node_filesystem_files.*",mountpoint="{#FSNAME}"}`</p><p>- JAVASCRIPT: `//count vfs.fs.inode.pfree var inode_free; var inode_total; JSON.parse(value).forEach(function(metric) {   if (metric['name'] == 'node_filesystem_files'){       inode_total = metric['value'];   } else if (metric['name'] == 'node_filesystem_files_free'){       inode_free = metric['value'];   } }); return (inode_free/inode_total)*100;`</p>|
|Storage|{#DEVNAME}: Disk read rate|<p>r/s. The number (after merges) of read requests completed per second for the device.</p>|DEPENDENT|node_exporter.vfs.dev.read.rate[{#DEVNAME}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_disk_reads_completed_total{device="{#DEVNAME}"} `</p><p>- CHANGE_PER_SECOND|
|Storage|{#DEVNAME}: Disk write rate|<p>w/s. The number (after merges) of write requests completed per second for the device.</p>|DEPENDENT|node_exporter.vfs.dev.write.rate[{#DEVNAME}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_disk_writes_completed_total{device="{#DEVNAME}"} `</p><p>- CHANGE_PER_SECOND|
|Storage|{#DEVNAME}: Disk read request avg waiting time (r_await)|<p>This formula contains two boolean expressions that evaluates to 1 or 0 in order to set calculated metric to zero and to avoid division by zero exception.</p>|CALCULATED|node_exporter.vfs.dev.read.await[{#DEVNAME}]<p>**Expression**:</p>`(last(node_exporter.vfs.dev.read.time.rate[{#DEVNAME}])/(last(node_exporter.vfs.dev.read.rate[{#DEVNAME}])+(last(node_exporter.vfs.dev.read.rate[{#DEVNAME}])=0)))*1000*(last(node_exporter.vfs.dev.read.rate[{#DEVNAME}]) > 0)`|
|Storage|{#DEVNAME}: Disk write request avg waiting time (w_await)|<p>This formula contains two boolean expressions that evaluates to 1 or 0 in order to set calculated metric to zero and to avoid division by zero exception.</p>|CALCULATED|node_exporter.vfs.dev.write.await[{#DEVNAME}]<p>**Expression**:</p>`(last(node_exporter.vfs.dev.write.time.rate[{#DEVNAME}])/(last(node_exporter.vfs.dev.write.rate[{#DEVNAME}])+(last(node_exporter.vfs.dev.write.rate[{#DEVNAME}])=0)))*1000*(last(node_exporter.vfs.dev.write.rate[{#DEVNAME}]) > 0)`|
|Storage|{#DEVNAME}: Disk average queue size (avgqu-sz)|<p>-</p>|DEPENDENT|node_exporter.vfs.dev.queue_size[{#DEVNAME}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_disk_io_time_weighted_seconds_total{device="{#DEVNAME}"} `</p><p>- CHANGE_PER_SECOND|
|Storage|{#DEVNAME}: Disk utilization|<p>-</p>|DEPENDENT|node_exporter.vfs.dev.util[{#DEVNAME}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_disk_io_time_seconds_total{device="{#DEVNAME}"} `</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `100`</p>|
|Zabbix_raw_items|Get node_exporter metrics|<p>-</p>|HTTP_AGENT|node_exporter.get|
|Zabbix_raw_items|{#DEVNAME}: Disk read time (rate)|<p>Rate of total read time counter. Used in r_await calculation</p>|DEPENDENT|node_exporter.vfs.dev.read.time.rate[{#DEVNAME}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_disk_read_time_seconds_total{device="{#DEVNAME}"} `</p><p>- CHANGE_PER_SECOND|
|Zabbix_raw_items|{#DEVNAME}: Disk write time (rate)|<p>Rate of total write time counter. Used in w_await calculation</p>|DEPENDENT|node_exporter.vfs.dev.write.time.rate[{#DEVNAME}]<p>**Preprocessing**:</p><p>- PROMETHEUS_PATTERN: `node_disk_write_time_seconds_total{device="{#DEVNAME}"} `</p><p>- CHANGE_PER_SECOND|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Load average is too high|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:node_exporter.node_load1.avg(5m)}/{Template OS Linux Prom:node_exporter.system.cpu.num.last()}>{$LOAD_AVG_CRIT}`|AVERAGE||
|Lack of available memory ({ITEM.VALUE1} of {ITEM.VALUE2})|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:node_exporter.node_memory_memavailable_bytes.last(0)}<{$MEMORY_AVAILABLE_MIN} and {Template OS Linux Prom:node_exporter.node_memory_memtotal_bytes.last(0)}>0`|AVERAGE||
|High swap space usage (free: {ITEM.VALUE1}, total: {ITEM.VALUE2})|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This trigger is ignored, if there is no swap configured</p>|`{TEMPLATE_NAME:node_exporter.system.swap.pfree.last()}<{$SWAP_PFREE_WARN} and {Template OS Linux Prom:node_exporter.node_memory_swaptotal_bytes.last()}>0`|WARNING||
|Interface {#IFNAME}({#IFALIAS}): High bandwidth usage >{$IF_UTIL_MAX:"{#IFNAME}"}%|<p>Last value: {ITEM.LASTVALUE1}.</p>|`({TEMPLATE_NAME:node_exporter.net.if.in["{#IFNAME}"].avg(15m)}>({$IF_UTIL_MAX:"{#IFNAME}"}/100)*{Template OS Linux Prom:node_exporter.net.if.speed["{#IFNAME}"].last()} or {Template OS Linux Prom:node_exporter.net.if.out["{#IFNAME}"].avg(15m)}>({$IF_UTIL_MAX:"{#IFNAME}"}/100)*{Template OS Linux Prom:node_exporter.net.if.speed["{#IFNAME}"].last()}) and {Template OS Linux Prom:node_exporter.net.if.speed["{#IFNAME}"].last()}>0`<p>Recovery expression:</p>`{TEMPLATE_NAME:node_exporter.net.if.in["{#IFNAME}"].avg(15m)}<(({$IF_UTIL_MAX:"{#IFNAME}"}-3)/100)*{Template OS Linux Prom:node_exporter.net.if.speed["{#IFNAME}"].last()} and {Template OS Linux Prom:node_exporter.net.if.out["{#IFNAME}"].avg(15m)}<(({$IF_UTIL_MAX:"{#IFNAME}"}-3)/100)*{Template OS Linux Prom:node_exporter.net.if.speed["{#IFNAME}"].last()}`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}({#IFALIAS}): Link down</p>|
|Interface {#IFNAME}({#IFALIAS}): High error rate|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Recovers when below 80% of {$IF_ERRORS_WARN:"{#IFNAME}"} threshold</p>|`{TEMPLATE_NAME:node_exporter.net.if.in.errors["{#IFNAME}"].avg(5m)}>{$IF_ERRORS_WARN:"{#IFNAME}"} or {Template OS Linux Prom:node_exporter.net.if.out.errors["{#IFNAME}"].avg(5m)}>{$IF_ERRORS_WARN:"{#IFNAME}"}`<p>Recovery expression:</p>`{TEMPLATE_NAME:node_exporter.net.if.in.errors["{#IFNAME}"].avg(5m)}<{$IF_ERRORS_WARN:"{#IFNAME}"}*0.8 and {Template OS Linux Prom:node_exporter.net.if.out.errors["{#IFNAME}"].avg(5m)}<{$IF_ERRORS_WARN:"{#IFNAME}"}*0.8`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}({#IFALIAS}): Link down</p>|
|Interface {#IFNAME}({#IFALIAS}): Ethernet has changed to lower speed than it was before|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of autonegotiation issues. Ack to close.</p>|`{TEMPLATE_NAME:node_exporter.net.if.speed["{#IFNAME}"].change()}<0 and {TEMPLATE_NAME:node_exporter.net.if.speed["{#IFNAME}"].last()}>0 and ( {Template OS Linux Prom:node_exporter.net.if.type["{#IFNAME}"].last()}=6 or {Template OS Linux Prom:node_exporter.net.if.type["{#IFNAME}"].last()}=7 or {Template OS Linux Prom:node_exporter.net.if.type["{#IFNAME}"].last()}=11 or {Template OS Linux Prom:node_exporter.net.if.type["{#IFNAME}"].last()}=62 or {Template OS Linux Prom:node_exporter.net.if.type["{#IFNAME}"].last()}=69 or {Template OS Linux Prom:node_exporter.net.if.type["{#IFNAME}"].last()}=117 ) and ({Template OS Linux Prom:node_exporter.net.if.status["{#IFNAME}"].last()}<>2)`<p>Recovery expression:</p>`({TEMPLATE_NAME:node_exporter.net.if.speed["{#IFNAME}"].change()}>0 and {TEMPLATE_NAME:node_exporter.net.if.speed["{#IFNAME}"].prev()}>0) or ({Template OS Linux Prom:node_exporter.net.if.status["{#IFNAME}"].last()}=2)`|INFO|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}({#IFALIAS}): Link down</p>|
|Interface {#IFNAME}({#IFALIAS}): Ethernet has changed to lower speed than it was before|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of autonegotiation issues. Ack to close.</p>|`{TEMPLATE_NAME:node_exporter.net.if.type["{#IFNAME}"].change()}<0 and {TEMPLATE_NAME:node_exporter.net.if.type["{#IFNAME}"].last()}>0 and ({Template OS Linux Prom:node_exporter.net.if.type["{#IFNAME}"].last()}=6 or {Template OS Linux Prom:node_exporter.net.if.type["{#IFNAME}"].last()}=1) and ({Template OS Linux Prom:node_exporter.net.if.status["{#IFNAME}"].last()}<>2)`<p>Recovery expression:</p>`({TEMPLATE_NAME:node_exporter.net.if.type["{#IFNAME}"].change()}>0 and {TEMPLATE_NAME:node_exporter.net.if.type["{#IFNAME}"].prev()}>0) or ({Template OS Linux Prom:node_exporter.net.if.status["{#IFNAME}"].last()}=2)`|INFO|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}({#IFALIAS}): Link down</p>|
|Interface {#IFNAME}({#IFALIAS}): Link down|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Interface is down</p>|`{$IFCONTROL:"{#IFNAME}"}=1 and ({TEMPLATE_NAME:node_exporter.net.if.status["{#IFNAME}"].last()}=2 and {TEMPLATE_NAME:node_exporter.net.if.status["{#IFNAME}"].diff()}=1)`<p>Recovery expression:</p>`{TEMPLATE_NAME:node_exporter.net.if.status["{#IFNAME}"].last()}<>2`|AVERAGE||
|{HOST.NAME} has been restarted (uptime < 10m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The device uptime is less than 10 minutes</p>|`{TEMPLATE_NAME:system.uptime.last()}<10m`|WARNING|<p>Manual close: YES</p>|
|{#FSNAME}: Disk space is critically low (used > {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"})|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</p><p>Two conditions should match: First, space utilization should be above {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"}.</p><p> Second condition should be one of the following:</p><p> - The disk free space is less than 5G.</p><p> - The disk will be full in less than 24hours.</p>|`{TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].last()}>{$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"} and (({Template OS Linux Prom:node_exporter.vfs.fs.total[{#FSNAME}].last()}-{Template OS Linux Prom:node_exporter.vfs.fs.used[{#FSNAME}].last()})<5G or {TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].timeleft(1h,,100)}<1d)`|AVERAGE|<p>Manual close: YES</p>|
|{#FSNAME}: Disk space is low (used > {$VFS.FS.PUSED.MAX.WARN:"{#FSNAME}"})|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Space used: {ITEM.VALUE3} of {ITEM.VALUE2} ({ITEM.VALUE1}), time left till full: < 24h.</p><p>Two conditions should match: First, space utilization should be above {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"}.</p><p> Second condition should be one of the following:</p><p> - The disk free space is less than 10G.</p><p> - The disk will be full in less than 24hours.</p>|`{TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].last()}>{$VFS.FS.PUSED.MAX.WARN:"{#FSNAME}"} and (({Template OS Linux Prom:node_exporter.vfs.fs.total[{#FSNAME}].last()}-{Template OS Linux Prom:node_exporter.vfs.fs.used[{#FSNAME}].last()})<10G or {TEMPLATE_NAME:node_exporter.vfs.fs.pused[{#FSNAME}].timeleft(1h,,100)}<1d)`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- {#FSNAME}: Disk space is critically low (used > {$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"})</p>|
|{#FSNAME}: Free inodes is critically low, below {$INODE_PFREE_CRIT:"{#FSNAME}"}%|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:node_exporter.vfs.fs.inode.pfree[{#FSNAME}].last()}<{$INODE_PFREE_CRIT:"{#FSNAME}"}`|AVERAGE||
|{#FSNAME}: Free inodes is below {$INODE_PFREE_WARN:"{#FSNAME}"}%|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:node_exporter.vfs.fs.inode.pfree[{#FSNAME}].last()}<{$INODE_PFREE_WARN:"{#FSNAME}"}`|WARNING|<p>**Depends on**:</p><p>- {#FSNAME}: Free inodes is critically low, below {$INODE_PFREE_CRIT:"{#FSNAME}"}%</p>|
|{#DEVNAME}: Disk read request response are too high (read > {$VFS.DEV.READ.AWAIT.WARN:"{#DEVNAME}"} ms for 5m or write > {$VFS.DEV.WRITE.AWAIT.WARN:"{#DEVNAME}"} ms for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This trigger might indicate disk {#DEVNAME} saturation.</p>|`{TEMPLATE_NAME:node_exporter.vfs.dev.read.await[{#DEVNAME}].min(5m)} > {$VFS.DEV.READ.AWAIT.WARN:"{#DEVNAME}"} or {TEMPLATE_NAME:node_exporter.vfs.dev.read.await[{#DEVNAME}].min(5m)} > {$VFS.DEV.WRITE.AWAIT.WARN:"{#DEVNAME}"}`|WARNING|<p>Manual close: YES</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

## Known Issues

- Description: node_exporter v0.16.0 renamed many metrics. CPU utilisation for 'guest' and 'guest_nice' metrics are not supported in this template with node_exporter < 0.16. Disk IO metrics are not supported. Other metrics provided as 'best effort'.  
 See https://github.com/prometheus/node_exporter/releases/tag/v0.16.0 for details.
  - Version: below 0.16.0

- Description: metric node_network_info with label 'device' cannot be found, so network discovery is not possible.
  - Version: below 0.18


## References

https://github.com/prometheus/node_exporter
