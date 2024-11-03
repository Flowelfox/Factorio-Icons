"""
This script provides functionality to overlay multiple images with optional downscaling.
It uses the Python Imaging Library (PIL) to manipulate images and combine them into a single output.
"""

from PIL import Image

def overlay_two_images(base_image: Image.Image, overlay_image: Image.Image, downscale: float = 1.0) -> Image.Image:
    # Ensure both images are in RGBA mode to preserve alpha channel
    base_image = base_image.convert("RGBA")
    overlay_image = overlay_image.convert("RGBA")

    # Downscale the overlay image if necessary
    if 0 < downscale < 1:
        new_size = (int(overlay_image.width * downscale), int(overlay_image.height * downscale))
        overlay_image = overlay_image.resize(new_size, Image.LANCZOS)

    # Create a copy of the base image to overlay on
    combined_image = base_image.copy()

    # Calculate position to center the overlay image on the base image
    position = ((base_image.width - overlay_image.width) // 2, (base_image.height - overlay_image.height) // 2)

    # Paste the overlay image onto the combined image
    combined_image.paste(overlay_image, position, overlay_image)

    return combined_image


if __name__ == "__main__":
    # Example usage
    image_paths = [
        'icons/64x64/recycling.png',
        'icons/64x64/scrap.png',
        'icons/64x64/recycling-top.png'
    ]
    output_path = 'compiled/scrap_recycling.png'

    image1 = Image.open(image_paths[0]).convert("RGBA")
    image2 = Image.open(image_paths[1]).convert("RGBA")
    image3 = Image.open(image_paths[2]).convert("RGBA")

    combined_image = overlay_two_images(image1, image2, downscale=0.75)
    combined_image = overlay_two_images(combined_image, image3, downscale=1)
    combined_image.save(output_path)