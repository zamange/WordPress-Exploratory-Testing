# WordPress Exploratory Testing

## Overview

This project involves exploratory testing of a WordPress site using Selenium WebDriver with Python. The objective is to automate the testing process for essential functionalities like user login and to document the findings and improvements.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing Script](#testing-script)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automated user login test for WordPress.
- Easy to modify for additional test cases (e.g., post creation, theme customization).
- Documentation of findings and suggestions for improvements.

## Requirements

- Python 3.x
- Selenium
- Google Chrome (and ChromeDriver compatible with your Chrome version)
- A running instance of a WordPress site

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/zamange/WordPress-Exploratory-Testing.git
   cd WordPress-Exploratory-Testing

2. **Set up a virtual environment**:
    '''python3 -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
'''

3. **INstall required packages**:
    '''pip install selenium'''

4. **Download ChromeDriver**:
    Ensure you download the ChromeDriver version that matches your installed Google Chrome version. Place it in a known location (e.g., /usr/local/bin/chromedriver).

## Usage
1. Update the Testing_script.py file with your WordPress username and password.
2. Run: python Automated_Tests/Testing_script.py

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. 


