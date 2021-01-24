# -*- coding:utf-8 -*-

import argparse
import collections

from git import GitError

from pycode_stat import *
from report import make_report
from vcs import clone_repository

parser = argparse.ArgumentParser(
    description="Collect statistics from python scripts about most common used verbs"
)

parser.add_argument('path', default=os.getcwd(), help="Path to scan for .py files")
parser.add_argument('-c', '--count', default=0, type=int, help="Count of most common used words to collect")
parser.add_argument('-w', '--words', default='verbs', help="Find verbs or nouns. Default: verbs")
parser.add_argument('-f', '--format', default="console", help="Output format. Variants: console(default), json, csv")
parser.add_argument("-r", "--report-file")
parser.add_argument("--vcs", help="Clone repository from version control system. 'path' will be used as target dir")

args = parser.parse_args()


def main():
    if args.vcs:
        try:
            clone_repository(args.vcs, args.path)
        except GitError as err:
            logger.critical(err)
            exit(1)
    ast_trees = get_trees(get_filenames(args.path))

    if args.words == "verbs":
        words = get_verbs_from_trees(ast_trees)
    else:
        words = get_nouns_from_trees(ast_trees)

    print('-' * 80)
    print('total %s words, %s unique' % (len(words), len(set(words))))
    print('-' * 80)

    top_size = args.count if args.count else None

    make_report(args.format, args.report_file, collections.Counter(words).most_common(top_size))


if __name__ == "__main__":
    main()

