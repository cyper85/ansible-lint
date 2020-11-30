#!/usr/bin/env python3
"""Dumps a YAML file with all platform names and releases reported by galaxy."""
import json
import pprint
import sys
import urllib.request
from typing import Dict, Generator, List


def each_platform(base="https://galaxy.ansible.com", page="/api/v1/platforms/") -> Generator:
    """Return galaxy platforms."""
    url = base + page
    json_string = urllib.request.urlopen(url).read()
    data = json.loads(json_string)
    for platform in data['results']:
        yield platform
    if "next_link" in data and data["next_link"]:
        for platform in each_platform(base=base, page=data['next_link']):
            yield platform


def main() -> int:
    """Rewrites list of ansible galaxy platforms."""
    platforms: Dict[str, List[str]] = {}
    for platform in each_platform():
        name = platform['name']
        release = platform['release']
        if name in platforms:
            platforms[name].append(release)
        else:
            platforms[name] = [release]

    new = """# Generated by dump-platforms
PLATFORMS = """
    pp = pprint.PrettyPrinter(indent=4, width=79, compact=True)
    new += pp.pformat(platforms)
    new += "\n"
    # for platform, releases in platforms.items():
    #     new += platforms
    #     f"{platform}: {releases}\n"
    filename = "lib/ansiblelint/_galaxy.py"
    old = open(filename).read()
    if old != new:
        print("Galaxy platform list was changed, include it in commit.")
        open(filename, "w").write(new)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
