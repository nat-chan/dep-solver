import argparse
from argparse import Namespace

import requests
from packaging.version import Version


def get_pypi_versions(package_name: str):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        versions = data["releases"].keys()
        return sorted(versions, reverse=True)
    else:
        print(f"Failed to fetch data for package: {package_name}")
        return []


def sort_versions(versions):
    return sorted(versions, key=Version)


def main(args: Namespace):
    versions = get_pypi_versions(args.package)
    versions.sort(key=Version)
    for version in versions:
        print(version)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", type=str, help="パッケージ名", default="diffusers")
    args = parser.parse_args()
    main(args)
