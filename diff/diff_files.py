import argparse
import difflib


class DiffCLI():
    def __init__(self):
        """Initialize CLI args
        """
        parser = argparse.ArgumentParser(
            description='Display a diff between two files in HTML.'
        )
        parser.add_argument(
            '-f1',
            '--file1',
            required=True,
            help='The path to the base file to compare a second file to.'
        )
        parser.add_argument(
            '-f2',
            '--file2',
            required=True,
            help='The path to the second file compared to the base file.'
        )
        parser.add_argument(
            '-o',
            '--output',
            required=False,
            help='The path to the output file including filename.'
        )
        parser.parse_args(namespace=self)

    def run(self):
        Diff.run(
            self.file1,
            self.file2,
        )


class Diff():
    @classmethod
    def run(self, file1, file2, path='diff.html'):
        """Display a diff between two files in HTML.
        """

        diff = difflib.HtmlDiff()
        file1 = self.open_file1(file1)
        file2 = self.open_file2(file2)
        with open(path, 'w') as output:
            output.write(diff.make_file(
                file1, file2, context=True, numlines=3))
        print((f'Diff generated as {path}, '
               'open this file in a browser to see your diff.'))

    @staticmethod
    def open_file1(file1):
        with open(file1, 'r') as file:
            content = file.readlines()
        return content

    @staticmethod
    def open_file2(file2):
        with open(file2, 'r') as file:
            content = file.readlines()
        return content


if __name__ == "__main__":
    DiffCLI().run()
