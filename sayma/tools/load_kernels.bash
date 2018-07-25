#!/bin/bash

# $ tools/load_kernels.bash repository/misc/blink_led.py

ARTIQ_PYTHON_SCRIPT="$1"


#artiq_compile "$ARTIQ_PYTHON_SCRIPT" -o idle_kernel.elf
artiq_compile "$ARTIQ_PYTHON_SCRIPT" -o startup_kernel.elf
#artiq_mkfs -s net_trace 1 -s panic_reset 1 -s mac 00:0a:35:03:1e:75 -s ip 192.168.1.75 -f startup_kernel startup_kernel.elf -f idle_kernel idle_kernel.elf sayma.config
artiq_mkfs -s net_trace 0 -s panic_reset 0 -s mac 00:0a:35:03:1e:75 -s ip 192.168.1.75 -f startup_kernel startup_kernel.elf sayma.config
artiq_flash -t sayma -f sayma.config storage 