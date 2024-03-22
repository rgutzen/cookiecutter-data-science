#!/usr/bin/env bash
#SBATCH -o /home/ {{ cookiecutter.user_name }}/ {{ cookiecutter.repo_name }}/slurm/%j.out
#SBATCH -e home/ {{ cookiecutter.user_name }}/ {{ cookiecutter.repo_name }}/slurm/%j.err
#SBATCH --time=01:00:00
#SBATCH --mem=60G
#SBATCH --nodes=1                        # requests 3 compute servers
#SBATCH --ntasks-per-node=10             # runs 2 tasks on each server
#SBATCH --cpus-per-task=1                # uses 1 compute core per task
#SBATCH --job-name={{ cookiecutter.short_name }}
#SBATCH --mail-type=END,FAIL
# #SBATCH --gres=cpu

conda activate {{ cookiecutter.short_name }}

snakemake --unlock --cores=1
snakemake --jobname '{jobid}.{rulename}' \
	      --latency-wait 90 \
          --keep-going \
          --nolock \
          --rerun-incomplete \
          --cores=1 \
          --jobs=1 