from wand.image import Image
import os

def convert_heic_to_jpg(source_folder, target_folder):
    os.makedirs(target_folder, exist_ok=True)

    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(".heic"):
            source_file = os.path.join(source_folder, file_name)
            target_file = os.path.join(target_folder, file_name[:-5] + ".jpg")
            
            try:
                with Image(filename=source_file) as img:
                    img.format = 'jpg'
                    img.save(filename=target_file)
                
                print(f"Converted: {source_file} -> {target_file}")
            except Exception as e:
                print(f"Error converting {source_file}: {str(e)}")

                
def check_folder_exists(folder_path):
    if not os.path.isdir(folder_path):
        raise ValueError(f"Folder does not exist: {folder_path}")
    else:
        print(folder_path," is exist.")

# Example usage:
source_folder = "HEIC-Source/"
target_folder = "JPG-Output/"

# check_folder_exists(source_folder)
# check_folder_exists(target_folder)
convert_heic_to_jpg(source_folder, target_folder)
