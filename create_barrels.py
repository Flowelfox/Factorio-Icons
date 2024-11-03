"""
This script generates barrel icons for various fluids in a game or application using the Python Imaging
Library (PIL). It creates composite icons for filled and empty barrels based on fluid colors.

Key Features:
- Generates barrel icons with tinted masks based on fluid colors.
- Processes a dictionary of fluids to generate corresponding icons.

Usage:
- Ensure the necessary icons and masks are available in the specified paths.
- Run the script to generate barrel icons for the defined fluids.
"""

import os
from PIL import Image

from fluids import fluids_for_barrels

# Define constants
DEFAULT_ICON_SIZE = 64
SIDE_ALPHA = 0.75  # Adjusted intensity for side mask
TOP_HOOP_ALPHA = 0.75  # Adjusted intensity for hoop top mask

# Define global constants for file paths
BARREL_FILL_ICON = "icons/barrel/barrel-fill.png"
BARREL_SIDE_MASK_ICON = "icons/barrel/barrel-side-mask.png"
BARREL_TOP_MASK_ICON = "icons/barrel/barrel-hoop-top-mask.png"

BARREL_EMPTY_ICON = "icons/barrel/barrel-empty.png"
BARREL_EMPTY_SIDE_MASK_ICON = "icons/barrel/barrel-empty-side-mask.png"
BARREL_EMPTY_TOP_MASK_ICON = "icons/barrel/barrel-empty-top-mask.png"

FLUID_ICON_TEMPLATE = "icons/barrel/fluids/{fluid_name}.png"

STANDING_BARREL_LAYERS = {
    'base': BARREL_FILL_ICON,
    'side': BARREL_SIDE_MASK_ICON,
    'top': BARREL_TOP_MASK_ICON
}

EMPTY_BARREL_LAYERS = {
    'base': BARREL_EMPTY_ICON,
    'side': BARREL_EMPTY_SIDE_MASK_ICON,
    'top': BARREL_EMPTY_TOP_MASK_ICON
}


# Utility functions
def get_color_with_alpha(color, alpha):
    return (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255), int(alpha * 255))


def apply_tint(image, tint_color):
    r, g, b, a = image.split()
    r = r.point(lambda i: i * tint_color[0] / 255)
    g = g.point(lambda i: i * tint_color[1] / 255)
    b = b.point(lambda i: i * tint_color[2] / 255)
    return Image.merge('RGBA', (r, g, b, a))


# Generate barrel icons
def generate_barrel_icons(fluid: dict, layers: dict[str, str], icon_position: str=None):


    base_icon = Image.open(layers['base']).convert("RGBA")
    side_mask = Image.open(layers['side']).convert("RGBA")
    top_mask = Image.open(layers['top']).convert("RGBA")
    side_tint = get_color_with_alpha(fluid['base_color'], SIDE_ALPHA)
    fluid_icon_path = FLUID_ICON_TEMPLATE.format(fluid_name=fluid['name'])

    # Apply tints to masks
    side_mask = apply_tint(side_mask, side_tint)

    # Composite the images
    base_icon.paste(side_mask, (0, 0), side_mask)
    top_tint = get_color_with_alpha(fluid['flow_color'], TOP_HOOP_ALPHA)
    top_mask = apply_tint(top_mask, top_tint)
    base_icon.paste(top_mask, (0, 0), top_mask)

    if icon_position is not None:
        fluid_icon = Image.open(fluid_icon_path).convert("RGBA")
        scale = 16.0 / (DEFAULT_ICON_SIZE / 2)
        new_size = (int(fluid_icon.width * scale), int(fluid_icon.height * scale))
        fluid_icon = fluid_icon.resize(new_size, Image.LANCZOS)

        if icon_position == "top-left":
            base_icon.paste(fluid_icon, (0, 0), fluid_icon)
        elif icon_position == "bottom-right":
            base_icon.paste(fluid_icon, (base_icon.width - fluid_icon.width, base_icon.height - fluid_icon.height),
                            fluid_icon)

    return base_icon


# Example usage
if __name__ == "__main__":
    output_dir = "icons/barrel/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for fluid_name, barrel_fluid in fluids_for_barrels.items():

        # Generate barrel icon
        barrel_icon = generate_barrel_icons(barrel_fluid, STANDING_BARREL_LAYERS)
        barrel_icon_path = os.path.join(output_dir, f"{fluid_name}.png")
        barrel_icon.save(barrel_icon_path)
        print(f"Generated barrel icon for {fluid_name}: {barrel_icon_path}")


        # Generate filled barrel icon
        filled_barrel_icon = generate_barrel_icons(barrel_fluid, STANDING_BARREL_LAYERS, "top-left")
        filled_icon_path = os.path.join(output_dir, f"{fluid_name}_barrel_fill.png")
        filled_barrel_icon.save(filled_icon_path)
        print(f"Generated filled barrel icon for {fluid_name}: {filled_icon_path}")

        # Generate empty barrel icon
        empty_barrel_icon = generate_barrel_icons(barrel_fluid, EMPTY_BARREL_LAYERS, "bottom-right")
        empty_icon_path = os.path.join(output_dir, f"{fluid_name}_barrel_empty.png")
        empty_barrel_icon.save(empty_icon_path)
        print(f"Generated empty barrel icon for {fluid_name}: {empty_icon_path}")
