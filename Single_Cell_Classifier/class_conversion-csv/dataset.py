import os
import sys
import pandas as pd

from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

from PIL import Image
import numpy as np

import label_converter
import pickle

##### Paths, Info about dataset
PATH_DATASET = '/storage/groups/qscd01/datasets/200409_mll_extended/prepared_100_folders'
PATH_PRELOAD = '/home/icb/matthias.hehr/projects/server_run/200721_mll_large_classifier/preloaded_data_register/split_80_20_20_excluded_2'


##### Actual dataset definition
class dataset(Dataset):

    '''MLL dataset'''

    def __init__(self, split='tvt', fold='train', rand_transforms=None, const_transforms=None, log_obj=None):

        self.dataset_string = "MLL dataset"
    
        # fuse transforms to one method
        self.random_transform=rand_transforms
        self.constant_transform=const_transforms

        ##### Set up proper root directories for general dataset
        if not (PATH_PRELOAD is None):
            self.data = pickle.load( open(os.path.join(PATH_PRELOAD, 'data_registry' + split + '_' + fold + '.pkl'), "rb" ) )
            self.targets = pickle.load( open(os.path.join(PATH_PRELOAD, 'label_registry' + split + '_' + fold + '.pkl'), "rb" ) )
            label_converter.initialize_conversion(path=os.path.join(PATH_PRELOAD, 'class_conversion.csv'))

            #for a in range(len(self.data))[::-1]:
            #    if(label_converter.shall_exclude_art(self.targets[a])):
            #        self.targets.pop(a)
            #        self.data.pop(a)

            return
        ##### Set up proper root directories for general dataset
        root_dirs = []
        if(split=='tt'):
            if(fold=='train'):
                for a in range(80):
                    root_dirs.append(os.path.join(PATH_DATASET, "fold_" + str(a)))
            if(fold=='test' or fold=='val'):
                for a in range(20):
                    root_dirs.append(os.path.join(PATH_DATASET, 'fold_' + str(a+80)))
        elif (split=='tvt'):
            if(fold=='train'):
                for a in range(60):
                    root_dirs.append(os.path.join(PATH_DATASET, "fold_" + str(a)))
            if(fold=='val'):
                for a in range(20):
                    root_dirs.append(os.path.join(PATH_DATASET, "fold_" + str(a+60)))
            if(fold=='test'):
                for a in range(20):
                    root_dirs.append(os.path.join(PATH_DATASET, "fold_" + str(a+80)))

        self.data = []
        self.targets = []
        for sgl_dir in root_dirs:
            print("Working on ", sgl_dir)
            for file_sgl in os.listdir(sgl_dir):

                if not '.TIF' in file_sgl:
                    continue

                true_lbl = str(file_sgl[:2])
                label_converter.add_entry(true_lbl, 1)

                label = self.retrieve_label(file_sgl)

                if not (label_converter.shall_exclude_true(true_lbl)):
                    self.data.append(os.path.join(sgl_dir, file_sgl))
                    self.targets.append(label)

        if not (log_obj is None):
            log_obj.save_pickle(name = ('data_registry' + split + '_' + fold + '.pkl'), obj=self.data)
            log_obj.save_pickle(name = ('label_registry' + split + '_' + fold + '.pkl'), obj=self.targets)

        


    def retrieve_label(self, filename):
        '''Define dataset-specific function, to retrieve true label for file.
        Here, Extracts data from the conversion table.                  '''
        
        true_lbl = str(filename[:2])
        try:
            result = label_converter.convert_true_to_art(true_lbl)
            return result
        except KeyError:
            return -1


    def __len__(self):
        '''returns amount of images contained in dataset'''
        return len(self.targets)


    def __getitem__(self, idx):
        '''returns specific item from this dataset'''

        # load image, remove alpha channel, transform
        image = Image.open(self.data[idx])
        image_arr = np.asarray(image)[:,:,:3]
        image = Image.fromarray(image_arr)

        if not (self.random_transform is None):
            image = self.random_transform(image)
        image = self.constant_transform(image)

        # load label
        label = self.targets[idx]

        return image, label







''' Scheme for distributing folds depending on the primary fold integer given
if FOLD >= 0:
    folds_train = []
    folds_val = []
    folds_test = []

    folds_train.append((FOLD*2+0)%10)
    folds_train.append((FOLD*2+1)%10)
    folds_train.append((FOLD*2+2)%10)
    folds_train.append((FOLD*2+3)%10)
    folds_train.append((FOLD*2+4)%10)
    folds_train.append((FOLD*2+5)%10)
    folds_val.append((FOLD*2+6)%10)
    folds_val.append((FOLD*2+7)%10)
    folds_test.append((FOLD*2+8)%10)
    folds_test.append((FOLD*2+9)%10)
else:
    folds_train = "train"
    folds_val = "val"
    folds_test = "test"
'''