
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

## Template links

There are no template links in this template.

## Discovery rules

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Keyspace discovery|<p>Individual keyspace metrics</p>|DEPENDENT|redis.keyspace.discovery<p>**Preprocessing**:</p><p>- JAVASCRIPT: `return JSON.stringify(Object.keys(JSON.parse(value).Keyspace).map(function (v){return {"{#DB}": v}}));`</p><p>**Filter**:</p>AND <p>- A: {#DB} MATCHES_REGEX `{$REDIS.LLD.FILTER.DB.MATCHES}`</p><p>- B: {#DB} NOT_MATCHES_REGEX `{$REDIS.LLD.FILTER.DB.NOT_MATCHES}`</p>|

## Items collected

|Group|Name|Description|Type|Key and additional info|
|-----|----|-----------|----|---------------------|
|Redis|Redis: Get ping||ZABBIX_PASSIVE|redis.ping["{$REDIS.CONN.URI}"]|
|Redis|Redis: CPU sys|<p>System CPU consumed by the Redis server</p>|DEPENDENT|redis.cpu.sys<p>**Preprocessing**:</p><p>- JSONPATH: `$.CPU.used_cpu_sys`</p>|
|Redis|Redis: CPU sys children|<p>System CPU consumed by the background processes</p>|DEPENDENT|redis.cpu.sys_children<p>**Preprocessing**:</p><p>- JSONPATH: `$.CPU.used_cpu_sys_children`</p>|
|Redis|Redis: CPU user|<p>User CPU consumed by the Redis server</p>|DEPENDENT|redis.cpu.user<p>**Preprocessing**:</p><p>- JSONPATH: `$.CPU.used_cpu_user`</p>|
|Redis|Redis: CPU user children|<p>User CPU consumed by the background processes</p>|DEPENDENT|redis.cpu.user_children<p>**Preprocessing**:</p><p>- JSONPATH: `$.CPU.used_cpu_user_children`</p>|
|Redis|Redis: Blocked clients|<p>The number of connections waiting on a blocking call</p>|DEPENDENT|redis.clients.blocked<p>**Preprocessing**:</p><p>- JSONPATH: `$.Clients.blocked_clients`</p>|
|Redis|Redis: Connected clients|<p>The number of connected clients</p>|DEPENDENT|redis.clients.connected<p>**Preprocessing**:</p><p>- JSONPATH: `$.Clients.connected_clients`</p>|
|Redis|Redis: Max input buffer|<p>The biggest input buffer among current client connections</p>|DEPENDENT|redis.clients.max_input_buffer<p>**Preprocessing**:</p><p>- JSONPATH: `$.Clients.client_recent_max_input_buffer`</p>|
|Redis|Redis: Max output buffer|<p>The biggest output buffer among current client connections</p>|DEPENDENT|redis.clients.max_output_buffer<p>**Preprocessing**:</p><p>- JSONPATH: `$.Clients.client_recent_max_output_buffer`</p>|
|Redis|Redis: Cluster enabled||DEPENDENT|redis.cluster.enabled<p>**Preprocessing**:</p><p>- JSONPATH: `$.Cluster.cluster_enabled`</p>|
|Redis|Redis: Active defrag running||DEPENDENT|redis.memory.active_defrag_running<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.active_defrag_running`</p>|
|Redis|Redis: Allocator active||DEPENDENT|redis.memory.allocator_active<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_active`</p>|
|Redis|Redis: Allocator allocated||DEPENDENT|redis.memory.allocator_allocated<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_allocated`</p>|
|Redis|Redis: Allocator fragmentation bytes||DEPENDENT|redis.memory.allocator_frag_bytes<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_frag_bytes`</p>|
|Redis|Redis: Allocator fragmentation ratio||DEPENDENT|redis.memory.allocator_frag_ratio<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_frag_ratio`</p>|
|Redis|Redis: Allocator resident||DEPENDENT|redis.memory.allocator_resident<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_resident`</p>|
|Redis|Redis: Allocator RSS bytes||DEPENDENT|redis.memory.allocator_rss_bytes<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_rss_bytes`</p>|
|Redis|Redis: Allocator RSS ratio||DEPENDENT|redis.memory.allocator_rss_ratio<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.allocator_rss_ratio`</p>|
|Redis|Redis: Lazyfree pending objects||DEPENDENT|redis.memory.lazyfree_pending_objects<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.lazyfree_pending_objects`</p>|
|Redis|Redis: Max memory||DEPENDENT|redis.memory.maxmemory<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.maxmemory`</p>|
|Redis|Redis: Max memory policy||DEPENDENT|redis.memory.maxmemory_policy<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.maxmemory_policy`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Memory AOF buffer||DEPENDENT|redis.memory.mem_aof_buffer<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_aof_buffer`</p>|
|Redis|Redis: Memory clients normal||DEPENDENT|redis.memory.mem_clients_normal<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_clients_normal`</p>|
|Redis|Redis: Memory clients slaves||DEPENDENT|redis.memory.mem_clients_slaves<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_clients_slaves`</p>|
|Redis|Redis: Memory fragmentation bytes||DEPENDENT|redis.memory.fragmentation_bytes<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_fragmentation_bytes`</p>|
|Redis|Redis: Memory fragmentation ratio||DEPENDENT|redis.memory.fragmentation_ratio<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_fragmentation_ratio`</p>|
|Redis|Redis: Memory not counted for evict||DEPENDENT|redis.memory.not_counted_for_evict<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_not_counted_for_evict`</p>|
|Redis|Redis: Memory replication backlog||DEPENDENT|redis.memory.replication_backlog<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.mem_replication_backlog`</p>|
|Redis|Redis: Memory number of cached scripts||DEPENDENT|redis.memory.number_of_cached_scripts<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.number_of_cached_scripts`</p>|
|Redis|Redis: Memory RSS overhead bytes||DEPENDENT|redis.memory.rss_overhead_bytes<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.rss_overhead_bytes`</p>|
|Redis|Redis: Memory RSS overhead ratio||DEPENDENT|redis.memory.rss_overhead_ratio<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.rss_overhead_ratio`</p>|
|Redis|Redis: Total system memory||DEPENDENT|redis.memory.total_system_memory<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.total_system_memory`</p>|
|Redis|Redis: Memory used||DEPENDENT|redis.memory.used_memory<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory`</p>|
|Redis|Redis: Memory used dataset||DEPENDENT|redis.memory.used_memory_dataset<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_dataset`</p>|
|Redis|Redis: Memory used dataset %||DEPENDENT|redis.memory.used_memory_dataset_perc<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_dataset_perc`</p><p>- REGEX: `(.+)% \1`</p>|
|Redis|Redis: Memory used Lua||DEPENDENT|redis.memory.used_memory_lua<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_lua`</p>|
|Redis|Redis: Memory used overhead||DEPENDENT|redis.memory.used_memory_overhead<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_overhead`</p>|
|Redis|Redis: Memory used peak||DEPENDENT|redis.memory.used_memory_peak<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_peak`</p>|
|Redis|Redis: Memory used peak %||DEPENDENT|redis.memory.used_memory_peak_perc<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_peak_perc`</p><p>- REGEX: `(.+)% \1`</p>|
|Redis|Redis: Memory used RSS||DEPENDENT|redis.memory.used_memory_rss<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_rss`</p>|
|Redis|Redis: Memory used scripts||DEPENDENT|redis.memory.used_memory_scripts<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_scripts`</p>|
|Redis|Redis: Memory used startup||DEPENDENT|redis.memory.used_memory_startup<p>**Preprocessing**:</p><p>- JSONPATH: `$.Memory.used_memory_startup`</p>|
|Redis|Redis: AOF current rewrite time in seconds||DEPENDENT|redis.persistence.aof_current_rewrite_time_sec<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_current_rewrite_time_sec`</p>|
|Redis|Redis: AOF enabled||DEPENDENT|redis.persistence.aof_enabled<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_enabled`</p>|
|Redis|Redis: AOF last bgrewrite status||DEPENDENT|redis.persistence.aof_last_bgrewrite_status<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_last_bgrewrite_status`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: AOF last cow size||DEPENDENT|redis.persistence.aof_last_cow_size<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_last_cow_size`</p>|
|Redis|Redis: AOF last rewrite time sec||DEPENDENT|redis.persistence.aof_last_rewrite_time_sec<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_last_rewrite_time_sec`</p>|
|Redis|Redis: AOF last write status||DEPENDENT|redis.persistence.aof_last_write_status<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_last_write_status`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Loading||DEPENDENT|redis.persistence.aof_rewrite_in_progress<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_rewrite_in_progress`</p>|
|Redis|Redis: AOF rewrite scheduled||DEPENDENT|redis.persistence.aof_rewrite_scheduled<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.aof_rewrite_scheduled`</p>|
|Redis|Redis: Loading||DEPENDENT|redis.persistence.loading<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.loading`</p>|
|Redis|Redis: RDB bgsave in progress||DEPENDENT|redis.persistence.rdb_bgsave_in_progress<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_bgsave_in_progress`</p>|
|Redis|Redis: RDB changes since last save||DEPENDENT|redis.persistence.rdb_changes_since_last_save<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_changes_since_last_save`</p>|
|Redis|Redis: RDB current bgsave time sec||DEPENDENT|redis.persistence.rdb_current_bgsave_time_sec<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_current_bgsave_time_sec`</p>|
|Redis|Redis: RDB last bgsave status||DEPENDENT|redis.persistence.rdb_last_bgsave_status<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_last_bgsave_status`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: RDB last bgsave time sec||DEPENDENT|redis.persistence.rdb_last_bgsave_time_sec<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_last_bgsave_time_sec`</p>|
|Redis|Redis: RDB last cow size||DEPENDENT|redis.persistence.rdb_last_cow_size<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_last_cow_size`</p>|
|Redis|Redis: RDB last save time||DEPENDENT|redis.persistence.rdb_last_save_time<p>**Preprocessing**:</p><p>- JSONPATH: `$.Persistence.rdb_last_save_time`</p>|
|Redis|Redis: Connected slaves||DEPENDENT|redis.replication.connected_slaves<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.connected_slaves`</p>|
|Redis|Redis: Master replication offset||DEPENDENT|redis.replication.master_repl_offset<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.master_repl_offset`</p>|
|Redis|Redis: Master replication id||DEPENDENT|redis.replication.master_replid<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.master_replid`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Master replication id 2||DEPENDENT|redis.replication.master_replid2<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.master_replid2`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Replication backlog active||DEPENDENT|redis.replication.repl_backlog_active<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.repl_backlog_active`</p>|
|Redis|Redis: Replication backlog first byte offset||DEPENDENT|redis.replication.repl_backlog_first_byte_offset<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.repl_backlog_first_byte_offset`</p>|
|Redis|Redis: Replication backlog history length||DEPENDENT|redis.replication.repl_backlog_histlen<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.repl_backlog_histlen`</p>|
|Redis|Redis: Replication backlog size||DEPENDENT|redis.replication.repl_backlog_size<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.repl_backlog_size`</p>|
|Redis|Redis: Replication role||DEPENDENT|redis.replication.role<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.role`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Replication second offset||DEPENDENT|redis.replication.second_repl_offset<p>**Preprocessing**:</p><p>- JSONPATH: `$.Replication.second_repl_offset`</p>|
|Redis|Redis: Arch bits||DEPENDENT|redis.server.arch_bits<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.arch_bits`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Config file||DEPENDENT|redis.server.config_file<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.config_file`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Executable path||DEPENDENT|redis.server.executable<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.executable`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Process id||DEPENDENT|redis.server.process_id<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.process_id`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Redis mode||DEPENDENT|redis.server.redis_mode<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.redis_mode`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Redis version||DEPENDENT|redis.server.redis_version<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.redis_version`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: TCP port||DEPENDENT|redis.server.tcp_port<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.tcp_port`</p><p>- DISCARD_UNCHANGED_HEARTBEAT: `1d`</p>|
|Redis|Redis: Uptime in days||DEPENDENT|redis.server.uptime_in_days<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.uptime_in_days`</p>|
|Redis|Redis: Uptime in seconds||DEPENDENT|redis.server.uptime_in_seconds<p>**Preprocessing**:</p><p>- JSONPATH: `$.Server.uptime_in_seconds`</p>|
|Redis|Redis: Active defrag hits||DEPENDENT|redis.stats.active_defrag_hits<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.active_defrag_hits`</p>|
|Redis|Redis: Active defrag key hits||DEPENDENT|redis.stats.active_defrag_key_hits<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.active_defrag_key_hits`</p>|
|Redis|Redis: Active defrag key misses||DEPENDENT|redis.stats.active_defrag_key_misses<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.active_defrag_key_misses`</p>|
|Redis|Redis: Active defrag misses||DEPENDENT|redis.stats.active_defrag_misses<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.active_defrag_misses`</p>|
|Redis|Redis: Evicted keys||DEPENDENT|redis.stats.evicted_keys<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.evicted_keys`</p>|
|Redis|Redis: Expired keys||DEPENDENT|redis.stats.expired_keys<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.expired_keys`</p>|
|Redis|Redis: Expired stale %||DEPENDENT|redis.stats.expired_stale_perc<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.expired_stale_perc`</p>|
|Redis|Redis: Expired time cap reached count||DEPENDENT|redis.stats.expired_time_cap_reached_count<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.expired_time_cap_reached_count`</p>|
|Redis|Redis: Expired time cap reached count||DEPENDENT|redis.stats.expired_time_cap_reached_count<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.expired_time_cap_reached_count`</p>|
|Redis|Redis: Instantaneous input bytes per second||DEPENDENT|redis.stats.instantaneous_input.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.instantaneous_input_kbps`</p><p>- MULTIPLIER: `1024`</p>|
|Redis|Redis: Instantaneous operations per sec||DEPENDENT|redis.stats.instantaneous_ops.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.instantaneous_ops_per_sec`</p>|
|Redis|Redis: Instantaneous output bytes per second||DEPENDENT|redis.stats.instantaneous_output.rate<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.instantaneous_output_kbps`</p><p>- MULTIPLIER: `1024`</p>|
|Redis|Redis: Keyspace hits||DEPENDENT|redis.stats.keyspace_hits<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.keyspace_hits`</p>|
|Redis|Redis: Keyspace misses||DEPENDENT|redis.stats.keyspace_misses<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.keyspace_misses`</p>|
|Redis|Redis: Latest fork usec||DEPENDENT|redis.stats.latest_fork_usec<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.latest_fork_usec`</p>|
|Redis|Redis: Migrate cached sockets||DEPENDENT|redis.stats.migrate_cached_sockets<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.migrate_cached_sockets`</p>|
|Redis|Redis: Pubsub channels||DEPENDENT|redis.stats.pubsub_channels<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.pubsub_channels`</p>|
|Redis|Redis: Pubsub patterns||DEPENDENT|redis.stats.pubsub_patterns<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.pubsub_patterns`</p>|
|Redis|Redis: Rejected connections||DEPENDENT|redis.stats.rejected_connections<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.rejected_connections`</p>|
|Redis|Redis: Slave expires tracked keys||DEPENDENT|redis.stats.slave_expires_tracked_keys<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.slave_expires_tracked_keys`</p>|
|Redis|Redis: Sync full||DEPENDENT|redis.stats.sync_full<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.sync_full`</p>|
|Redis|Redis: Sync partial err||DEPENDENT|redis.stats.sync_partial_err<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.sync_partial_err`</p>|
|Redis|Redis: Sync partial ok||DEPENDENT|redis.stats.sync_partial_ok<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.sync_partial_ok`</p>|
|Redis|Redis: Total commands processed||DEPENDENT|redis.stats.total_commands_processed<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.total_commands_processed`</p>|
|Redis|Redis: Total connections received||DEPENDENT|redis.stats.total_connections_received<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.total_connections_received`</p>|
|Redis|Redis: Total net input bytes||DEPENDENT|redis.stats.total_net_input_bytes<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.total_net_input_bytes`</p>|
|Redis|Redis: Total net output bytes||DEPENDENT|redis.stats.total_net_output_bytes<p>**Preprocessing**:</p><p>- JSONPATH: `$.Stats.total_net_output_bytes`</p>|
|Redis|Redis: DB {#DB}: Average TTL||DEPENDENT|redis.db.avg_ttl["{#DB}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Keyspace["{#DB}"].avg_ttl`</p>|
|Redis|Redis: DB {#DB}: Expires||DEPENDENT|redis.db.expires["{#DB}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Keyspace["{#DB}"].expires`</p>|
|Redis|Redis: DB {#DB}: Keys||DEPENDENT|redis.db.keys["{#DB}"]<p>**Preprocessing**:</p><p>- JSONPATH: `$.Keyspace["{#DB}"].keys`</p>|
|Zabbix_raw_items|Redis: Get info||ZABBIX_PASSIVE|redis.info["{$REDIS.CONN.URI}"]|
|Zabbix_raw_items|Redis: Get config||ZABBIX_PASSIVE|redis.config["{$REDIS.CONN.URI}"]|

## Triggers

|Name|Description|Expression|Severity|Dependencies and additional info|
|----|-----------|----|----|----|

## Feedback

Please report any issues with the template at https://support.zabbix.com

You can also provide feedback, discuss the template or ask for help with it at
[ZABBIX forums](forum url).

