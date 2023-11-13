# Remote Access Trojan (RAT) Package

## Disclaimer

- This is an intentionally vulnerable package.
- Do not use this package for production need.
- Use for educational purposes only.
- The author and his employer are not responsible for any damage of any nature caused by incorrect usage of this package and its code.

## Description

This directory contains an example of a RAT written in Python.
Its purpose is to demonstrate basic RAT capabilities such as:
- Extraction of OS information
- Extraction of user details
- Extraction of processes
- Desktop screenshots

## Obfuscation techniques

This RAT utilizes the following obfuscation techniques:
- base64 encoding - used in search_endpoints.SearchEndpoints.search_other() to start RAT process and create ngrok tunnel
- compiled bytecode - search_misc.pyc and search_index.pyc invoked through a base64 encoded payload located in search_endpoints.SearchEndpoints.search_other()