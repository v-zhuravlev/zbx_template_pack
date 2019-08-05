
# Template Server Dell iDRAC SNMPv2

## Overview

For Zabbix version: 4.0  
for Dell servers with iDRAC controllers</br>http://www.dell.com/support/manuals/us/en/19/dell-openmanage-server-administrator-v8.3/snmp_idrac8/idrac-mib?guid=guid-e686536d-bc8e-4e09-8e8b-de8eb052efee</br>Supported systems: http://www.dell.com/support/manuals/us/en/04/dell-openmanage-server-administrator-v8.3/snmp_idrac8/supported-systems?guid=guid-f72b75ba-e686-4e8a-b8c5-ca11c7c21381

This template was tested on:

- iDRAC7, PowerEdge R620, version 
- iDRAC8, PowerEdge R730xd, version 
- iDRAC8, PowerEdge R720, version 

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$DISK_ARRAY_CACHE_BATTERY_CRIT_STATUS}|-|3|
|{$DISK_ARRAY_CACHE_BATTERY_OK_STATUS}|-|2|
|{$DISK_ARRAY_CACHE_BATTERY_WARN_STATUS}|-|4|
|{$DISK_ARRAY_CRIT_STATUS:"critical"}|-|5|
|{$DISK_ARRAY_FAIL_STATUS:"nonRecoverable"}|-|6|
|{$DISK_ARRAY_WARN_STATUS:"nonCritical"}|-|4|
|{$DISK_FAIL_STATUS:"critical"}|-|5|
|{$DISK_FAIL_STATUS:"nonRecoverable"}|-|6|
|{$DISK_SMART_FAIL_STATUS}|-|1|
|{$DISK_WARN_STATUS:"nonCritical"}|-|4|
|{$FAN_CRIT_STATUS:"criticalLower"}|-|8|
|{$FAN_CRIT_STATUS:"criticalUpper"}|-|5|
|{$FAN_CRIT_STATUS:"failed"}|-|10|
|{$FAN_CRIT_STATUS:"nonRecoverableLower"}|-|9|
|{$FAN_CRIT_STATUS:"nonRecoverableUpper"}|-|6|
|{$FAN_WARN_STATUS:"nonCriticalLower"}|-|7|
|{$FAN_WARN_STATUS:"nonCriticalUpper"}|-|4|
|{$HEALTH_CRIT_STATUS}|-|5|
|{$HEALTH_DISASTER_STATUS}|-|6|
|{$HEALTH_WARN_STATUS}|-|4|
|{$PSU_CRIT_STATUS:"critical"}|-|5|
|{$PSU_CRIT_STATUS:"nonRecoverable"}|-|6|
|{$PSU_WARN_STATUS:"nonCritical"}|-|4|
|{$TEMP_CRIT:"Ambient"}|-|35|
|{$TEMP_CRIT:"CPU"}|-|75|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT_STATUS}|-|5|
|{$TEMP_CRIT}|-|60|
|{$TEMP_DISASTER_STATUS}|-|6|
|{$TEMP_WARN:"Ambient"}|-|30|
|{$TEMP_WARN:"CPU"}|-|70|
|{$TEMP_WARN_STATUS}|-|4|
|{$TEMP_WARN}|-|50|
|{$VDISK_CRIT_STATUS:"failed"}|-|3|
|{$VDISK_WARN_STATUS:"degraded"}|-|4|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Temperature CPU Discovery|Scanning table of Temperature Probe Table IDRAC-MIB-SMIv2::temperatureProbeTable|SNMP|
|Temperature Ambient Discovery|Scanning table of Temperature Probe Table IDRAC-MIB-SMIv2::temperatureProbeTable|SNMP|
|PSU Discovery|IDRAC-MIB-SMIv2::powerSupplyTable|SNMP|
|FAN Discovery|IDRAC-MIB-SMIv2::coolingDeviceTable|SNMP|
|Physical Disk Discovery|IDRAC-MIB-SMIv2::physicalDiskTable|SNMP|
|Virtual Disk Discovery|IDRAC-MIB-SMIv2::virtualDiskTable|SNMP|
|Array Controller Discovery|IDRAC-MIB-SMIv2::controllerTable|SNMP|
|Array Controller Cache Discovery|IDRAC-MIB-SMIv2::batteryTable|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Overall system health status|MIB: IDRAC-MIB-SMIv2</br>This attribute defines the overall rollup status of all components in the system being monitored by the remote access card. Includes system, storage, IO devices, iDRAC, CPU, memory, etc.|SNMP|
|Hardware model name|MIB: IDRAC-MIB-SMIv2</br>This attribute defines the model name of the system.|SNMP|
|Operating system|MIB: IDRAC-MIB-SMIv2</br>This attribute defines the name of the operating system that the hostis running.|SNMP|
|Hardware serial number|MIB: IDRAC-MIB-SMIv2</br>This attribute defines the service tag of the system.|SNMP|
|Firmware version|MIB: IDRAC-MIB-SMIv2</br>This attribute defines the firmware version of a remote access card.|SNMP|
|{#SENSOR_LOCALE}: Temperature|MIB: IDRAC-MIB-SMIv2</br>0700.0020.0001.0006 This attribute defines the reading for a temperature probe of type other than temperatureProbeTypeIsDiscrete.  When the value for temperatureProbeType is other than temperatureProbeTypeIsDiscrete,the value returned for this attribute is the temperature that the probeis reading in tenths of degrees Centigrade. When the value for temperatureProbeType is temperatureProbeTypeIsDiscrete, a value is not returned for this attribute.|SNMP|
|{#SENSOR_LOCALE}: Temperature status|MIB: IDRAC-MIB-SMIv2</br>0700.0020.0001.0005 This attribute defines the probe status of the temperature probe.|SNMP|
|{#SENSOR_LOCALE}: Temperature|MIB: IDRAC-MIB-SMIv2</br>0700.0020.0001.0006 This attribute defines the reading for a temperature probe of type other than temperatureProbeTypeIsDiscrete.  When the value for temperatureProbeType is other than temperatureProbeTypeIsDiscrete,the value returned for this attribute is the temperature that the probeis reading in tenths of degrees Centigrade. When the value for temperatureProbeType is temperatureProbeTypeIsDiscrete, a value is not returned for this attribute.|SNMP|
|{#SENSOR_LOCALE}: Temperature status|MIB: IDRAC-MIB-SMIv2</br>0700.0020.0001.0005 This attribute defines the probe status of the temperature probe.|SNMP|
|{#PSU_DESCR}: Power supply status|MIB: IDRAC-MIB-SMIv2</br>0600.0012.0001.0005 This attribute defines the status of the power supply.|SNMP|
|{#FAN_DESCR}: Fan status|MIB: IDRAC-MIB-SMIv2</br>0700.0012.0001.0005 This attribute defines the probe status of the cooling device.|SNMP|
|{#FAN_DESCR}: Fan speed|MIB: IDRAC-MIB-SMIv2</br>0700.0012.0001.0006 This attribute defines the reading for a cooling device</br>of subtype other than coolingDeviceSubTypeIsDiscrete.  When the value</br>for coolingDeviceSubType is other than coolingDeviceSubTypeIsDiscrete, the</br>value returned for this attribute is the speed in RPM or the OFF/ON value</br>of the cooling device.  When the value for coolingDeviceSubType is</br>coolingDeviceSubTypeIsDiscrete, a value is not returned for this attribute.|SNMP|
|{#DISK_NAME}: Physical disk status|MIB: IDRAC-MIB-SMIv2</br>The status of the physical disk itself without the propagation of any contained component status.</br>Possible values:</br>1: Other</br>2: Unknown</br>3: OK</br>4: Non-critical</br>5: Critical</br>6: Non-recoverable|SNMP|
|{#DISK_NAME}: Physical disk serial number|MIB: IDRAC-MIB-SMIv2</br>The physical disk's unique identification number from the manufacturer.|SNMP|
|{#DISK_NAME}: Physical disk S.M.A.R.T. status|MIB: IDRAC-MIB-SMIv2</br>Indicates whether the physical disk has received a predictive failure alert.|SNMP|
|{#DISK_NAME}: Physical disk model name|MIB: IDRAC-MIB-SMIv2</br>The model number of the physical disk.|SNMP|
|{#DISK_NAME}: Physical disk part number|MIB: IDRAC-MIB-SMIv2</br>The part number of the disk.|SNMP|
|{#DISK_NAME}: Physical disk media type|MIB: IDRAC-MIB-SMIv2</br>The media type of the physical disk. Possible Values:</br>1: The media type could not be determined.</br>2: Hard Disk Drive (HDD).</br>3: Solid State Drive (SSD).|SNMP|
|{#DISK_NAME}: Disk size|MIB: IDRAC-MIB-SMIv2</br>The size of the physical disk in megabytes.|SNMP|
|Disk {#SNMPVALUE}({#DISK_NAME}): Layout type |MIB: IDRAC-MIB-SMIv2</br>The virtual disk's RAID type.</br>Possible values:</br>1: Not one of the following</br>2: RAID-0</br>3: RAID-1</br>4: RAID-5</br>5: RAID-6</br>6: RAID-10</br>7: RAID-50</br>8: RAID-60</br>9: Concatenated RAID 1</br>10: Concatenated RAID 5|SNMP|
|Disk {#SNMPVALUE}({#DISK_NAME}): Current state|MIB: IDRAC-MIB-SMIv2</br>The state of the virtual disk when there are progressive operations ongoing.</br>Possible values:</br>1: There is no active operation running.</br>2: The virtual disk configuration has changed. The physical disks included in the virtual disk are being modified to support the new configuration.</br>3: A Consistency Check (CC) is being performed on the virtual disk.</br>4: The virtual disk is being initialized.</br>5: BackGround Initialization (BGI) is being performed on the virtual disk.|SNMP|
|Disk {#SNMPVALUE}({#DISK_NAME}): Read policy|MIB: IDRAC-MIB-SMIv2</br>The read policy used by the controller for read operations on this virtual disk.</br>Possible values:</br>1: No Read Ahead.</br>2: Read Ahead.</br>3: Adaptive Read Ahead.|SNMP|
|Disk {#SNMPVALUE}({#DISK_NAME}): Write policy|MIB: IDRAC-MIB-SMIv2</br>The write policy used by the controller for write operations on this virtual disk.</br>Possible values:</br>1: Write Through.</br>2: Write Back.</br>3: Force Write Back.|SNMP|
|Disk {#SNMPVALUE}({#DISK_NAME}): Disk size|MIB: IDRAC-MIB-SMIv2</br>The size of the virtual disk in megabytes.|SNMP|
|Disk {#SNMPVALUE}({#DISK_NAME}): Status|MIB: IDRAC-MIB-SMIv2</br>The current state of this virtual disk (which includes any member physical disks.)</br>Possible states:</br>1: The current state could not be determined.</br>2: The virtual disk is operating normally or optimally.</br>3: The virtual disk has encountered a failure. The data on disk is lost or is about to be lost.</br>4: The virtual disk encounterd a failure with one or all of the constituent redundant physical disks.</br>The data on the virtual disk might no longer be fault tolerant.|SNMP|
|{#CNTLR_NAME}: Disk array controller status|MIB: IDRAC-MIB-SMIv2</br>The status of the controller itself without the propagation of any contained component status.</br>Possible values:</br>1: Other</br>2: Unknown</br>3: OK</br>4: Non-critical</br>5: Critical</br>6: Non-recoverable</br>                |SNMP|
|{#CNTLR_NAME}: Disk array controller model|MIB: IDRAC-MIB-SMIv2</br>The controller's name as represented in Storage Management.|SNMP|
|Battery {#BATTERY_NUM}: Disk array cache controller battery status|MIB: IDRAC-MIB-SMIv2</br>Current state of battery.</br>Possible values:</br>1: The current state could not be determined.</br>2: The battery is operating normally.</br>3: The battery has failed and needs to be replaced.</br>4: The battery temperature is high or charge level is depleting.</br>5: The battery is missing or not detected.</br>6: The battery is undergoing the re-charge phase.</br>7: The battery voltage or charge level is below the threshold.</br>                |SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|System is in unrecoverable state!|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.status[globalSystemStatus.0].count(#1,{$HEALTH_DISASTER_STATUS},eq)}=1`|HIGH|
|System status is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for errors|`{TEMPLATE_NAME:system.status[globalSystemStatus.0].count(#1,{$HEALTH_CRIT_STATUS},eq)}=1`|HIGH|
|System status is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for warnings|`{TEMPLATE_NAME:system.status[globalSystemStatus.0].count(#1,{$HEALTH_WARN_STATUS},eq)}=1`|WARNING|
|Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber.diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber.strlen()}>0`|INFO|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|INFO|
|{#SENSOR_LOCALE}: Temperature is above warning threshold: >{$TEMP_WARN:"CPU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.CPU.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"CPU"} or {Template Server Dell iDRAC SNMPv2:sensor.temp.status[temperatureProbeStatus.CPU.{#SNMPINDEX}].last(0)}={$TEMP_WARN_STATUS}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.CPU.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"CPU"}-3`|WARNING|
|{#SENSOR_LOCALE}: Temperature is above critical threshold: >{$TEMP_CRIT:"CPU"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.CPU.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"CPU"} or {Template Server Dell iDRAC SNMPv2:sensor.temp.status[temperatureProbeStatus.CPU.{#SNMPINDEX}].last(0)}={$TEMP_CRIT_STATUS} or {Template Server Dell iDRAC SNMPv2:sensor.temp.status[temperatureProbeStatus.CPU.{#SNMPINDEX}].last(0)}={$TEMP_DISASTER_STATUS}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.CPU.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"CPU"}-3`|HIGH|
|{#SENSOR_LOCALE}: Temperature is too low: <{$TEMP_CRIT_LOW:"CPU"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.CPU.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"CPU"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.CPU.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"CPU"}+3`|AVERAGE|
|{#SENSOR_LOCALE}: Temperature is above warning threshold: >{$TEMP_WARN:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.Ambient.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:"Ambient"} or {Template Server Dell iDRAC SNMPv2:sensor.temp.status[temperatureProbeStatus.Ambient.{#SNMPINDEX}].last(0)}={$TEMP_WARN_STATUS}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.Ambient.{#SNMPINDEX}].max(5m)}<{$TEMP_WARN:"Ambient"}-3`|WARNING|
|{#SENSOR_LOCALE}: Temperature is above critical threshold: >{$TEMP_CRIT:"Ambient"}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.Ambient.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:"Ambient"} or {Template Server Dell iDRAC SNMPv2:sensor.temp.status[temperatureProbeStatus.Ambient.{#SNMPINDEX}].last(0)}={$TEMP_CRIT_STATUS} or {Template Server Dell iDRAC SNMPv2:sensor.temp.status[temperatureProbeStatus.Ambient.{#SNMPINDEX}].last(0)}={$TEMP_DISASTER_STATUS}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.Ambient.{#SNMPINDEX}].max(5m)}<{$TEMP_CRIT:"Ambient"}-3`|HIGH|
|{#SENSOR_LOCALE}: Temperature is too low: <{$TEMP_CRIT_LOW:"Ambient"}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.Ambient.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:"Ambient"}`</br>Recovery expression: `{TEMPLATE_NAME:sensor.temp.value[temperatureProbeReading.Ambient.{#SNMPINDEX}].min(5m)}>{$TEMP_CRIT_LOW:"Ambient"}+3`|AVERAGE|
|{#PSU_DESCR}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[powerSupplyStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS:"critical"},eq)}=1 or {TEMPLATE_NAME:sensor.psu.status[powerSupplyStatus.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS:"nonRecoverable"},eq)}=1`|AVERAGE|
|{#PSU_DESCR}: Power supply is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[powerSupplyStatus.{#SNMPINDEX}].count(#1,{$PSU_WARN_STATUS:"nonCritical"},eq)}=1`|WARNING|
|{#FAN_DESCR}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[coolingDeviceStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"criticalUpper"},eq)}=1 or {TEMPLATE_NAME:sensor.fan.status[coolingDeviceStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"nonRecoverableUpper"},eq)}=1 or {TEMPLATE_NAME:sensor.fan.status[coolingDeviceStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"criticalLower"},eq)}=1 or {TEMPLATE_NAME:sensor.fan.status[coolingDeviceStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"nonRecoverableLower"},eq)}=1 or {TEMPLATE_NAME:sensor.fan.status[coolingDeviceStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS:"failed"},eq)}=1`|AVERAGE|
|{#FAN_DESCR}: Fan is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[coolingDeviceStatus.{#SNMPINDEX}].count(#1,{$FAN_WARN_STATUS:"nonCriticalUpper"},eq)}=1 or {TEMPLATE_NAME:sensor.fan.status[coolingDeviceStatus.{#SNMPINDEX}].count(#1,{$FAN_WARN_STATUS:"nonCriticalLower"},eq)}=1`|WARNING|
|{#DISK_NAME}: Physical disk failed|Last value: {ITEM.LASTVALUE1}.</br>Please check physical disk for warnings or errors|`{TEMPLATE_NAME:system.hw.physicaldisk.status[physicalDiskComponentStatus.{#SNMPINDEX}].count(#1,{$DISK_FAIL_STATUS:"critical"},eq)}=1 or {TEMPLATE_NAME:system.hw.physicaldisk.status[physicalDiskComponentStatus.{#SNMPINDEX}].count(#1,{$DISK_FAIL_STATUS:"nonRecoverable"},eq)}=1`|HIGH|
|{#DISK_NAME}: Physical disk is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check physical disk for warnings or errors|`{TEMPLATE_NAME:system.hw.physicaldisk.status[physicalDiskComponentStatus.{#SNMPINDEX}].count(#1,{$DISK_WARN_STATUS:"nonCritical"},eq)}=1`|WARNING|
|{#DISK_NAME}: Disk has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Disk serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.physicaldisk.serialnumber[physicalDiskSerialNo.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.physicaldisk.serialnumber[physicalDiskSerialNo.{#SNMPINDEX}].strlen()}>0`|INFO|
|{#DISK_NAME}: Physical disk S.M.A.R.T. failed|Last value: {ITEM.LASTVALUE1}.</br>Disk probably requires replacement.|`{TEMPLATE_NAME:system.hw.physicaldisk.smart_status[physicalDiskSmartAlertIndication.{#SNMPINDEX}].count(#1,{$DISK_SMART_FAIL_STATUS},eq)}=1`|HIGH|
|Disk {#SNMPVALUE}({#DISK_NAME}): Virtual disk failed|Last value: {ITEM.LASTVALUE1}.</br>Please check virtual disk for warnings or errors|`{TEMPLATE_NAME:system.hw.virtualdisk.status[virtualDiskState.{#SNMPINDEX}].count(#1,{$VDISK_CRIT_STATUS:"failed"},eq)}=1`|HIGH|
|Disk {#SNMPVALUE}({#DISK_NAME}): Virtual disk is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check virtual disk for warnings or errors|`{TEMPLATE_NAME:system.hw.virtualdisk.status[virtualDiskState.{#SNMPINDEX}].count(#1,{$VDISK_WARN_STATUS:"degraded"},eq)}=1`|AVERAGE|
|{#CNTLR_NAME}: Disk array controller is in unrecoverable state!|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.status[controllerComponentStatus.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_FAIL_STATUS:"nonRecoverable"},eq)}=1`|DISASTER|
|{#CNTLR_NAME}: Disk array controller is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.status[controllerComponentStatus.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CRIT_STATUS:"critical"},eq)}=1`|HIGH|
|{#CNTLR_NAME}: Disk array controller is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.status[controllerComponentStatus.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_WARN_STATUS:"nonCritical"},eq)}=1`|AVERAGE|
|Battery {#BATTERY_NUM}: Disk array cache controller battery is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.cache.battery.status[batteryState.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_BATTERY_WARN_STATUS},eq)}=1`|WARNING|
|Battery {#BATTERY_NUM}: Disk array cache controller battery is not in optimal state|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.cache.battery.status[batteryState.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_BATTERY_OK_STATUS},ne)}=1`|WARNING|
|Battery {#BATTERY_NUM}: Disk array cache controller battery is in critical state!|Last value: {ITEM.LASTVALUE1}.</br>Please check the device for faults|`{TEMPLATE_NAME:system.hw.diskarray.cache.battery.status[batteryState.{#SNMPINDEX}].count(#1,{$DISK_ARRAY_CACHE_BATTERY_CRIT_STATUS},eq)}=1`|AVERAGE|


