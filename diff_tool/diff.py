import argparse
import difflib


class Cli:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Display a diff between two files in HTML.',
        )
        parser.add_argument(
            '-f1',
            '--file1',
            required=True,
            help='The path to the base file to compare a second file to.',
        )
        parser.add_argument(
            '-f2',
            '--file2',
            required=True,
            help='The path to the second file compared to the base file.',
        )
        parser.add_argument(
            '-o',
            '--output',
            required=False,
            default='diff.html',
            help='The output to the output file including filename.',
        )
        parser.parse_args(namespace=self)

    def run(self):
        DiffTool.run(
            self.file1,
            self.file2,
            self.output,
        )


class DiffTool:
    @staticmethod
    def run(file1, file2, output='diff.html'):
        """Display a diff between two files in HTML."""
        file1_content = DiffTool._open_file(file1)
        file2_content = DiffTool._open_file(file2)
        diff = DiffTool.generate_diff(file1_content, file2_content)
        DiffTool._write_file(diff, output)
        print(f'Diff generated as {output}, open this file in a browser to see your diff.')

    @staticmethod
    def generate_diff(file1, file2):
        """Generate the content for the diff file"""
        generated_diff = difflib.HtmlDiff().make_file(
            file1,
            file2,
            context=True,
            numlines=3,
        )

        return generated_diff

    @staticmethod
    def _open_file(filename):
        with open(filename, 'r') as opened_file:
            content = opened_file.readlines()

        return content

    @staticmethod
    def _write_file(content, output='diff.html'):
        with open(output, 'w') as output_file:
            output_file.write(content)


def main():
    Cli().run()


if __name__ == '__main__':
    main()
