"""Tests for our gdget CLI module."""


from subprocess import PIPE, Popen as popen
import unittest
import warnings
from gdget import __version__ as VERSION


class TestHelp(unittest.TestCase):
    def setUp(self):
        try:
            warnings.simplefilter("ignore", ResourceWarning)
        except NameError:
            pass

    def test_help_flag(self):
        output = popen(["gdget", "-h"], stdout=PIPE).communicate()[0]
        self.assertTrue("Google Drive" in str(output))

        output = popen(["gdget", "--help"], stdout=PIPE).communicate()[0]
        self.assertTrue("Google Drive" in str(output))


class TestVersion(unittest.TestCase):
    def setUp(self):
        try:
            warnings.simplefilter("ignore", ResourceWarning)
        except NameError:
            pass

    def test_version_flag(self):
        output = popen(["gdget", "--version"], stdout=PIPE).communicate()[0]
        self.assertTrue(VERSION in str(output))


if __name__ == "__main__":
    unittest.main()
