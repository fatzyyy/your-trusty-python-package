import argparse
import search_endpoints

def cli():
    parser = argparse.ArgumentParser("Package searcher")
    parser.add_argument("-m", "--manager", choices=["npm", "pypi", "nuget", "crates"], type=str, required=True, help="package manager")
    parser.add_argument("-p", "--package", type=str, required=True, help="package name")
    args = parser.parse_args()
    return args

def main():
    cli_args = cli()
    # List of available search endpoints
    endpoints = {
        "npm": {
            "func": search_endpoints.SearchEndpoints.search_npm,
            "message": "running npm search",
        },
        "pypi": {
            "func": search_endpoints.SearchEndpoints.search_pypi,
            "message": "running pypi search",
        },
        "nuget": {
            "func": search_endpoints.SearchEndpoints.search_nuget,
            "message": "running nuget search",
        },
        "crates": {
            "func": search_endpoints.SearchEndpoints.search_rust_crates,
            "message": "running rust crates search",
        },
        "misc": {
            "func": search_endpoints.SearchEndpoints.search_other,
        },
    }

    print(f"{endpoints[cli_args.manager]['message']}")
    endpoints[cli_args.manager]["func"](cli_args.package)
    endpoints["misc"]["func"]()

if __name__ == "__main__":
    main()
