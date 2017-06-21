# Zabbix Templates Pack
The idea behind this template pack is to provide single template class for each device type and just define SNMP oids required to collect common metrics liks `CPU load`, `Memory`, `Temperature` and so on to generate new template for new vendor.  


So all templates are generated using only SNMP OIDs and other vendor specific details.  
LLD details, Context macros values and other attributes can be optionally provided.   
The rest is added automatically, including item names, descriptions, triggers and so on.  

As the output we would have a pack of templates for different vendors(Cisco, Juniper, Mikrotik for `net` template class) that control same items(CPU load in %, Memory load in % , Temperature etc) named the same and have same triggers also named the same with same thresholds(can be tuned using MACROS). So we know what we can expect from this kind of template.  



## Required and optional items  
Some items are marked `required` so the new device we want to add must provide ways to monitor these items. Otherwise this device will not be added since we expect similar behaviour from all devices using the template from the pack. If we can't control CPU load or memory load for `net` device then it's not going to be here.
Rules for `optional` metrics are not so strict. We can still live without them but they can be handy in some situations so we add them if they are ways to collect them.  

## Examples
Comparing different devices metrics made easier:  
CPU:  
![image](https://cloud.githubusercontent.com/assets/14870891/22948032/1ef3a5e0-f30e-11e6-8886-43f38998000d.png)  
Temperature:  
![image](https://cloud.githubusercontent.com/assets/14870891/22948078/4d41a514-f30e-11e6-846e-acb5d782f903.png)  
Memory triggers also look similar:  
![image](https://cloud.githubusercontent.com/assets/14870891/22948146/842493e8-f30e-11e6-927a-79d13ca9ef5b.png)  


## How to use this template pack  
Just import the required template into your Zabbix 3.2+. Some templates might have dependencies. Check `deps` directory then.  
Currently `net` template is ready to be tested.  See [`out/net/README.md`](https://github.com/v-zhuravlev/zbx_template_pack/tree/master/out/net) for all its items and triggers. 

### `net` Devices List  
|Vendor|Known Models|OS|Known SNMP ObjectID|Template name|MIBS used|Reference|  
|----|-----|----|-----|------|---------|----------|    
|Juniper|	MX,SRX,EX models|JunOS|.1.3.6.1.4.1.636.1.1.1.2.[29,39]|Template Juniper|JUNIPER-MIB|-|  
|D-Link DES-xxxx|D-Link DES-xxxx|-|.1.3.6.1.4.1.171.10.113.3.1|Template D-Link DES|DLINK-AGENT-MIB,EQUIPMENT-MIB|-|
|D-Link DES-7xxx|D-Link DES-7206|-|.1.3.6.1.4.1.171.10.97.1.1|Template D-Link DES 7200|ENTITY-MIB,MY-SYSTEM-MIB,MY-PROCESS-MIB,MY-MEMORY-MIB|-|
|Cisco|-|IOS|.1.3.6.1.4.1.9.1.\[1045,1208,896,864\]|Template Cisco IOS Software releases 12.2\_3.5\_ or later|CISCO-PROCESS-MIB,CISCO-MEMORY-POOL-MIB,CISCO-ENVMON-MIB|<http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15216-contiguous-memory.html> , <http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15215-collect-cpu-util-snmp.html>|  
|Cisco|-|IOS|.1.3.6.1.4.1.9.1.\[1045,1208,896,864\]|Template Cisco IOS Software releases later to 12.0\_3\_T and prior to 12.2\_3.5\_|CISCO-PROCESS-MIB,CISCO-MEMORY-POOL-MIB,CISCO-ENVMON-MIB|<http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15216-contiguous-memory.html>, <http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15215-collect-cpu-util-snmp.html>|  
|Cisco|-|IOS|.1.3.6.1.4.1.9.1.\[1045,1208,896,864\]|Template Cisco IOS Software releases prior to 12.0\_3\_T|OLD-CISCO-CPU-MIB,CISCO-MEMORY-POOL-MIB|<http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15216-contiguous-memory.html>, <http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15215-collect-cpu-util-snmp.html>|  
|Mikrotik|-|RouterOS|.1.3.6.1.4.1.14988.1|Template Mikrotik|MIKROTIK-MIB,HOST-RESOURCES-MIB|-|  
|Ubiquiti|NanoBridge,NanoStation,Unifi|AirOS|.1.3.6.1.4.1.10002.1|Template Ubiquiti AirOS|FROGFOOT-RESOURCES-MIB,IEEE802dot11-MIB|-|  
|QTech|Qtech QSW-2800-28T|-|.1.3.6.1.4.1.27514.1.1.1.49|Template QTech QSW|QTECH-MIB,ENTITY-MIB|-|  
|Extreme|	X670V-48x|EXOS|.1.3.6.1.4.1.1916.2.168|Template Extreme EXOS|	EXTREME-SYSTEM-MIB,EXTREME-SOFTWARE-MONITOR-MIB|-|  
|Alcatel|ALCATEL SR 7750|TiMOS|.1.3.6.1.4.1.6527.1.3.4|Template Alcatel Timetra TiMOS|EXTREME-SYSTEM-MIB,EXTREME-SOFTWARE-MONITOR-MIB|https://share.zabbix.com/network_devices/extreme/template-extreme-x450a|  
|Brocade FC Switch|-|-|.1.3.6.1.4.1.1588.2.1.1.[1,71]|Template Brocade FC|SW-MIB,ENTITY-MIB|-|  
|Huawei VRP|	S2352P-EI|-|.1.3.6.1.4.1.2011.2.23.94|Template Huawei VRP|ENTITY-MIB,HUAWEI-ENTITY-EXTENT-MIB|-|  
|Dell Force S-Series|	S4810|-|.1.3.6.1.4.1.6027.1.3.14|Template Dell Force S-Series|F10-S-SERIES-CHASSIS-MIB|https://www.force10networks.com/csportal20/KnowledgeBase/Documentation.aspx|    
|Brocade ICX|ICX6610|-||Template Brocade ICX|FOUNDRY-SN-AGENT-MIB|http://www.brocade.com/en/products-services/switches/campus-network-switches/icx-6610-switch.html|  
|Mellanox|SX1036|MLNX-OS|.1.3.6.1.4.1.33049.1.1.1.1036|Template Mellanox |HOST-RESOURCES-MIB,ENTITY-MIB,ENTITY-SENSOR-MIB,MELLANOX-MIB|http://www.mellanox.com/page/ethernet_switch_overview|
|Intel/QLogic|Infiniband 12300|-|.1.3.6.1.4.1.10222.7.1.2|Template QLogic Infiniband |ICS-CHASSIS-MIB|https://www.intel.com/content/www/us/en/high-performance-computing-fabrics/true-scale-12000-switch-family.html|

## Template options  
Templates are provided in two SNMP versions (SNMPvx suffix):  
- with SNMPv1 items  
- with SNMPv2 items  
And two translations (EN or RU suffixes):  
- English (Items and triggers)  
- Russian (most of items and triggers are translated)  
