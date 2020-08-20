import mock
import pytest
import argparse
from diff import diff_files


@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                file1='file1.txt',
                file2='file2.txt',
                output='output.html',
                )
            )
def test_cli(mock_args):
    diff_files.DiffCLI()


@pytest.mark.skip('Skipping this test until we can mock "self" in argparse.')
def test_cli_run():
    raise Exception('TODO: finish this test')


def test_diff_run():
    diff_file = 'test/files/diff.html'
    with mock.patch('builtins.open', mock.mock_open()):
        result = diff_files.Diff.run(
            'test/files/file1.txt',
            'test/files/file2.txt',
            diff_file,
        )
    assert '<!DOCTYPE html' in result


def test_open_file():
    """Open a file and check if the contents can be read
    """
    content = 'Hello'
    mock_open = mock.mock_open(read_data=content)
    with mock.patch('builtins.open', mock_open):
        result = diff_files.Diff.open_file('file1.txt')
    assert content in result


def test_generating_diff():
    """Generate a diff.html file and check if the contents are the output
    of the generate_diff function
    """
    diff_file = 'test/files/diff.html'
    with mock.patch('builtins.open', mock.mock_open()) as mocked_file:
        result = diff_files.Diff.generate_diff_file(
            'test/files/file1.txt',
            'test/files/file2.txt',
            diff_file,
        )
        mocked_file.assert_called_with(diff_file, 'w')
        mocked_file().write.assert_called_once_with(result)
