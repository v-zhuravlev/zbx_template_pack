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

Install snmpd agent on Linux OS, enable SNMPv2. change {$SNMP_COMMUNITY} on the host level in Zabbix.

## Zabix configuration

Change those macros on host level if needed:

|Macro|Description|Default|
|---|----|---|
|{$LOAD_AVG_CRIT}| | 1.5| 
|{$MEMORY_AVAILABLE_MIN}| | 20M |
|{$SWAP_PFREE_WARN}|Trigger(warning) if drops below this value, in % | 50 |


## Items

See what items are collected in the templates.

### CPU

|Item|Triggers|Graphs|Zabbix agent template|Prometheus template|SNMP template|
|---|---|---|---|---|--|
|system.cpu.load.avg1|y|y|y|y|-|
|system.cpu.load.avg5|-|y|y|y|-|
|system.cpu.load.avg15|-|y|y|y|-|
|system.cpu.num|-|-|-|y|-|
|system.cpu.util| y* | y | y | y | y |
|system.cpu.system| - | y | y | y | - |
|system.cpu.user| - | y | y | y | - |
|system.cpu.nice| - | y | y | y | - |
|system.cpu.idle| - | y | y | y | - |
|system.cpu.iowait| - | y | y | y | - |
|system.cpu.interrupt| - | y | y | y | - |
|system.cpu.softirq| - | y | y | y | - |
|system.cpu.steal| - | y | y | y | - |
|system.cpu.guest| - | y | y | y | - |
|system.cpu.guest_nice| - | y | y | y | - |
|system.cpu.switches| - | y | y | y | - |
|system.cpu.intr| - | y | y | y | - |
|vm.memory.total    | - | y | y | y | y |
|vm.memory.available| y | y | y | y | - |
|vm.memory.used    | - | - | - | - | y |
|vm.memory.pused| y | y | - | - | y |

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