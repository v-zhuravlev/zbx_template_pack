
# Template Net TP-LINK SNMPv2

## Overview

For Zabbix version: 4.0  
Link to MIBs: http://www.tp-linkru.com/download/T2600G-28TS.html#MIBs_Files</br>Sample device overview page: http://www.tp-linkru.com/products/details/cat-39_T2600G-28TS.html#overview</br>emulation page(web): http://www.tp-linkru.com/resources/simulator/T2600G-28TS(UN)_1.0/Index.htm

This template was tested on:

- T2600G-28TS revision 2.0, version 2.0.0 Build 20170628 Rel.55184(Beta)

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$MEMORY_UTIL_MAX}|-|90|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|
|Template Module Interfaces Simple SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|CPU Discovery|Discovering TPLINK-SYSMONITOR-MIB::tpSysMonitorCpuTable, displays the CPU utilization of all UNITs.|SNMP|
|Memory Discovery|Discovering TPLINK-SYSMONITOR-MIB::tpSysMonitorMemoryTable, displays the memory utilization of all UNITs.|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Hardware model name|MIB: TPLINK-SYSINFO-MIB</br>The hardware version of the product.|SNMP|
|Hardware serial number|MIB: TPLINK-SYSINFO-MIB</br>The Serial number of the product.|SNMP|
|Firmware version|MIB: TPLINK-SYSINFO-MIB</br>The software version of the product.|SNMP|
|Hardware version(revision)|MIB: TPLINK-SYSINFO-MIB</br>The hardware version of the product.|SNMP|
|#{#SNMPVALUE}: CPU utilization|MIB: TPLINK-SYSMONITOR-MIB</br>Displays the CPU utilization in 1 minute.</br>Reference: http://www.tp-link.com/faq-1330.html|SNMP|
|#{#SNMPVALUE}: Memory utilization|MIB: TPLINK-SYSMONITOR-MIB</br>Displays the memory utilization.</br>Reference: http://www.tp-link.com/faq-1330.html|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|INFO|
|#{#SNMPVALUE}: High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[tpSysMonitorCpu1Minute.{#SNMPINDEX}].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|
|#{#SNMPVALUE}: High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[tpSysMonitorMemoryUtilization.{#SNMPINDEX}].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|


