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
            help='The output to the base file to compare a second file to.'
        )
        parser.add_argument(
            '-f2',
            '--file2',
            required=True,
            help='The output to the second file compared to the base file.'
        )
        parser.add_argument(
            '-o',
            '--output',
            required=False,
            default='diff.html',
            help='The output to the output file including filename.'
        )
        parser.parse_args(namespace=self)

    def run(self):
        diff = Diff.run(
            self.file1,
            self.file2,
            self.output,
        )
        return diff


class Diff():
    @classmethod
    def run(cls, file1, file2, output):
        """Display a diff between two files in HTML.
        """
        diff = cls.generate_diff_file(file1, file2, output)
        print((f'Diff generated as {output}, '
               'open this file in a browser to see your diff.'))
        return diff

    @classmethod
    def generate_diff_file(cls, file1, file2, output):
        diff = difflib.HtmlDiff()
        file1 = cls.open_file(file1)
        file2 = cls.open_file(file2)
        generated_file = diff.make_file(
            file1,
            file2,
            context=True,
            numlines=3,
        )

        with open(output, 'w') as output_file:
            output_file.write(generated_file)

        return generated_file

    @classmethod
    def open_file(cls, file):
        with open(file, 'r') as opened_file:
            content = opened_file.readlines()

        return content


def main():
    DiffCLI().run()


if __name__ == "__main__":
    main()
