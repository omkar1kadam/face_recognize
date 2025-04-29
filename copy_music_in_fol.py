import os
import shutil
import random

# Path to the folder with all images (after download and unzip)
source_folder = 'angry'
train_folder = 'train'
test_folder = 'test'

# Create train and test folders if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Get all image filenames from the source folder
all_images = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Copy all images to the train folder
for image in all_images:
    shutil.copy(os.path.join(source_folder, image), os.path.join(train_folder, image))

# Randomly select 20% of the images for the test set
test_size = int(0.2 * len(all_images))
test_images = random.sample(all_images, test_size)

# Copy selected images to the test folder
for image in test_images:
    shutil.copy(os.path.join(source_folder, image), os.path.join(test_folder, image))

print(f"Copied {len(all_images)} images to '{train_folder}'")
print(f"Copied {len(test_images)} images to '{test_folder}'")
