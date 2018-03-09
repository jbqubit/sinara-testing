#!/bin/bash

#conda config --prepend channels http://conda.anaconda.org/conda-forge/label/main
#conda config --prepend channels http://conda.anaconda.org/m-labs/label/main
#conda config --prepend channels http://conda.anaconda.org/conda-forge/label/dev
#conda config --prepend channels http://conda.anaconda.org/m-labs/label/dev


# create artiq build environment for sayma

source activate root
conda env remove -n artiq-dev --yes --quiet
rm -rf ~/artiq-dev

mkdir ~/artiq-dev
cd ~/artiq-dev

git clone --recursive http://github.com/m-labs/artiq


conda env create -f artiq/conda/artiq-dev.yaml 
source activate artiq-dev
cd artiq 
git apply  ~/github/jbqubit/sinara-testing/sayma/tools/bypass_hmc830.diff
pip install -e .

/usr/bin/time -o sayma_rtm.time python artiq/gateware/targets/sayma_rtm.py
/usr/bin/time -o sayma_amc.time python artiq/gateware/targets/sayma_amc.py

