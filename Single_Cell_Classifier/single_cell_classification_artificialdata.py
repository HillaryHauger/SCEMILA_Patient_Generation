#!/usr/bin/env python
# coding: utf-8

# In[1]:


# all neccessary imports
import torch
import os
from PIL import Image
import label_converter # make sure the label_converter.py is in the folder with this notebook
import numpy as np
import glob
from torchvision import transforms
import torch.nn as nn
import pickle


# In[9]:


# define paths
#PATH_TO_IMAGES = '/mnt/volume/shared/data'
#PATH_TO_IMAGES = "/mnt/volume/shared/data_file/test_data"
PATH_TO_IMAGES = '/mnt/volume/shared/data_file/artificialdata/experiment_3_seed42/data'
PATH_TO_MODEL = os.path.join(os.getcwd(), "/home/hhauger/CMSCB-SCEMILA/Single_Cell_Classifier/class_conversion-csv/model.pt")
#PATH_TO_MODEL = os.path.join(os.getcwd(), "class_conversion-csv/model.pt")
# load model and print architecture
model = torch.load(PATH_TO_MODEL, map_location=torch.device('cpu'))
#model.state_dict


# In[12]:


def create_dataset(file_paths):
    # Convert the list to a NumPy array
    data = np.array(file_paths)

    # Use the sorted indices to rearrange the file names array
    sorted_images = np.sort(data)

    return sorted_images

def get_image(idx, data):
        '''returns specific item from this dataset'''

        # load image, remove alpha channel, transform
        image = Image.open(data[idx])
        image_arr = np.asarray(image)[:,:,:3]
        image = Image.fromarray(image_arr)

        return torch.tensor(image_arr)

def save_single_cell_probabilities(data, folder_patient):
    array_list = []
    #print("Target \t Prediction")
    print(len(data))
    for idx in range(len(data)):
        input = get_image(idx, data)
        input = input.permute(2, 0, 1).unsqueeze(0)
        
        # Convert input to float
        input = input.float()
        input = input / 255.

        # Normalize the input
        normalize = transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        input = normalize(input)
        
        model.eval()
        pred = model(input)
        softmax = nn.Softmax(dim=1)
        pred_probability = softmax(pred)

        # Save probabilities in a file
        pred_vect = pred_probability.detach().numpy().flatten()
        array_list.append([pred_vect])
    print("Concatenate single_cell_props")
    #Concatenate all features for one artificial patient    
    single_cell_probs = np.concatenate(array_list,axis=0)
    output_npy_file = folder_patient + '/single_cell_probabilities.npy'
    # Save the array to the .npy file
    np.save(output_npy_file, single_cell_probs)


# In[ ]:


# Save class probabilities for each patient
for folder_class in os.listdir(PATH_TO_IMAGES):
    folder_class = os.path.join(PATH_TO_IMAGES, folder_class)
    
    if os.path.isdir(folder_class):
       print(folder_class)
       for folder_patient in os.listdir(folder_class):
            folder_patient = os.path.join(folder_class, folder_patient)
            if os.path.isdir(folder_patient):
                #Get filepaths to images:
                path_to_list = folder_patient+"/image_file_paths"
                with open(path_to_list, 'rb') as file: 
                    tif_files = pickle.load(file)
                if tif_files:
                    print("Processing patient folder with .tif files:", folder_patient)
                    data = create_dataset(tif_files)
                    save_single_cell_probabilities(data, folder_patient)
                else:
                    print("Skipping patient folder without .tif files:", folder_patient)


# In[ ]:




