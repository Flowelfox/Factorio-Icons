"""
Image Processing Module
=======================

This module provides functionality to process PNG images by cropping them into specified parts based on their
dimensions. It is designed to handle images with specific width-to-height ratios, supporting both 2-part and
4-part cropping modes.

Features:
- **Automatic Mode Detection**: Determines whether an image should be processed in 2-part or 4-part mode
  based on its width-to-height ratio.
- **Flexible Cropping**: Allows cropping of different parts of the image by specifying the `part` parameter.
- **Error Handling**: Skips unsupported image formats and size ratios, providing informative messages.
- **Batch Processing**: Processes all PNG images in the specified input folder and saves the cropped images to
  the output folder.

Usage:
1. **Configure Folders**:
   - Set the `input_folder` to the directory containing the images you want to process.
   - Set the `output_folder` to the directory where you want to save the cropped images.

2. **Run the Script**:
   Execute the script directly to process the images with the desired part.

3. **Customize Parameters**:
   - Modify the `part` parameter in the `process_images` function call to crop different parts of the image.

"""
import os
from PIL import Image

def process_images(input_folder: str, output_folder: str, part=1):
    """
    Processes images by cropping a specified part based on the image size.

    Parameters:
    - input_folder (str): Path to the folder containing input images.
    - output_folder (str): Path to the folder where processed images will be saved.
    - part (int, optional): The part to crop. For 4-part images, valid values are 1-4.
                            For 2-part images, valid values are 1-2. Defaults to 1.

    What it does:
    - Validates the `part` parameter based on image ratio.
    - Checks if each image fits either 4-part or 2-part mode based on its width-to-height ratio.
    - Computes the crop size and position based on the specified `part` and mode.
    - Crops the image accordingly and saves it to the output folder.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".png"):
            img_path = os.path.join(input_folder, filename)
            try:
                with Image.open(img_path) as img:
                    width, height = img.size

                    if (width / 2) == height or (width - height) == height / 2:
                        mode = '2_part'
                        max_part = 2
                    elif (width / 4) == height:
                        mode = '4_part'
                        max_part = 4
                    else:
                        print(f"Skipping {filename}: Unsupported size ratio ({width}x{height}).")
                        continue

                    if not isinstance(part, int) or not (1 <= part <= max_part):
                        print(f"Skipping {filename}: 'part' parameter {part} is out of range for {mode} mode.")
                        continue

                    s = height  # Base size

                    if mode == '4_part':
                        if part == 1:
                            x = 0
                            crop_width, crop_height = s, s
                        elif part == 2:
                            x = s
                            crop_width, crop_height = s // 2, s // 2
                        elif part == 3:
                            x = s + (s // 2)
                            crop_width, crop_height = s // 4, s // 4
                        elif part == 4:
                            x = s + (s // 2) + (s // 4)
                            crop_width, crop_height = s // 8, s // 8
                    elif mode == '2_part':
                        if part == 1:
                            x = 0
                            crop_width, crop_height = s, s
                        elif part == 2:
                            x = s
                            crop_width, crop_height = s // 2, s // 2

                    # Validate crop boundaries
                    if width < x + crop_width or height < crop_height:
                        print(f"Skipping {filename}: Crop area out of bounds for part {part}.")
                        continue

                    # Perform cropping
                    cropped_img = img.crop((x, 0, x + crop_width, crop_height))
                    output_path = os.path.join(output_folder, filename)
                    cropped_img.save(output_path, "PNG")
                    print(f"Saved cropped part {part} of {filename} to {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
        else:
            print(f"Skipping {filename}: Not a PNG file.")

if __name__ == "__main__":
    # Define the input and output folders
    input_folder = 'icons/collected/120x64'
    output_folder = 'icons/compiled/64x64'

    # Process the images with the desired part
    process_images(input_folder, output_folder, part=1)
