# Factorio Icons Processing Repository

Welcome to the **Factorio Icons Repository**! This repository hosts scripts to extract and process the icons used in the [Factorio](https://www.factorio.com/) game and its [Space Age](https://www.factorio.com/blog/post/space-age-released) DLC.

**⚠️ Disclaimer:** *This repository is not affiliated with, endorsed by, or associated with Factorio developers in any way.*

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Scripts](#scripts)
    - [collect.py](#collectpy)
    - [create_barrels.py](#create_barrelspy)
    - [crop.py](#croppy)
    - [upscale.py](#upscalepy)
    - [combine.py](#combinepy)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features
- **Automated Icon Processing**: Leverage Python scripts to collect, create variations, crop, upscale, and combine icons effortlessly.
- **Customization**: Tailor icons to your project's specific needs with easy-to-use processing tools.

## Installation

1. **Clone the Repository**
2. **Navigate to the Project Directory**
3. **Install Dependencies**

Ensure you have Python installed. Install necessary Python packages using pip:
```bash
pip install -r requirements.txt
```

## Usage
This repository includes five Python scripts, each serving a specific purpose in managing and processing icons.

### Scripts

#### `collect.py`

**Description**:  
This script searches for PNG images within a specified directory and its subdirectories.
It copies images that match target sizes to a designated destination folder, ensuring no
filename conflicts by generating unique filenames when necessary.

---

#### `create_barrels.py`

**Description**:  
This script generates barrel icons for various fluids in a game or application using the Python Imaging
Library (PIL). It creates composite icons for filled and empty barrels based on fluid colors.

---

#### `crop.py`

**Description**:  
This module provides functionality to process PNG images by cropping them into specified parts based on their
dimensions. It is designed to handle images with specific width-to-height ratios, supporting both 2-part and
4-part cropping modes.

---

#### `upscale.py`

**Description**:  
This module provides functions to rescale images from a specified size to a target size.
It supports processing individual image files or entire folders containing images.

---

#### `combine.py`

**Description**:  
This script provides functionality to overlay multiple images with optional downscaling.
It uses the Python Imaging Library (PIL) to manipulate images and combine them into a single output.

---

## Contributing

Contributions are welcome! Whether it's improving the scripts, adding new icons, or enhancing documentation, your contributions help make this project better.

1. **Fork the Repository**
2. **Create a New Branch**
3. **Commit Your Changes**
4. **Push to the Branch**
5. **Open a Pull Request**

Please ensure your code follows the project's coding standards and that you've included appropriate tests.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the scripts as per the license terms.

## Acknowledgments

- [Factorio](https://www.factorio.com/) for the amazing game and icons.
- Open-source community contributors for their invaluable tools and resources.

---

*Happy Crafting!*
