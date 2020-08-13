import unittest
from unittest.mock import mock_open
from diff import diff_files


class TestDiff(unittest.TestCase):
    def test_open_file(self):
        """Open a file and check if the contents can be read
        """
        content = 'Hello'
        mock_open = unittest.mock.mock_open(read_data=content)
        with unittest.mock.patch('builtins.open', mock_open):
            result = diff_files.Diff.open_file('file1.txt')
        assert content in result

    def test_generating_diff(self):
        """Generate a diff.html file and check if the contents are the output
        of the generate_diff function
        """
        diff_file = 'test/files/diff.html'
        with unittest.mock.patch('builtins.open', mock_open()) as mocked_file:
            result = diff_files.Diff.generate_diff_file(
                'test/files/file1.txt',
                'test/files/file2.txt',
                diff_file,
            )

            mocked_file.assert_called_with(diff_file, 'w')
            mocked_file().write.assert_called_once_with(result)


if __name__ == '__main__':
    unittest.main()
