import difflib
from typing import List, Optional


def generate_diff(file1_path: str, file2_path: str) -> str:
    """Generate the content for the diff file."""
    generated_diff = difflib.HtmlDiff().make_file(
        file1_path,
        file2_path,
        context=True,
        numlines=3,
    )

    return generated_diff


def _open_file(filename: str) -> List:
    with open(filename, 'r') as opened_file:
        content = opened_file.readlines()

    return content


def _write_file(content: str, output: Optional[str] = 'diff.html'):
    with open(output, 'w') as output_file:
        output_file.write(content)
