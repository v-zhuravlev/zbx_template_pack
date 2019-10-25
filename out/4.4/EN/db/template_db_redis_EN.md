
# Template DB Redis

## Overview

For Zabbix version: 4.4  
Overview



This template was tested on:

- Redis, version 5.0.6

## Setup

Setup


## Zabbix configuration

No specific Zabbix configuration is required.

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$REDIS.CONN.URI}|<p>Connection string in the URI format (password is not used). This param overwrites a value configured in the "Server" option of the configuration file (if it's set), otherwise, the plugin's default value is used: "tcp://localhost:6379"</p>|`tcp://localhost:6379`|
|{$REDIS.LLD.FILTER.DB.MATCHES}|<p>Filter of discoverable databases</p>|`.*`|
|{$REDIS.LLD.FILTER.DB.NOT_MATCHES}|<p>Filter to exclude discovered databases</p>|`CHANGE_IF_NEEDED`|
|{$REDIS.LLD.PROCESS_NAME}|<p>Redis server process name for LLD</p>|`redis-server`|
|{$REDIS.PROCESS_NAME}|<p>Redis server process name</p>|`redis-server`|

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Keyspace discovery|<p>Individual keyspace metrics</p>|DEPENDENT|redis.keyspace.discovery<p>**Preprocessing**:</p><p>- JAVASCRIPT: `return JSON.stringify(Object.keys(JSON.parse(value).Keyspace).map(function (v){return {"{#DB}": v}}));`</p><p>**Filter**:</p>AND <p>- A: {#DB} MATCHES_REGEX `{$REDIS.LLD.FILTER.DB.MATCHES}`</p><p>- B: {#DB} NOT_MATCHES_REGEX `{$REDIS.LLD.FILTER.DB.NOT_MATCHES}`</p>|
|AOF metrics discovery|<p>If AOF is activated, additional metrics will be added</p>|DEPENDENT|redis.persistence.aof.discovery<p>**Preprocessing**:</p><p>- JAVASCRIPT: `return JSON.stringify(JSON.parse(value).Persistence.aof_enabled === '1' ? [{'{#SINGLETON}': ''}] : []);`</p>|
|Slave metrics discovery|<p>If the instance is a replica, additional metrics are provided</p>|DEPENDENT|redis.replication.slave.discovery<p>**Preprocessing**:</p><p>- JAVASCRIPT: `return JSON.stringify(JSON.parse(value).Replication.role === 'slave' ? [{'{#SINGLETON}': ''}] : []);`</p>|
|Process metrics discovery|<p>Collect metrics by Zabbix agent if it exists</p>|ZABBIX_PASSIVE|proc.num["{$REDIS.LLD.PROCESS_NAME}"]<p>**Preprocessing**:</p><p>- JAVASCRIPT: `return JSON.stringify(value > 0 ? [{'{#SINGLETON}': ''}] : []);`</p>|
|Version 4+ metrics discovery|<p>Additional metrics for version 4+</p>|DEPENDENT|redis.metrics.v4.discovery<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.redis_version`</p><p>- JAVASCRIPT: `return JSON.stringify(parseInt(value.split('.')[0]) >= 4 ? [{'{#SINGLETON}': ''}] : []);`</p>|
|Version 5+ metrics discovery|<p>Additional metrics for version 5+</p>|DEPENDENT|redis.metrics.v5.discovery<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.redis_version`</p><p>- JAVASCRIPT: `return JSON.stringify(value.split('.')[0] === '5' ? [{'{#SINGLETON}': ''}] : []);`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Redis|Redis: Get ping||ZABBIX_PASSIVE|redis.ping["{$REDIS.CONN.URI}"]|
|Redis|Redis: CPU sys|<p>System CPU consumed by the Redis server</p>|DEPENDENT|redis.cpu.sys<p>**Preprocessing**:</p><p>- JSONPATH: `$.CPU.used_cpu_sys`</p>|
|Redis|Redis: CPU sys children|<p>System CPU consumed by the background processes</p>|DEPENDENT|redis.cpu.sys_children<p>**Preprocessing**:</p><p>- JSONPATH: `$.CPU.used_cpu_sys_children`</p>|
|Redis|Redis: CPU user|<p>User CPU consumed by the Redis server</p>|DEPENDENT|redis.cpu.user<p>**Preprocessing**:</p><p>- JSONPATH: `$.CPU.used_cpu_user`</p>|
|Redis|Redis: CPU user children|<p>User CPU consumed by the background processes</p>|DEPENDENT|redis.cpu.user_children<p>**Preprocessing**:</p><p>- JSONPATH: `$.CPU.used_cpu_user_children`</p>|
|Redis|Redis: Blocked clients|<p>The number of connections waiting on a blocking call</p>|DEPENDENT|redis.clients.blocked<p>**Preprocessing**:</p><p>- JSONPATH: `$.Clients.blocked_clients`</p>|
|Redis|Redis: Max input buffer|<p>The biggest input buffer among current client connections</p>|DEPENDENT|redis.clients.max_input_buffer<p>**Preprocessing**:</p><p>- JAVASCRIPT: `var clients = JSON.parse(value).Clients return clients.client_recent_max_input_buffer || clients.client_biggest_input_buf`</p>|
|Redis|Redis: Max output buffer|<p>The biggest output buffer among current client connections</p>|DEPENDENT|redis.clients.max_output_buffer<p>**Preprocessing**:</p><p>- JAVASCRIPT: `var clients = JSON.parse(value).Clients return clients.client_recent_max_output_buffer || clients.client_longest_output_list`</p>|
|Redis|Redis: Connected clients|<p>The number of connected clients</p>|DEPENDENT|redis.clients.connected<p>**Preprocessing**:</p><p>- JSONPATH: `$.Clients.connected_clients`</p>|
|Redis|Redis: Cluster enabled||DEPENDENT|redis.cluster.enabled<p>**Preprocessing**:</p><p>- JSONPATH: `$.Cluster.cluster_enabled`</p>|
|Redis|Redis: Memory used|<p>Amount of memory allocated by Redis</p>|DEPENDENT|redis.memory.used_memory<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory`</p>|
|Redis|Redis: Memory used Lua|<p>Amount of memory used by the Lua engine</p>|DEPENDENT|redis.memory.used_memory_lua<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_lua`</p>|
|Redis|Redis: Memory used peak|<p>Peak amount of memory used by Redis</p>|DEPENDENT|redis.memory.used_memory_peak<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_peak`</p>|
|Redis|Redis: Memory used RSS|<p>Amount of memory that Redis allocated as seen by the os</p>|DEPENDENT|redis.memory.used_memory_rss<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_rss`</p>|
|Redis|Redis: AOF current rewrite time in seconds||DEPENDENT|redis.persistence.aof_current_rewrite_time_sec<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_current_rewrite_time_sec`</p>|
|Redis|Redis: AOF enabled|<p>Flag indicating AOF logging is activated</p>|DEPENDENT|redis.persistence.aof_enabled<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_enabled`</p>|
|Redis|Redis: AOF last bgrewrite status||DEPENDENT|redis.persistence.aof_last_bgrewrite_status<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_last_bgrewrite_status`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: AOF last rewrite time sec|<p>Duration of the last AOF rewrite</p>|DEPENDENT|redis.persistence.aof_last_rewrite_time_sec<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_last_rewrite_time_sec`</p>|
|Redis|Redis: AOF last write status||DEPENDENT|redis.persistence.aof_last_write_status<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_last_write_status`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: AOF rewrite in progress|<p>Flag indicating a AOF rewrite operation is on-going</p>|DEPENDENT|redis.persistence.aof_rewrite_in_progress<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_rewrite_in_progress`</p>|
|Redis|Redis: AOF rewrite scheduled||DEPENDENT|redis.persistence.aof_rewrite_scheduled<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_rewrite_scheduled`</p>|
|Redis|Redis: Loading|<p>Flag indicating if the load of a dump file is on-going</p>|DEPENDENT|redis.persistence.loading<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.loading`</p>|
|Redis|Redis: RDB bgsave in progress|<p>"1" if bgsave is in progress and "0" otherwise</p>|DEPENDENT|redis.persistence.rdb_bgsave_in_progress<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_bgsave_in_progress`</p>|
|Redis|Redis: RDB changes since last save|<p>Number of changes since the last background save</p>|DEPENDENT|redis.persistence.rdb_changes_since_last_save<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_changes_since_last_save`</p>|
|Redis|Redis: RDB current bgsave time sec||DEPENDENT|redis.persistence.rdb_current_bgsave_time_sec<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_current_bgsave_time_sec`</p>|
|Redis|Redis: RDB last bgsave status||DEPENDENT|redis.persistence.rdb_last_bgsave_status<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_last_bgsave_status`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: RDB last bgsave time in seconds|<p>Duration of the last bg_save operation</p>|DEPENDENT|redis.persistence.rdb_last_bgsave_time_sec<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_last_bgsave_time_sec`</p>|
|Redis|Redis: RDB last save time||DEPENDENT|redis.persistence.rdb_last_save_time<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_last_save_time`</p>|
|Redis|Redis: Connected slaves|<p>Number of connected slaves</p>|DEPENDENT|redis.replication.connected_slaves<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.connected_slaves`</p>|
|Redis|Redis: Replication backlog active||DEPENDENT|redis.replication.repl_backlog_active<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.repl_backlog_active`</p>|
|Redis|Redis: Replication backlog first byte offset||DEPENDENT|redis.replication.repl_backlog_first_byte_offset<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.repl_backlog_first_byte_offset`</p>|
|Redis|Redis: Replication backlog history length|<p>Amount of data in the backlog sync buffer</p>|DEPENDENT|redis.replication.repl_backlog_histlen<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.repl_backlog_histlen`</p>|
|Redis|Redis: Replication backlog size||DEPENDENT|redis.replication.repl_backlog_size<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.repl_backlog_size`</p>|
|Redis|Redis: Replication role|<p>Value is "master" if the instance is replica of no one, or "slave" if the instance is a replica of some master instance. Note that a replica can be master of another replica (chained replication).</p>|DEPENDENT|redis.replication.role<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.role`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Arch bits||DEPENDENT|redis.server.arch_bits<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.arch_bits`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Config file||DEPENDENT|redis.server.config_file<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.config_file`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Process id||DEPENDENT|redis.server.process_id<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.process_id`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Redis mode||DEPENDENT|redis.server.redis_mode<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.redis_mode`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Redis version||DEPENDENT|redis.server.redis_version<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.redis_version`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: TCP port||DEPENDENT|redis.server.tcp_port<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.tcp_port`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Uptime in days||DEPENDENT|redis.server.uptime_in_days<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.uptime_in_days`</p>|
|Redis|Redis: Uptime in seconds||DEPENDENT|redis.server.uptime_in_seconds<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.uptime_in_seconds`</p>|
|Redis|Redis: Evicted keys|<p>Total number of keys evicted due to the maxmemory limit</p>|DEPENDENT|redis.stats.evicted_keys<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.evicted_keys`</p>|
|Redis|Redis: Expired keys|<p>Total number of keys expired from the db</p>|DEPENDENT|redis.stats.expired_keys<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.expired_keys`</p>|
|Redis|Redis: Expired time cap reached count||DEPENDENT|redis.stats.expired_time_cap_reached_count<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.expired_time_cap_reached_count`</p>|
|Redis|Redis: Instantaneous input bytes per second||DEPENDENT|redis.stats.instantaneous_input.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.instantaneous_input_kbps`</p><p>- MULTIPLIER: `1024`</p>|
|Redis|Redis: Instantaneous operations per sec|<p>Number of commands processed by the server per second</p>|DEPENDENT|redis.stats.instantaneous_ops.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.instantaneous_ops_per_sec`</p>|
|Redis|Redis: Instantaneous output bytes per second||DEPENDENT|redis.stats.instantaneous_output.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.instantaneous_output_kbps`</p><p>- MULTIPLIER: `1024`</p>|
|Redis|Redis: Keyspace hits|<p>Total number of successful lookups in the main db</p>|DEPENDENT|redis.stats.keyspace_hits<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.keyspace_hits`</p>|
|Redis|Redis: Keyspace misses|<p>Total number of missed lookups in the main db</p>|DEPENDENT|redis.stats.keyspace_misses<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.keyspace_misses`</p>|
|Redis|Redis: Latest fork usec|<p>Duration of the latest fork</p>|DEPENDENT|redis.stats.latest_fork_usec<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.latest_fork_usec`</p><p>- MULTIPLIER: `1.0E-5`</p>|
|Redis|Redis: Migrate cached sockets||DEPENDENT|redis.stats.migrate_cached_sockets<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.migrate_cached_sockets`</p>|
|Redis|Redis: Pubsub channels|<p>Number of active pubsub channels</p>|DEPENDENT|redis.stats.pubsub_channels<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.pubsub_channels`</p>|
|Redis|Redis: Pubsub patterns|<p>Number of active pubsub patterns</p>|DEPENDENT|redis.stats.pubsub_patterns<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.pubsub_patterns`</p>|
|Redis|Redis: Rejected connections|<p>Number of rejected connections</p>|DEPENDENT|redis.stats.rejected_connections<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.rejected_connections`</p>|
|Redis|Redis: Sync full||DEPENDENT|redis.stats.sync_full<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.sync_full`</p>|
|Redis|Redis: Sync partial err||DEPENDENT|redis.stats.sync_partial_err<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.sync_partial_err`</p>|
|Redis|Redis: Sync partial ok||DEPENDENT|redis.stats.sync_partial_ok<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.sync_partial_ok`</p>|
|Redis|Redis: Total commands processed|<p>Number of commands processed by the server</p>|DEPENDENT|redis.stats.total_commands_processed<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.total_commands_processed`</p>|
|Redis|Redis: Total connections received||DEPENDENT|redis.stats.total_connections_received<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.total_connections_received`</p>|
|Redis|Redis: Total net input bytes||DEPENDENT|redis.stats.total_net_input_bytes<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.total_net_input_bytes`</p>|
|Redis|Redis: Total net output bytes||DEPENDENT|redis.stats.total_net_output_bytes<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.total_net_output_bytes`</p>|
|Redis|Redis: DB {#DB}: Average TTL||DEPENDENT|redis.db.avg_ttl["{#DB}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Keyspace["{#DB}"].avg_ttl`</p>|
|Redis|Redis: DB {#DB}: Expires|<p>Number of keys with an expiration</p>|DEPENDENT|redis.db.expires["{#DB}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Keyspace["{#DB}"].expires`</p>|
|Redis|Redis: DB {#DB}: Keys||DEPENDENT|redis.db.keys["{#DB}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Keyspace["{#DB}"].keys`</p>|
|Redis|Redis: AOF current size{#SINGLETON}|<p>AOF current file size</p>|DEPENDENT|redis.persistence.aof_current_size[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_current_size`</p>|
|Redis|Redis: AOF base size{#SINGLETON}|<p>AOF file size on latest startup or rewrite</p>|DEPENDENT|redis.persistence.aof_base_size[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_base_size`</p>|
|Redis|Redis: AOF pending rewrite{#SINGLETON}|<p>Flag indicating an AOF rewrite operation will</p>|DEPENDENT|redis.persistence.aof_pending_rewrite[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_pending_rewrite`</p>|
|Redis|Redis: AOF buffer length{#SINGLETON}|<p>Size of the AOF buffer</p>|DEPENDENT|redis.persistence.aof_buffer_length[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_buffer_length`</p>|
|Redis|Redis: AOF rewrite buffer length{#SINGLETON}|<p>Size of the AOF rewrite buffer</p>|DEPENDENT|redis.persistence.aof_rewrite_buffer_length[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_rewrite_buffer_length`</p>|
|Redis|Redis: AOF pending background I/O fsync{#SINGLETON}|<p>Number of fsync pending jobs in background I/O queue</p>|DEPENDENT|redis.persistence.aof_pending_bio_fsync[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_pending_bio_fsync`</p>|
|Redis|Redis: AOF delayed fsync{#SINGLETON}|<p>Delayed fsync counter</p>|DEPENDENT|redis.persistence.aof_delayed_fsync[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_delayed_fsync`</p>|
|Redis|Redis: Master host{#SINGLETON}|<p>Host or IP address of the master</p>|DEPENDENT|redis.replication.master_host[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.master_host`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Master port{#SINGLETON}|<p>Master listening TCP port</p>|DEPENDENT|redis.replication.master_port[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.master_port`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Master link status{#SINGLETON}|<p>Status of the link (up/down)</p>|DEPENDENT|redis.replication.master_link_status[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.master_link_status`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Master last I/O seconds ago{#SINGLETON}|<p>Number of seconds since the last interaction with master</p>|DEPENDENT|redis.replication.master_last_io_seconds_ago[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.master_last_io_seconds_ago`</p>|
|Redis|Redis: Master sync in progress{#SINGLETON}|<p>Indicate the master is syncing to the replica</p>|DEPENDENT|redis.replication.master_sync_in_progress[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.master_sync_in_progress`</p>|
|Redis|Redis: Slave replication offset{#SINGLETON}|<p>The replication offset of the replica instance</p>|DEPENDENT|redis.replication.slave_repl_offset[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.slave_repl_offset`</p>|
|Redis|Redis: Slave priority{#SINGLETON}|<p>The priority of the instance as a candidate for failover</p>|DEPENDENT|redis.replication.slave_priority[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.slave_priority`</p>|
|Redis|Redis: Slave priority{#SINGLETON}|<p>Flag indicating if the replica is read-only</p>|DEPENDENT|redis.replication.slave_read_only[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.slave_read_only`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Number of processes running|<p>-</p>|ZABBIX_PASSIVE|proc.num["{$REDIS.PROCESS_NAME}{#SINGLETON}"]|
|Redis|Redis: Memory usage (rss)|<p>Resident set size memory used by process in bytes.</p>|ZABBIX_PASSIVE|proc.mem["{$REDIS.PROCESS_NAME}{#SINGLETON}",,,,rss]|
|Redis|Redis: Memory usage (vsize)|<p>Virtual memory size used by process in bytes.</p>|ZABBIX_PASSIVE|proc.mem["{$REDIS.PROCESS_NAME}{#SINGLETON}",,,,vsize]|
|Redis|Redis: CPU utilization|<p>Process CPU utilization percentage.</p>|ZABBIX_PASSIVE|proc.cpu.util["{$REDIS.PROCESS_NAME}{#SINGLETON}"]|
|Redis|Redis: Executable path{#SINGLETON}||DEPENDENT|redis.server.executable[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.executable`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Memory used peak %{#SINGLETON}||DEPENDENT|redis.memory.used_memory_peak_perc[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_peak_perc`</p><p>- REGEX: `(.+)% \1`</p>|
|Redis|Redis: Memory used overhead{#SINGLETON}|<p>Sum of all overheads allocated by Redis for managing its internal datastructures</p>|DEPENDENT|redis.memory.used_memory_overhead[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_overhead`</p>|
|Redis|Redis: Memory used startup{#SINGLETON}|<p>Amount of memory consumed by Redis at startup</p>|DEPENDENT|redis.memory.used_memory_startup[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_startup`</p>|
|Redis|Redis: Memory used dataset{#SINGLETON}||DEPENDENT|redis.memory.used_memory_dataset[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_dataset`</p>|
|Redis|Redis: Memory used dataset %{#SINGLETON}||DEPENDENT|redis.memory.used_memory_dataset_perc[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_dataset_perc`</p><p>- REGEX: `(.+)% \1`</p>|
|Redis|Redis: Total system memory{#SINGLETON}||DEPENDENT|redis.memory.total_system_memory[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.total_system_memory`</p>|
|Redis|Redis: Max memory{#SINGLETON}|<p>Maximum amount of memory allocated to the Redisdb system</p>|DEPENDENT|redis.memory.maxmemory[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.maxmemory`</p>|
|Redis|Redis: Max memory policy{#SINGLETON}||DEPENDENT|redis.memory.maxmemory_policy[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.maxmemory_policy`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Active defrag running{#SINGLETON}||DEPENDENT|redis.memory.active_defrag_running[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.active_defrag_running`</p>|
|Redis|Redis: Lazyfree pending objects{#SINGLETON}||DEPENDENT|redis.memory.lazyfree_pending_objects[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.lazyfree_pending_objects`</p>|
|Redis|Redis: RDB last cow size{#SINGLETON}||DEPENDENT|redis.persistence.rdb_last_cow_size[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_last_cow_size`</p>|
|Redis|Redis: AOF last cow size{#SINGLETON}||DEPENDENT|redis.persistence.aof_last_cow_size[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_last_cow_size`</p>|
|Redis|Redis: Expired stale %{#SINGLETON}||DEPENDENT|redis.stats.expired_stale_perc[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.expired_stale_perc`</p>|
|Redis|Redis: Expired time cap reached count{#SINGLETON}||DEPENDENT|redis.stats.expired_time_cap_reached_count[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.expired_time_cap_reached_count`</p>|
|Redis|Redis: Slave expires tracked keys{#SINGLETON}||DEPENDENT|redis.stats.slave_expires_tracked_keys[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.slave_expires_tracked_keys`</p>|
|Redis|Redis: Active defrag hits{#SINGLETON}||DEPENDENT|redis.stats.active_defrag_hits[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.active_defrag_hits`</p>|
|Redis|Redis: Active defrag misses{#SINGLETON}||DEPENDENT|redis.stats.active_defrag_misses[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.active_defrag_misses`</p>|
|Redis|Redis: Active defrag key hits{#SINGLETON}||DEPENDENT|redis.stats.active_defrag_key_hits[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.active_defrag_key_hits`</p>|
|Redis|Redis: Active defrag key misses{#SINGLETON}||DEPENDENT|redis.stats.active_defrag_key_misses[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.active_defrag_key_misses`</p>|
|Redis|Redis: Master replication id{#SINGLETON}||DEPENDENT|redis.replication.master_replid[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.master_replid`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Master replication id 2{#SINGLETON}||DEPENDENT|redis.replication.master_replid2[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.master_replid2`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Master replication offset{#SINGLETON}|<p>Replication offset reported by the master</p>|DEPENDENT|redis.replication.master_repl_offset[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.master_repl_offset`</p>|
|Redis|Redis: Replication second offset{#SINGLETON}|<p>Offset up to which replication IDs are accepted</p>|DEPENDENT|redis.replication.second_repl_offset[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.second_repl_offset`</p>|
|Redis|Redis: Allocator active{#SINGLETON}||DEPENDENT|redis.memory.allocator_active[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_active`</p>|
|Redis|Redis: Allocator allocated{#SINGLETON}||DEPENDENT|redis.memory.allocator_allocated[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_allocated`</p>|
|Redis|Redis: Allocator resident{#SINGLETON}||DEPENDENT|redis.memory.allocator_resident[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_resident`</p>|
|Redis|Redis: Memory used scripts{#SINGLETON}||DEPENDENT|redis.memory.used_memory_scripts[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_scripts`</p>|
|Redis|Redis: Memory number of cached scripts{#SINGLETON}||DEPENDENT|redis.memory.number_of_cached_scripts[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.number_of_cached_scripts`</p>|
|Redis|Redis: Allocator fragmentation bytes{#SINGLETON}||DEPENDENT|redis.memory.allocator_frag_bytes[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_frag_bytes`</p>|
|Redis|Redis: Allocator fragmentation ratio{#SINGLETON}||DEPENDENT|redis.memory.allocator_frag_ratio[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_frag_ratio`</p>|
|Redis|Redis: Allocator RSS bytes{#SINGLETON}||DEPENDENT|redis.memory.allocator_rss_bytes[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_rss_bytes`</p>|
|Redis|Redis: Allocator RSS ratio{#SINGLETON}||DEPENDENT|redis.memory.allocator_rss_ratio[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_rss_ratio`</p>|
|Redis|Redis: Memory RSS overhead bytes{#SINGLETON}||DEPENDENT|redis.memory.rss_overhead_bytes[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.rss_overhead_bytes`</p>|
|Redis|Redis: Memory RSS overhead ratio{#SINGLETON}||DEPENDENT|redis.memory.rss_overhead_ratio[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.rss_overhead_ratio`</p>|
|Redis|Redis: Memory fragmentation bytes{#SINGLETON}||DEPENDENT|redis.memory.fragmentation_bytes[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_fragmentation_bytes`</p>|
|Redis|Redis: Memory fragmentation ratio{#SINGLETON}|<p>Ratio between used_memory_rss and used_memory</p>|DEPENDENT|redis.memory.fragmentation_ratio[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_fragmentation_ratio`</p>|
|Redis|Redis: Memory not counted for evict{#SINGLETON}||DEPENDENT|redis.memory.not_counted_for_evict[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_not_counted_for_evict`</p>|
|Redis|Redis: Memory replication backlog{#SINGLETON}||DEPENDENT|redis.memory.replication_backlog[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_replication_backlog`</p>|
|Redis|Redis: Memory clients normal{#SINGLETON}||DEPENDENT|redis.memory.mem_clients_normal[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_clients_normal`</p>|
|Redis|Redis: Memory clients slaves{#SINGLETON}||DEPENDENT|redis.memory.mem_clients_slaves[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_clients_slaves`</p>|
|Redis|Redis: Memory AOF buffer{#SINGLETON}|<p>Size of the AOF buffer</p>|DEPENDENT|redis.memory.mem_aof_buffer[{#SINGLETON}]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_aof_buffer`</p>|
|Zabbix_raw_items|Redis: Get info||ZABBIX_PASSIVE|redis.info["{$REDIS.CONN.URI}"]|
|Zabbix_raw_items|Redis: Get config||ZABBIX_PASSIVE|redis.config["{$REDIS.CONN.URI}"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|
|Redis: Process is not running|<p>-</p>|`{TEMPLATE_NAME:proc.num["{$REDIS.PROCESS_NAME}{#SINGLETON}"].last()}=0`|HIGH||

## Feedback

Please report any issues with the template at https://support.zabbix.com

You can also provide feedback, discuss the template or ask for help with it at
[ZABBIX forums](forum url).

