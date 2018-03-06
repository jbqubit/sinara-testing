#!/bin/bash

mkdir ~/artiq-phaser
cd ~/artiq-phaser

git clone --recursive http://github.com/m-labs/artiq
cd artiq
git checkout 3.4

cd ~/artiq-phaser
conda config --prepend channels http://conda.anaconda.org/conda-forge/label/main
conda config --prepend channels http://conda.anaconda.org/m-labs/label/main
conda config --prepend channels http://conda.anaconda.org/conda-forge/label/dev
conda config --prepend channels http://conda.anaconda.org/m-labs/label/dev
conda create -n artiq-phaser artiq=3.4 artiq-kc705-phaser matplotlib misoc migen openocd
source activate artiq-phaser

artiq_flash -t kc705 -m phaser 

cd ~/artiq-phaser/artiq/artiq/examples/master
artiq_compile repository/coredevice_examples/simple/blink_forever.py -o idle_kernel.elf
artiq_compile repository/coredevice_examples/simple/blink_forever.py -o default_kernel.elf
artiq_mkfs flash_storage.img -s mac 00:0a:35:03:1e:53 -s ip 192.168.1.71 -f idle_kernel idle_kernel.elf -f default_kernel default_kernel.elf
artiq_flash -t kc705 -m phaser -f flash_storage.img proxy storage start

ping 192.168.1.71
python3 -m serial.tools.list_ports -v
# port corresponding to MiSoC serial interface on core device uP
python3 -c """import serial.tools.list_ports; p=serial.tools.list_ports; hwid= 'USB VID:PID=10C4:EA60 SER=0001 LOCATION=1-9.2'; print(next(p.grep(hwid)))"""
