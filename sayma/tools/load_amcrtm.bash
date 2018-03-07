#!/bin/bash
#$ source tools/sayma_load_to_ram.bash ~/artiq-dev/artiq/artiq_sayma_20180305_AMConly

ARTIQ_BUILD_DIR="$1"
FLASH_SCRIPT=~/github/jbqubit/sinara-testing/sayma/tools/sayma_flash.cfg
OPENOCD_SCRIPT_DIR=~/miniconda3/envs/artiq-dev/share/openocd/scripts
SAYMA_AMC_CMD="pld load 1 $ARTIQ_BUILD_DIR/standalone/gateware/top.bit; exit"
SAYMA_RTM_CMD="pld load 0 $ARTIQ_BUILD_DIR/rtm_gateware/rtm.bit; exit"

openocd -f "$FLASH_SCRIPT" -s "$OPENOCD_SCRIPT_DIR" -c "$SAYMA_AMC_CMD"
echo "DONE AMC"
sleep 5s
openocd -f "$FLASH_SCRIPT" -s "$OPENOCD_SCRIPT_DIR" -c "$SAYMA_RTM_CMD"
