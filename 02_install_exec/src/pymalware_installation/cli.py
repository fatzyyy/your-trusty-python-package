import argparse
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
    return args


def main():
    cli_args = cli()
    pip = cli_args.pip

    if pip:
        utils.NetUtils.pip_info()


if __name__ == "__main__":
    main()
