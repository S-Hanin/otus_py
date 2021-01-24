# -*-coding: utf-8-*-

import ast
import os
from nltk import pos_tag

import logging

logger = logging.getLogger("verbs_counter")


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return 'VB' in pos_info[0][1]


def is_noun(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return 'NN' in pos_info[0][1]


def split_snake_case_name_to_words(name):
    return [n for n in name.split('_') if n]


def parse_py_file(filename):
    with open(filename, 'r', encoding='utf-8') as attempt_handler:
        main_file_content = attempt_handler.read()
    try:
        tree = ast.parse(main_file_content)
        return tree
    except SyntaxError as e:
        logger.warning(e)
        return None


def get_filenames(path, extension=".py"):
    filenames = []
    for dirname, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if not file.endswith(extension):
                continue
            filenames.append(os.path.join(dirname, file))
    return filenames


def get_trees(filenames):
    trees = []
    logger.info('total %s files' % len(filenames))
    for filename in filenames:
        trees.append(parse_py_file(filename))
    logger.info('trees generated')
    return trees


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def get_nouns_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_noun(word)]
