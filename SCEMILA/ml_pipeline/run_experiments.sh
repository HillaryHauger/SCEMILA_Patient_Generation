#!/bin/bash

# Set the common parameters
result_folder="result_folder"

# Define an array of source folders
source_folders=(
    #"/mnt/volume/shared/data_file/artificialdata/experiment_3_seed1"
    "/mnt/volume/shared/data_file/artificialdata/experiment_3_seed20"
    "/mnt/volume/shared/data_file/artificialdata/experiment_3_seed42"
    # Add more source folders as needed
)

# Define an array of target folders
target_folders=(
   # "/mnt/volume/shared/new_results/experiment_3_seed1"
    "/mnt/volume/shared/new_results/experiment_3_seed20"
    "/mnt/volume/shared/new_results/experiment_3_seed42"
    # Add more target folders as needed
)

# Iterate over the arrays and run the Python script
for ((i=0; i<${#source_folders[@]}; i++)); do
    mkdir -p "${target_folders[i]}"
    python3 run_pipeline.py --result_folder="$result_folder" --source_folder="${source_folders[i]}" --target_folder="${target_folders[i]}"
done
