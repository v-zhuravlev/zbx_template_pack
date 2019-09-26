# Template OS Linux *

Templates to monitor Linux by Zabbix agent, prometheus exporter and SNMP agent.

Three templates are available:  

- Template OS Linux Zabbix agent
- Template OS Linux Prom
- Template OS Linux SNMPv2

## Setup

### Zabbix agent

Install Zabbix agent to Linux OS according to Zabbix documentation.

### Prom (Node exporter)

Install node exporter, change {$NODE_EXPORTER_PORT} on the host level value if needed.

### SNMP agent

Install snmpd agent on Linux OS, enable SNMPv2.  

Make sure access to UCD-SNMP-MIB is allowed from Zabbix server/proxy host, since  
by default snmpd (in Ubuntu) limits access to basic system information only:

```text
rocommunity public  default    -V systemonly
```

Make sure you change that in order to read metrics from UCD-SNMP-MIB.

Change {$SNMP_COMMUNITY} on the host level in Zabbix.

## Zabbix configuration

Change those macros on host level if needed:

|Macro|Description|Default|
|---|----|---|
|{$LOAD_AVG_CRIT}| | 1.5| 
|{$MEMORY_AVAILABLE_MIN}| | 20M |
|{$SWAP_PFREE_WARN}|Trigger(warning) if drops below this value, in % | 50 |
|{$VFS.FS.PUSED.MAX.WARN:"{#FSNAME}"}|Disk space trigger(warning) if above this value, in % | 80 |
|{$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"}|Disk space trigger(critical) if above this value, in % | 90 |
|{$VFS.FS.INODE.PFREE.MIN.CRIT:"{#FSNAME}"}|low percentage of free inode trigger(critical) if drops below this value, in % | 10 |
|{$VFS.FS.INODE.PFREE.MIN.WARN:"{#FSNAME}"}|low percentage of free inode trigger(warning) if drops below this value, in % | 20 |


## Items

See what items are collected in the templates.


|Item|Triggers|Graphs|Zabbix agent template|Prometheus template|SNMP template|
|---|---|---|---|---|--|
|system.cpu.load.avg1|y|y|y|y|y|
|system.cpu.load.avg5|-|y|y|y|y|
|system.cpu.load.avg15|-|y|y|y|y|
|system.cpu.num|y|-|-|y|y|
|system.cpu.util| y* | y | y | y | y |
|system.cpu.system| - | y | y | y | y |
|system.cpu.user| - | y | y | y | y |
|system.cpu.nice| - | y | y | y | y |
|system.cpu.idle| - | y | y | y | y |
|system.cpu.iowait| - | y | y | y | y |
|system.cpu.interrupt| - | y | y | y | y |
|system.cpu.softirq| - | y | y | y | y |
|system.cpu.steal| - | y | y | y | y |
|system.cpu.guest| - | y | y | y | y |
|system.cpu.guest_nice| - | y | y | y | y |
|system.cpu.switches| - | y | y | y | y |
|system.cpu.intr| - | y | y | y | y |
|vm.memory.total    | - | y | y | y | y |
|vm.memory.available| y | y | y | y | y |
|vm.memory.used    | - | - | - | - | - |
|vm.memory.cached    | - | - | - | - | y |
|vm.memory.buffers    | - | - | - | - | y |
|system.swap.total| y | - | y | y | y |
|system.swap.free| - | - | y | y | y |
|system.swap.pfree| y | - | y | y | y |
|vfs.fs.total| y | y | y | y | y |
|vfs.fs.free| - | - | y | y | - |
|vfs.fs.used| y | y | y | y | y |
|vfs.fs.pused| y | - | y | y | y |
|vfs.fs.inode.pfree| y | - | y | y | y |
|vfs.dev.read.rate| y | - | y | y | y |
|vfs.dev.write.rate| y | - | y | y | y |
|vfs.dev.read.await| y | - | y | y | - |
|vfs.dev.write.await| y | - | y | y | - |
|vfs.dev.queue_size| y | - | y | y | - |
|vfs.dev.util| y | - | y | y | y |

\* for SNMP only

### Memory



## Triggers

See in template

## Demo

Available:

## Next steps

- prom template: CPU usage for all cpus

## References

http://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html  
https://www.robustperception.io/understanding-machine-cpu-usage  
https://www.zabbix.com/documentation/4.2/manual/appendix/items/vm.memory.size_params  
https://blog.zabbix.com/when-alexei-isnt-looking/#vm.memory.size  
https://www.kernel.org/doc/gorman/html/understand/understand014.html  
https://serverfault.com/questions/714952/lack-of-free-swap-space-on-windows-server  
https://upload.wikimedia.org/wikipedia/commons/3/30/IO_stack_of_the_Linux_kernel.svg  
http://www.linfo.org/inode.html  
https://www.robustperception.io/mapping-iostat-to-the-node-exporters-node_disk_-metrics  
https://contextswitching.tumblr.com/post/156398304918/how-is-the-await-field-in-iostat-calculated  
https://www.kernel.org/doc/Documentation/ABI/testing/procfs-diskstats
https://support.zabbix.com/browse/ZBXNEXT-1302
http://www.net-snmp.org/docs/mibs/UCD-SNMP-MIB.txt
https://www.percona.com/blog/2017/08/28/looking-disk-utilization-and-saturation/  
https://en.wikipedia.org/wiki/Hard_disk_drive_performance_characteristics
https://www.kernel.org/doc/Documentation/filesystems/sysfs.txt
https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net
https://www.debian.org/releases/stable/armhf/apds01.en.html
https://docs.fedoraproject.org/en-US/Fedora/18/html/System_Administrators_Guide/sect-System_Monitoring_Tools-Net-SNMP-Retrieving.html

memory: 
https://stackoverflow.com/questions/31851951/monitor-real-memory-usage-in-linux-using-perl-and-snmp/31862651#31862651
