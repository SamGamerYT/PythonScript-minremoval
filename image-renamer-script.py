import os
import datetime

def rename_images(root_directory, log_file_path):
    with open(log_file_path, 'a') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"=== Renaming Log ({timestamp}) ===\n")

        for root, _, files in os.walk(root_directory):
            for filename in files:
                if filename.endswith("-min.png"):
                    original_path = os.path.join(root, filename)
                    
                    # Remove the "-min" suffix
                    new_filename = filename.replace("-min", "")
                    new_path = os.path.join(root, new_filename)
                    
                    # Rename the file
                    os.rename(original_path, new_path)
                    
                    # Log the renaming activity
                    log_message = f"Renamed: {filename} to {new_filename}\n"
                    log_file.write(log_message)
                    print(log_message.strip())

# Replace 'your_root_directory_path' with the path to the root directory containing your images and subdirectories
root_directory_path = 'your_root_directory_path'

# Replace 'rename_log.txt' with the desired name of the log file
log_file_path = 'rename_log.txt'

rename_images(root_directory_path, log_file_path)