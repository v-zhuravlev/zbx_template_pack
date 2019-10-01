
# Template App RabbitMQ Cluster by HTTP

## Overview

For Zabbix version: 4.2  
The template to monitor RabbitMQ by Zabbix that work without any external scripts.
Most of the metrics are collected in one go, thanks to Zabbix bulk data collection.

Template App RabbitMQ Cluster — (Zabbix version >= 4.2) collects metrics by polling [RabbitMQ management plugin](https://www.rabbitmq.com/management.html) with HTTP agent remotely.



This template was tested on:

- RabbitMQ, version 3.5.7, 3.7.17, 3.7.18

## Setup

Enable the RabbitMQ management plugin. See [RabbitMQ’s documentation](https://www.rabbitmq.com/management.html) to enable it.

Create a user to monitor the service:

```bash
rabbitmqctl add_user zbx_monitor <PASSWORD>
rabbitmqctl set_permissions  -p / zbx_monitor "" "" ".*"
rabbitmqctl set_user_tags zbx_monitor monitoring
```

Login and password are also set in macros:

- {$RABBITMQ.API.USER}
- {$RABBITMQ.API.PASSWORD}


## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$RABBITMQ.API.PASSWORD}|<p>-</p>|`zabbix`|
|{$RABBITMQ.API.PORT}|<p>The port of RabbitMQ API endpoint</p>|`15672`|
|{$RABBITMQ.API.SCHEME}|<p>Request scheme which may be http or https</p>|`http`|
|{$RABBITMQ.API.USER}|<p>-</p>|`zbx_monitor`|
|{$RABBITMQ.CONN.MAX.WARN}|<p>Maximum RabbitMQ connections for trigger expression</p>|`1000`|
|{$RABBITMQ.LLD.FILTER.EXCHANGE.MATCHES}|<p>Filter of discoverable exchanges</p>|`.*`|
|{$RABBITMQ.LLD.FILTER.EXCHANGE.NOT_MATCHES}|<p>Filter to exclude discovered exchanges</p>|`CHANGE_IF_NEEDED`|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Exchanges discovery|<p>Individual exchange metrics</p>|DEPENDENT|rabbitmq.exchanges.discovery<p>**Filter**:</p>AND <p>- A: {#EXCHANGE} MATCHES_REGEX `{$RABBITMQ.LLD.FILTER.EXCHANGE.MATCHES}`</p><p>- B: {#EXCHANGE} NOT_MATCHES_REGEX `{$RABBITMQ.LLD.FILTER.EXCHANGE.NOT_MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|RabbitMQ|RabbitMQ: Connections total|<p>Total number of connections</p>|DEPENDENT|rabbitmq.overview.object_totals.connections<p>**Preprocessing**:</p><p>- JSONPATH: `$.object_totals.connections`</p></p>|
|RabbitMQ|RabbitMQ: Channels total|<p>Total number of channels</p>|DEPENDENT|rabbitmq.overview.object_totals.channels<p>**Preprocessing**:</p><p>- JSONPATH: `$.object_totals.channels`</p></p>|
|RabbitMQ|RabbitMQ: Queues total|<p>Total number of queues</p>|DEPENDENT|rabbitmq.overview.object_totals.queues<p>**Preprocessing**:</p><p>- JSONPATH: `$.object_totals.queues`</p></p>|
|RabbitMQ|RabbitMQ: Consumers total|<p>Total number of consumers</p>|DEPENDENT|rabbitmq.overview.object_totals.consumers<p>**Preprocessing**:</p><p>- JSONPATH: `$.object_totals.consumers`</p></p>|
|RabbitMQ|RabbitMQ: Exchanges total|<p>Total number of exchanges</p>|DEPENDENT|rabbitmq.overview.object_totals.exchanges<p>**Preprocessing**:</p><p>- JSONPATH: `$.object_totals.exchanges`</p></p>|
|RabbitMQ|RabbitMQ: Messages total|<p>Total number of messages (ready plus unacknowledged)</p>|DEPENDENT|rabbitmq.overview.queue_totals.messages<p>**Preprocessing**:</p><p>- JSONPATH: `$.queue_totals.messages`</p></p>|
|RabbitMQ|RabbitMQ: Messages ready for delivery|<p>Number of messages ready for deliver</p>|DEPENDENT|rabbitmq.overview.queue_totals.messages.ready<p>**Preprocessing**:</p><p>- JSONPATH: `$.queue_totals.messages_ready`</p></p>|
|RabbitMQ|RabbitMQ: Messages unacknowledged|<p>Number of unacknowledged messages</p>|DEPENDENT|rabbitmq.overview.queue_totals.messages.unacknowledged<p>**Preprocessing**:</p><p>- JSONPATH: `$.queue_totals.messages_unacknowledged`</p></p>|
|RabbitMQ|RabbitMQ: Messages acknowledged|<p>Number of messages delivered to clients and acknowledged</p>|DEPENDENT|rabbitmq.overview.messages.ack<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.ack`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages acknowledged per second|<p>Rate of messages delivered to clients and acknowledged per second</p>|DEPENDENT|rabbitmq.overview.messages.ack.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.ack_details.rate`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages confirmed|<p>Count of messages confirmed</p>|DEPENDENT|rabbitmq.overview.messages.confirm<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.confirm`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages confirmed per second|<p>Rate of messages confirmed per second</p>|DEPENDENT|rabbitmq.overview.messages.confirm.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.confirm_details.rate`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages delivered|<p>Sum of messages delivered in acknowledgement mode to consumers, in no-acknowledgement mode to consumers, in acknowledgement mode in response to basic.get, and in no-acknowledgement mode in response to basic.get</p>|DEPENDENT|rabbitmq.overview.messages.deliver_get<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.deliver_get`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages delivered per second|<p>Rate per second of the sum of messages delivered in acknowledgement mode to consumers, in no-acknowledgement mode to consumers, in acknowledgement mode in response to basic.get, and in no-acknowledgement mode in response to basic.get</p>|DEPENDENT|rabbitmq.overview.messages.deliver_get.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.deliver_get_details.rate`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages published|<p>Count of messages published</p>|DEPENDENT|rabbitmq.overview.messages.publish<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.publish`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages published per second|<p>Rate of messages published per second</p>|DEPENDENT|rabbitmq.overview.messages.publish.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.publish_details.rate`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages publish_in|<p>Count of messages published from channels into this overview</p>|DEPENDENT|rabbitmq.overview.messages.publish_in<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.publish_in`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages publish_in per second|<p>Rate of messages published from channels into this overview per sec</p>|DEPENDENT|rabbitmq.overview.messages.publish_in.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.publish_in_details.rate`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages publish_out|<p>Count of messages published from this overview into queues</p>|DEPENDENT|rabbitmq.overview.messages.publish_out<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.publish_out`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages publish_out per second|<p>Rate of messages published from this overview into queues per second,0,rabbitmq,total msgs pub out rate</p>|DEPENDENT|rabbitmq.overview.messages.publish_out.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.publish_out_details.rate`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages returned unroutable|<p>Count of messages returned to publisher as unroutable</p>|DEPENDENT|rabbitmq.overview.messages.return_unroutable<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.return_unroutable`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages returned unroutable|<p>Rate of messages returned to publisher as unroutable per second</p>|DEPENDENT|rabbitmq.overview.messages.return_unroutable.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.return_unroutable_details.rate`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages returned unroutable|<p>Count of subset of messages in deliver_get which had the redelivered flag set</p>|DEPENDENT|rabbitmq.overview.messages.redeliver<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.redeliver`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Messages returned unroutable|<p>Rate of subset of messages in deliver_get which had the redelivered flag set per second</p>|DEPENDENT|rabbitmq.overview.messages.redeliver.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.message_stats.redeliver_details.rate`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages acknowledged|<p>Number of messages delivered to clients and acknowledged</p>|DEPENDENT|rabbitmq.exchange.messages.ack["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.ack.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages acknowledged per second|<p>Rate of messages delivered to clients and acknowledged per second</p>|DEPENDENT|rabbitmq.exchange.messages.ack.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.ack_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages confirmed|<p>Count of messages confirmed</p>|DEPENDENT|rabbitmq.exchange.messages.confirm["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.confirm.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages confirmed per second|<p>Rate of messages confirmed per second</p>|DEPENDENT|rabbitmq.exchange.messages.confirm.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.confirm_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages delivered|<p>Sum of messages delivered in acknowledgement mode to consumers, in no-acknowledgement mode to consumers, in acknowledgement mode in response to basic.get, and in no-acknowledgement mode in response to basic.get</p>|DEPENDENT|rabbitmq.exchange.messages.deliver_get["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.deliver_get.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages delivered per second|<p>Rate per second of the sum of messages delivered in acknowledgement mode to consumers, in no-acknowledgement mode to consumers, in acknowledgement mode in response to basic.get, and in no-acknowledgement mode in response to basic.get</p>|DEPENDENT|rabbitmq.exchange.messages.deliver_get.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.deliver_get_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages published|<p>Count of messages published</p>|DEPENDENT|rabbitmq.exchange.messages.publish["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.publish.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages published per second|<p>Rate of messages published per second</p>|DEPENDENT|rabbitmq.exchange.messages.publish.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.publish_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages publish_in|<p>Count of messages published from channels into this overview</p>|DEPENDENT|rabbitmq.exchange.messages.publish_in["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.publish_in.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages publish_in per second|<p>Rate of messages published from channels into this overview per sec</p>|DEPENDENT|rabbitmq.exchange.messages.publish_in.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.publish_in_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages publish_out|<p>Count of messages published from this overview into queues</p>|DEPENDENT|rabbitmq.exchange.messages.publish_out["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.publish_out.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages publish_out per second|<p>Rate of messages published from this overview into queues per second,0,rabbitmq,total msgs pub out rate</p>|DEPENDENT|rabbitmq.exchange.messages.publish_out.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.publish_out_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages returned unroutable|<p>Count of messages returned to publisher as unroutable</p>|DEPENDENT|rabbitmq.exchange.messages.return_unroutable["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.return_unroutable.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages returned unroutable per second|<p>Rate of messages returned to publisher as unroutable per second</p>|DEPENDENT|rabbitmq.exchange.messages.return_unroutable.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.return_unroutable_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages redelivered|<p>Count of subset of messages in deliver_get which had the redelivered flag set</p>|DEPENDENT|rabbitmq.exchange.messages.redeliver["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.redeliver.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages redelivered per second|<p>Rate of subset of messages in deliver_get which had the redelivered flag set per second</p>|DEPENDENT|rabbitmq.exchange.messages.redeliver.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#EXCHANGE}" && @.vhost == "{#VHOST}" && @.type =="{#TYPE}")].message_stats.redeliver_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|Zabbix_raw_items|RabbitMQ: Get Overview|<p>The HTTP API endpoint that returns cluster-wide metrics</p>|HTTP_AGENT|rabbitmq.get_overview|
|Zabbix_raw_items|RabbitMQ: Get Exchanges|<p>The HTTP API endpoint that returns exchanges metrics</p>|HTTP_AGENT|rabbitmq.get_exchanges|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|RabbitMQ: Total number of connections is too high (over {$RABBITMQ.CONN.MAX.WARN} for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:rabbitmq.overview.object_totals.connections.min(5m)}>{$RABBITMQ.CONN.MAX.WARN}`|WARNING||
|RabbitMQ: Failed to fetch overview data (or no data for 30m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Zabbix has not received data for items for the last 30 minutes.</p>|`{TEMPLATE_NAME:rabbitmq.get_overview.nodata(30m)}=1`|WARNING|<p>Manual close: YES</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

You can also provide feedback, discuss the template or ask for help with it at
[ZABBIX forums](forum url).

