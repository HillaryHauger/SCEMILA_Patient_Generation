#!/bin/bash

# Set the common parameters
result_folder="result_folder"

# Define an array of source folders
source_folders=(
    "/mnt/volume/shared/data_file/mixed_seed1/10_percent"
    "/mnt/volume/shared/data_file/mixed_seed1/20_percent"
    "/mnt/volume/shared/data_file/mixed_seed1/30_percent"
    "/mnt/volume/shared/data_file/mixed_seed1/50_percent"
    "/mnt/volume/shared/data_file/mixed_seed20/10_percent"
    "/mnt/volume/shared/data_file/mixed_seed20/20_percent"
    "/mnt/volume/shared/data_file/mixed_seed20/30_percent"
    "/mnt/volume/shared/data_file/mixed_seed20/50_percent"
    "/mnt/volume/shared/data_file/mixed_seed42/10_percent"
    "/mnt/volume/shared/data_file/mixed_seed42/20_percent"
    "/mnt/volume/shared/data_file/mixed_seed42/30_percent"
    "/mnt/volume/shared/data_file/mixed_seed42/50_percent"
    # Add more source folders as needed
)

# Define an array of target folders
target_folders=(
    "/mnt/volume/shared/new_results/mixed_seed1/10_percent"
    "/mnt/volume/shared/new_results/mixed_seed1/20_percent"
    "/mnt/volume/shared/new_results/mixed_seed1/30_percent"
    "/mnt/volume/shared/new_results/mixed_seed1/50_percent"
    "/mnt/volume/shared/new_results/mixed_seed20/10_percent"
    "/mnt/volume/shared/new_results/mixed_seed20/20_percent"
    "/mnt/volume/shared/new_results/mixed_seed20/30_percent"
    "/mnt/volume/shared/new_results/mixed_seed20/50_percent"
     "/mnt/volume/shared/new_results/mixed_seed42/10_percent"
    "/mnt/volume/shared/new_results/mixed_seed42/20_percent"
    "/mnt/volume/shared/new_results/mixed_seed42/30_percent"
    "/mnt/volume/shared/new_results/mixed_seed42/50_percent"
    # Add more target folders as needed
)

# Iterate over the arrays and run the Python script
for ((i=0; i<${#source_folders[@]}; i++)); do
    mkdir -p "${target_folders[i]}"
    python3 run_pipeline_mixed.py --result_folder="$result_folder" --source_folder="${source_folders[i]}" --target_folder="${target_folders[i]}"
done
