#!/bin/sh -l
#SBATCH -c 2              # 2 CPU-core for each process
#SBATCH -N 2              # 2 nodes
#SBATCH -p gpu
#SBATCH --gpus-per-node 3 # Each process will see 3 GPUs
#SBATCH -t 30
#SBATCH --export=ALL

source /work/projects/ulhpc-tutorials/PS10-Horovod/soft/miniconda/scripts/env.sh

mpirun -n 6 python /work/projects/ulhpc-tutorials/PS10-Horovod/test_horovod.py