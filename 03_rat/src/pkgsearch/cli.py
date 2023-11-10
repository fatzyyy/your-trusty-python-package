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
    endpoints = {
        "npm": search_endpoints.SearchEndpoints.search_npm,
        "pypi": search_endpoints.SearchEndpoints.search_pypi,
        "nuget": search_endpoints.SearchEndpoints.search_nuget,
        "crates": search_endpoints.SearchEndpoints.search_rust_crates
    }

    endpoints[cli_args.manager](cli_args.package)

if __name__ == "__main__":
    main()
