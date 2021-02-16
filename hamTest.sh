#!/bin/bash

# Request resources:
#SBATCH -n 1          # 1 CPU core
#SBATCH --mem=1G      # 1 GB RAM
#SBATCH --time=6:0:0  # 6 hours (hours:minutes:seconds)

# Run on the queue for serial ("sequential") work
# (job will share node with other jobs)
#SBATCH -p test.q

# Commands to be run:

module load python/3.6.8

python3 -m pip install numba

python3 hamTest.py
