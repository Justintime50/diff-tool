import unittest
import os
from diff import diff_files


class TestDiff(unittest.TestCase):
    def test_opening_file1(self):
        file1 = diff_files.Diff.open_file1('test/files/file1.txt')
        assert 'Hello' in str(file1)

    def test_opening_file2(self):
        file2 = diff_files.Diff.open_file2('test/files/file2.txt')
        assert 'Hola' in str(file2)

    def test_generating_diff(self):
        diff_files.Diff.run(
            'test/files/file1.txt',
            'test/files/file2.txt',
            'test/files/diff.html',
        )
        assert os.path.exists('test/files/diff.html')


if __name__ == '__main__':
    unittest.main()
