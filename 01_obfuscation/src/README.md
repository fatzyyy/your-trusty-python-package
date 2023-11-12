# PyMalware Obfuscation Techniques Package

## Disclaimer

- This is an intentionally vulnerable package.
- Do not use this package for production need.
- Use for educational purposes only.
- The author and his employer are not responsible for any damage of any nature caused by incorrect usage of this package and its code.

## Description

This Python package provides a collection of obfuscation techniques for Python-based malware.

To install this package, run the following command:

```bash
pip install malware-obfuscation
```

## Features

- ObfuscationTechniques.base64_payload(): reverse base64 string payload example
- ObfuscationTechniques.unicode_payload(): reverse unicode chars list payload example
- ObfuscationTechniques.base64_unicode_combined_payload(): reverse base64 + reverse unicode chars list payload example
- ObfuscationTechniques.encryption_payload(): encrypted payload example
- ObfuscationTechniques.bytecode_payload(): compiled bytecode payload example
- ObfuscationTechniques.embedded_binary(): embedded go lang binary payload example

## Usage

### base64_payload

```python
from pymalware-obfuscation import base64_payload
base64_payload()
```

### unicode_payload

```python
from pymalware-obfuscation import unicode_payload
unicode_payload()
```

### base64_unicode_combined_payload

```python
from pymalware-obfuscation import base64_unicode_combined_payload
base64_unicode_combined_payload()
```

### encryption_payload

The docstring of this method contains encryption key used to encrypt the payload string.
Place this key to pastebin and supply method with a pastebin raw ulr.

```python
from pymalware-obfuscation import encryption_payload
encryption_payload("https://pastebin.com/raw/<url>")
```

### bytecode_payload

```python
from pymalware-obfuscation import compiled
compiled.payload()
```

### embedded_binary
```python
from pymalware-obfuscation import embedded_binary
embedded_binary()
```

## License

This project is licensed under the MIT - see the LICENSE file for details.

## Contact

For any queries or feedback, please contact us at fatzy@protonmail.com.
