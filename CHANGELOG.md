# Changelog

## Unreleased

### Bug Fixes and updates

* **linux,linux_prom**: renamed value mapping 'Ethernet 10Mbs' to 'Ethernet' [#32](https://github.com/v-zhuravlev/zbx_template_pack/pull/32)
* **linux,linux_prom,linux_snmp**: added ploop md hcp zram to LLD filter for vfs.dev(block devices) [b490e217922d0d619d93cb83cf64e51d60a41cf2](https://github.com/v-zhuravlev/zbx_template_pack/commit/b490e217922d0d619d93cb83cf64e51d60a41cf2)
* **hp_hpn**: removed not used macros [67268650f87ad682543a1a2b04228e041e3d53f0](https://github.com/v-zhuravlev/zbx_template_pack/commit/67268650f87ad682543a1a2b04228e041e3d53f0)
* **cisco**: changed poll time of CPU metrics to 5m by default [#34](https://github.com/v-zhuravlev/zbx_template_pack/pull/34)
* **ALL**: removed mode=recovery from trigger prototypes, version triggers now close after some timeout [#30](https://github.com/v-zhuravlev/zbx_template_pack/pull/30)

### Added

* **windows_agent**: added Windows services monitoring as module template [#36](https://github.com/v-zhuravlev/zbx_template_pack/pull/36)
* **redis**: added redis template [#24](https://github.com/v-zhuravlev/zbx_template_pack/pull/24)
