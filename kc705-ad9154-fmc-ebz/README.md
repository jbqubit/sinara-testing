
This folder contains acceptance tests for the Smart Arbitrary Waveform Generator (SAWG) conducted in July 2017. A python script repository/phaser/test_suite.py facilitates running many test scripts in sequence using an oscilloscope and a spectrum analyzer. 

Phaser is an AD9154-FMC-EBZ, a 4 channel 2.4 GHz DAC on an FMC HPC card. Phaser is a proof-of-concept design of a GHz-datarate, multi-channel, interpolating, multi-tone, direct digital synthesizer (DDS) compatible with ARTIQ’s RTIO channels. Ultimately it will be the basis for the ARTIQ Sayma Smart Arbitrary Waveform Generator (SAWG) project. See https://github.com/m-labs/sinara.

## Comments

Support for phaser including [installation instructions](http://m-labs.hk/artiq/manual-release-3/core_device.html?highlight=phaser#phaser), [documentation](http://m-labs.hk/artiq/manual-release-3/core_drivers_reference.html?highlight=sawg#module-artiq.coredevice.sawg) and [examples](https://github.com/m-labs/artiq/tree/3.4/artiq/examples/phaser) and are maintained in 
[ARTIQ Release 3.4](https://github.com/m-labs/artiq/tree/3.4). 
- [M-labs](http://m-labs.hk/artiq/index.html) continues to maintain and occasionally build .bit for the KC705 phaser demo.
-  Use conda to get .bit file: [package](https://anaconda.org/m-labs/artiq-kc705-phaser/files)
- Support for phaser on KC705 is discontinued for [ARTIQ >4.0](https://github.com/m-labs/artiq) (github master)
