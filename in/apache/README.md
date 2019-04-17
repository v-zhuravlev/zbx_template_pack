# Template App Apache *

Templates to monitor Apache HTTPD by Zabbix that work without any external scripts.  Most of the metrics are collected in one go, thanks to Zabbix bulk data collection.  
Two templates are available:  
`Template App Apache Zabbix agent` - (Zabbix version >= 3.4) - collects metrics by polling [mod_status](https://httpd.apache.org/docs/current/mod/mod_status.html) locally with Zabbix agent:

```text
HTTP/1.1 200 OK
Date: Tue, 16 Apr 2019 14:10:56 GMT
Server: Apache/2.4.33 (Unix)
Content-Length: 1074
Connection: close
Content-Type: text/plain; charset=ISO-8859-1

localhost
ServerVersion: Apache/2.4.33 (Unix)
ServerMPM: event
Server Built: Apr 30 2018 04:30:01
CurrentTime: Tuesday, 16-Apr-2019 14:10:56 UTC
RestartTime: Tuesday, 16-Apr-2019 13:15:56 UTC
ParentServerConfigGeneration: 1
ParentServerMPMGeneration: 0
ServerUptimeSeconds: 3299
ServerUptime: 54 minutes 59 seconds
Load1: 0.09
Load5: 0.17
Load15: 0.24
Total Accesses: 1051
Total kBytes: 266
CPUUser: .21
CPUSystem: .25
CPUChildrenUser: 0
CPUChildrenSystem: 0
CPULoad: .0139436
Uptime: 3299
ReqPerSec: .318581
BytesPerSec: 82.5656
BytesPerReq: 259.167
BusyWorkers: 1
IdleWorkers: 99
ConnsTotal: 0
ConnsAsyncWriting: 0
ConnsAsyncKeepAlive: 0
ConnsAsyncClosing: 0
Scoreboard: ________________W___________________________________________________________________________________.................................................................................................................................................................................
```

It also uses Zabbix agent to collect `httpd` Linux process stats like CPU usage, memory usage and whether process is running or not.

`Template App Apache HTTP` - (Zabbix version >= 4.0) - collects metrics by polling [mod_status](https://httpd.apache.org/docs/current/mod/mod_status.html) with HTTP agent remotely.  

## Setup

- Setup [mod_status](https://httpd.apache.org/docs/current/mod/mod_status.html)
- (If using `Template App Apache Zabbix agent`) install and setup [Zabbix agent](https://www.zabbix.com/documentation/current/manual/installation/install_from_packages)

## Zabbix configuration

Change those macros on host level if needed:

|Macro|Description|Default(agent)|Default(HTTP)|
|---|----|---|---|
|{$APACHE_STATUS_HOST}| | localhost | n/a |
|{$APACHE_STATUS_PATH}| | server-status?auto | server-status?auto|
|{$APACHE_STATUS_PORT}| | 80 | 80 |
|{$APACHE_PROC_NAME}| | httpd | n/a |

## Items

|Item|Triggers|Graphs|HTTP agent template|Zabbix agent template|
|---|---|---|---|---|
|apache.get_stub_status|x| |x|x|
|apache.version| | |x|x|
|apache.uptime| | |x|x|
|apache.requests.total.rate| |x|x|x|
|apache.requests.total| | |x|x|
|apache.bytes_per_second| | |x|x|
|apache.connections.async_closing| |x|x|x|
|apache.connections.async_keep_alive| |x|x|x|
|apache.connections.async_writing| |x|x|x|
|apache.connections.total| |x|x|x|
|apache.workers.busy| |x|x|x|
|apache.workers.idle| |x|x|x|
|apache.proc.num|x| | |x|
|apache.proc.mem.vsize| |x| |x|
|apache.proc.mem.rss| |x| |x|
|apache.proc.cpu.util| | | |x|

## Triggers

See in template

## Demo

![image](https://user-images.githubusercontent.com/14870891/56309444-42f3d780-6152-11e9-8677-03089dafb525.png)

![image](https://user-images.githubusercontent.com/14870891/56310724-3d4bc100-6155-11e9-9a82-907b3206c748.png)

![image](https://user-images.githubusercontent.com/14870891/56310788-5bb1bc80-6155-11e9-9d08-bb6c1fe52a0b.png)

![image](https://user-images.githubusercontent.com/14870891/56310973-b0553780-6155-11e9-9bf1-ca82535814d1.png)

## Next steps

TBD

## References

https://httpd.apache.org/docs/current/mod/mod_status.html