#!/bin/bash

# Request resources:
#SBATCH -n 1
#SBATCH --mem=60G
#SBATCH --time=30:0:0

# Run on the queue for serial ("sequential") work
# (job will share node with other jobs)
#SBATCH -p seq7.q

# Commands to be run:

module load python/3.6.8

python3 hamTest.py
