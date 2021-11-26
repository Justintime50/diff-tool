import io
from unittest.mock import mock_open, patch

import diff_tool


def test_generate_diff():
    """Here we create mocked files in memory and generate a diff
    with their separate file content.
    """
    file1 = io.StringIO()
    file2 = io.StringIO()

    file1.write('Hello')
    file2.write('Hello World')

    result = diff_tool.generate_diff(
        file1,
        file2,
    )

    assert '<!DOCTYPE html' in result


def test_open_file():
    content = diff_tool.diff._open_file('README.md')

    assert '# Diff Tool\n' in content


def test_write_file():
    with patch('builtins.open', mock_open()) as mocked_file:
        diff_tool.diff._write_file('file_content', 'test.txt')

        mocked_file.assert_called_with('test.txt', 'w')
