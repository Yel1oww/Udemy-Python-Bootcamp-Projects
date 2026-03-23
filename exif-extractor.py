"""
--------------------------------------------------------------------------------
PROGRAM: Exif Extractor
AUTHOR:  Yel1oww
VERSION: 1.0
PURPOSE: A digital forensics tool designed to audit and extract hidden 
         metadata (EXIF) from image files for OSINT and investigation.
--------------------------------------------------------------------------------
"""

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Define the path to your image
image_path = "your_image.png"

try:
    # Open the image
    img = Image.open(image_path)
    print(f"Successfully loaded: {image_path}")
    print(f"Format: {img.format} | Size: {img.size} | Mode: {img.mode}")

except Exception as e:
    print(f"Error: {e}")

# Get the EXIF data
exif_data = img._getexif()

if not exif_data:
    print('There was no metadata found.')
else:
    # Everything below this is now INSIDE the else block
    print(f"Found {len(exif_data)} metadata entries")

    # Iterate and translate the data
    for tag_id, value in exif_data.items():
        tag_name = TAGS.get(tag_id, tag_id)

        if tag_name == "GPSInfo":
            gps_data = {}
            for t in value:
                sub_tag = GPSTAGS.get(t, t)
                gps_data[sub_tag] = value[t]

            print("\n--- GPS DATA FOUND ---") 
            for key, val in gps_data.items():
                print(f"{key:20}: {val}")
            print("-" * 20)

        # Print the results for all tags
        print(f"{tag_name:20}: {value}")