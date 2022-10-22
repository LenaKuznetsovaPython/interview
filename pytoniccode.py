import os
import re
import argparse
from dataclasses import dataclass

import colorama


@dataclass
class TreePrintConfig:
    indent: int
    include: str
    exclude: str
    all: bool
    full_name: bool
    folders_only: bool


class PathInfo:
    def __init__(self, path, name):
        self.name = name
        self.path = os.path.join(path, name)
        self.is_hidden = bool(re.search(r'^\.[^/]', name))
        self.is_file = os.path.isfile(self.path)
        self.is_folder = os.path.isdir(self.path)
        self.files = []
        self.folders = []

        if self.is_folder:
            for name in os.listdir(self.path):
                info = PathInfo(self.path, name)
                if info.is_file:
                    self.files.append(info)
                elif info.is_folder:
                    self.folders.append(info)


def print_tree(conf: TreePrintConfig, root: str):
    _print_tree(conf, PathInfo('', root), 0)


def _print_tree(conf: TreePrintConfig, root: PathInfo, nested: int):
    if root.is_file:
        if conf.include and conf.include not in root.name:
            return
        if conf.exclude and conf.exclude in root.name:
            return
    if not conf.all and root.is_hidden:
        return

    with colorama.colorama_text():
        indent = '    ' * nested
        color = colorama.Fore.BLUE if root.is_file else ''
        path = root.path if conf.full_name else root.name

        print(f'{color}{indent}{path}')

    for node in root.folders:
        _print_tree(conf, node, nested + 1)
    for node in root.files:
        _print_tree(conf, node, nested + 1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tree')
    parser.add_argument('path', )
    parser.add_argument('-fo', '--folders_only', action='store_true', help='Show folders only')
    parser.add_argument('-i', '--include', help='Include files')
    parser.add_argument('-e', '--exclude', help='Exclude files')
    parser.add_argument('-a', '--all', action='store_true', help='Show hidden files')
    parser.add_argument('-f', '--full_name', action='store_true', )
    args = parser.parse_args()

    colorama.init()

    print_tree(
        TreePrintConfig(
            indent=4,
            include=args.include,
            exclude=args.exclude,
            all=args.all,
            full_name=args.full_name,
            folders_only=args.folders_only
        ),
        args.path
    )
