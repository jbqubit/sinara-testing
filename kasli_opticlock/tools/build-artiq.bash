#!/bin/bash
#set -e

#conda config --prepend channels http://conda.anaconda.org/conda-forge/label/main
#conda config --prepend channels http://conda.anaconda.org/m-labs/label/main
#conda config --prepend channels http://conda.anaconda.org/conda-forge/label/dev
#conda config --prepend channels http://conda.anaconda.org/m-labs/label/dev


# create artiq build environment for sayma
# source build-artiq master

pushd .
source activate root
conda env remove -n artiq-dev --yes --quiet
rm -rf ~/artiq-dev

mkdir ~/artiq-dev
cd ~/artiq-dev

git clone --recursive http://github.com/m-labs/artiq
cd artiq 
git checkout $1 

conda env create -f conda/artiq-dev.yaml 
source activate artiq-dev
#git apply  ~/github/jbqubit/sinara-testing/sayma/tools/bypass_hmc830.diff
#conda install --force --yes --quiet jesd204b=0.6
conda install cython --yes --quiet 
pip install -e .


/usr/bin/time -o kasli_opticlock.time python artiq/gateware/targets/kasli.py --variant opticlock


# opticlock
# EEM0 TTL
# EEM1 TTL
# EEM2 TTL
# EEM3 Nogogorny
# EEM5, EEM4 Urukul
# EEM6 Urukul
# EEM7 Zotino