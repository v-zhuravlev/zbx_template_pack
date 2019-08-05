
# Template Server HP iLO SNMPv2

## Overview

For Zabbix version: 4.0  
for HP iLO adapters that support SNMP get. Or via operating system, using SNMP HP subagent

This template was tested on:

- iLo4, HP Proliant G9

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$DISK_ARRAY_CACHE_BATTERY_CRIT_STATUS:"capacitorFailed"}|-|7|
|{$DISK_ARRAY_CACHE_BATTERY_CRIT_STATUS:"failed"}|-|4|
|{$DISK_ARRAY_CACHE_BATTERY_WARN_STATUS:"degraded"}|-|5|
|{$DISK_ARRAY_CACHE_BATTERY_WARN_STATUS:"notPresent"}|-|6|
|{$DISK_ARRAY_CACHE_CRIT_STATUS:"cacheModCriticalFailure"}|-|8|
|{$DISK_ARRAY_CACHE_OK_STATUS:"enabled"}|-|3|
|{$DISK_ARRAY_CACHE_WARN_STATUS:"cacheModDegradedFailsafeSpeed"}|-|7|
|{$DISK_ARRAY_CACHE_WARN_STATUS:"cacheModFlashMemNotAttached"}|-|6|
|{$DISK_ARRAY_CACHE_WARN_STATUS:"cacheReadCacheNotMapped"}|-|9|
|{$DISK_ARRAY_CACHE_WARN_STATUS:"invalid"}|-|2|
|{$DISK_ARRAY_CRIT_STATUS}|-|4|
|{$DISK_ARRAY_WARN_STATUS}|-|3|
|{$DISK_FAIL_STATUS}|-|3|
|{$DISK_SMART_FAIL_STATUS:"replaceDrive"}|-|3|
|{$DISK_SMART_FAIL_STATUS:"replaceDriveSSDWearOut"}|-|4|
|{$DISK_WARN_STATUS}|-|4|
|{$FAN_CRIT_STATUS}|-|4|
|{$FAN_WARN_STATUS}|-|3|
|{$HEALTH_CRIT_STATUS}|-|4|
|{$HEALTH_WARN_STATUS}|-|3|
|{$PSU_CRIT_STATUS}|-|4|
|{$PSU_WARN_STATUS}|-|3|
|{$TEMP_CRIT:"Ambient"}|-|35|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN:"Ambient"}|-|30|
|{$TEMP_WARN}|-|50|
|{$VDISK_CRIT_STATUS}|-|3|
|{$VDISK_OK_STATUS}|-|2|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Temperature Discovery|Scanning table of Temperature Sensor Entries: CPQHLTH-MIB::cpqHeTemperatureTable|SNMP|
|Temperature Discovery Ambient|Scanning table of Temperature Sensor Entries: CPQHLTH-MIB::cpqHeTemperatureTable with ambient(11) and 0.1 index filter|SNMP|
|Temperature Discovery CPU|Scanning table of Temperature Sensor Entries: CPQHLTH-MIB::cpqHeTemperatureTable with cpu(6) filter|SNMP|
|Temperature Discovery Memory|Scanning table of Temperature Sensor Entries: CPQHLTH-MIB::cpqHeTemperatureTable with memory(7) filter|SNMP|
|Temperature Discovery PSU|Scanning table of Temperature Sensor Entries: CPQHLTH-MIB::cpqHeTemperatureTable with powerSupply(10) filter|SNMP|
|Temperature Discovery I/O|Scanning table of Temperature Sensor Entries: CPQHLTH-MIB::cpqHeTemperatureTable with ioBoard(5) filter|SNMP|
|Temperature Discovery System|Scanning table of Temperature Sensor Entries: CPQHLTH-MIB::cpqHeTemperatureTable with system(3) filter|SNMP|
|PSU Discovery|CPQHLTH-MIB::cpqHeFltTolPowerSupplyStatus|SNMP|
|FAN Discovery|CPQHLTH-MIB::cpqHeFltTolFanCondition|SNMP|
|Array Controller Discovery|Scanning table of Array controllers: CPQIDA-MIB::cpqDaCntlrTable|SNMP|
|Array Controller Cache Discovery|Scanning table of Array controllers: CPQIDA-MIB::cpqDaAccelTable|SNMP|
|Physical Disk Discovery|Scanning  table of physical drive entries CPQIDA-MIB::cpqDaPhyDrvTable.|SNMP|
|Virtual Disk Discovery|CPQIDA-MIB::cpqDaLogDrvTable|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|System: Temperature status|MIB: CPQHLTH-MIB</br>This value specifies the overall condition of the system's thermal environment.</br>This value will be one of the following:</br>other(1)  Temperature could not be determined.</br>ok(2)  The temperature sensor is within normal operating range.</br>degraded(3)  The temperature sensor is outside of normal operating range.</br>failed(4)  The temperature sensor detects a condition that could  permanently damage the system.|SNMP|
|Overall system health status|MIB: CPQHLTH-MIB</br>The overall condition. This object represents the overall status of the server information represented by this MIB.|SNMP|
|Hardware model name|MIB: CPQSINFO-MIB</br>The machine product name.The name of the machine used in this system.|SNMP|
|Hardware serial number|MIB: CPQSINFO-MIB</br>The serial number of the physical system unit. The string will be empty if the system does not report the serial number function.|SNMP|
|{#SNMPINDEX}: Temperature|MIB: CPQHLTH-MIB</br>Temperature readings of testpoint: {#SNMPINDEX}|SNMP|
|{#SNMPINDEX}: Temperature sensor location|MIB: CPQHLTH-MIB</br>This specifies the location of the temperature sensor present in the system.|SNMP|
|Ambient: Temperature|MIB: CPQHLTH-MIB</br>Temperature readings of testpoint: Ambient|SNMP|
|CPU-{#SNMPINDEX}: Temperature|MIB: CPQHLTH-MIB</br>Temperature readings of testpoint: CPU-{#SNMPINDEX}|SNMP|
|Memory-{#SNMPINDEX}: Temperature|MIB: CPQHLTH-MIB</br>Temperature readings of testpoint: Memory-{#SNMPINDEX}|SNMP|
|PSU-{#SNMPINDEX}: Temperature|MIB: CPQHLTH-MIB</br>Temperature readings of testpoint: PSU-{#SNMPINDEX}|SNMP|
|I/O-{#SNMPINDEX}: Temperature|MIB: CPQHLTH-MIB</br>Temperature readings of testpoint: I/O-{#SNMPINDEX}|SNMP|
|System-{#SNMPINDEX}: Temperature|MIB: CPQHLTH-MIB</br>Temperature readings of testpoint: System-{#SNMPINDEX}|SNMP|
|Chassis {#CHASSIS_NUM}, bay {#BAY_NUM}: Power supply status|MIB: CPQHLTH-MIB</br>The condition of the power supply. This value will be one of the following:</br>other(1)  The status could not be determined or not present.</br>ok(2)  The power supply is operating normally.</br>degraded(3)  A temperature sensor, fan or other power supply component is  outside of normal operating range.</br>failed(4)  A power supply component detects a condition that could  permanently damage the system.|SNMP|
|Fan {#SNMPINDEX}: Fan status|MIB: CPQHLTH-MIB</br>The condition of the fan.</br>This value will be one of the following:</br>other(1)  Fan status detection is not supported by this system or driver.</br>ok(2)  The fan is operating properly.</br>degraded(2)  A redundant fan is not operating properly.</br>failed(4)  A non-redundant fan is not operating properly.|SNMP|
|{#CNTLR_LOCATION}: Disk array controller status|MIB: CPQIDA-MIB</br>This value represents the overall condition of this controller,</br>and any associated logical drives,physical drives, and array accelerators.|SNMP|
|{#CNTLR_LOCATION}: Disk array controller model|MIB: CPQIDA-MIB</br>Array Controller Model. The type of controller card.|SNMP|
|#{#CACHE_CNTRL_INDEX}: Disk array cache controller status|MIB: CPQIDA-MIB</br>Cache Module/Operations Status. This describes the status of the cache module and/or cache operations.</br>Note that for some controller models, a cache module board that physically attaches to the controller or chipset may not be an available option.|SNMP|
|#{#CACHE_CNTRL_INDEX}: Disk array cache controller battery status|MIB: CPQIDA-MIB</br>Cache Module Board Backup Power Status. This monitors the status of each backup power source on the board.</br>The backup power source can only recharge when the system has power applied. The type of backup power source used is indicated by cpqDaAccelBackupPowerSource.</br>The following values are valid:</br>Other (1)  Indicates that the instrument agent does not recognize  backup power status.  You may need to update your software.</br>Ok (2)  The backup power source is fully charged.</br>Recharging (3)  The array controller has one or more cache module backup power  sources that are recharging.</br>Cache module operations such as Battery/Flash Backed Write Cache, Expansion, Extension and Migration are temporarily suspended until the backup power source is fully charged.</br>Cache module operations will automatically resume  when charging is complete.</br>Failed (4)  The battery pack is below the sufficient voltage level and  has not recharged in 36 hours.</br>Your Cache Module board  needs to be serviced.</br>Degraded (5)  The battery is still operating, however, one of the batteries  in the pack has failed to recharge properly.</br>Your Cache  Module board should be serviced as soon as possible.</br>NotPresent (6)  A backup power source is not present on the cache module board. Some controllers do not have backup power sources.</br>Capacitor Failed (7)  The flash backed cache module capacitor is below the sufficient voltage level and has not recharged in 10 minutes.  Your Cache Module board needs to be serviced.</br>                |SNMP|
|{#DISK_LOCATION}: Physical disk status|MIB: CPQIDA-MIB</br>Physical Drive Status. This shows the status of the physical drive. The following values are valid for the physical drive status:</br>other (1)  Indicates that the instrument agent does not recognize  the drive.</br>You may need to upgrade your instrument agent  and/or driver software.</br>ok (2)  Indicates the drive is functioning properly.</br>failed (3)  Indicates that the drive is no longer operating and  should be replaced.</br>predictiveFailure(4)  Indicates that the drive has a predictive failure error and  should be replaced.|SNMP|
|{#DISK_LOCATION}: Physical disk S.M.A.R.T. status|MIB: CPQIDA-MIB</br>Physical Drive S.M.A.R.T Status.The following values are defined:</br>other(1)  The agent is unable to determine if the status of S.M.A.R.T  predictive failure monitoring for this drive.</br>ok(2)  Indicates the drive is functioning properly.</br>replaceDrive(3)  Indicates that the drive has a S.M.A.R.T predictive failure  error and should be replaced.|SNMP|
|{#DISK_LOCATION}: Physical disk serial number|MIB: CPQIDA-MIB</br>Physical Drive Serial Number.</br>This is the serial number assigned to the physical drive.</br>This value is based upon the serial number as returned by the SCSI inquiry command</br>but may have been modified due to space limitations.  This can be used for identification purposes.|SNMP|
|{#DISK_LOCATION}: Physical disk model name|MIB: CPQIDA-MIB</br>Physical Drive Model.This is a text description of the physical drive.</br>The text that appears depends upon who manufactured the drive and the drive type.</br>If a drive fails, note the model to identify the type of drive necessary for replacement.</br>If a model number is not present, you may not have properly initialized the drive array to which the physical drive is attached for monitoring.|SNMP|
|{#DISK_LOCATION}: Physical disk media type|MIB: CPQIDA-MIB</br>Drive Array Physical Drive Media Type.The following values are defined:</br>other(1)  The instrument agent is unable to determine the physical drive’s media type.</br>rotatingPlatters(2)  The physical drive media is composed of rotating platters.</br>solidState(3)  The physical drive media is composed of solid state electronics.|SNMP|
|{#DISK_LOCATION}: Disk size|MIB: CPQIDA-MIB</br>Physical Drive Size in MB.</br>This is the size of the physical drive in megabytes.</br>This value is calculated using the value 1,048,576 (2^20) as a megabyte.</br>Drive manufacturers sometimes use the number 1,000,000 as a megabyte when giving drive capacities so this value may differ</br>from the advertised size of a drive. This field is only applicable for controllers which support SCSI drives,</br>and therefore is not supported by the IDA or IDA-2 controllers. The field will contain 0xFFFFFFFF if the drive capacity cannot be calculated</br>or if the controller does not support SCSI drives.|SNMP|
|Disk {#SNMPINDEX}({#DISK_NAME}): Status|Logical Drive Status.|SNMP|
|Disk {#SNMPINDEX}({#DISK_NAME}): Layout type |Logical Drive Fault Tolerance.</br>This shows the fault tolerance mode of the logical drive.|SNMP|
|Disk {#SNMPINDEX}({#DISK_NAME}): Disk size|Logical Drive Size.</br>This is the size of the logical drive in megabytes.  This value</br>is calculated using the value 1,048,576 (2^20) as a megabyte.</br>Drive manufacturers sometimes use the number 1,000,000 as a</br>megabyte when giving drive capacities so this value may</br>differ from the advertised size of a drive.|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|System status is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for errors|`{TEMPLATE_NAME:system.status[cpqHeMibCondition.0].count(#1,{$HEALTH_CRIT_STATUS},eq)}=1`|HIGH|
|System status is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for warnings|`{TEMPLATE_NAME:system.status[cpqHeMibCondition.0].count(#1,{$HEALTH_WARN_STATUS},eq)}=1`|WARNING|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|
|{#SNMPINDEX}: Temperature is above warning threshold: >{$TEMP_WARN:"{#SNMPINDEX}"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"{#SNMPINDEX}"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"{#SNMPINDEX}"}-3`|WARNING|
|{#SNMPINDEX}: Temperature is above critical threshold: >{$TEMP_CRIT:"{#SNMPINDEX}"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"{#SNMPINDEX}"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"{#SNMPINDEX}"}-3`|HIGH|
|{#SNMPINDEX}: Temperature is too low: <{$TEMP_CRIT_LOW:"{#SNMPINDEX}"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"{#SNMPINDEX}"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"{#SNMPINDEX}"}+3`|AVERAGE|
|Ambient: Temperature is above warning threshold: >{$TEMP_WARN:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Ambient.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Ambient.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"Ambient"}-3`|WARNING|
|Ambient: Temperature is above critical threshold: >{$TEMP_CRIT:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Ambient.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Ambient.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"Ambient"}-3`|HIGH|
|Ambient: Temperature is too low: <{$TEMP_CRIT_LOW:"Ambient"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Ambient.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Ambient.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"Ambient"}+3`|AVERAGE|
|CPU-{#SNMPINDEX}: Temperature is above warning threshold: >{$TEMP_WARN:"CPU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.CPU.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"CPU"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.CPU.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"CPU"}-3`|WARNING|
|CPU-{#SNMPINDEX}: Temperature is above critical threshold: >{$TEMP_CRIT:"CPU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.CPU.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"CPU"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.CPU.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"CPU"}-3`|HIGH|
|CPU-{#SNMPINDEX}: Temperature is too low: <{$TEMP_CRIT_LOW:"CPU"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.CPU.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"CPU"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.CPU.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"CPU"}+3`|AVERAGE|
|Memory-{#SNMPINDEX}: Temperature is above warning threshold: >{$TEMP_WARN:"Memory"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Memory.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"Memory"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Memory.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"Memory"}-3`|WARNING|
|Memory-{#SNMPINDEX}: Temperature is above critical threshold: >{$TEMP_CRIT:"Memory"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Memory.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"Memory"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Memory.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"Memory"}-3`|HIGH|
|Memory-{#SNMPINDEX}: Temperature is too low: <{$TEMP_CRIT_LOW:"Memory"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Memory.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"Memory"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.Memory.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"Memory"}+3`|AVERAGE|
|PSU-{#SNMPINDEX}: Temperature is above warning threshold: >{$TEMP_WARN:"PSU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.PSU.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"PSU"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.PSU.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"PSU"}-3`|WARNING|
|PSU-{#SNMPINDEX}: Temperature is above critical threshold: >{$TEMP_CRIT:"PSU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.PSU.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"PSU"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.PSU.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"PSU"}-3`|HIGH|
|PSU-{#SNMPINDEX}: Temperature is too low: <{$TEMP_CRIT_LOW:"PSU"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.PSU.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"PSU"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.PSU.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"PSU"}+3`|AVERAGE|
|I/O-{#SNMPINDEX}: Temperature is above warning threshold: >{$TEMP_WARN:"I/O"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius."I/O.{#SNMPINDEX}"].avg(5m)}>{$TEMP_WARN:"I/O"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius."I/O.{#SNMPINDEX}"].max(5m)}<{$TEMP_WARN:"I/O"}-3`|WARNING|
|I/O-{#SNMPINDEX}: Temperature is above critical threshold: >{$TEMP_CRIT:"I/O"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius."I/O.{#SNMPINDEX}"].avg(5m)}>{$TEMP_CRIT:"I/O"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius."I/O.{#SNMPINDEX}"].max(5m)}<{$TEMP_CRIT:"I/O"}-3`|HIGH|
|I/O-{#SNMPINDEX}: Temperature is too low: <{$TEMP_CRIT_LOW:"I/O"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius."I/O.{#SNMPINDEX}"].avg(5m)}<{$TEMP_CRIT_LOW:"I/O"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius."I/O.{#SNMPINDEX}"].min(5m)}>{$TEMP_CRIT_LOW:"I/O"}+3`|AVERAGE|
|System-{#SNMPINDEX}: Temperature is above warning threshold: >{$TEMP_WARN:"Device"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.System.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"Device"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.System.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"Device"}-3`|WARNING|
|System-{#SNMPINDEX}: Temperature is above critical threshold: >{$TEMP_CRIT:"Device"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.System.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"Device"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.System.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"Device"}-3`|HIGH|
|System-{#SNMPINDEX}: Temperature is too low: <{$TEMP_CRIT_LOW:"Device"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.System.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"Device"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cpqHeTemperatureCelsius.System.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"Device"}+3`|AVERAGE|
|Chassis {#CHASSIS_NUM}, bay {#BAY_NUM}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[cpqHeFltTolPowerSupplyCondition.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|AVERAGE|
|Chassis {#CHASSIS_NUM}, bay {#BAY_NUM}: Power supply is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[cpqHeFltTolPowerSupplyCondition.{#SNMPINDEX}].count(#1,{$PSU_WARN_STATUS},eq)}=1`|WARNING|
|Fan {#SNMPINDEX}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[cpqHeFltTolFanCondition.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|AVERAGE|
|Fan {#SNMPINDEX}: Fan is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[cpqHeFltTolFanCondition.{#SNMPINDEX}].count(#1,{$FAN_WARN_STATUS},eq)}=1`|WARNING|
|{#CNTLR_LOCATION}: Disk array controller is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.status[cpqDaCntlrCondition.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CRIT_STATUS},eq)}=1`|HIGH|
|{#CNTLR_LOCATION}: Disk array controller is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.status[cpqDaCntlrCondition.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_WARN_STATUS},eq)}=1`|AVERAGE|
|#{#CACHE_CNTRL_INDEX}: Disk array cache controller is in critical state!|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.cache.status[cpqDaAccelStatus.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_CRIT_STATUS:"cacheModCriticalFailure"},eq)}=1`|AVERAGE|
|#{#CACHE_CNTRL_INDEX}: Disk array cache controller is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.cache.status[cpqDaAccelStatus.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_WARN_STATUS:"invalid"},eq)}=1 or {TEMPLATE_NAME:system.hw.diskarray.cache.status[cpqDaAccelStatus.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_WARN_STATUS:"cacheModDegradedFailsafeSpeed"},eq)}=1 or {TEMPLATE_NAME:system.hw.diskarray.cache.status[cpqDaAccelStatus.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_WARN_STATUS:"cacheReadCacheNotMapped"},eq)}=1 or {TEMPLATE_NAME:system.hw.diskarray.cache.status[cpqDaAccelStatus.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_WARN_STATUS:"cacheModFlashMemNotAttached"},eq)}=1`|WARNING|
|#{#CACHE_CNTRL_INDEX}: Disk array cache controller is not in optimal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.cache.status[cpqDaAccelStatus.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_OK_STATUS:"enabled"},ne)}=1`|WARNING|
|#{#CACHE_CNTRL_INDEX}: Disk array cache controller battery is in critical state!|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.cache.battery.status[cpqDaAccelBattery.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_BATTERY_CRIT_STATUS:"failed"},eq)}=1 or {TEMPLATE_NAME:system.hw.diskarray.cache.battery.status[cpqDaAccelBattery.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_BATTERY_CRIT_STATUS:"capacitorFailed"},eq)}=1`|AVERAGE|
|#{#CACHE_CNTRL_INDEX}: Disk array cache controller battery is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.cache.battery.status[cpqDaAccelBattery.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_BATTERY_WARN_STATUS:"degraded"},eq)}=1 or {TEMPLATE_NAME:system.hw.diskarray.cache.battery.status[cpqDaAccelBattery.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_BATTERY_WARN_STATUS:"notPresent"},eq)}=1`|WARNING|
|{#DISK_LOCATION}: Physical disk failed|Last value: {ITEM.LASTVALUE1}.</br>Please check physical disk for warnings or errors|`{TEMPLATE_NAME:system.hw.physicaldisk.status[cpqDaPhyDrvStatus.{#SNMPINDEX}].count(#1,{$DISK_FAIL_STATUS},eq)}=1`|HIGH|
|{#DISK_LOCATION}: Physical disk is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check physical disk for warnings or errors|`{TEMPLATE_NAME:system.hw.physicaldisk.status[cpqDaPhyDrvStatus.{#SNMPINDEX}].count(#1,{$DISK_WARN_STATUS},eq)}=1`|WARNING|
|{#DISK_LOCATION}: Physical disk S.M.A.R.T. failed|Last value: {ITEM.LASTVALUE1}.</br>Disk probably requires replacement.|`{TEMPLATE_NAME:system.hw.physicaldisk.smart_status[cpqDaPhyDrvSmartStatus.{#SNMPINDEX}].count(#1,{$DISK_SMART_FAIL_STATUS:"replaceDrive"},eq)}=1 or {TEMPLATE_NAME:system.hw.physicaldisk.smart_status[cpqDaPhyDrvSmartStatus.{#SNMPINDEX}].count(#1,{$DISK_SMART_FAIL_STATUS:"replaceDriveSSDWearOut"},eq)}=1`|HIGH|
|{#DISK_LOCATION}: Disk has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Disk serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.physicaldisk.serialnumber[cpqDaPhyDrvSerialNum.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.physicaldisk.serialnumber[cpqDaPhyDrvSerialNum.{#SNMPINDEX}].strlen()}>0`|INFO|
|Disk {#SNMPINDEX}({#DISK_NAME}): Virtual disk failed|Last value: {ITEM.LASTVALUE1}.</br>Please check virtual disk for warnings or errors|`{TEMPLATE_NAME:system.hw.virtualdisk.status[cpqDaLogDrvStatus.{#SNMPINDEX}].count(#1,{$VDISK_CRIT_STATUS},eq)}=1`|HIGH|
|Disk {#SNMPINDEX}({#DISK_NAME}): Virtual disk is not in OK state|Last value: {ITEM.LASTVALUE1}.</br>Please check virtual disk for warnings or errors|`{TEMPLATE_NAME:system.hw.virtualdisk.status[cpqDaLogDrvStatus.{#SNMPINDEX}].count(#1,{$VDISK_OK_STATUS},ne)}=1`|WARNING|


