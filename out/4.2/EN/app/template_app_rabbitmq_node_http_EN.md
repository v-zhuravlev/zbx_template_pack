
# Template App RabbitMQ Node by HTTP

## Overview

For Zabbix version: 4.2  
The template to monitor RabbitMQ by Zabbix that work without any external scripts.
Most of the metrics are collected in one go, thanks to Zabbix bulk data collection.

Template App RabbitMQ Node — (Zabbix version >= 4.2) collects metrics by polling [RabbitMQ management plugin](https://www.rabbitmq.com/management.html) with HTTP agent remotely.



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
|{$RABBITMQ.CLUSTER.NAME}|<p>The name of RabbitMQ cluster</p>|`rabbit`|
|{$RABBITMQ.LLD.FILTER.QUEUE.MATCHES}|<p>Filter of discoverable queues</p>|`.*`|
|{$RABBITMQ.LLD.FILTER.QUEUE.NOT_MATCHES}|<p>Filter to exclude discovered queues</p>|`CHANGE_IF_NEEDED`|
|{$RABBITMQ.MESSAGES.MAX.WARN}|<p>Maximum number of messages in the queue for trigger expression</p>|`1000`|
|{$RABBITMQ.RESPONSE_TIME.MAX.WARN}|<p>Maximum RabbitMQ response time in seconds for trigger expression</p>|`10`|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Queues discovery|<p>Individual queue metrics</p>|DEPENDENT|rabbitmq.queues.discovery<p>**Filter**:</p>AND <p>- A: {#QUEUE} MATCHES_REGEX `{$RABBITMQ.LLD.FILTER.QUEUE.MATCHES}`</p><p>- B: {#QUEUE} NOT_MATCHES_REGEX `{$RABBITMQ.LLD.FILTER.QUEUE.NOT_MATCHES}`</p><p>- C: {#NODE} MATCHES_REGEX `{$RABBITMQ.CLUSTER.NAME}@{HOST.NAME}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|RabbitMQ|RabbitMQ: Healthcheck|<p>Runs basic healthchecks in the current node. Checks that the rabbit application is running, channels and queues can be listed successfully, and that no alarms are in effect.</p>|HTTP_AGENT|rabbitmq.healthcheck<p>**Preprocessing**:</p><p>- JSONPATH: `$.status`</p></p><p>- BOOL_TO_DECIMAL|
|RabbitMQ|RabbitMQ: Management version|<p>Version of the management plugin in use</p>|DEPENDENT|rabbitmq.overview.management_version<p>**Preprocessing**:</p><p>- JSONPATH: `$.management_version`</p></p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p></p>|
|RabbitMQ|RabbitMQ: Rabbitmq version|<p>Version of RabbitMQ on the node which processed this request</p>|DEPENDENT|rabbitmq.overview.rabbitmq_version<p>**Preprocessing**:</p><p>- JSONPATH: `$.rabbitmq_version`</p></p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p></p>|
|RabbitMQ|RabbitMQ: Used file descriptors|<p>Used file descriptors</p>|DEPENDENT|rabbitmq.node.fd_used<p>**Preprocessing**:</p><p>- JSONPATH: `$.fd_used`</p></p>|
|RabbitMQ|RabbitMQ: Free disk space|<p>Current free disk space</p>|DEPENDENT|rabbitmq.node.disk_free<p>**Preprocessing**:</p><p>- JSONPATH: `$.disk_free`</p></p>|
|RabbitMQ|RabbitMQ: Disk free limit|<p>Disk free space limit in bytes</p>|DEPENDENT|rabbitmq.node.disk_free_limit<p>**Preprocessing**:</p><p>- JSONPATH: `$.disk_free_limit`</p></p>|
|RabbitMQ|RabbitMQ: Memory used|<p>Memory used in bytes</p>|DEPENDENT|rabbitmq.node.mem_used<p>**Preprocessing**:</p><p>- JSONPATH: `$.mem_used`</p></p>|
|RabbitMQ|RabbitMQ: Memory limit|<p>Memory usage high watermark in bytes</p>|DEPENDENT|rabbitmq.node.mem_limit<p>**Preprocessing**:</p><p>- JSONPATH: `$.mem_limit`</p></p>|
|RabbitMQ|RabbitMQ: Runtime run queue|<p>Average number of Erlang processes waiting to run</p>|DEPENDENT|rabbitmq.node.run_queue<p>**Preprocessing**:</p><p>- JSONPATH: `$.run_queue`</p></p>|
|RabbitMQ|RabbitMQ: Sockets used|<p>Number of file descriptors used as sockets</p>|DEPENDENT|rabbitmq.node.sockets_used<p>**Preprocessing**:</p><p>- JSONPATH: `$.sockets_used`</p></p>|
|RabbitMQ|RabbitMQ: Sockets available|<p>File descriptors available for use as sockets</p>|DEPENDENT|rabbitmq.node.sockets_total<p>**Preprocessing**:</p><p>- JSONPATH: `$.sockets_total`</p></p>|
|RabbitMQ|RabbitMQ: Number of network partitions|<p>Number of network partitions this node is seeing</p>|DEPENDENT|rabbitmq.node.partitions<p>**Preprocessing**:</p><p>- JSONPATH: `$.partitions`</p></p><p>- JAVASCRIPT: `return JSON.parse(value).length;`</p></p>|
|RabbitMQ|RabbitMQ: Is running|<p>Is the node running or not</p>|DEPENDENT|rabbitmq.node.running<p>**Preprocessing**:</p><p>- JSONPATH: `$.running`</p></p><p>- BOOL_TO_DECIMAL|
|RabbitMQ|RabbitMQ: Memory alarm|<p>Does the host has memory alarm</p>|DEPENDENT|rabbitmq.node.mem_alarm<p>**Preprocessing**:</p><p>- JSONPATH: `$.mem_alarm`</p></p><p>- BOOL_TO_DECIMAL|
|RabbitMQ|RabbitMQ: Disk free alarm|<p>Does the node have disk alarm</p>|DEPENDENT|rabbitmq.node.disk_free_alarm<p>**Preprocessing**:</p><p>- JSONPATH: `$.disk_free_alarm`</p></p><p>- BOOL_TO_DECIMAL|
|RabbitMQ|RabbitMQ: Uptime|<p>Uptime in milliseconds</p>|DEPENDENT|rabbitmq.node.uptime<p>**Preprocessing**:</p><p>- JSONPATH: `$.uptime`</p></p><p>- MULTIPLIER: `0.001`</p></p>|
|RabbitMQ|RabbitMQ: Service ping|<p>-</p>|SIMPLE|net.tcp.service[http,"{HOST.CONN}","{$RABBITMQ.API.PORT}"]<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `10m`</p></p>|
|RabbitMQ|RabbitMQ: Service response time|<p>-</p>|SIMPLE|net.tcp.service.perf[http,"{HOST.CONN}","{$RABBITMQ.API.PORT}"]|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages|<p>Count of the total messages in the queue</p>|DEPENDENT|rabbitmq.queue.messages["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].messages.first()`</p></p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages per second|<p>Count per second of the total messages in the queue</p>|DEPENDENT|rabbitmq.queue.messages.rate["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].messages_details.rate.first()`</p></p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Consumers|<p>Number of consumers</p>|DEPENDENT|rabbitmq.queue.consumers["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].consumers.first()`</p></p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Memory|<p>Bytes of memory consumed by the Erlang process associated with the queue, including stack, heap and internal structures</p>|DEPENDENT|rabbitmq.queue.memory["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].memory.first()`</p></p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages ready|<p>Number of messages ready to be delivered to clients</p>|DEPENDENT|rabbitmq.queue.messages_ready["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].messages_ready.first()`</p></p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages ready per second|<p>Number per second of messages ready to be delivered to clients</p>|DEPENDENT|rabbitmq.queue.messages_ready.rate["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].messages_ready_details.rate.first()`</p></p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages unacknowledged|<p>Number of messages delivered to clients but not yet acknowledged</p>|DEPENDENT|rabbitmq.queue.messages_unacknowledged["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].messages_unacknowledged.first()`</p></p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages unacknowledged per second|<p>Number per second of messages delivered to clients but not yet acknowledged</p>|DEPENDENT|rabbitmq.queue.messages_unacknowledged.rate["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].messages_unacknowledged_details.rate.first()`</p></p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages acknowledged|<p>Number of messages delivered to clients and acknowledged</p>|DEPENDENT|rabbitmq.queue.messages.ack["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].message_stats.ack.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages acknowledged per second|<p>Number per second of messages delivered to clients and acknowledged</p>|DEPENDENT|rabbitmq.queue.messages.ack.rate["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].message_stats.ack_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages delivered|<p>Count of messages delivered in acknowledgement mode to consumers</p>|DEPENDENT|rabbitmq.queue.messages.deliver["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].message_stats.deliver.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages delivered per second|<p>Count of messages delivered in acknowledgement mode to consumers</p>|DEPENDENT|rabbitmq.queue.messages.deliver.rate["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].message_stats.deliver_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages delivered|<p>Sum of messages delivered in acknowledgement mode to consumers, in no-acknowledgement mode to consumers, in acknowledgement mode in response to basic.get, and in no-acknowledgement mode in response to basic.get</p>|DEPENDENT|rabbitmq.queue.messages.deliver_get["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].message_stats.deliver_get.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages delivered per second|<p>Rate per second of the sum of messages delivered in acknowledgement mode to consumers, in no-acknowledgement mode to consumers, in acknowledgement mode in response to basic.get, and in no-acknowledgement mode in response to basic.get</p>|DEPENDENT|rabbitmq.queue.messages.deliver_get.rate["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].message_stats.deliver_get_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages published|<p>Count of messages published</p>|DEPENDENT|rabbitmq.queue.messages.publish["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].message_stats.publish.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages published per second|<p>Rate per second of messages published</p>|DEPENDENT|rabbitmq.queue.messages.publish.rate["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].message_stats.publish_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages redelivered|<p>Count of subset of messages in deliver_get which had the redelivered flag set</p>|DEPENDENT|rabbitmq.queue.messages.redeliver["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].message_stats.redeliver.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|RabbitMQ|RabbitMQ: Queue {#VHOST}/{#QUEUE}: Messages redelivered per second|<p>Rate per second of subset of messages in deliver_get which had the redelivered flag set</p>|DEPENDENT|rabbitmq.queue.messages.redeliver.rate["{#VHOST}/{#QUEUE}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$[?(@.name == "{#QUEUE}" && @.vhost == "{#VHOST}")].message_stats.redeliver_details.rate.first()`</p><p>⛔️ON_FAIL: `CUSTOM_VALUE -> 0`</p>|
|Zabbix_raw_items|RabbitMQ: Get Overview|<p>The HTTP API endpoint that returns cluster-wide metrics</p>|HTTP_AGENT|rabbitmq.get_overview|
|Zabbix_raw_items|RabbitMQ: Get Nodes|<p>The HTTP API endpoint that returns nodes metrics</p>|HTTP_AGENT|rabbitmq.get_nodes|
|Zabbix_raw_items|RabbitMQ: Get Queues|<p>The HTTP API endpoint that returns queues metrics</p>|HTTP_AGENT|rabbitmq.get_queues|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|RabbitMQ: Node healthcheck failed|<p>Last value: {ITEM.LASTVALUE1}.</p><p>https://www.rabbitmq.com/monitoring.html#health-checks</p>|`{TEMPLATE_NAME:rabbitmq.healthcheck.last(0)}=0`|AVERAGE||
|RabbitMQ: Version has changed (new version: {ITEM.VALUE})|<p>Last value: {ITEM.LASTVALUE1}.</p><p>RabbitMQ version has changed. Ack to close.</p>|`{TEMPLATE_NAME:rabbitmq.overview.rabbitmq_version.diff()}=1 and {TEMPLATE_NAME:rabbitmq.overview.rabbitmq_version.strlen()}>0`|INFO|<p>Manual close: YES</p>|
|RabbitMQ: Number of network partitions is too high (more than 0 for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:rabbitmq.node.partitions.min(5m)}>0`|WARNING||
|RabbitMQ: Node is not running|<p>Last value: {ITEM.LASTVALUE1}.</p><p>RabbitMQ node is not running</p>|`{TEMPLATE_NAME:rabbitmq.node.running.max(5m)}=0`|AVERAGE|<p>**Depends on**:</p><p>- RabbitMQ: Service is down</p>|
|RabbitMQ: Memory alarm (Memory usage threshold has been reached)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>https://www.rabbitmq.com/memory.html</p>|`{TEMPLATE_NAME:rabbitmq.node.mem_alarm.last(0)}=1`|AVERAGE||
|RabbitMQ: Free disk space alarm (Free space threshold has been reached)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>https://www.rabbitmq.com/disk-alarms.html</p>|`{TEMPLATE_NAME:rabbitmq.node.disk_free_alarm.last(0)}=1`|AVERAGE||
|RabbitMQ: has been restarted (uptime < 10m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>The RabbitMQ uptime is less than 10 minutes</p>|`{TEMPLATE_NAME:rabbitmq.node.uptime.last()}<10m`|INFO|<p>Manual close: YES</p>|
|RabbitMQ: Service is down|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:net.tcp.service[http,"{HOST.CONN}","{$RABBITMQ.API.PORT}"].last()}=0`|AVERAGE|<p>Manual close: YES</p>|
|RabbitMQ: Service response time is too high (over {$RABBITMQ.RESPONSE_TIME.MAX.WARN}s for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:net.tcp.service.perf[http,"{HOST.CONN}","{$RABBITMQ.API.PORT}"].min(5m)}>{$RABBITMQ.RESPONSE_TIME.MAX.WARN}`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- RabbitMQ: Service is down</p>|
|RabbitMQ: Too many messages in queue (over {$RABBITMQ.MESSAGES.MAX.WARN} for 5m)|<p>Last value: {ITEM.LASTVALUE1}.</p>|`{TEMPLATE_NAME:rabbitmq.queue.messages["{#VHOST}/{#QUEUE}"].min(5m)}>{$RABBITMQ.MESSAGES.MAX.WARN:"{#QUEUE}"}`|WARNING||
|RabbitMQ: Failed to fetch overview data (or no data for 30m)|<p>Last value: {ITEM.LASTVALUE1}.</p><p>Zabbix has not received data for items for the last 30 minutes.</p>|`{TEMPLATE_NAME:rabbitmq.get_overview.nodata(30m)}=1`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- RabbitMQ: Service is down</p>|

## Feedback

Please report any issues with the template at https://support.zabbix.com

You can also provide feedback, discuss the template or ask for help with it at
[ZABBIX forums](forum url).

