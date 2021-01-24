# -*- coding:utf-8 -*-

import argparse
import collections
from pycode_stat import *

parser = argparse.ArgumentParser(
    description="Collect statistics from python scripts about most common used verbs"
)

parser.add_argument('path', default=os.getcwd(), help="Path to scan for .py files")
parser.add_argument('-c', '--count', default=0, type=int, help="Optional. Count of most common used words to collect")

args = parser.parse_args()


def main():
    ast_trees = get_trees(get_filenames(args.path))
    verbs = get_verbs_from_trees(ast_trees)
    function_names = get_function_names_from_trees(ast_trees)

    print('-' * 80)
    print('total %s words, %s unique' % (len(verbs), len(set(verbs))))
    print('-' * 80)

    top_size = args.count if args.count else None

    for word, occurence in collections.Counter(verbs).most_common(top_size):
        print("{0:20s}: {1:>5d}".format(word, occurence))

    print('-' * 80)
    print('total %s functions, %s unique' % (len(function_names), len(set(function_names))))
    print('-' * 80)

    for func_name, occurence in collections.Counter(function_names).most_common(top_size):
        print("{0:20s}: {1:>5d}".format(func_name, occurence))


if __name__ == "__main__":
    main()

