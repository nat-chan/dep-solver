import re
from collections import defaultdict


def parse_requirements(requirements):
    version_dict = defaultdict(list)
    pattern = re.compile(r"([a-zA-Z0-9_-]+)([<>=!]+[0-9a-zA-Z.]+)")

    for req in requirements:
        matches = pattern.findall(req)
        for match in matches:
            package, version = match
            version_dict[package].append(version)

    return version_dict


def consolidate_versions(version_list):
    if not version_list:
        return ""

    version_set = sorted(set(version_list), key=lambda x: re.sub(r"([<>=!]+)", "", x))
    return ",".join(version_set)


def consolidate_requirements(requirements):
    version_dict = parse_requirements(requirements)
    consolidated = []

    for package, versions in version_dict.items():
        consolidated.append(f"{package}{consolidate_versions(versions)}")

    return consolidated


if __name__ == "__main__":
    requirements = [
        "pip",
        "diffusers<0.29.0",
        "diffusers>=0.25.0",
        # 他の必要な依存関係をここに追加
    ]

    consolidated = consolidate_requirements(requirements)
    for req in consolidated:
        print(req)
