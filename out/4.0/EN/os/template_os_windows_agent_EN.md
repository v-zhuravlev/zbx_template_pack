
# Template OS Windows CPU by Zabbix agent

## Overview

For Zabbix version: 4.0  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|<p>-</p>|90|

## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|CPU|CPU utilisation, in %|<p>-</p>|ZABBIX_PASSIVE|system.cpu.util|
|CPU|Interrupt Time, %|<p>-</p>|ZABBIX_PASSIVE|wmi.get[root\cimv2,SELECT PercentInterruptTime FROM Win32_PerfFormattedData_PerfOS_Processor]|
|CPU|Load, %|<p>-</p>|ZABBIX_PASSIVE|wmi.get[root\cimv2,select PercentProcessorTime from Win32_PerfformattedData_PerfOS_Processor where Name='_Total']|
|CPU|Privileged time, %|<p>-</p>|ZABBIX_PASSIVE|wmi.get[root\cimv2, SELECT PercentPrivilegedTime FROM Win32_PerfFormattedData_PerfOS_Processor]|
|CPU|User time, %|<p>-</p>|ZABBIX_PASSIVE|wmi.get[root\cimv2,SELECT PercentUserTime FROM Win32_PerfFormattedData_PerfOS_Processor]|
|CPU|Queue Length|<p>-</p>|ZABBIX_PASSIVE|wmi.get[root\cimv2, SELECT ProcessorQueueLength FROM Win32_PerfFormattedData_PerfOS_System]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template OS Windows Filesystems by Zabbix agent

## Overview

For Zabbix version: 4.0  

## Setup


## Zabbix configuration



## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Mounted filesystem discovery|<p>Discovery of file systems of different types as defined in MACRO</p>|ZABBIX_PASSIVE|vfs.fs.discovery|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Filesystems|Filesystem {#FSNAME}: {#FSNAME}: Total disk space|<p>.</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},total]|
|Filesystems|Filesystem {#FSNAME}: {#FSNAME}: Used disk space|<p>.</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},used]|
|Filesystems|Filesystem {#FSNAME}: {#FSNAME}: Used disk space, %|<p>.</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},pused]|
|Filesystems|Filesystem {#FSNAME}: {#FSNAME}: Free disk space|<p>.</p>|ZABBIX_PASSIVE|vfs.fs.size[{#FSNAME},free]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template OS Windows Inventory by Zabbix agent

## Overview

For Zabbix version: 4.0  

## Setup


## Zabbix configuration



## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|General|System information|<p>-</p>|ZABBIX_PASSIVE|system.uname|
|General|System uptime|<p>-</p>|ZABBIX_PASSIVE|system.uptime|
|General|latest update installed days ago|<p>-</p>|ZABBIX_PASSIVE|custom.os.updates.latestupdatesinstalled|
|General|number of processes|<p>-</p>|ZABBIX_PASSIVE|proc.num[]|
|General|pending reboot|<p>-</p>|ZABBIX_PASSIVE|custom.os.pendingreboot|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Host has been restarted (uptime < 10m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The device uptime is less than 10 minutes</p>|`{TEMPLATE_NAME:system.uptime.last()}<10m`|WARNING|<p>Manual close: YES</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template OS Windows Memory by Zabbix agent

## Overview

For Zabbix version: 4.0  

## Setup


## Zabbix configuration



## Template links

There are no template links in this template.

## Discovery rules


## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Memory|Free memory|<p>-</p>|ZABBIX_PASSIVE|vm.memory.size[free]|
|Memory|Free swap space|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,free]|
|Memory|Free virtual memory, in %|<p>-</p>|ZABBIX_PASSIVE|vm.vmemory.size[pavailable]|
|Memory|Total memory|<p>-</p>|ZABBIX_PASSIVE|vm.memory.size[total]|
|Memory|Total swap space|<p>-</p>|ZABBIX_PASSIVE|system.swap.size[,total]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|

## Feedback

Please report any issues with the template at https://support.zabbix.com

# Template OS Windows by Zabbix agent

## Overview

For Zabbix version: 4.0  
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

