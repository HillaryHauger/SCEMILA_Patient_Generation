# SCEMILA_Patient_Generation

Welcome to the Github repository supplementing the publication “Improvement of Acute Myeloid Leukemia Subtype Classification using Artificial Patient Generation." (    Sadafi A, Marr C, Navab N, Chernysheva A,  El-Wafi J, Hauger H, Ivanova A)

Table of contents
1.	Description
2.	Getting started
	2.1 Data
	2.2 Dependencies 
	2.3 Code setup
	2.4 Execution
	2.5 Analysis
3.	Authors
4.	Acknowledgements
5.	License

## About


Argument	Description	Possible input	Default
--fold	Change this parameter to rotate through different folds of cross validation.For 5-fold cross validation (default), simply launch the code five times, every time with a different value for --fold in range of [0,1,2,3,4]	Integer, suggested: [0,1,2,3,4]	0
--lr	Learning rate	Float	0.00005
--ep	Maximum epochs to train for, until training stops	Integer	150
--es	Early stopping. Amount of epochs to keep training, while no improvement on the validation loss is made.	Integer	20
--multi_att	Enable multiple attention values for each image (one value per image, per possible class) as suggested in our paper.	Integer (0=False, 1=True)	1
--prefix	The prefix defines the set of features that should be loaded. If an own method for feature extraction is generated and the features are saved in the dataset folder, change this value to make use of the newly generated features.	String	fnl34_
--filter_diff	Filter out patients based on the amount of myeloblasts derived from human blood smear differential count (data stored the dataset master csv file). Value represents % of cells, patients with less (<) myeloblasts are filtered out.	Integer	20
--filter_mediocre_quality	Filter out patients with borderline acceptable sample quality. This data is derived from cytologist assessment of the digitized samples.	Integer (0=False, 1=True)	0
--bootstrap_idx	For further experiments: Integer value, which is responsible for dropping out a specific patient from the dataset. Setting this to -1 deactivates the mechanism.	Integer	-1
--save_model	Deactivate model saving to save storage (e.g. if only accuracy is relevant). The model file is required to generate the occlusion maps, so deactivating will prevent generating the data used for the occlusion maps.	Integer (0=False, 1=True)	1

