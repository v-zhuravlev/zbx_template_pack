
# Template App HAProxy by HTTP

## Overview

For Zabbix version: 4.4  
The template to monitor HAProxy by Zabbix that work without any external scripts.
Most of the metrics are collected in one go, thanks to Zabbix bulk data collection.

`Template App HAProxy by HTTP` collects metrics by polling [HAProxy Stats Page](https://www.haproxy.com/blog/exploring-the-haproxy-stats-page/) with HTTP agent remotely:

Note that this solution supports https and redirects.


This template was tested on:

- HAProxy, version 1.8
- Zabbix, version 4.4

## Setup

Setup [HAProxy Stats Page](https://www.haproxy.com/blog/exploring-the-haproxy-stats-page/).
Test availability of http_stub_status module with `nginx -V 2>&1 | grep -o with-http_stub_status_module`.

Example configuration of HAProxy:        
```text
frontend stats
    bind *:8404
    stats enable
    stats uri /stats
    stats refresh 10s
    stats admin if LOCALHOST        }
```

If you use another location, don't forget to change {$HAPROXY.STATS.PATH} macro.


## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$HAPROXY.BACK_QCUR.MAX.WARN}|<p>Maximum number of requests on BACKEND unassigned in queue for trigger expression.</p>|`10`|
|{$HAPROXY.FRONT_DREQ.MAX.WARN}|<p>The HAProxy maximum denied requests for trigger expression.</p>|`10`|
|{$HAPROXY.FRONT_EREQ.MAX.WARN}|<p>The HAProxy maximum number of request errors for trigger expression.</p>|`10`|
|{$HAPROXY.RESPONSE_TIME.MAX.WARN}|<p>The HAProxy stats page maximum response time in seconds for trigger expression.</p>|`10`|
|{$HAPROXY.SERVER_ERESP.MAX.WARN}|<p>Maximum of responses with error on server for trigger expression.</p>|`10`|
|{$HAPROXY.SERVER_QCUR.MAX.WARN}|<p>Maximum number of requests on server unassigned in queue for trigger expression.</p>|`10`|
|{$HAPROXY.SERVER_QTIME.MAX.WARN}|<p>Maximum of average time spent in queue on server for trigger expression.</p>|`10`|
|{$HAPROXY.SERVER_RTIME.MAX.WARN}|<p>Maximum of average server response time for trigger expression.</p>|`10`|
|{$HAPROXY.STATS.PATH}|<p>The path of HAProxy stats page.</p>|`http://haproxy:9000/stats;csv`|
|{$HAPROXY.STATS.PORT}|<p>The port of the HAProxy stats host or container.</p>|`9000`|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|BACKEND discovery|<p>Discovery backends</p>|DEPENDENT|haproxy.backend.discovery<p>**Filter**:</p>AND <p>- A: {#SVNAME} MATCHES_REGEX `BACKEND`</p>|
|FRONTEND discovery|<p>Discovery frontends</p>|DEPENDENT|haproxy.frontend.discovery<p>**Filter**:</p>AND <p>- A: {#SVNAME} MATCHES_REGEX `FRONTEND`</p>|
|Servers discovery|<p>Discovery Servers</p>|DEPENDENT|haproxy.server.discovery<p>**Filter**:</p>AND <p>- A: {#SVNAME} NOT_MATCHES_REGEX `FRONTEND|BACKEND`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|HAProxy|HAProxy: Service status|<p>-</p>|SIMPLE|net.tcp.service[http,"haproxy","{$HAPROXY.STATS.PORT}"]<p>**Preprocessing**:</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `10m`</p>|
|HAProxy|HAProxy: Service response time|<p>-</p>|SIMPLE|net.tcp.service.perf[http,"haproxy","{$HAPROXY.STATS.PORT}"]|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} status|<p>-</p>|DEPENDENT|haproxy.backend.status.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].status.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} rtime|<p>Average backend response time (in ms) for the last 1,024 requests</p>|DEPENDENT|haproxy.backend.rtime.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].rtime.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} econ|<p>Number of requests that encountered an error attempting to connect to a backend server</p>|DEPENDENT|haproxy.backend.econ.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].econ.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} dresp|<p>Responses denied due to security concerns (ACL-restricted)</p>|DEPENDENT|haproxy.backend.dresp.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].dresp.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} eresp|<p>Number of requests whose responses yielded an error</p>|DEPENDENT|haproxy.backend.eresp.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].eresp.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} qcur|<p>Current number of requests unassigned in queue</p>|DEPENDENT|haproxy.backend.qcur.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].qcur.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} qtime|<p>Average time spent in queue (in ms) for the last 1,024 requests</p>|DEPENDENT|haproxy.backend.qtime.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].qtime.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} wredis|<p>Number of times a request was redispatched to a different backend</p>|DEPENDENT|haproxy.backend.wredis.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].wredis.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} wretr|<p>Number of times a connection was retried</p>|DEPENDENT|haproxy.backend.wretr.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].wretr.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} status|<p>-</p>|DEPENDENT|haproxy.frontend.status.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].status.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} req_rate|<p>HTTP requests per second</p>|DEPENDENT|haproxy.frontend.req_rate.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].req_rate.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} rate|<p>Number of sessions created per second</p>|DEPENDENT|haproxy.frontend.rate.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].rate.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} ereq|<p>Number of request errors</p>|DEPENDENT|haproxy.frontend.ereq.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].ereq.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} dreq|<p>Requests denied due to security concerns (ACL-restricted)</p>|DEPENDENT|haproxy.frontend.dreq.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].dreq.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} hrsp_1xx|<p>-</p>|DEPENDENT|haproxy.frontend.hrsp_1xx.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].hrsp_1xx.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} hrsp_2xx|<p>-</p>|DEPENDENT|haproxy.frontend.hrsp_2xx.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].hrsp_2xx.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} hrsp_3xx|<p>-</p>|DEPENDENT|haproxy.frontend.hrsp_3xx.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].hrsp_3xx.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} hrsp_4xx|<p>Number of HTTP client errors</p>|DEPENDENT|haproxy.frontend.hrsp_4xx.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].hrsp_4xx.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} hrsp_5xx|<p>Number of HTTP server errors</p>|DEPENDENT|haproxy.frontend.hrsp_5xx.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].hrsp_5xx.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} bin|<p>Number of bytes received by the frontend</p>|DEPENDENT|haproxy.frontend.bin.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].bin.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} bout|<p>Number of bytes sent by the frontend</p>|DEPENDENT|haproxy.frontend.bout.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].bout.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} status|<p>-</p>|DEPENDENT|haproxy.server.status.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].status.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} rtime|<p>Average server response time (in ms) for the last 1,024 requests</p>|DEPENDENT|haproxy.server.rtime.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].rtime.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} econ|<p>Number of requests that encountered an error attempting to connect to a backend server</p>|DEPENDENT|haproxy.server.econ.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].econ.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} dresp|<p>Responses denied due to security concerns (ACL-restricted)</p>|DEPENDENT|haproxy.server.dresp.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].dresp.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} eresp|<p>Number of requests whose responses yielded an error</p>|DEPENDENT|haproxy.server.eresp.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].eresp.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} qcur|<p>Current number of requests unassigned in queue</p>|DEPENDENT|haproxy.server.qcur.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].qcur.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} qtime|<p>Average time spent in queue (in ms) for the last 1,024 requests</p>|DEPENDENT|haproxy.server.qtime.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].qtime.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} wredis|<p>Number of times a request was redispatched to a different backend</p>|DEPENDENT|haproxy.server.wredis.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].wredis.first()`</p>|
|HAProxy|HAProxy: {#PXNAME} {#SVNAME} wretr|<p>Number of times a connection was retried</p>|DEPENDENT|haproxy.server.wretr.[{#PXNAME}:{#SVNAME}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.[?(@.pxname == '{#PXNAME}' && @.svname == '{#SVNAME}')].wretr.first()`</p>|
|Zabbix_raw_items|HAProxy: Get stats|<p>HAProxy Statistics Report in CSV format</p>|HTTP_AGENT|haproxy.get<p>**Preprocessing**:</p><p>- JAVASCRIPT: `return value.slice(2,-1)`</p><p>- CSV_TO_JSON: ` 1`</p>|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|HAProxy: Service is down|<p>-</p>|`{TEMPLATE_NAME:net.tcp.service[http,"haproxy","{$HAPROXY.STATS.PORT}"].last()}=0`|AVERAGE|<p>Manual close: YES</p>|
|HAProxy: Service response time is too high (over {$HAPROXY.RESPONSE_TIME.MAX.WARN}s for 5m)|<p>-</p>|`{TEMPLATE_NAME:net.tcp.service.perf[http,"haproxy","{$HAPROXY.STATS.PORT}"].min(5m)}>{$HAPROXY.RESPONSE_TIME.MAX.WARN}`|WARNING|<p>Manual close: YES</p><p>**Depends on**:</p><p>- HAProxy: Service is down</p>|
|HAProxy: Current number of requests unassigned in queue more than {$HAPROXY.BACK_QCUR.MAX.WARN}|<p>Current number of requests unassigned in queue more than {$HAPROXY.BACK_QCUR.MAX.WARN}.</p>|`{TEMPLATE_NAME:haproxy.backend.qcur.[{#PXNAME}:{#SVNAME}].min(5m)}>{$HAPROXY.BACK_QCUR.MAX.WARN}`|WARNING||
|HAProxy: Number of request errors more than {$HAPROXY.FRONT_EREQ.MAX.WARN}|<p>Number of request errors more than {$HAPROXY.FRONT_EREQ.MAX.WARN}.</p>|`{TEMPLATE_NAME:haproxy.frontend.ereq.[{#PXNAME}:{#SVNAME}].min(5m)}>{$HAPROXY.FRONT_EREQ.MAX.WARN}`|WARNING||
|HAProxy: Number of requests denied more than {$HAPROXY.FRONT_DREQ.MAX.WARN}|<p>Number of requests denied due to security concerns (ACL-restricted) more than {$HAPROXY.FRONT_DREQ.MAX.WARN}.</p>|`{TEMPLATE_NAME:haproxy.frontend.dreq.[{#PXNAME}:{#SVNAME}].min(5m)}>{$HAPROXY.FRONT_DREQ.MAX.WARN}`|WARNING||
|HAProxy: Average server response time on {#PXNAME}:{#SVNAME} more than {$HAPROXY.SERVER_RTIME.MAX.WARN}|<p>Average server response time (in ms) for the last 1,024 requests more than {$HAPROXY.SERVER_RTIME.MAX.WARN}.</p>|`{TEMPLATE_NAME:haproxy.server.rtime.[{#PXNAME}:{#SVNAME}].min(5m)}>{$HAPROXY.SERVER_RTIME.MAX.WARN}`|WARNING||
|HAProxy: Number of responses with error on {#PXNAME}:{#SVNAME} more than {$HAPROXY.SERVER_ERESP.MAX.WARN}|<p>Number of requests on server, whose responses yielded an error, more than {$HAPROXY.SERVER_ERESP.MAX.WARN}.</p>|`{TEMPLATE_NAME:haproxy.server.eresp.[{#PXNAME}:{#SVNAME}].min(5m)}>{$HAPROXY.SERVER_ERESP.MAX.WARN}`|WARNING||
|HAProxy: Current number of requests on {#PXNAME}:{#SVNAME} unassigned in queue more than {$HAPROXY.SERVER_QCUR.MAX.WARN}|<p>Current number of requests unassigned in queue more than {$HAPROXY.SERVER_QCUR.MAX.WARN}.</p>|`{TEMPLATE_NAME:haproxy.server.qcur.[{#PXNAME}:{#SVNAME}].min(5m)}>{$HAPROXY.SERVER_QCUR.MAX.WARN}`|WARNING||
|HAProxy: Average time spent in queue on {#PXNAME}:{#SVNAME} more than {$HAPROXY.SERVER_QTIME.MAX.WARN}|<p>Average time spent in queue (in ms) for the last 1,024 requests more than {$HAPROXY.SERVER_QTIME.MAX.WARN}.</p>|`{TEMPLATE_NAME:haproxy.server.qtime.[{#PXNAME}:{#SVNAME}].min(5m)}>{$HAPROXY.SERVER_QTIME.MAX.WARN}`|WARNING||

## Feedback

Please report any issues with the template at https://support.zabbix.com

You can also provide feedback, discuss the template or ask for help with it at
[ZABBIX forums](https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/384765-discussion-thread-for-official-zabbix-template-nginx).

