
# Template Module Brocade_Foundry Performance SNMPv2

## Overview

Minimum version: 4.2  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$CPU_UTIL_MAX}|-|90|
|{$MEMORY_UTIL_MAX}|-|90|


## Discovery rules


## Items collected

|Name|Description|Type|
|----|-----------|----|
|CPU utilization|MIB: FOUNDRY-SN-AGENT-MIB</br>The statistics collection of 1 minute CPU utilization.|SNMP|
|Memory utilization|MIB: FOUNDRY-SN-AGENT-MIB</br>The system dynamic memory utilization, in unit of percentage.</br>Deprecated: Refer to snAgSystemDRAMUtil.</br>For NI platforms, refer to snAgentBrdMemoryUtil100thPercent|SNMP|


## Triggers

|Name|Description|Expression|
|----|-----------|----|
|High CPU utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:system.cpu.util[snAgGblCpuUtil1MinAvg.0].avg(5m)}>{$CPU_UTIL_MAX}`|
|High memory utilization|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:vm.memory.pused[snAgGblDynMemUtil.0].avg(5m)}>{$MEMORY_UTIL_MAX}`|

## References
# Template Net Brocade_Foundry Nonstackable SNMPv2

## Overview

Minimum version: 4.2  
For devices(old Foundry devices, MLXe and so on) that doesn't support Stackable SNMP Tables: snChasFan2Table, snChasPwrSupply2Table,snAgentTemp2Table -
FOUNDRY-SN-AGENT-MIB::snChasFanTable, snChasPwrSupplyTable,snAgentTempTable are used instead.
For example:
The objects in table snChasPwrSupply2Table is not supported on the NetIron and the FastIron SX devices.
snChasFan2Table is not supported on  on the NetIron devices.
snAgentTemp2Table is not supported on old versions of MLXe
This template was tested on:

- Brocade MLXe, version (System Mode: MLX), IronWare Version V5.4.0eT163 Compiled on Oct 30 2013 at 16:40:24 labeled as V5.4.00e
- Foundry FLS648, version Foundry Networks, Inc. FLS648, IronWare Version 04.1.00bT7e1 Compiled on Feb 29 2008 at 21:35:28 labeled as FGS04100b
- Foundry FWSX424, version Foundry Networks, Inc. FWSX424, IronWare Version 02.0.00aT1e0 Compiled on Dec 10 2004 at 14:40:19 labeled as FWXS02000a

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$FAN_CRIT_STATUS}|-|3|
|{$FAN_OK_STATUS}|-|2|
|{$PSU_CRIT_STATUS}|-|3|
|{$PSU_OK_STATUS}|-|2|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|75|
|{$TEMP_WARN}|-|65|

## Template links

|Name|
|----|
|Template Module Brocade_Foundry Performance SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|PSU Discovery|snChasPwrSupplyTable: A table of each power supply information. Only installed power supply appears in a table row.|SNMP|
|FAN Discovery|snChasFanTable: A table of each fan information. Only installed fan appears in a table row.|SNMP|
|Temperature Discovery|snAgentTempTable:Table to list temperatures of the modules in the device. This table is applicable to only those modules with temperature sensors.|SNMP|
|Temperature Discovery Chassis|Since temperature of the chassis is not available on all Brocade/Foundry hardware, this LLD is here to avoid unsupported items.|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Hardware serial number|MIB: FOUNDRY-SN-AGENT-MIB</br>|SNMP|
|Firmware version|MIB: FOUNDRY-SN-AGENT-MIB</br>The version of the running software in the form'major.minor.maintenance[letters]'|SNMP|
|PSU {#PSU_INDEX}: Power supply status|MIB: FOUNDRY-SN-AGENT-MIB</br>|SNMP|
|Fan {#FAN_INDEX}: Fan status|MIB: FOUNDRY-SN-AGENT-MIB</br>|SNMP|
|{#SENSOR_DESCR}: Temperature|MIB: FOUNDRY-SN-AGENT-MIB</br>Temperature of the sensor represented by this row. Each unit is 0.5 degrees Celsius.|SNMP|
|Chassis #{#SNMPINDEX}: Temperature|MIB: FOUNDRY-SN-AGENT-MIB</br>Temperature of the chassis. Each unit is 0.5 degrees Celcius.</br>Only management module built with temperature sensor hardware is applicable.</br>For those non-applicable management module, it returns no-such-name.|SNMP|


## Triggers

|Name|Description|Expression|
|----|-----------|----|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|
|PSU {#PSU_INDEX}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[snChasPwrSupplyOperStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|
|PSU {#PSU_INDEX}: Power supply is not in normal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[snChasPwrSupplyOperStatus.{#SNMPINDEX}].count(#1,{$PSU_OK_STATUS},ne)}=1`|
|Fan {#FAN_INDEX}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[snChasFanOperStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|
|Fan {#FAN_INDEX}: Fan is not in normal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[snChasFanOperStatus.{#SNMPINDEX}].count(#1,{$FAN_OK_STATUS},ne)}=1`|
|{#SENSOR_DESCR}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[snAgentTempValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`|
|{#SENSOR_DESCR}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[snAgentTempValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|
|{#SENSOR_DESCR}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[snAgentTempValue.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|
|Chassis #{#SNMPINDEX}: Temperature is above warning threshold: >{$TEMP_WARN:"Chassis"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[snChasActualTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"Chassis"}`|
|Chassis #{#SNMPINDEX}: Temperature is above critical threshold: >{$TEMP_CRIT:"Chassis"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[snChasActualTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"Chassis"}`|
|Chassis #{#SNMPINDEX}: Temperature is too low: <{$TEMP_CRIT_LOW:"Chassis"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[snChasActualTemperature.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"Chassis"}`|

## References
# Template Net Brocade_Foundry Stackable SNMPv2

## Overview

Minimum version: 4.2  
For devices(most of the IronWare Brocade devices) that support Stackable SNMP Tables in FOUNDRY-SN-AGENT-MIB: snChasFan2Table, snChasPwrSupply2Table,snAgentTemp2Table - so objects from all Stack members are provided.
This template was tested on:

- Brocade ICX7250-48, version ICX7250-48, IronWare Version 08.0.30kT211 Compiled on Oct 18 2016 at 05:40:38 labeled as SPS08030k
- Brocade ICX7250-48(Stacked), version Stacking System ICX7250-48, IronWare Version 08.0.30kT211 Compiled on Oct 18 2016 at 05:40:38 labeled as SPS08030k
- Brocade ICX7450-48(Stacked), version Stacking System ICX7450-48, IronWare Version 08.0.30kT211 Compiled on Oct 18 2016 at 05:40:38 labeled as SPS08030k"
- Brocade ICX7250-48(Stacked), version Stacking System ICX7250-48, IronWare Version 08.0.30kT211 Compiled on Oct 18 2016 at 05:40:38 labeled as SPS08030k
- Brocade ICX7450-48F(Stacked), version Stacking System ICX7750-48F, IronWare Version 08.0.40bT203 Compiled on Oct 20 2016 at 23:48:43 labeled as SWR08040b
- Brocade ICX 6600, version 

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$FAN_CRIT_STATUS}|-|3|
|{$FAN_OK_STATUS}|-|2|
|{$PSU_CRIT_STATUS}|-|3|
|{$PSU_OK_STATUS}|-|2|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|75|
|{$TEMP_WARN}|-|65|

## Template links

|Name|
|----|
|Template Module Brocade_Foundry Performance SNMPv2|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|PSU Discovery|snChasPwrSupply2Table: A table of each power supply information for each unit. Only installed power supply appears in a table row.|SNMP|
|FAN Discovery|snChasFan2Table: A table of each fan information for each unit. Only installed fan appears in a table row.|SNMP|
|Temperature Discovery|snAgentTemp2Table:Table to list temperatures of the modules in the device for each unit. This table is applicable to only those modules with temperature sensors.|SNMP|
|Stack Discovery|Discovering snStackingConfigUnitTable for Model names|SNMP|
|Chassis Discovery|snChasUnitIndex: The index to chassis table.|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Firmware version|MIB: FOUNDRY-SN-AGENT-MIB</br>The version of the running software in the form 'major.minor.maintenance[letters]'|SNMP|
|Unit {#PSU_UNIT} PSU {#PSU_INDEX}: Power supply status|MIB: FOUNDRY-SN-AGENT-MIB</br>|SNMP|
|Unit {#FAN_UNIT} Fan {#FAN_INDEX}: Fan status|MIB: FOUNDRY-SN-AGENT-MIB</br>|SNMP|
|{#SENSOR_DESCR}: Temperature|MIB: FOUNDRY-SN-AGENT-MIB</br>Temperature of the sensor represented by this row. Each unit is 0.5 degrees Celsius.|SNMP|
|Unit {#SNMPINDEX}: Hardware model name|MIB: FOUNDRY-SN-STACKING-MIB</br>A description of the configured/active system type for each unit.|SNMP|
|Unit {#SNMPVALUE}: Hardware serial number|MIB: FOUNDRY-SN-AGENT-MIB</br>The serial number of the chassis for each unit. If the serial number is unknown or unavailable then the value should be a zero length string.|SNMP|


## Triggers

|Name|Description|Expression|
|----|-----------|----|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|
|Unit {#PSU_UNIT} PSU {#PSU_INDEX}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[snChasPwrSupply2OperStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|
|Unit {#PSU_UNIT} PSU {#PSU_INDEX}: Power supply is not in normal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[snChasPwrSupply2OperStatus.{#SNMPINDEX}].count(#1,{$PSU_OK_STATUS},ne)}=1`|
|Unit {#FAN_UNIT} Fan {#FAN_INDEX}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[snChasFan2OperStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|
|Unit {#FAN_UNIT} Fan {#FAN_INDEX}: Fan is not in normal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[snChasFan2OperStatus.{#SNMPINDEX}].count(#1,{$FAN_OK_STATUS},ne)}=1`|
|{#SENSOR_DESCR}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[snAgentTemp2Value.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""}`|
|{#SENSOR_DESCR}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[snAgentTemp2Value.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""}`|
|{#SENSOR_DESCR}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[snAgentTemp2Value.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|
|Unit {#SNMPVALUE}: Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber[snChasUnitSerNum.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[snChasUnitSerNum.{#SNMPINDEX}].strlen()}>0`|

## References

