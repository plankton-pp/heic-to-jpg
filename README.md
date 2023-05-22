# HEIC to JPG Converter

This is a simple Python script that converts HEIC (High Efficiency Image Format) files to JPG format using the `wand.image` library. It allows you to convert all HEIC files in a specified source folder and save them as JPG files in a target folder.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- wand (Python binding for ImageMagick)

You can install the required packages by running:

```shell
pip install wand

Usage
1.Place your HEIC files in the HEIC-Source/ folder.
2.Run the script by executing the following command:

python heic_to_jpg_converter.py

3.The converted JPG files will be saved in the JPG-Output/ folder.
4.Any errors encountered during the conversion process will be displayed in the console.

Example
To provide an example usage, the script is already set up to convert files from `HEIC-Source/` to `JPG-Output/`. You can modify the source and target folders as per your requirements by updating the `source_folder` and `target_folder` variables in the script.

source_folder = "HEIC-Source/"
target_folder = "JPG-Output/"

convert_heic_to_jpg(source_folder, target_folder)

Make sure to create the source and target folders if they don't exist.

Notes
This script utilizes the wand.image library, which is a Python binding for ImageMagick. Make sure you have ImageMagick installed on your system.
The script will skip any files in the source folder that do not have a .heic extension.
If you encounter any issues or errors during the conversion process, please check the error message displayed in the console for more information.
Feel free to customize and modify the script according to your specific needs. Enjoy converting your HEIC files to JPG!