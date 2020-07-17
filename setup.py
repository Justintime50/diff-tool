import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'argparse >= 1.4.0',
]

setuptools.setup(
    name='diff-tool',
    version='1.0.0',
    description='Display a diff between two files in HTML.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/diff',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'pylint >= 2.5.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'diff-tool=diff.diff_files:run'
        ]
    },
    python_requires='>=3.6',
)
