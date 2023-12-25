import os

def rename_images(root_directory):
    for root, _, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith("-min.png"):
                original_path = os.path.join(root, filename)
                
                # Remove the "-min" suffix
                new_filename = filename.replace("-min", "")
                new_path = os.path.join(root, new_filename)
                
                # Rename the file
                os.rename(original_path, new_path)
                print(f"Renamed: {filename} to {new_filename}")

# Replace 'your_root_directory_path' with the path to the root directory containing your images and subdirectories
root_directory_path = 'your_root_directory_path'

rename_images(root_directory_path)