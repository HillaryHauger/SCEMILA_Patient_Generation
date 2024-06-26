# SCEMILA_Patient_Generation

Welcome to the Github repository supplementing the publication “Improvement of Acute Myeloid Leukemia Subtype Classification using Artificial Patient Generation." (  Sadafi A, Chernysheva A,  El-Wafi J, Hauger H, Ivanova A, Hehr M, Navab N, Marr C)

Table of contents
1.	Description
2.	Getting started

	2.1. Data

	2.2. Dependencies

	2.3. Code Setup

	2.4. Execution

	2.5. Analysis
4.	Authors
5.	Acknowledgements
6.	License

## Description
This repository contains the machine learning model implementation along with data augmentation techniques used in the research paper titled “Improvement of Acute Myeloid Leukemia Subtype Classification using Artificial Patient Generation." (Sadafi A, Chernysheva A,  El-Wafi J, Hauger H, Ivanova A, Hehr M, Navab N, Marr C)[Link to the paper]. In addition, it provides various plots and metrics produced during the experimentation and patient generation process outlined in the paper.

## Getting started
### Data
To reproduce results, download the data and unzip it.  
The data is available at The Cancer Imaging Archive (TCIA): https://doi.org/10.7937/6ppe-4020 	
Hehr, M., Sadafi, A., Matek, C., Lienemann, P., Pohlkamp, C., Haferlach, T., Spiekermann, K., & Marr, C. (2023). A morphological dataset of white blood cells from patients with four different genetic AML entities and non-malignant controls (AML-Cytomorphology_MLL_Helmholtz) (Version 1) [Data set]. The Cancer Imaging Archive.  
The metadata for train/test split to reproduce the results from paper can be found in the Data folder.  
### Code setup
The Code Setup is similar to the orignal SCEMILA paper. See https://github.com/marrlab/SCEMILA for reference.  
Reference: "Explainable AI identifies diagnostic cells of genetic AML subtypes." (Hehr M, Sadafi A, Matek C, Lienemann P, Pohlkamp C, et al. (2023) PLOS Digital Health 2(3): e0000187. https://doi.org/10.1371/journal.pdig.0000187)
### Execution

#### Creating Artficial patients
The artifcial patients can be generated in SCEMILA/create_artifcial_patients. This includes 5 different experiments:
1. random shuffle over the whole data set
2. random shuffle within each AML subtype
3. random shuffle according to the single cell distribution
4. Naive mixture of real and artificial patients
5. Uncertainty mixture of ral and artifical patients

For all of these experiments, it is necessary to create the single cell probabilites by running Single_Cell_Classifier/single_cell_classification.ipynb first.
Furthermore, for experiment 3, you need to create a csv file in SCEMILA/create_artifcial_patients/create_single_cell_results.ipynb.
For experiment 5, you need to calculate to run SCEMILA_Dropout first and perform SCEMILA_Dropout/ml_pipeline/uncertainty.test

#### Running SCEMILA
Running the original data and the pure artificial data works like in the orginal SCEMILA. So you have to specify which data you want to use in run_pipeline.py then run SCEMILA with:

	python3 run_pipeline.py --result_folder=result_folder_1

The data mixed with artifically generated patients and real patients is run like this:

	python3 run_pipeline_mixed.py --result_folder=result_folder --source_folder=source_folders --target_folder=target_folders[i]
 
### Analysis
## Authors
## Acknowledgements
