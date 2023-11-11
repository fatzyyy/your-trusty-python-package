# Network Utilities Package

## Disclaimer

- This is an intentionally vulnerable package. Its purpose is to demonstrate certain techniques of supply-chain attackes in Python.
- Do not use this package for production need.
- Use for educational purposes only.
- The author and his employer are not responsible for any damage of any nature caused by incorrect usage of this package and its code.

## Description

This Python package provides a collection of network utilities, including a feature to automatically determine the public IP assigned by your internet service provider and export its details. It's designed to be easy to use for both beginners and experienced developers needing to perform common network operations.
Installation

To install this package, run the following command:

```bash
pip install your-package-name
```

## Features

    Public IP Detection: Automatically detect the public IP address assigned by your ISP.
    Export IP Details: Export the detected IP address details, such as location, ISP, and more.
    [List other features here]

## Usage

### Getting Your Public IP

To export details of your public IP:

```python
from nettools.utils.NetUtils import pip_info
from json import dumps

pip_details = pip_info()
print(dumps(pip_details, indent=4))
```

## License

This project is licensed under the MIT - see the LICENSE file for details.

## Contact

For any queries or feedback, please contact us at fatzy@protonmail.com.
