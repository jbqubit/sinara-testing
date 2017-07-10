
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