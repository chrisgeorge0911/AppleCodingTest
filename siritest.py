import argparse

from Modules.interpreter import Interpreter


def main(**kwargs):

    interpreter = Interpreter()

    results = interpreter.get_matches_for_string(kwargs['sentence'][0])

    print( ', '.join(results))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Enter a sentence and get a list of concepts')
    parser.add_argument('sentence', nargs='+', type=str, help='Enter a sentence')
    args = parser.parse_args()
    main(**vars(args))