
First stab at guidance on creating new DRTIO devices for ARTIQ.

Files to look at are the following.


https://github.com/m-labs/migen/blob/master/migen/build/platforms/kc705.py
https://github.com/m-labs/misoc/blob/master/misoc/targets/kc705.py
https://github.com/m-labs/artiq/blob/release-2/artiq/gateware/targets/kc705.py
https://github.com/m-labs/artiq/blob/release-2/artiq/gateware/nist_clock.py
https://m-labs.hk/artiq/manual-release-2/installing_from_source.html
https://m-labs.hk/artiq/manual-release-2/core_device.html#fpga-board-ports

Chops

- [] installed ARTIQ source from github
- [] compiled .bit files from stock ARTIQ from source, flashed FPGA
and can ran ARTIQ programs
- [] modified ARTIQ source to match local hardware, compile .bit
files, flashed FPGA and ran ARTIQ programs on said hardware [1]
- [] contributed code back to m-labs github repository
- [] written Migen code from scratch, compiled .bit and run it on an FPGA
- [] added support for new FPGA or protoboard to MiSoC (eg AFCK)

[1] This is the level required to test the VHDCI Carrier using ARTIQ.

Examples of ARTIQ extensions.

Add a new instance of an existing PHY to a lab setup
- add SPI to KC705 (https://github.com/m-labs/artiq/pull/776)

IC configuration using firmware
- AD9616 and AD9154 initialization moved from gateware to firmware (https://github.com/mntng/artiq/commit/7ff77bceacd1b8649a24789b066c24b91b40f5db)
- firmware: add si5324 programming functions (https://github.com/m-labs/artiq/commit/13c45c876603fc4486d2c9fac9a963c0ce5a2922)