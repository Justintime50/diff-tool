import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

DEV_REQUIREMENTS = [
    'coveralls == 3.*',
    'flake8',
    'pytest == 6.*',
    'pytest-cov == 2.*',
]

setuptools.setup(
    name='diff-tool',
    version='2.3.0',
    description='Display a diff between two files in HTML.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/diff-tool',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    entry_points={
        'console_scripts': [
            'diff-tool=diff_tool.diff:main',
        ],
    },
    python_requires='>=3.7',
)
