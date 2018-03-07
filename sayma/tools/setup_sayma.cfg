#!/bin/bash

mkdir ~/artiq-phaser
cd ~/artiq-phaser

git clone --recursive http://github.com/m-labs/artiq


cd ~/artiq-phaser
conda config --prepend channels http://conda.anaconda.org/conda-forge/label/main
conda config --prepend channels http://conda.anaconda.org/m-labs/label/main
conda config --prepend channels http://conda.anaconda.org/conda-forge/label/dev
conda config --prepend channels http://conda.anaconda.org/m-labs/label/dev
conda create -n artiq-phaser artiq=3.4 artiq-kc705-phaser matplotlib misoc migen openocd
source activate artiq-phaser

source tools/sayma_load_to_ram.bash ~/artiq-dev/artiq/artiq_sayma_20180305_AMConly

cd ~/artiq-phaser/artiq/artiq/examples/master
artiq_compile repository/misc/blink_led.py -o idle_kernel.elf
artiq_mkfs -s mac 00:0a:35:03:1e:75 -s ip 192.168.1.75 -f idle_kernel idle_kernel.elf sayma.config
artiq_flash -t sayma -f sayma.config storage start

ping 192.168.1.75
