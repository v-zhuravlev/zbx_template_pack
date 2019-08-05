
# Template Net Intel_Qlogic Infiniband SNMPv2

## Overview

Minimum version: 4.0  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$FAN_CRIT_STATUS}|-|3|
|{$PSU_CRIT_STATUS}|-|3|
|{$PSU_WARN_STATUS}|-|4|
|{$TEMP_CRIT_LOW}|-|5|
|{$TEMP_CRIT_STATUS}|-|3|
|{$TEMP_CRIT}|-|60|
|{$TEMP_WARN_STATUS}|-|2|
|{$TEMP_WARN}|-|50|

## Template links

|Name|
|----|
|Template Module Generic SNMPv2|
|Template Module Interfaces SNMPv2|

## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Temperature Discovery|Discovering sensor's table with temperature filter|SNMP|
|Unit Discovery|-|SNMP|
|PSU Discovery|A textual description of the power supply, that can be assigned by the administrator.|SNMP|
|FAN Discovery|icsChassisFanDescription of icsChassisFanTable|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Hardware model name|MIB: ICS-CHASSIS-MIB</br>|SNMP|
|Firmware version|MIB: ICS-CHASSIS-MIB</br>|SNMP|
|{#SENSOR_INFO}: Temperature|MIB: ICS-CHASSIS-MIB</br>The current value read from the sensor.|SNMP|
|{#SENSOR_INFO}: Temperature status|MIB: ICS-CHASSIS-MIB</br>The operational status of the sensor.|SNMP|
|{#ENT_NAME}: Hardware serial number|MIB: ICS-CHASSIS-MIB</br>The serial number of the FRU.  If not available, this value is a zero-length string.|SNMP|
|{#SNMPVALUE}: Power supply status|MIB: ICS-CHASSIS-MIB</br>Actual status of the power supply:</br>(1) unknown: status not known.</br>(2) disabled: power supply is disabled.</br>(3) failed - power supply is unable to supply power due to failure.</br>(4) warning - power supply is supplying power, but an output or sensor is bad or warning.</br>(5) standby - power supply believed usable,but not supplying power.</br>(6) engaged - power supply is supplying power.</br>(7) redundant - power supply is supplying power, but not needed.</br>(8) notPresent - power supply is supplying power is not present.|SNMP|
|{#SNMPVALUE}: Fan status|MIB: ICS-CHASSIS-MIB</br>The operational status of the fan unit.|SNMP|


## Triggers

|Name|Description|Expression|
|----|-----------|----|
|Firmware has changed|Last value: {ITEM.LASTVALUE1}.</br>Firmware version has changed. Ack to close|`{TEMPLATE_NAME:system.hw.firmware.diff()}=1 and {TEMPLATE_NAME:system.hw.firmware.strlen()}>0`|
|{#SENSOR_INFO}: Temperature is above warning threshold: >{$TEMP_WARN:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[icsChassisSensorSlotValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_WARN:""} or {Template Net Intel_Qlogic Infiniband SNMPv2:sensor.temp.status[icsChassisSensorSlotOperStatus.{#SNMPINDEX}].last(0)}={$TEMP_WARN_STATUS}`|
|{#SENSOR_INFO}: Temperature is above critical threshold: >{$TEMP_CRIT:""}|Last value: {ITEM.LASTVALUE1}.</br>This trigger uses temperature sensor values as well as temperature sensor status if available|`{TEMPLATE_NAME:sensor.temp.value[icsChassisSensorSlotValue.{#SNMPINDEX}].avg(5m)}>{$TEMP_CRIT:""} or {Template Net Intel_Qlogic Infiniband SNMPv2:sensor.temp.status[icsChassisSensorSlotOperStatus.{#SNMPINDEX}].last(0)}={$TEMP_CRIT_STATUS}`|
|{#SENSOR_INFO}: Temperature is too low: <{$TEMP_CRIT_LOW:""}|Last value: {ITEM.LASTVALUE1}.|`{TEMPLATE_NAME:sensor.temp.value[icsChassisSensorSlotValue.{#SNMPINDEX}].avg(5m)}<{$TEMP_CRIT_LOW:""}`|
|{#ENT_NAME}: Device has been replaced (new serial number received)|Last value: {ITEM.LASTVALUE1}.</br>Device serial number has changed. Ack to close|`{TEMPLATE_NAME:system.hw.serialnumber[icsChassisSystemUnitFruSerialNumber.{#SNMPINDEX}].diff()}=1 and {TEMPLATE_NAME:system.hw.serialnumber[icsChassisSystemUnitFruSerialNumber.{#SNMPINDEX}].strlen()}>0`|
|{#SNMPVALUE}: Power supply is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[icsChassisPowerSupplyEntry.{#SNMPINDEX}].count(#1,{$PSU_CRIT_STATUS},eq)}=1`|
|{#SNMPVALUE}: Power supply is in warning state|Last value: {ITEM.LASTVALUE1}.</br>Please check the power supply unit for errors|`{TEMPLATE_NAME:sensor.psu.status[icsChassisPowerSupplyEntry.{#SNMPINDEX}].count(#1,{$PSU_WARN_STATUS},eq)}=1`|
|{#SNMPVALUE}: Fan is in critical state|Last value: {ITEM.LASTVALUE1}.</br>Please check the fan unit|`{TEMPLATE_NAME:sensor.fan.status[icsChassisFanOperStatus.{#SNMPINDEX}].count(#1,{$FAN_CRIT_STATUS},eq)}=1`|

## References

