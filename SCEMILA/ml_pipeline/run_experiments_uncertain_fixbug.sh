#!/bin/bash

# Set the common parameters
result_folder="result_folder"

# Define an array of source folders
source_folders=(
#seed1
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed1/max_10_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed1/max_20_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed1/max_30_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed1/max_40_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed1/max_50_percent"
#seed20
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed20/max_10_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed20/max_20_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed20/max_30_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed20/max_40_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed20/max_50_percent"

#seed42
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed42/max_10_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed42/max_20_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed42/max_30_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed42/max_40_percent"
"/mnt/volume/shared/data_file/mixed_uncertain_fixbug_seed42/max_50_percent"
    # Add more source folders as needed
)

# Define an array of target folders
target_folders=(
       #seed1
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed1/max_10_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed1/max_20_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed1/max_30_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed1/max_40_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed1/max_50_percent"

    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed20/max_10_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed20/max_20_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed20/max_30_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed20/max_40_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed20/max_50_percent"

    #seed42
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed42/max_10_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed42/max_20_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed42/max_30_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed42/max_40_percent"
    "/mnt/volume/shared/new_results/mixed_uncertain_fixbug_seed42/max_50_percent"

    # Add more target folders as needed
)

# Iterate over the arrays and run the Python script
for ((i=0; i<${#source_folders[@]}; i++)); do
    mkdir -p "${target_folders[i]}"
    python3 run_pipeline_mixed.py --result_folder="$result_folder" --source_folder="${source_folders[i]}" --target_folder="${target_folders[i]}"
done
