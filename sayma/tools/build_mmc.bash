#!/bin/bash

git clone https://github.com/m-labs/mmc-firmware/
cd mmc-firmware
mkdir build
cd build
cmake .. -DBOARD=sayma -DBOARD_RTM=sayma -DTARGET_CONTROLLER=LPC1776 -DCMAKE_BUILD_TYPE=Release -DBENCH_TEST=false
make
cd out
objcopy -I binary openMMC.bin -O ihex openMMC.hex
cp openMMC.hex ../../../
cd ../../../
rm -rf mmc-firmware