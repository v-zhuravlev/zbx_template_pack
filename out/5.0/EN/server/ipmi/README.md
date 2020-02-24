
# Template Server by IPMI

## Overview

For Zabbix version: 5.0  

## Setup


## Zabbix configuration


### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$IPMI.SENSOR_TYPE.MATCHES}|<p>This macro is used in sensors discovery. Can be overridden on the host or linked template level.</p>|`.*`|
|{$IPMI.SENSOR_TYPE.NOT_MATCHES}|<p>This macro is used in sensors discovery. Can be overridden on the host or linked template level.</p>|`invalid`|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Discrete sensors discovery||DEPENDENT|ipmi.discrete.discovery<p>**Filter**:</p>AND <p>- A: {#SENSOR_READING_TYPE} NOT_MATCHES_REGEX `threshold`</p><p>- B: {#SENSOR_TYPE} MATCHES_REGEX `{$IPMI.SENSOR_TYPE.MATCHES}`</p><p>- C: {#SENSOR_TYPE} NOT_MATCHES_REGEX `{$IPMI.SENSOR_TYPE.NOT_MATCHES}`</p>|
|Threshold sensors discovery||DEPENDENT|ipmi.sensors.discovery<p>**Filter**:</p>AND <p>- A: {#SENSOR_READING_TYPE} MATCHES_REGEX `threshold`</p><p>- B: {#SENSOR_TYPE} MATCHES_REGEX `{$IPMI.SENSOR_TYPE.MATCHES}`</p><p>- C: {#SENSOR_TYPE} NOT_MATCHES_REGEX `{$IPMI.SENSOR_TYPE.NOT_MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|General|IPMI: {#SENSOR_ID}||DEPENDENT|ipmi.state_text[{#SENSOR_ID}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.id=='{#SENSOR_ID}')].state.text.first()`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|General|IPMI: {#SENSOR_ID}, {#SENSOR_UNIT}||DEPENDENT|ipmi.value[{#SENSOR_ID}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.id=='{#SENSOR_ID}')].value.first()`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1h`</p>|
|Zabbix_raw_items|Get IPMI sensors||IPMI|ipmi.get|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|IPMI: {#SENSOR_ID} value is low (over {#SENSOR_LO_WARN} for 5m)||`{TEMPLATE_NAME:ipmi.value[{#SENSOR_ID}].min(5m)}<{#SENSOR_LO_WARN}`|WARNING|<p>**Depends on**:</p><p>- IPMI: {#SENSOR_ID} value is critically low (over {#SENSOR_LO_DISAST} for 5m)</p><p>- IPMI: {#SENSOR_ID} value is too low (over {#SENSOR_LO_CRIT} for 5m)</p>|
|IPMI: {#SENSOR_ID} value is too low (over {#SENSOR_LO_CRIT} for 5m)||`{TEMPLATE_NAME:ipmi.value[{#SENSOR_ID}].min(5m)}<{#SENSOR_LO_CRIT}`|HIGH|<p>**Depends on**:</p><p>- IPMI: {#SENSOR_ID} value is critically low (over {#SENSOR_LO_DISAST} for 5m)</p>|
|IPMI: {#SENSOR_ID} value is critically low (over {#SENSOR_LO_DISAST} for 5m)||`{TEMPLATE_NAME:ipmi.value[{#SENSOR_ID}].min(5m)}<{#SENSOR_LO_DISAST}`|DISASTER||
|IPMI: {#SENSOR_ID} value is high (over {#SENSOR_HI_WARN} for 5m)||`{TEMPLATE_NAME:ipmi.value[{#SENSOR_ID}].min(5m)}>{#SENSOR_HI_WARN}`|WARNING|<p>**Depends on**:</p><p>- IPMI: {#SENSOR_ID} value is critically high (over {#SENSOR_HI_DISAST} for 5m)</p><p>- IPMI: {#SENSOR_ID} value is too high (over {#SENSOR_HI_CRIT} for 5m)</p>|
|IPMI: {#SENSOR_ID} value is too high (over {#SENSOR_HI_CRIT} for 5m)||`{TEMPLATE_NAME:ipmi.value[{#SENSOR_ID}].min(5m)}>{#SENSOR_HI_CRIT}`|HIGH|<p>**Depends on**:</p><p>- IPMI: {#SENSOR_ID} value is critically high (over {#SENSOR_HI_DISAST} for 5m)</p>|
|IPMI: {#SENSOR_ID} value is critically high (over {#SENSOR_HI_DISAST} for 5m)||`{TEMPLATE_NAME:ipmi.value[{#SENSOR_ID}].min(5m)}>{#SENSOR_HI_DISAST}`|DISASTER||

## Feedback

Please report any issues with the template at https://support.zabbix.com

