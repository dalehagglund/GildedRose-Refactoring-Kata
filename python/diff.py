import sys
from difflib import unified_diff

def readlines(filename):
    with open(filename) as f:
        return f.readlines()

def diff(old, new):
    old_lines = readlines(old)
    new_lines = readlines(new)
    return unified_diff(
        old_lines, new_lines,
        fromfile=old, tofile=new,
    )

def main():
    args = sys.argv[1:]
    for line in diff(args[0], args[1]):
        print(line, end='')

main()