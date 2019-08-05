
# Template Module Generic SNMPv2

## Overview

Minimum version: 3.4  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$SNMP_TIMEOUT}|-|3m|

## Template links

|Name|
|----|
|Template Module ICMP Ping|

## Discovery rules


## Items collected

|Name|Description|Type|
|----|-----------|----|
|Device uptime|MIB: SNMPv2-MIB</br>The time (in hundredths of a second) since the network management portion of the system was last re-initialized.|SNMP|
|SNMP traps (fallback)|Item is used to collect all SNMP traps unmatched by other snmptrap items|SNMP_TRAP|
|Device location|MIB: SNMPv2-MIB</br>The physical location of this node (e.g., `telephone closet, 3rd floor').  If the location is unknown, the value is the zero-length string.|SNMP|
|Device contact details|MIB: SNMPv2-MIB</br>The textual identification of the contact person for this managed node, together with information on how to contact this person.  If no contact information is known, the value is the zero-length string.|SNMP|
|System object ID|MIB: SNMPv2-MIB</br>The vendor's authoritative identification of the network management subsystem contained in the entity.  This value is allocated within the SMI enterprises subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining`what kind of box' is being managed.  For example, if vendor`Flintstones, Inc.' was assigned the subtree1.3.6.1.4.1.4242, it could assign the identifier 1.3.6.1.4.1.4242.1.1 to its `Fred Router'.|SNMP|
|Device name|MIB: SNMPv2-MIB</br>An administratively-assigned name for this managed node.By convention, this is the node's fully-qualified domain name.  If the name is unknown, the value is the zero-length string.|SNMP|
|Device description|MIB: SNMPv2-MIB</br>A textual description of the entity.  This value should</br>include the full name and version identification of the system's hardware type, software operating-system, and</br>networking software.|SNMP|
|SNMP availability|-|INTERNAL|


## Triggers

|Name|Description|Expression|
|----|-----------|----|
|{HOST.NAME} has been restarted|Last value: {ITEM.LASTVALUE1}.</br>The device uptime is less than 10 minutes|`{TEMPLATE_NAME:system.uptime[sysUpTime].last()}<10m`|
|No SNMP data collection|Last value: {ITEM.LASTVALUE1}.</br>SNMP is not available for polling. Please check device connectivity and SNMP settings.|`{TEMPLATE_NAME:zabbix[host,snmp,available].max({$SNMP_TIMEOUT})}=0`|

## References

