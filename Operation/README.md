# HEIC to JPG Converter

This is a Python script that converts HEIC (High Efficiency Image Format) files to JPG (JPEG) format using the `wand.image` library. It takes a source folder containing HEIC files and converts them to JPG format, saving the converted files to a target folder.

## Requirements

- Python 3.x
- `wand` library

## Installation

To use this script, follow these steps:

1. Install Python 3.x on your system if it is not already installed. You can download Python from the official website: https://www.python.org/downloads/

2. Install the `wand` library by running the following command:

   ```shell
   pip install Wand


## Usage
1. Place the HEIC files you want to convert in a source folder. By default, the source folder is set to HEIC-Source/.

2. Create a target folder where the converted JPG files will be saved. By default, the target folder is set to JPG-Output/. Make sure the target folder exists or is a valid path.

3. Open the Python script and modify the source_folder and target_folder variables if you want to use custom folders.

4. Uncomment the check_folder_exists lines if you want to validate the existence of the source and target folders before converting. This is optional.

5. Run the script using Python:

   ```shell
   python heic_to_jpg_converter.py
   
6. The script will iterate over the files in the source folder and convert any HEIC files to JPG format. The converted files will be saved in the target folder. Any errors encountered during the conversion process will be displayed in the console.

## Notes
The script uses the os.makedirs function to create the target folder if it doesn't already exist. If the target folder already exists, it will not be overwritten.

The wand.image library is used to open and save the images. It relies on the ImageMagick software, so make sure it is installed on your system.

The script only converts files with the .heic extension. If you have files with a different extension or want to convert files with multiple extensions, you can modify the if file_name.lower().endswith(".heic") line in the script.

The converted JPG files will have the same name as the original HEIC files, with the extension changed to .jpg.

The print statements in the script provide feedback on the conversion process. You can remove or modify them as needed.


# Disclaimer
This script is provided as-is without any warranties. Use it at your own risk. Make sure to test it thoroughly and backup your files before running it on a large number of files.

Please note that the HEIC format is subject to patent rights and may require licensing for certain uses. Ensure that you have the necessary rights and permissions to convert HEIC files to JPG format.
