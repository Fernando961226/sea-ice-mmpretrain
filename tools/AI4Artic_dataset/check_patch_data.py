#%%
import joblib

# Specify the path to the saved .pkl file
file_path = '/home/fernando/scratch/train/20211112T201942_dmi_prep_down_scale_2X/00000.pkl'

# Load the dictionary from the .pkl file
loaded_data_patch = joblib.load(file_path)

# Now 'loaded_data_patch' contains the deserialized dictionary
print(loaded_data_patch)
# %%
