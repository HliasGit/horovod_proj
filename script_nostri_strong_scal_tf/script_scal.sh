#!/bin/sh -l
#SBATCH -c 2              # 2 CPU-core for each process
#SBATCH -N 4              # 4 nodes
#SBATCH -p gpu
#SBATCH --gpus-per-node 4 # Each process will see 3 GPUs
#SBATCH -t 30
#SBATCH --export=ALL

source /work/projects/ulhpc-tutorials/PS10-Horovod/soft/miniconda/scripts/env.sh

for node in 1 2 3 4; do
    echo "Using $nodes nodes"
    mpirun -n $node python /work/projects/ulhpc-tutorials/PS10-Horovod/tensorflow_horovod_basic.py
    echo " "
    echo " "
done