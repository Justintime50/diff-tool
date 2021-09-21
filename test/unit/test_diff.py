import io
from unittest.mock import mock_open, patch

from diff_tool import DiffTool


@patch('diff_tool.diff.DiffTool._open_file')
@patch('diff_tool.diff.DiffTool._write_file')
def test_diff_run(mock_write, mock_open):
    DiffTool.run('setup.py', 'README.md', 'output.html')

    assert mock_open.call_count == 2
    mock_write.assert_called_once()


def test_generate_diff():
    """Here we create mocked files in memory and generate a diff
    with their separate file content.
    """
    file1 = io.StringIO()
    file2 = io.StringIO()

    file1.write('Hello')
    file2.write('Hello World')

    result = DiffTool.generate_diff(
        file1,
        file2,
    )

    assert '<!DOCTYPE html' in result


def test_open_file():
    content = DiffTool._open_file('README.md')

    assert '# Diff Tool\n' in content


def test_write_file():
    with patch('builtins.open', mock_open()) as mocked_file:
        DiffTool._write_file('file_content', 'test.txt')

        mocked_file.assert_called_with('test.txt', 'w')
