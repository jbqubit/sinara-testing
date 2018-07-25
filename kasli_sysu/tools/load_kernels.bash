#!/bin/bash

# $ source activate artiq-dev
# $ source tools/load_kernels.bash 

ARTIQ_PYTHON_SCRIPT="$1"

artiq_compile idle_kernel.py -o idle_kernel.elf
#artiq_compile "$ARTIQ_PYTHON_SCRIPT" -o startup_kernel.elf
artiq_mkfs -s startup_clock e -s mac 00:0a:35:03:1e:76 -s ip 192.168.1.76 -f idle_kernel idle_kernel.elf kasli.config
artiq_flash -t kasli -f kasli.config storage start