import sys


def interpreter_version():
  return '.'.join(map(str, sys.version_info))


def main():
  print('Running under python {}'.format(interpreter_version()))
