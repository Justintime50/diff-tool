import argparse

import diff_tool


class DiffToolCli:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Display a diff between two files in HTML.',
        )
        parser.add_argument(
            '-f1',
            '--file1',
            required=True,
            type=str,
            help='The path to the base file to compare a second file to.',
        )
        parser.add_argument(
            '-f2',
            '--file2',
            required=True,
            type=str,
            help='The path to the second file compared to the base file.',
        )
        parser.add_argument(
            '-o',
            '--output',
            required=False,
            type=str,
            default='diff.html',
            help='The path/name to the output file where the diff will be stored.',
        )
        parser.parse_args(namespace=self)

    def run(self):
        """Display a diff between two files in HTML when used via CLI."""
        file1_content = diff_tool.diff._open_file(self.file1)
        file2_content = diff_tool.diff._open_file(self.file2)
        diff = diff_tool.generate_diff(file1_content, file2_content)
        diff_tool.diff._write_file(diff, self.output)

        print(f'Diff generated as {self.output}, open this file in a browser to see your diff.')


def main():
    DiffToolCli().run()


if __name__ == '__main__':
    main()
