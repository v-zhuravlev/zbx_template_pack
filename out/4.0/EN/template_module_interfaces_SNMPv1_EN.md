
# Template Module Interfaces SNMPv1

## Overview

For Zabbix version: 4.0  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$IFCONTROL}|-|1|
|{$IF_ERRORS_WARN}|-|2|
|{$IF_UTIL_MAX}|-|90|


## Discovery rules

|Name|Description|Type|
|----|-----------|----|
|Network Interfaces Discovery|Discovering interfaces from IF-MIB. Interfaces are not discovered:</br>- with down(2) Administrative status</br>- with notPresent(6) Operational status</br>- loopbacks</br>|SNMP|

## Items collected

|Name|Description|Type|
|----|-----------|----|
|Interface {#IFNAME}({#IFALIAS}): Operational status|MIB: IF-MIB</br>The current operational state of the interface.</br>- The testing(3) state indicates that no operational packet scan be passed</br>- If ifAdminStatus is down(2) then ifOperStatus should be down(2)</br>- If ifAdminStatus is changed to up(1) then ifOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic</br>- It should change todormant(5) if the interface is waiting for external actions (such as a serial line waiting for an incoming connection)</br>- It should remain in the down(2) state if and only if there is a fault that prevents it from going to the up(1) state</br>- It should remain in the notPresent(6) state if the interface has missing(typically, hardware) components.|SNMP|
|Interface {#IFNAME}({#IFALIAS}): Bits received|MIB: IF-MIB</br>The total number of octets received on the interface,including framing characters.  This object is a 64-bit version of ifInOctets. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.|SNMP|
|Interface {#IFNAME}({#IFALIAS}): Bits sent|MIB: IF-MIB</br>The total number of octets transmitted out of the interface, including framing characters.  This object is a 64-bit version of ifOutOctets.Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.|SNMP|
|Interface {#IFNAME}({#IFALIAS}): Inbound packets with errors|MIB: IF-MIB</br>For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.|SNMP|
|Interface {#IFNAME}({#IFALIAS}): Outbound packets with errors|MIB: IF-MIB</br>For packet-oriented interfaces, the number of outbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of outbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.|SNMP|
|Interface {#IFNAME}({#IFALIAS}): Outbound packets discarded|MIB: IF-MIB</br>The number of outbound packets which were chosen to be discarded</br>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.</br>One possible reason for discarding such a packet could be to free up buffer space.</br>Discontinuities in the value of this counter can occur at re-initialization of the management system,</br>and at other times as indicated by the value of ifCounterDiscontinuityTime.|SNMP|
|Interface {#IFNAME}({#IFALIAS}): Inbound packets discarded|MIB: IF-MIB</br>The number of inbound packets which were chosen to be discarded</br>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.</br>One possible reason for discarding such a packet could be to free up buffer space.</br>Discontinuities in the value of this counter can occur at re-initialization of the management system,</br>and at other times as indicated by the value of ifCounterDiscontinuityTime.|SNMP|
|Interface {#IFNAME}({#IFALIAS}): Interface type|MIB: IF-MIB</br>The type of interface.</br>Additional values for ifType are assigned by the Internet Assigned NumbersAuthority (IANA),</br>through updating the syntax of the IANAifType textual convention.|SNMP|
|Interface {#IFNAME}({#IFALIAS}): Speed|MIB: IF-MIB</br>An estimate of the interface's current bandwidth in units of 1,000,000 bits per second.  If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n-500,000' to`n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.  For a sub-layer which has no concept of bandwidth, this object should be zero.|SNMP|


## Triggers

|Name|Description|Expression|Severity|
|----|-----------|----|----|
|Interface {#IFNAME}({#IFALIAS}): Link down|Last value: {ITEM.LASTVALUE1}.</br>Interface is down|`{$IFCONTROL:"{#IFNAME}"}=1 and ({TEMPLATE_NAME:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}=2 and {TEMPLATE_NAME:net.if.status[ifOperStatus.{#SNMPINDEX}].diff()}=1)`|AVERAGE|
|Interface {#IFNAME}({#IFALIAS}): High bandwidth usage >{$IF_UTIL_MAX:"{#IFNAME}"}%|Last value: {ITEM.LASTVALUE1}.|`({TEMPLATE_NAME:net.if.in[ifHCInOctets.{#SNMPINDEX}].avg(15m)}>({$IF_UTIL_MAX:"{#IFNAME}"}/100)*{Template Module Interfaces SNMPv1:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()} or {Template Module Interfaces SNMPv1:net.if.out[ifHCOutOctets.{#SNMPINDEX}].avg(15m)}>({$IF_UTIL_MAX:"{#IFNAME}"}/100)*{Template Module Interfaces SNMPv1:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()}) and {Template Module Interfaces SNMPv1:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()}>0`|WARNING|
|Interface {#IFNAME}({#IFALIAS}): High error rate|Last value: {ITEM.LASTVALUE1}.</br>Recovers when below 80% of {$IF_ERRORS_WARN:"{#IFNAME}"} threshold|`{TEMPLATE_NAME:net.if.in.errors[ifInErrors.{#SNMPINDEX}].avg(5m)}>{$IF_ERRORS_WARN:"{#IFNAME}"} or {Template Module Interfaces SNMPv1:net.if.out.errors[ifOutErrors.{#SNMPINDEX}].avg(5m)}>{$IF_ERRORS_WARN:"{#IFNAME}"}`|WARNING|
|Interface {#IFNAME}({#IFALIAS}): Ethernet has changed to lower speed than it was before|Last value: {ITEM.LASTVALUE1}.</br>This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of autonegotiation issues. Ack to close.|`{TEMPLATE_NAME:net.if.speed[ifHighSpeed.{#SNMPINDEX}].change()}<0 and {TEMPLATE_NAME:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()}>0 and ( {Template Module Interfaces SNMPv1:net.if.type[ifType.{#SNMPINDEX}].last()}=6 or {Template Module Interfaces SNMPv1:net.if.type[ifType.{#SNMPINDEX}].last()}=7 or {Template Module Interfaces SNMPv1:net.if.type[ifType.{#SNMPINDEX}].last()}=11 or {Template Module Interfaces SNMPv1:net.if.type[ifType.{#SNMPINDEX}].last()}=62 or {Template Module Interfaces SNMPv1:net.if.type[ifType.{#SNMPINDEX}].last()}=69 or {Template Module Interfaces SNMPv1:net.if.type[ifType.{#SNMPINDEX}].last()}=117 ) and ({Template Module Interfaces SNMPv1:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}<>2)`|INFO|


