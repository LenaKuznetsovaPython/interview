"""
badcode.py problems:

1) dir is Built-in Function.
dir = os.listdir(path)
2) This code works only in Windows
path + '\\' + dir[i]
3) Unclear conditionals.
4) Misleading CLI interface.
5) Duplicate code.
6) Module should not run code if we import it.
7) Variables can be undefined
if args.include:
    itext = args.include
if args.exclude:
    etext = args.exclude
8) Extra code
for i in range(len(dir)):
...
dir[i]
"""
import os
import argparse


def print_file_path(path, name, n):
    if args.include and args.include not in name:
        return
    if args.exclude and args.exclude in name:
        return
    if args.full_name:
        print(n * ' ', path)
    else:
        print(n * ' ', name)


def print_directory_path(path, name, n):
    if args.full_name:
        print(n * ' ', path)
    else:
        print(n * ' ', name)


def print_tree(root, n):
    for name in os.listdir(root):
        path = os.path.join(root, name)
        if not args.all and name.startswith('.'):
            continue

        if os.path.isfile(os.path.join(root, name)):
            if not args.folders_only:
                print_file_path(path, name, n)

        if os.path.isdir(path):
            print_directory_path(path, name, n)
            n += 4
            print_tree(path, n)
            n -= 4


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tree')
    parser.add_argument('path', )
    parser.add_argument('-fo', '--folders_only', action='store_true', help='Show folders only')
    parser.add_argument('-i', '--include', help='Include files')
    parser.add_argument('-e', '--exclude', help='Exclude files')
    parser.add_argument('-a', '--all', action='store_true', help='Show hidden files')
    parser.add_argument('-f', '--full_name', action='store_true', )
    args = parser.parse_args()

    print(args.path)
    print_tree(args.path, 4)
