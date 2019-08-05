
# Template Module EtherLike-MIB SNMPv2

## Overview

For Zabbix version: 3.2  

## Setup


## Zabbix configuration




## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|EtherLike-MIB Discovery|Discovering interfaces from IF-MIB and EtherLike-MIB. Interfaces with up(1) Operational Status are discovered.|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Interface {#IFNAME}({#IFALIAS}): Duplex status|MIB: EtherLike-MIB</br>The current mode of operation of the MAC</br>entity.  'unknown' indicates that the current</br>duplex mode could not be determined.</br>Management control of the duplex mode is</br>accomplished through the MAU MIB.  When</br>an interface does not support autonegotiation,</br>or when autonegotiation is not enabled, the</br>duplex mode is controlled using</br>ifMauDefaultType.  When autonegotiation is</br>supported and enabled, duplex mode is controlled</br>using ifMauAutoNegAdvertisedBits.  In either</br>case, the currently operating duplex mode is</br>reflected both in this object and in ifMauType.</br>Note that this object provides redundant</br>information with ifMauType.  Normally, redundant</br>objects are discouraged.  However, in this</br>instance, it allows a management application to</br>determine the duplex status of an interface</br>without having to know every possible value of</br>ifMauType.  This was felt to be sufficiently</br>valuable to justify the redundancy.</br>Reference: [IEEE 802.3 Std.], 30.3.1.1.32,aDuplexStatus.|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|Interface {#IFNAME}({#IFALIAS}): In half-duplex mode|Last value: {ITEM.LASTVALUE1}.</br>Please check autonegotiation settings and cabling|`{TEMPLATE_NAME:net.if.duplex[dot3StatsDuplexStatus.{#SNMPINDEX}].last()}=2`|WARNING|

## References

