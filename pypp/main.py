import argparse
import ast


class PyppVisitor(ast.NodeVisitor):
    pass

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    return parser.parse_args()


def main():
    args = parse_args()
    with open(args.source, 'r') as f:
        PyppVisitor().visit(ast.parse(f.read()))
