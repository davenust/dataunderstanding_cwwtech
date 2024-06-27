import os
import random
import shutil

# Path to your original dataset directory
dataset_dir = 'C:\Users\hp\Desktop\dataunderstanding_cww\dataunderstanding_cwwtech\new_data'

# Destination directories for train, validation, and test sets
train_dir = 'C:\Users\hp\Desktop\dataunderstanding_cww\dataunderstanding_cwwtech\new_data'
val_dir = 'C:\Users\hp\Desktop\dataunderstanding_cww\dataunderstanding_cwwtech\new_data'
test_dir = 'C:\Users\hp\Desktop\dataunderstanding_cww\dataunderstanding_cwwtech\new_data'

# Create destination directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# List all files in the dataset directory (assuming all are images)
files = os.listdir(dataset_dir)
random.shuffle(files)

# Calculate split sizes
total_files = len(files)
train_split = int(total_files * 0.6)
val_split = int(total_files * 0.2)

# Splitting the files
train_files = files[:train_split]
val_files = files[train_split:train_split + val_split]
test_files = files[train_split + val_split:]

# Move files to respective directories
def move_files(files, src_dir, dest_dir):
    for file in files:
        src = os.path.join(src_dir, file)
        dest = os.path.join(dest_dir, file)
        shutil.move(src, dest)

move_files(train_files, dataset_dir, train_dir)
move_files(val_files, dataset_dir, val_dir)
move_files(test_files, dataset_dir, test_dir)

print("Dataset split into train, validation, and test sets successfully!")
