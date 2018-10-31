#!/bin/bash
# create artiq build environment for sayma
# source build-artiq master

pushd .
source activate root
conda env remove -n artiq-dev --yes --quiet
rm -rf ~/artiq-dev

mkdir ~/artiq-dev
cd ~/artiq-dev

git clone --recursive http://github.com/jbqubit/artiq
cd artiq 
git checkout $1 

conda env create -f conda/artiq-dev.yaml 
source activate artiq-dev
conda install cython --yes --quiet 
pip install -e .

/usr/bin/time -o kasli_brittonlaba.time python artiq/gateware/targets/kasli.py --variant brittonlaba

# brittonlaba
# EEM0 TTL
# EEM1 TTL
# EEM2 TTL
# EEM3 Nogogorny
# EEM5, EEM4 Urukul
# EEM6 Urukul
# EEM7 Zotino
