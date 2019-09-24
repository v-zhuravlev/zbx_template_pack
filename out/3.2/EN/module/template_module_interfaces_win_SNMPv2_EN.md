
# Template Module Interfaces Windows SNMPv2

## Overview

For Zabbix version: 3.2  
Special version of interfaces template that is required for Windows OS. Since MS doesn't support 64 bit counters but supports ifAlias and ifHighSpeed.

## Setup

Refer to the vendor documentation.

## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$IFCONTROL}|<p>-</p>|`1`|
|{$IF_ERRORS_WARN}|<p>-</p>|`2`|
|{$IF_UTIL_MAX}|<p>-</p>|`90`|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Network Interfaces Discovery|<p>Discovering interfaces from IF-MIB. Interfaces are not discovered:</p><p>- with down(2) Administrative status</p><p>- with notPresent(6) Operational status</p><p>- loopbacks</p>|SNMP|net.if.discovery<p>**Filter**:</p>AND <p>- A: {#IFADMINSTATUS} MATCHES_REGEX `(1|3)`</p><p>- C: {#IFOPERSTATUS} MATCHES_REGEX `(1|2|3|4|5|7)`</p><p>- B: {#IFNAME} MATCHES_REGEX `@Network interfaces for discovery`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Operational status|<p>MIB: IF-MIB</p><p>The current operational state of the interface.</p><p>- The testing(3) state indicates that no operational packet scan be passed</p><p>- If ifAdminStatus is down(2) then ifOperStatus should be down(2)</p><p>- If ifAdminStatus is changed to up(1) then ifOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic</p><p>- It should change todormant(5) if the interface is waiting for external actions (such as a serial line waiting for an incoming connection)</p><p>- It should remain in the down(2) state if and only if there is a fault that prevents it from going to the up(1) state</p><p>- It should remain in the notPresent(6) state if the interface has missing(typically, hardware) components.</p>|SNMP|net.if.status[ifOperStatus.{#SNMPINDEX}]|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Bits received|<p>MIB: IF-MIB</p><p>The total number of octets received on the interface,including framing characters. Discontinuities in the value of this counter can occurat re-initialization of the management system, and atother times as indicated by the value of ifCounterDiscontinuityTime.</p>|SNMP|net.if.in[ifInOctets.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `8`</p>|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Bits sent|<p>MIB: IF-MIB</p><p>The total number of octets transmitted out of the interface, including framing characters. Discontinuities in the value of this counter can occurat re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|SNMP|net.if.out[ifOutOctets.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND<p>- MULTIPLIER: `8`</p>|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Inbound packets with errors|<p>MIB: IF-MIB</p><p>For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|SNMP|net.if.in.errors[ifInErrors.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Outbound packets with errors|<p>MIB: IF-MIB</p><p>For packet-oriented interfaces, the number of outbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of outbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|SNMP|net.if.out.errors[ifOutErrors.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Outbound packets discarded|<p>MIB: IF-MIB</p><p>The number of outbound packets which were chosen to be discarded</p><p>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.</p><p>One possible reason for discarding such a packet could be to free up buffer space.</p><p>Discontinuities in the value of this counter can occur at re-initialization of the management system,</p><p>and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|SNMP|net.if.out.discards[ifOutDiscards.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Inbound packets discarded|<p>MIB: IF-MIB</p><p>The number of inbound packets which were chosen to be discarded</p><p>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.</p><p>One possible reason for discarding such a packet could be to free up buffer space.</p><p>Discontinuities in the value of this counter can occur at re-initialization of the management system,</p><p>and at other times as indicated by the value of ifCounterDiscontinuityTime.</p>|SNMP|net.if.in.discards[ifInDiscards.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- CHANGE_PER_SECOND|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Interface type|<p>MIB: IF-MIB</p><p>The type of interface.</p><p>Additional values for ifType are assigned by the Internet Assigned NumbersAuthority (IANA),</p><p>through updating the syntax of the IANAifType textual convention.</p>|SNMP|net.if.type[ifType.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Network_interfaces|Interface {#IFNAME}({#IFALIAS}): Speed|<p>MIB: IF-MIB</p><p>An estimate of the interface's current bandwidth in units of 1,000,000 bits per second. If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n-500,000' to`n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. For a sub-layer which has no concept of bandwidth, this object should be zero.</p>|SNMP|net.if.speed[ifHighSpeed.{#SNMPINDEX}]<p>**Preprocessing**:</p><p>- MULTIPLIER: `1000000`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1h`</p>|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Interface {#IFNAME}({#IFALIAS}): Link down|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This trigger expression works as follows:</p><p>1. Can be triggered if operations status is down.</p><p>2. {$IFCONTROL:"{#IFNAME}"}=1 - user can redefine Context macro to value - 0. That marks this interface as not important. No new trigger will be fired if this interface is down.</p><p>3. {TEMPLATE_NAME:METRIC.diff()}=1) - trigger fires only if operational status was up(1) sometime before. (So, do not fire 'ethernal off' interfaces.)</p><p>WARNING: if closed manually - won't fire again on next poll, because of .diff.</p>|`{$IFCONTROL:"{#IFNAME}"}=1 and ({TEMPLATE_NAME:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}=2 and {TEMPLATE_NAME:net.if.status[ifOperStatus.{#SNMPINDEX}].diff()}=1)`<p>Recovery expression:</p>`{TEMPLATE_NAME:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}<>2`|AVERAGE|<p>Manual close: YES</p>|
|Interface {#IFNAME}({#IFALIAS}): High bandwidth usage ( > {$IF_UTIL_MAX:"{#IFNAME}"}% )|<p>Last value: {ITEM.LASTVALUE1}.</p>|`({TEMPLATE_NAME:net.if.in[ifInOctets.{#SNMPINDEX}].avg(15m)}>({$IF_UTIL_MAX:"{#IFNAME}"}/100)*{Template Module Interfaces Windows SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()} or {Template Module Interfaces Windows SNMPv2:net.if.out[ifOutOctets.{#SNMPINDEX}].avg(15m)}>({$IF_UTIL_MAX:"{#IFNAME}"}/100)*{Template Module Interfaces Windows SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()}) and {Template Module Interfaces Windows SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()}>0`<p>Recovery expression:</p>`{TEMPLATE_NAME:net.if.in[ifInOctets.{#SNMPINDEX}].avg(15m)}<(({$IF_UTIL_MAX:"{#IFNAME}"}-3)/100)*{Template Module Interfaces Windows SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()} and {Template Module Interfaces Windows SNMPv2:net.if.out[ifOutOctets.{#SNMPINDEX}].avg(15m)}<(({$IF_UTIL_MAX:"{#IFNAME}"}-3)/100)*{Template Module Interfaces Windows SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()}`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}({#IFALIAS}): Link down</p>|
|Interface {#IFNAME}({#IFALIAS}): High error rate ( > {$IF_ERRORS_WARN:"{#IFNAME}"} for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Recovers when below 80% of {$IF_ERRORS_WARN:"{#IFNAME}"} threshold</p>|`{TEMPLATE_NAME:net.if.in.errors[ifInErrors.{#SNMPINDEX}].min(5m)}>{$IF_ERRORS_WARN:"{#IFNAME}"} or {Template Module Interfaces Windows SNMPv2:net.if.out.errors[ifOutErrors.{#SNMPINDEX}].min(5m)}>{$IF_ERRORS_WARN:"{#IFNAME}"}`<p>Recovery expression:</p>`{TEMPLATE_NAME:net.if.in.errors[ifInErrors.{#SNMPINDEX}].max(5m)}<{$IF_ERRORS_WARN:"{#IFNAME}"}*0.8 and {Template Module Interfaces Windows SNMPv2:net.if.out.errors[ifOutErrors.{#SNMPINDEX}].max(5m)}<{$IF_ERRORS_WARN:"{#IFNAME}"}*0.8`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}({#IFALIAS}): Link down</p>|
|Interface {#IFNAME}({#IFALIAS}): Ethernet has changed to lower speed than it was before|<p>Last value: {ITEM.LASTVALUE1}.</p><p>This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of autonegotiation issues. Ack to close.</p>|`{TEMPLATE_NAME:net.if.speed[ifHighSpeed.{#SNMPINDEX}].change()}<0 and {TEMPLATE_NAME:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()}>0 and ( {Template Module Interfaces Windows SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=6 or {Template Module Interfaces Windows SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=7 or {Template Module Interfaces Windows SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=11 or {Template Module Interfaces Windows SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=62 or {Template Module Interfaces Windows SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=69 or {Template Module Interfaces Windows SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=117 ) and ({Template Module Interfaces Windows SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}<>2)`<p>Recovery expression:</p>`({TEMPLATE_NAME:net.if.speed[ifHighSpeed.{#SNMPINDEX}].change()}>0 and {TEMPLATE_NAME:net.if.speed[ifHighSpeed.{#SNMPINDEX}].prev()}>0) or ({Template Module Interfaces Windows SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}=2)`|INFO|<p>Manual close: YES</p><p>**Depends on**:</p><p>- Interface {#IFNAME}({#IFALIAS}): Link down</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

