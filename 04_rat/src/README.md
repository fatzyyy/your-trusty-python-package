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

## Bypassing NAT/Firewall

This RAT example spins-up a flask instance on a victim's machine and creates an ngrok tunnel to pass traffic to the attacker.
These two entities are running in a separate processes in the OS. To stop the RAT you should find the main process and kill it:

```bash
ps aux | grep 'search_mic'
kill <PID>
```

Once the parent process is killed the ngrok tunnel will be automatically shutdown.

## How to?

### Build

Assuming you are in the root of this repository change directory:

```bash
cd 04_rat/src
python3 -m build
```

### Install

```bash
pip3 install dist dist/<package-name>.tar.gz
```

### Execute

- In a separate terminal session start [receiver.py](/00_misc/receiver.py)

```bash
./receiver.py
```

- Assuming you have built and installed this package, in another terminal session run the following command

```
pkgsearch -m <choose manager> -p <specicy package name>
```

If all steps were correctly completed in the first terminal you will see an instance of flask, followed by
two POST messages received, where one of the will contain an ngrok url that you can use to access the RAT.
