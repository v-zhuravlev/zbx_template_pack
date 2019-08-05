
# Template Module Cisco CISCO-MEMORY-POOL-MIB SNMPv2

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$MEMORY_UTIL_MAX}|-|90|


## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Memory Discovery|Discovery of ciscoMemoryPoolTable, a table of memory pool monitoring entries.</br>http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15216-contiguous-memory.html|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|{#SNMPVALUE}: Used memory|MIB: CISCO-MEMORY-POOL-MIB</br>Indicates the number of bytes from the memory pool that are currently in use by applications on the managed device.</br>Reference: http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15216-contiguous-memory.html|SNMP|
|{#SNMPVALUE}: Free memory|MIB: CISCO-MEMORY-POOL-MIB</br>Indicates the number of bytes from the memory pool that are currently unused on the managed device. Note that the sum of ciscoMemoryPoolUsed and ciscoMemoryPoolFree is the total amount of memory in the pool</br>Reference: http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15216-contiguous-memory.html|SNMP|
|{#SNMPVALUE}: Memory utilization|Memory utilization in %|CALCULATED|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|{#SNMPVALUE}: High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[vm.memory.pused.{#SNMPINDEX}].avg(5m)}>{$MEMORY_UTIL_MAX}`|AVERAGE|

# Template Module Cisco CISCO-PROCESS-MIB SNMPv2

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|


## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|CPU Discovery|If your IOS device has several CPUs, you must use CISCO-PROCESS-MIB and its object cpmCPUTotal5minRev from the table called cpmCPUTotalTable ,</br>indexed with cpmCPUTotalIndex .</br>This table allows CISCO-PROCESS-MIB to keep CPU statistics for different physical entities in the router,</br>like different CPU chips, group of CPUs, or CPUs in different modules/cards.</br>In case of a single CPU, cpmCPUTotalTable has only one entry.|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|#{#SNMPINDEX}: CPU utilization|MIB: CISCO-PROCESS-MIB</br>The cpmCPUTotal5minRev MIB object provides a more accurate view of the performance of the router over time than the MIB objects cpmCPUTotal1minRev and cpmCPUTotal5secRev . These MIB objects are not accurate because they look at CPU at one minute and five second intervals, respectively. These MIBs enable you to monitor the trends and plan the capacity of your network. The recommended baseline rising threshold for cpmCPUTotal5minRev is 90 percent. Depending on the platform, some routers that run at 90 percent, for example, 2500s, can exhibit performance degradation versus a high-end router, for example, the 7500 series, which can operate fine.</br>Reference: http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15215-collect-cpu-util-snmp.html|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|#{#SNMPINDEX}: High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[cpmCPUTotal5minRev.{#SNMPINDEX}].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|

# Template Module Cisco CISCO-PROCESS-MIB IOS versions 12.0_3_T-12.2_3.5 SNMPv2

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|


## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|CPU Discovery|If your IOS device has several CPUs, you must use CISCO-PROCESS-MIB and its object cpmCPUTotal5minRev from the table called cpmCPUTotalTable ,</br>indexed with cpmCPUTotalIndex .</br>This table allows CISCO-PROCESS-MIB to keep CPU statistics for different physical entities in the router,</br>like different CPU chips, group of CPUs, or CPUs in different modules/cards.</br>In case of a single CPU, cpmCPUTotalTable has only one entry.|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|{#SNMPVALUE}: CPU utilization|MIB: CISCO-PROCESS-MIB</br>The overall CPU busy percentage in the last 5 minute</br>period. This object deprecates the avgBusy5 object from</br>the OLD-CISCO-SYSTEM-MIB. This object is deprecated</br>by cpmCPUTotal5minRev which has the changed range</br>of value (0..100)</br>Reference: http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15215-collect-cpu-util-snmp.html|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|{#SNMPVALUE}: High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[cpmCPUTotal5min.{#SNMPINDEX}].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|

# Template Module Cisco OLD-CISCO-CPU-MIB SNMPv2

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|


## Discovery rules


## Items collected

|Name|Description|Type|
|----|-----------|----|
|CPU utilization|MIB: OLD-CISCO-CPU-MIB</br>5 minute exponentially-decayed moving average of the CPU busy percentage.</br>Reference: http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15215-collect-cpu-util-snmp.html|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[avgBusy5].avg(5m)}>{$CPU_UTIL_MAX}`|AVERAGE|

# Template Module Cisco Inventory SNMPv2

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration




## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Entity Serial Numbers Discovery|-|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Hardware model name|MIB: ENTITY-MIB</br>|SNMP|
|Hardware serial number|MIB: ENTITY-MIB</br>|SNMP|
|Operating system|MIB: SNMPv2-MIB</br>|SNMP|
|{#ENT_NAME}: Hardware serial number|MIB: ENTITY-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|
|{#ENT_NAME}: Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[entPhysicalSerialNum.{#SNMPINDEX}].strlen()}>0`|INFO|

# Template Module Cisco CISCO-ENVMON-MIB SNMPv2

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$FAN_CRIT_STATUS:"critical"}|-|3|
|{$FAN_CRIT_STATUS:"shutdown"}|-|4|
|{$FAN_WARN_STATUS:"notFunctioning"}|-|6|
|{$FAN_WARN_STATUS:"warning"}|-|2|
|{$PSU_CRIT_STATUS:"critical"}|-|3|
|{$PSU_CRIT_STATUS:"shutdown"}|-|4|
|{$PSU_WARN_STATUS:"notFunctioning"}|-|6|
|{$PSU_WARN_STATUS:"warning"}|-|2|
|{$TEMP_CRIT:"CPU"}|-|75|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT_STATUS}|-|3|
|{$TEMP_CRIT}|-|60|
|{$TEMP_DISASTER_STATUS}|-|4|
|{$TEMP_WARN:"CPU"}|-|70|
|{$TEMP_WARN_STATUS}|-|2|
|{$TEMP_WARN}|-|50|


## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Temperature Discovery|Discovery of ciscoEnvMonTemperatureTable (ciscoEnvMonTemperatureDescr), a table of ambient temperature status</br>maintained by the environmental monitor.|SNMP|
|PSU Discovery|The table of power supply status maintained by the environmental monitor card.|SNMP|
|FAN Discovery|The table of fan status maintained by the environmental monitor.|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|{#SNMPVALUE}: Temperature|MIB: CISCO-ENVMON-MIB</br>The current measurement of the test point being instrumented.|SNMP|
|{#SNMPVALUE}: Temperature status|MIB: CISCO-ENVMON-MIB</br>The current state of the test point being instrumented.|SNMP|
|{#SENSOR_INFO}: Power supply status|MIB: CISCO-ENVMON-MIB</br>|SNMP|
|{#SENSOR_INFO}: Fan status|MIB: CISCO-ENVMON-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|{#SNMPVALUE}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[ciscoEnvMonTemperatureValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""} or {Template Module Cisco CISCO-ENVMON-MIB SNMPv2:sensor.temp.status[ciscoEnvMonTemperatureState.{#SNMPINDEX}].last(0)}={$TEMP_WARN_STATUS}`|WARNING|
|{#SNMPVALUE}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[ciscoEnvMonTemperatureValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""} or {Template Module Cisco CISCO-ENVMON-MIB SNMPv2:sensor.temp.status[ciscoEnvMonTemperatureState.{#SNMPINDEX}].last(0)}={$TEMP_CRIT_STATUS} or {Template Module Cisco CISCO-ENVMON-MIB SNMPv2:sensor.temp.status[ciscoEnvMonTemperatureState.{#SNMPINDEX}].last(0)}={$TEMP_DISASTER_STATUS}`|HIGH|
|{#SNMPVALUE}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[ciscoEnvMonTemperatureValue.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|AVERAGE|
|{#SENSOR_INFO}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[ciscoEnvMonSupplyState.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS:"critical"},eq)}=1 or {TEMPLATE_NAME:sensor.psu.status[ciscoEnvMonSupplyState.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS:"shutdown"},eq)}=1`|AVERAGE|
|{#SENSOR_INFO}: Power supply is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[ciscoEnvMonSupplyState.{#SNMPINDEX}].count(#1,{$PSU_WARN_STATUS:"warning"},eq)}=1 or {TEMPLATE_NAME:sensor.psu.status[ciscoEnvMonSupplyState.{#SNMPINDEX}].count(#1,{$PSU_WARN_STATUS:"notFunctioning"},eq)}=1`|WARNING|
|{#SENSOR_INFO}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[ciscoEnvMonFanState.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"critical"},eq)}=1 or {TEMPLATE_NAME:sensor.fan.status[ciscoEnvMonFanState.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"shutdown"},eq)}=1`|AVERAGE|
|{#SENSOR_INFO}: Fan is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[ciscoEnvMonFanState.{#SNMPINDEX}].count(#1,{$FAN_WARN_STATUS:"warning"},eq)}=1 or {TEMPLATE_NAME:sensor.fan.status[ciscoEnvMonFanState.{#SNMPINDEX}].count(#1,{$FAN_WARN_STATUS:"notFunctioning"},eq)}=1`|WARNING|

# Template Net Cisco IOS SNMPv2

## Overview

For Zabbix version: 3.4  

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.


## Template links

|Name|
|----|
|Template Module Cisco CISCO-ENVMON-MIB SNMPv2|
|Template Module Cisco CISCO-MEMORY-POOL-MIB SNMPv2|
|Template Module Cisco CISCO-PROCESS-MIB SNMPv2|
|Template Module Cisco Inventory SNMPv2|
|Template Module EtherLike-MIB SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules


## Items collected

|Name|Description|Type|
|----|-----------|----|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|

# Template Net Cisco IOS versions 12.0_3_T-12.2_3.5 SNMPv2

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration



## Template links

|Name|
|----|
|Template Module Cisco CISCO-ENVMON-MIB SNMPv2|
|Template Module Cisco CISCO-MEMORY-POOL-MIB SNMPv2|
|Template Module Cisco CISCO-PROCESS-MIB IOS versions 12.0_3_T-12.2_3.5 SNMPv2|
|Template Module Cisco Inventory SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules


## Items collected

|Name|Description|Type|
|----|-----------|----|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|

# Template Net Cisco IOS prior to 12.0_3_T SNMPv2

## Overview

For Zabbix version: 3.4  

## Setup


## Zabbix configuration



## Template links

|Name|
|----|
|Template Module Cisco CISCO-ENVMON-MIB SNMPv2|
|Template Module Cisco CISCO-MEMORY-POOL-MIB SNMPv2|
|Template Module Cisco Inventory SNMPv2|
|Template Module Cisco OLD-CISCO-CPU-MIB SNMPv2|
|Template Module Generic SNMPv2|

## Discovery rules


## Items collected

|Name|Description|Type|
|----|-----------|----|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|


