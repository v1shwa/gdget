"""
gdget

Usage:
  gdget <google-drive-url>
  gdget -h | --help
  gdget --version

Options:
  -h --help                         Show this screen.
  --version                         Show current gdget version.

Examples:
  gdget <google-drive-url>

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/v1shwa/gdget
"""
from inspect import getmembers, isclass
import argparse
import sys
from . import __version__ as VERSION

def print_version():
  sys.stdout.write("GdGet %s\n" % VERSION)


def main():
    """Main CLI entrypoint."""
    from .GdGet import GdGet
    parser = argparse.ArgumentParser(description='Command line utility to easily download Google Drive public URLs.')
    parser.add_argument("--version","-v", action='store_true', help="Display the version of gdget", required=False)
    parser.add_argument("--quiet","-q", action='store_true', help="Turn off gdget's output", required=False)
    parser.add_argument('URL',help="Google drive URL or ID", nargs="?")
    parser.add_argument('--output-document','-O', help='Name of the output file',type=str, required=False)
    args = parser.parse_args()
    if args.version:
      print_version()
    else:
      gdget = GdGet(options=args)
      gdget.run()




