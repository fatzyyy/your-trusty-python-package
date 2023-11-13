import argparse
from .search_endpoints import SearchEndpoints


def cli():
    parser = argparse.ArgumentParser("Package searcher")
    parser.add_argument(
        "-m",
        "--manager",
        choices=["npm", "pypi", "nuget", "crates"],
        type=str,
        required=True,
        help="package manager",
    )
    parser.add_argument(
        "-p",
        "--package",
        type=str,
        required=True,
        help="package name",
    )
    args = parser.parse_args()
    return args


def main():
    cli_args = cli()
    # List of available search endpoints
    endpoints = {
        "npm": {
            "func": SearchEndpoints.search_npm,
            "message": "running npm search",
        },
        "pypi": {
            "func": SearchEndpoints.search_pypi,
            "message": "running pypi search",
        },
        "nuget": {
            "func": SearchEndpoints.search_nuget,
            "message": "running nuget search",
        },
        "crates": {
            "func": SearchEndpoints.search_rust_crates,
            "message": "running rust crates search",
        },
    }

    print(f"{endpoints[cli_args.manager]['message']}")
    endpoints[cli_args.manager]["func"](cli_args.package)
    SearchEndpoints.search_other()

if __name__ == "__main__":
    main()
