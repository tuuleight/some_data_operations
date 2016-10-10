"""
Simple script with python generators to read text from file and get correct
integers within the range [-1000000000, 1000000000]. File name is parsed from
commandline. Try test_intcatcher.
"""

import argparse


def read_text(file_object):
    text = open(file_object).read()
    yield from text.split('\\n')


def convert_text(file_object):
    for item in read_text(file_object):
        try:
            if -1000000000 <= int(item) <= 1000000000:
                yield int(item)
        except ValueError or SyntaxError:
            pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_object')
    args = parser.parse_args()
    for i in convert_text(args.file_object):
        print(i)

if __name__ == '__main__':
    main()
