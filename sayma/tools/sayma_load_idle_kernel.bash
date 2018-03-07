#!/bin/bash
# source tools/sayma_load_idle_kernel.bash repository/misc/blink_led.py

ARTIQ_PYTHON_SCRIPT="$1"

artiq_compile "$ARTIQ_PYTHON_SCRIPT" -o idle_kernel.elf
artiq_compile "$ARTIQ_PYTHON_SCRIPT" -o startup_kernel.elf
artiq_mkfs -s mac 00:0a:35:03:1e:75 -s ip 192.168.1.75 -f idle_kernel idle_kernel.elf -f startup_kernel startup_kernel.elf sayma.config
artiq_flash -t sayma -f sayma.config storage 