# Template OS Linux *

Templates to monitor Linux by Zabbix agent, prometheus exporter and SNMP agent.

Three templates are available:  

- Template OS Linux Zabbix agent
- Template OS Linux Prom
- Template OS Linux SNMPv2

## Setup

TODO

## Zabix configuration

Change those macros on host level if needed:

|Macro|Description|Default|
|---|----|---|
|{$LOAD_AVG_CRIT}| | 1.5| 

## Items

See what items are collected in the templates.

|Item|Triggers|Graphs|Zabbix agent template|Prometheus template|SNMP template|
|---|---|---|---|---|--|
|system.cpu.load.avg1|y|y|y|y|-|
|system.cpu.load.avg5|-|y|y|y|-|
|system.cpu.load.avg15|-|y|y|y|-|
|system.cpu.num|-|-|-|y|-|
|system.cpu.util|
|system.cpu.system|
|system.cpu.user|
|system.cpu.nice|
|system.cpu.idle|
|system.cpu.iowait|
|system.cpu.interrupt|
|system.cpu.softirq|
|system.cpu.steal|
|system.cpu.guest|
|system.cpu.guest_nice|
|system.cpu.guest_nice|
|system.cpu.switches|
|system.cpu.intr|

## Triggers

See in template

## Demo

Available:

## Next steps





## References

http://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html
https://www.robustperception.io/understanding-machine-cpu-usage
https://stackoverflow.com/questions/23367857/accurate-calculation-of-cpu-usage-given-in-percentage-in-linux