
# Template Server Cisco UCS SNMPv2

## Overview

For Zabbix version: 4.0  
for Cisco UCS via Integrated Management Controller

This template was tested on:

- Cisco UCS C240 M4SX, version 

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$DISK_ARRAY_CACHE_BATTERY_CRIT_STATUS}|-|2|
|{$DISK_ARRAY_CACHE_BATTERY_OK_STATUS}|-|1|
|{$DISK_ARRAY_CRIT_STATUS:"inoperable"}|-|2|
|{$DISK_ARRAY_OK_STATUS:"operable"}|-|1|
|{$DISK_ARRAY_WARN_STATUS:"degraded"}|-|3|
|{$DISK_CRIT_STATUS:"bad"}|-|16|
|{$DISK_CRIT_STATUS:"predictiveFailure"}|-|11|
|{$DISK_FAIL_STATUS:"failed"}|-|9|
|{$FAN_CRIT_STATUS:"inoperable"}|-|2|
|{$FAN_WARN_STATUS:"degraded"}|-|3|
|{$HEALTH_CRIT_STATUS:"computeFailed"}|-|30|
|{$HEALTH_CRIT_STATUS:"configFailure"}|-|33|
|{$HEALTH_CRIT_STATUS:"inoperable"}|-|60|
|{$HEALTH_CRIT_STATUS:"unconfigFailure"}|-|34|
|{$HEALTH_WARN_STATUS:"diagnosticsFailed"}|-|204|
|{$HEALTH_WARN_STATUS:"powerProblem"}|-|62|
|{$HEALTH_WARN_STATUS:"testFailed"}|-|35|
|{$HEALTH_WARN_STATUS:"thermalProblem"}|-|60|
|{$HEALTH_WARN_STATUS:"voltageProblem"}|-|62|
|{$PSU_CRIT_STATUS:"inoperable"}|-|2|
|{$PSU_WARN_STATUS:"degraded"}|-|3|
|{$TEMP_CRIT:"Ambient"}|-|35|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN:"Ambient"}|-|30|
|{$TEMP_WARN}|-|50|
|{$VDISK_OK_STATUS:"equipped"}|-|10|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Temperature Discovery|-|SNMP|
|Temperature CPU Discovery|-|SNMP|
|PSU Discovery|-|SNMP|
|Unit Discovery|-|SNMP|
|FAN Discovery|-|SNMP|
|Physical Disk Discovery|Scanning table of physical drive entries CISCO-UNIFIED-COMPUTING-STORAGE-MIB::cucsStorageLocalDiskTable.|SNMP|
|Virtual Disk Discovery|CISCO-UNIFIED-COMPUTING-STORAGE-MIB::cucsStorageLocalLunTable|SNMP|
|Array Controller Discovery|Scanning table of Array controllers: CISCO-UNIFIED-COMPUTING-STORAGE-MIB::cucsStorageControllerTable.|SNMP|
|Array Controller Cache Discovery|Scanning table of Array controllers: CISCO-UNIFIED-COMPUTING-STORAGE-MIB::cucsStorageControllerTable.|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|{#SENSOR_LOCATION}.Ambient: Temperature|MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB</br>Temperature readings of testpoint: {#SENSOR_LOCATION}.Ambient|SNMP|
|{#SENSOR_LOCATION}.Front: Temperature|MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB</br>Cisco UCS compute:RackUnitMbTempStats:frontTemp managed object property|SNMP|
|{#SENSOR_LOCATION}.Rear: Temperature|MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB</br>Cisco UCS compute:RackUnitMbTempStats:rearTemp managed object property|SNMP|
|{#SENSOR_LOCATION}.IOH: Temperature|MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB</br>Cisco UCS compute:RackUnitMbTempStats:ioh1Temp managed object property|SNMP|
|{#SENSOR_LOCATION}: Temperature|MIB: CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB</br>Cisco UCS processor:EnvStats:temperature managed object property|SNMP|
|{#PSU_LOCATION}: Power supply status|MIB: CISCO-UNIFIED-COMPUTING-EQUIPMENT-MIB</br>Cisco UCS equipment:Psu:operState managed object property|SNMP|
|{#UNIT_LOCATION}: Overall system health status|MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB</br>Cisco UCS compute:RackUnit:operState managed object property|SNMP|
|{#UNIT_LOCATION}: Hardware model name|MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB</br>Cisco UCS compute:RackUnit:model managed object property|SNMP|
|{#UNIT_LOCATION}: Hardware serial number|MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB</br>Cisco UCS compute:RackUnit:serial managed object property|SNMP|
|{#FAN_LOCATION}: Fan status|MIB: CISCO-UNIFIED-COMPUTING-EQUIPMENT-MIB</br>Cisco UCS equipment:Fan:operState managed object property|SNMP|
|{#DISK_LOCATION}: Physical disk status|MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB</br>Cisco UCS storage:LocalDisk:diskState managed object property.|SNMP|
|{#DISK_LOCATION}: Physical disk model name|MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB</br>Cisco UCS storage:LocalDisk:serial managed object property. Actually returns part number code|SNMP|
|{#DISK_LOCATION}: Physical disk media type|MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB</br>Cisco UCS storage:LocalDisk:model managed object property. Actually returns 'HDD' or 'SSD'|SNMP|
|{#DISK_LOCATION}: Disk size|MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB</br>Cisco UCS storage:LocalDisk:size managed object property. In MB.|SNMP|
|{#VDISK_LOCATION}: Status|MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB</br>Cisco UCS storage:LocalLun:presence managed object property|SNMP|
|{#VDISK_LOCATION}: Layout type |MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB</br>Cisco UCS storage:LocalLun:type managed object property|SNMP|
|{#VDISK_LOCATION}: Disk size|MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB</br>Cisco UCS storage:LocalLun:size managed object property in MB.|SNMP|
|{#DISKARRAY_LOCATION}: Disk array controller status|MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB</br>|SNMP|
|{#DISKARRAY_LOCATION}: Disk array controller model|MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB</br>|SNMP|
|{#DISKARRAY_CACHE_LOCATION}: Disk array cache controller battery status|MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB</br>|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|{#SENSOR_LOCATION}.Ambient: Temperature is above warning threshold: >{$TEMP_WARN:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsAmbientTemp.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsAmbientTemp.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"Ambient"}-3`|WARNING|
|{#SENSOR_LOCATION}.Ambient: Temperature is above critical threshold: >{$TEMP_CRIT:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsAmbientTemp.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsAmbientTemp.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"Ambient"}-3`|HIGH|
|{#SENSOR_LOCATION}.Ambient: Temperature is too low: <{$TEMP_CRIT_LOW:"Ambient"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsAmbientTemp.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsAmbientTemp.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"Ambient"}+3`|AVERAGE|
|{#SENSOR_LOCATION}.Front: Temperature is above warning threshold: >{$TEMP_WARN:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsFrontTemp.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsFrontTemp.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"Ambient"}-3`|WARNING|
|{#SENSOR_LOCATION}.Front: Temperature is above critical threshold: >{$TEMP_CRIT:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsFrontTemp.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsFrontTemp.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"Ambient"}-3`|HIGH|
|{#SENSOR_LOCATION}.Front: Temperature is too low: <{$TEMP_CRIT_LOW:"Ambient"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsFrontTemp.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsFrontTemp.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"Ambient"}+3`|AVERAGE|
|{#SENSOR_LOCATION}.Rear: Temperature is above warning threshold: >{$TEMP_WARN:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsRearTemp.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsRearTemp.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"Ambient"}-3`|WARNING|
|{#SENSOR_LOCATION}.Rear: Temperature is above critical threshold: >{$TEMP_CRIT:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsRearTemp.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsRearTemp.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"Ambient"}-3`|HIGH|
|{#SENSOR_LOCATION}.Rear: Temperature is too low: <{$TEMP_CRIT_LOW:"Ambient"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsRearTemp.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempStatsRearTemp.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"Ambient"}+3`|AVERAGE|
|{#SENSOR_LOCATION}.IOH: Temperature is above warning threshold: >{$TEMP_WARN:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempSltatsIoh1Temp.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempSltatsIoh1Temp.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"Ambient"}-3`|WARNING|
|{#SENSOR_LOCATION}.IOH: Temperature is above critical threshold: >{$TEMP_CRIT:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempSltatsIoh1Temp.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempSltatsIoh1Temp.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"Ambient"}-3`|HIGH|
|{#SENSOR_LOCATION}.IOH: Temperature is too low: <{$TEMP_CRIT_LOW:"Ambient"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempSltatsIoh1Temp.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsComputeRackUnitMbTempSltatsIoh1Temp.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"Ambient"}+3`|AVERAGE|
|{#SENSOR_LOCATION}: Temperature is above warning threshold: >{$TEMP_WARN:"CPU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cucsProcessorEnvStatsTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"CPU"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsProcessorEnvStatsTemperature.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"CPU"}-3`|WARNING|
|{#SENSOR_LOCATION}: Temperature is above critical threshold: >{$TEMP_CRIT:"CPU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[cucsProcessorEnvStatsTemperature.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"CPU"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsProcessorEnvStatsTemperature.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"CPU"}-3`|HIGH|
|{#SENSOR_LOCATION}: Temperature is too low: <{$TEMP_CRIT_LOW:"CPU"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[cucsProcessorEnvStatsTemperature.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"CPU"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[cucsProcessorEnvStatsTemperature.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"CPU"}+3`|AVERAGE|
|{#PSU_LOCATION}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[cucsEquipmentPsuOperState.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS:"inoperable"},eq)}=1`|AVERAGE|
|{#PSU_LOCATION}: Power supply is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[cucsEquipmentPsuOperState.{#SNMPINDEX}].count(#1,{$PSU_WARN_STATUS:"degraded"},eq)}=1`|WARNING|
|{#UNIT_LOCATION}: System status is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for errors|`{TEMPLATE_NAME:system.status[cucsComputeRackUnitOperState.{#SNMPINDEX}].count(#1,{$HEALTH_CRIT_STATUS:"computeFailed"},eq)}=1 or {TEMPLATE_NAME:system.status[cucsComputeRackUnitOperState.{#SNMPINDEX}].count(#1,{$HEALTH_CRIT_STATUS:"configFailure"},eq)}=1 or {TEMPLATE_NAME:system.status[cucsComputeRackUnitOperState.{#SNMPINDEX}].count(#1,{$HEALTH_CRIT_STATUS:"unconfigFailure"},eq)}=1 or {TEMPLATE_NAME:system.status[cucsComputeRackUnitOperState.{#SNMPINDEX}].count(#1,{$HEALTH_CRIT_STATUS:"inoperable"},eq)}=1`|HIGH|
|{#UNIT_LOCATION}: System status is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for warnings|`{TEMPLATE_NAME:system.status[cucsComputeRackUnitOperState.{#SNMPINDEX}].count(#1,{$HEALTH_WARN_STATUS:"testFailed"},eq)}=1 or {TEMPLATE_NAME:system.status[cucsComputeRackUnitOperState.{#SNMPINDEX}].count(#1,{$HEALTH_WARN_STATUS:"thermalProblem"},eq)}=1 or {TEMPLATE_NAME:system.status[cucsComputeRackUnitOperState.{#SNMPINDEX}].count(#1,{$HEALTH_WARN_STATUS:"powerProblem"},eq)}=1 or {TEMPLATE_NAME:system.status[cucsComputeRackUnitOperState.{#SNMPINDEX}].count(#1,{$HEALTH_WARN_STATUS:"voltageProblem"},eq)}=1 or {TEMPLATE_NAME:system.status[cucsComputeRackUnitOperState.{#SNMPINDEX}].count(#1,{$HEALTH_WARN_STATUS:"diagnosticsFailed"},eq)}=1`|WARNING|
|{#UNIT_LOCATION}: Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber[cucsComputeRackUnitSerial.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[cucsComputeRackUnitSerial.{#SNMPINDEX}].strlen()}>0`|INFO|
|{#FAN_LOCATION}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[cucsEquipmentFanOperState.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"inoperable"},eq)}=1`|AVERAGE|
|{#FAN_LOCATION}: Fan is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[cucsEquipmentFanOperState.{#SNMPINDEX}].count(#1,{$FAN_WARN_STATUS:"degraded"},eq)}=1`|WARNING|
|{#DISK_LOCATION}: Physical disk failed|Last value: {ITEM.LASTVALUE1}.</br>Please check physical disk for warnings or errors|`{TEMPLATE_NAME:system.hw.physicaldisk.status[cucsStorageLocalDiskDiskState.{#SNMPINDEX}].count(#1,{$DISK_FAIL_STATUS:"failed"},eq)}=1`|HIGH|
|{#DISK_LOCATION}: Physical disk error|Last value: {ITEM.LASTVALUE1}.</br>Please check physical disk for warnings or errors|`{TEMPLATE_NAME:system.hw.physicaldisk.status[cucsStorageLocalDiskDiskState.{#SNMPINDEX}].count(#1,{$DISK_CRIT_STATUS:"bad"},eq)}=1 or {TEMPLATE_NAME:system.hw.physicaldisk.status[cucsStorageLocalDiskDiskState.{#SNMPINDEX}].count(#1,{$DISK_CRIT_STATUS:"predictiveFailure"},eq)}=1`|AVERAGE|
|{#VDISK_LOCATION}: Virtual disk is not in OK state|Last value: {ITEM.LASTVALUE1}.</br>Please check virtual disk for warnings or errors|`{TEMPLATE_NAME:system.hw.virtualdisk.status[cucsStorageLocalLunPresence.{#SNMPINDEX}].count(#1,{$VDISK_OK_STATUS:"equipped"},ne)}=1`|WARNING|
|{#DISKARRAY_LOCATION}: Disk array controller is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.status[cucsStorageControllerOperState.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CRIT_STATUS:"inoperable"},eq)}=1`|HIGH|
|{#DISKARRAY_LOCATION}: Disk array controller is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.status[cucsStorageControllerOperState.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_WARN_STATUS:"degraded"},eq)}=1`|AVERAGE|
|{#DISKARRAY_LOCATION}: Disk array controller is not in optimal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.status[cucsStorageControllerOperState.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_OK_STATUS:"operable"},ne)}=1`|WARNING|
|{#DISKARRAY_CACHE_LOCATION}: Disk array cache controller battery is in critical state!|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.cache.battery.status[cucsStorageRaidBatteryOperability.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_BATTERY_CRIT_STATUS},eq)}=1`|AVERAGE|
|{#DISKARRAY_CACHE_LOCATION}: Disk array cache controller battery is not in optimal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.cache.battery.status[cucsStorageRaidBatteryOperability.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_BATTERY_OK_STATUS},ne)}=1`|WARNING|


