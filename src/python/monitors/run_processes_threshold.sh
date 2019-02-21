#! /usr/bin/env bash

PRODROOT=${PRODROOT:-/home/roman/PycharmProjects/SoftServe/internship-project}
PYTHON=${PYTHON:-~/miniconda3/bin/python}

PYSRCROOT=${PYSRCROOT:-${PRODROOT}/src/python}
PYTHONPATH=${PYTHONPATH:-${PYSRCROOT}}
CONFROOT=${CONFROOT:-${PRODROOT}/etc}
PYTHON_EGG_CACHE=${PYTHON_EGG_CACHE:-/tmp/.python-eggs}

export PRODROOT PYSRCROOT PYTHONPATH CONFROOT PYTHON_EGG_CACHE PYTHON

${PYTHON} ${PYSRCROOT}/monitors/processes_threshold.py $*