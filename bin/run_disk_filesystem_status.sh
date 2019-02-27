#! /usr/bin/env bash


#!Need to run `sudo chmod +x run_disk_filesystem_status.sh`
#!And then just simply run the script with necessary arguments
PRODROOT=${PRODROOT:-/home/roman/PycharmProjects/SoftServe/internship-project}
PYTHON=${PYTHON:-~/anaconda3/bin/python}

PYSRCROOT=${PYSRCROOT:-${PRODROOT}/src/python}
PYTHONPATH=${PYTHONPATH:-${PYSRCROOT}}
CONFROOT=${CONFROOT:-${PRODROOT}/etc}
PYTHON_EGG_CACHE=${PYTHON_EGG_CACHE:-/tmp/.python-eggs}

export PRODROOT PYSRCROOT PYTHONPATH CONFROOT PYTHON_EGG_CACHE PYTHON

python ${PYSRCROOT}/monitors/disk_filesystem_status.py $*
