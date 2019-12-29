"""Gdget packaging settings."""

import codecs
from subprocess import call
from setuptools import Command, find_packages, setup
from gdget import __version__


class RunTests(Command):
    """Run all tests."""

    description = "run tests"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(["py.test", "--cov=skele", "--cov-report=term-missing"])
        raise SystemExit(errno)


setup(
    name="gdget",
    version=__version__,
    description="Google drive URLs downloader for command line.",
    long_description=codecs.open("./README.rst").read(),
    url="https://github.com/v1shwa/gdget",
    author="Vishwa",
    author_email="v1shwa@yahoo.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="googledrive cli google download",
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=["requests", "tqdm"],
    python_requires=">=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",
    extras_require={"test": ["pytest"]},
    entry_points={"console_scripts": ["gdget=gdget.cli:main"]},
    cmdclass={"test": RunTests},
)
