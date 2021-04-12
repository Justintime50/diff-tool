import mock
from diff_tool import DiffTool


@mock.patch('diff_tool.diff.DiffTool._open_file')
@mock.patch('diff_tool.diff.DiffTool._write_file')
def test_diff_run(mock_write, mock_open):
    DiffTool.run(
        'setup.py',
        'README.md',
        'output.html'
    )
    assert mock_open.call_count == 2
    mock_write.assert_called_once()


def test_generate_diff():
    result = DiffTool.generate_diff(
        'test/files/file1.txt',
        'test/files/file2.txt',
    )

    assert '<!DOCTYPE html' in result


def test_open_file():
    content = DiffTool._open_file('README.md')

    assert '# Diff Tool\n' in content


def test_write_file():
    with mock.patch('builtins.open', mock.mock_open()) as mocked_file:
        DiffTool._write_file('file_content', 'test.txt')

        mocked_file.assert_called_with('test.txt', 'w')
