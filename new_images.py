import os
from PIL import Image

# Path to your dataset
dataset_path = "Humans"

# Create a new directory for renamed images
new_folder = "New_humans"
os.makedirs(new_folder, exist_ok=True)

# Loop through the dataset
for i, filename in enumerate(os.listdir(dataset_path)):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        # Load the image
        image_path = os.path.join(dataset_path, filename)
        image = Image.open(image_path)

        # Convert RGBA images to RGB
        if image.mode == "RGBA":
            image = image.convert("RGB")

        # Rename and save the image with the original format
        new_filename = f"image_{i+1}{os.path.splitext(filename)[1]}"
        new_path = os.path.join(new_folder, new_filename)
        image.save(new_path)

print("All images renamed and saved in New_humans folder.")
