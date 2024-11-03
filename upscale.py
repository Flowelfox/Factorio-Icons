"""
Image Rescaling Module

This module provides functions to rescale images from a specified size to a target size.
It supports processing individual image files or entire folders containing images.
"""

import os
from typing import Tuple
from PIL import Image

# Global variables for image sizes
FROM_SIZE: Tuple[int, int] = (64, 64)
TO_SIZE: Tuple[int, int] = (100, 100)


def rescale_image(input_image_path: str, output_image_path: str, size: Tuple[int, int] = TO_SIZE) -> None:
    try:
        with Image.open(input_image_path) as img:
            if img.size == FROM_SIZE:
                img_rescaled = img.resize(size, Image.LANCZOS)
                os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
                img_rescaled.save(output_image_path)
                print(f"Image successfully rescaled to {size} and saved to {output_image_path}")
            else:
                print(f"Skipping {input_image_path}: size does not match {FROM_SIZE}")
    except Exception as e:
        print(f"An error occurred with {input_image_path}: {e}")


def rescale_images_in_folder(
    input_folder: str,
    output_folder: str,
    to_size: Tuple[int, int] = TO_SIZE
) -> None:
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                input_image_path: str = os.path.join(root, file)
                relative_path: str = os.path.relpath(input_image_path, input_folder)
                output_image_path: str = os.path.join(output_folder, relative_path)
                rescale_image(input_image_path, output_image_path, size=to_size)


def rescale(
    input_path: str,
    output_folder: str,
    to_size: Tuple[int, int] = TO_SIZE
) -> None:
    if os.path.isfile(input_path):
        file_name: str = os.path.basename(input_path)
        output_image_path: str = os.path.join(output_folder, file_name)
        rescale_image(input_path, output_image_path, size=to_size)
    elif os.path.isdir(input_path):
        rescale_images_in_folder(input_path, output_folder, to_size=to_size)
    else:
        print(f"Invalid input path: {input_path}")


# Example usage
if __name__ == "__main__":
    input_path: str = 'icons/64x64'  # Can be a file or a folder
    output_folder: str = 'icons/compiled/100x100'
    rescale(input_path, output_folder)