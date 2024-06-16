import argparse
from argparse import Namespace

import requests


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


def main():
    package_name = "diffusers"
    versions = get_pypi_versions(package_name)
    versions.sort()
    for version in versions:
        print(version)
