{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# all neccessary imports\n",
    "import torch\n",
    "import os\n",
    "from PIL import Image\n",
    "import label_converter # make sure the label_converter.py is in the folder with this notebook\n",
    "import numpy as np\n",
    "import glob\n",
    "from torchvision import transforms\n",
    "import torch.nn as nn\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# define paths\n",
    "#PATH_TO_IMAGES = '/mnt/volume/shared/data'\n",
    "#PATH_TO_IMAGES = \"/mnt/volume/shared/data_file/test_data\"\n",
    "PATH_TO_IMAGES = '/mnt/volume/shared/data_file/artificialdata/experiment_3_seed42/data'\n",
    "PATH_TO_MODEL = os.path.join(os.getcwd(), \"/home/hhauger/CMSCB-SCEMILA/Single_Cell_Classifier/class_conversion-csv/model.pt\")\n",
    "#PATH_TO_MODEL = os.path.join(os.getcwd(), \"class_conversion-csv/model.pt\")\n",
    "# load model and print architecture\n",
    "model = torch.load(PATH_TO_MODEL, map_location=torch.device('cpu'))\n",
    "#model.state_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_dataset(file_paths):\n",
    "    # Convert the list to a NumPy array\n",
    "    data = np.array(file_paths)\n",
    "\n",
    "    # Use the sorted indices to rearrange the file names array\n",
    "    sorted_images = np.sort(data)\n",
    "\n",
    "    return sorted_images\n",
    "\n",
    "def get_image(idx, data):\n",
    "        '''returns specific item from this dataset'''\n",
    "\n",
    "        # load image, remove alpha channel, transform\n",
    "        image = Image.open(data[idx])\n",
    "        image_arr = np.asarray(image)[:,:,:3]\n",
    "        image = Image.fromarray(image_arr)\n",
    "\n",
    "        return torch.tensor(image_arr)\n",
    "\n",
    "def save_single_cell_probabilities(data, folder_patient):\n",
    "    array_list = []\n",
    "    #print(\"Target \\t Prediction\")\n",
    "    print(len(data))\n",
    "    for idx in range(len(data)):\n",
    "        input = get_image(idx, data)\n",
    "        input = input.permute(2, 0, 1).unsqueeze(0)\n",
    "        \n",
    "        # Convert input to float\n",
    "        input = input.float()\n",
    "        input = input / 255.\n",
    "\n",
    "        # Normalize the input\n",
    "        normalize = transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])\n",
    "        input = normalize(input)\n",
    "        \n",
    "        model.eval()\n",
    "        pred = model(input)\n",
    "        softmax = nn.Softmax(dim=1)\n",
    "        pred_probability = softmax(pred)\n",
    "\n",
    "        # Save probabilities in a file\n",
    "        pred_vect = pred_probability.detach().numpy().flatten()\n",
    "        array_list.append([pred_vect])\n",
    "    print(\"Concatenate single_cell_props\")\n",
    "    #Concatenate all features for one artificial patient    \n",
    "    single_cell_probs = np.concatenate(array_list,axis=0)\n",
    "    output_npy_file = folder_patient + '/single_cell_probabilities.npy'\n",
    "    # Save the array to the .npy file\n",
    "    np.save(output_npy_file, single_cell_probs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save class probabilities for each patient\n",
    "for folder_class in os.listdir(PATH_TO_IMAGES):\n",
    "    folder_class = os.path.join(PATH_TO_IMAGES, folder_class)\n",
    "    \n",
    "    if os.path.isdir(folder_class):\n",
    "       print(folder_class)\n",
    "       for folder_patient in os.listdir(folder_class):\n",
    "            folder_patient = os.path.join(folder_class, folder_patient)\n",
    "            if os.path.isdir(folder_patient):\n",
    "                #Get filepaths to images:\n",
    "                path_to_list = folder_patient+\"/image_file_paths\"\n",
    "                with open(path_to_list, 'rb') as file: \n",
    "                    tif_files = pickle.load(file)\n",
    "                if tif_files:\n",
    "                    print(\"Processing patient folder with .tif files:\", folder_patient)\n",
    "                    data = create_dataset(tif_files)\n",
    "                    save_single_cell_probabilities(data, folder_patient)\n",
    "                else:\n",
    "                    print(\"Skipping patient folder without .tif files:\", folder_patient)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
