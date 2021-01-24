# -*- coding: utf-8 -*-
from common import *

logging.basicConfig(level=logging.WARNING)


def get_function_names_from_trees(trees):
    names = [f for f in
             flat([[node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)] for t in trees if t])
             if not (f.startswith('__') and f.endswith('__'))]
    return names


def get_verbs_from_trees(trees):
    fncs = get_function_names_from_trees(trees)
    verbs = flat([get_verbs_from_function_name(function_name) for function_name in fncs])
    return verbs


def get_nouns_from_trees(trees):
    fncs = get_function_names_from_trees(trees)
    verbs = flat([get_nouns_from_function_name(function_name) for function_name in fncs])
    return verbs
