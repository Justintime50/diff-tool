import mock
from diff_tool import DiffTool


def test_diff_run():
    with mock.patch('builtins.open', mock.mock_open()):
        result = DiffTool.run(
            'file1.txt',
            'file2.txt',
            'output.html'
        )
    assert '<!DOCTYPE html' in result


def test_open_file():
    """Open a file and check if the contents can be read
    """
    content = 'Hello'
    mock_open = mock.mock_open(read_data=content)
    with mock.patch('builtins.open', mock_open):
        result = DiffTool.open_file('file1.txt')
    assert content in result


def test_generating_diff():
    """Generate a diff.html file and check if the contents are the output
    of the generate_diff function
    """
    diff_file = 'test/files/diff.html'
    with mock.patch('builtins.open', mock.mock_open()) as mocked_file:
        result = DiffTool.generate_diff_file(
            'test/files/file1.txt',
            'test/files/file2.txt',
            diff_file,
        )
        mocked_file.assert_called_with(diff_file, 'w')
        mocked_file().write.assert_called_once_with(result)
