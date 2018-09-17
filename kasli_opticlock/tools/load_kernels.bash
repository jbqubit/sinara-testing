#!/bin/bash

# $ source activate artiq-dev
# $ source tools/load_kernels.bash 


artiq_compile repository/idle_kernel.py -o idle_kernel.elf
#artiq_compile "$ARTIQ_PYTHON_SCRIPT" -o startup_kernel.elf
artiq_mkfs -s mac 00:0a:35:03:1e:77 -s ip 192.168.1.77 -f idle_kernel idle_kernel.elf kasli.config
artiq_flash -t kasli -f kasli.config storage start