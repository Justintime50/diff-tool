"""Import modules"""
import difflib
import argparse

# Setup arguments
parser = argparse.ArgumentParser(
    description='Display a diff between two files in HTML.')
parser.add_argument(
    '-f1',
    '--file1',
    required=True,
    help='The base file to compare a second file to.'
)
parser.add_argument(
    '-f2',
    '--file2',
    required=True,
    help='The second file compared to the base first file.'
)
args = parser.parse_args()


def run():
    """Display a diff between two files in HTML."""
    diff = difflib.HtmlDiff()
    file_1 = open(args.file1).readlines()
    file_2 = open(args.file2).readlines()
    with open('diff.html', 'w') as output:
        output.write(diff.make_file(file_1, file_2, context=True, numlines=3))
    print('Diff generated as diff.html, open this file in a browser to see your diff.')


if __name__ == "__main__":
    run()
