#!/bin/bash

# Request resources:
#SBATCH -n 1
#SBATCH --mem=1G
#SBATCH --time=0:10:0

# Run on the queue for serial ("sequential") work
# (job will share node with other jobs)
#SBATCH -p test.q

# Commands to be run:

module load python/3.6.8

pip install --user numba

python3 hamTest.py
