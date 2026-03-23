"""
--------------------------------------------------------------------------------
PROGRAM: Exif Remover
AUTHOR:  Yel1oww
VERSION: 1.0
PURPOSE: A privacy-focused tool that "sanitizes" images by stripping all 
         metadata, leaving only the raw pixel data to prevent OSINT tracking.
--------------------------------------------------------------------------------
"""

from PIL import Image

# Define the input and output paths
image_path = "your_image.png"
output_path = "cleaned_your_image.png"

try:
    # Open the "dirty" image
    img = Image.open(image_path)
    print(f"Successfully loaded: {image_path}")
    
    # Create a brand new image using ONLY the pixel data
    data = list(img.getdata())
    clean_img = Image.new(img.mode, img.size)
    clean_img.putdata(data)
    
    # Save the new sanitized version
    clean_img.save(output_path)
    
    print("-" * 30)
    print(f"SUCCESS: Metadata has been stripped.")
    print(f"New sanitized file saved as: {output_path}")
    print("-" * 30)

except Exception as e:
    print(f"Error during sanitization: {e}")

# You can now run your 'exif-extractor.py' on the new file 
# to confirm that 'Found 0 metadata entries' is the result.