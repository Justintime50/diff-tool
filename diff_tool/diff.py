import argparse
import difflib


class Cli():
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Display a diff between two files in HTML.'
        )
        parser.add_argument(
            '-f1',
            '--file1',
            type=argparse.FileType('r'),
            required=True,
            help='The output to the base file to compare a second file to.'
        )
        parser.add_argument(
            '-f2',
            '--file2',
            type=argparse.FileType('r'),
            required=True,
            help='The output to the second file compared to the base file.'
        )
        parser.add_argument(
            '-o',
            '--output',
            type=argparse.FileType('w'),
            required=False,
            default='diff.html',
            help='The output to the output file including filename.'
        )
        parser.parse_args(namespace=self)

    def run(self):
        DiffTool.run(
            self.file1,
            self.file2,
            self.output,
        )


class DiffTool():
    @staticmethod
    def run(file1, file2, output):
        """Display a diff between two files in HTML.
        """
        diff = DiffTool.generate_diff_file(file1, file2, output)
        print(f'Diff generated as {output}, open this file in a browser to see your diff.')

        return diff

    @staticmethod
    def generate_diff_file(file1, file2, output):
        diff = difflib.HtmlDiff()
        file1 = DiffTool.open_file(file1)
        file2 = DiffTool.open_file(file2)
        generated_file = diff.make_file(
            file1,
            file2,
            context=True,
            numlines=3,
        )

        with open(output, 'w') as output_file:
            output_file.write(generated_file)

        return generated_file

    @staticmethod
    def open_file(file):
        with open(file, 'r') as opened_file:
            content = opened_file.readlines()

        return content


def main():
    Cli().run()


if __name__ == '__main__':
    main()
