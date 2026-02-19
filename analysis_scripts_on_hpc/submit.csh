#!/bin/tcsh

# LSF job settings
#BSUB -W 2000
#BSUB -q serial
#BSUB -n 1
#BSUB -oo /share/belmonte/athayam/Gastrulation_analysis_results/out.%J
#BSUB -eo /share/belmonte/athayam/Gastrulation_analysis_results/err.%J

# This job runs the main Python analysis script for the Gastrulation dataset
python analysis_main.py
