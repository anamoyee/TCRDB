import pathlib as p
import re as regex

from setup import PACKAGE_NAME

version_file = p.Path(f'./{PACKAGE_NAME}/version.py')

def main() -> str:
  version_pattern = r"__version__\s*=\s*[\"'](.*?)[\"']"

  version_parts = regex.search(version_pattern, version_file.read_text()).group(1).split('.')
  version_parts = [int(x) for x in version_parts]
  version_parts[-1] += 1
  version_parts = [str(x) for x in version_parts]


  version_after_bump = '.'.join(version_parts)

  version_file.write_text(f"__version__ = '{version_after_bump}'\n")

  return version_after_bump

if __name__ == '__main__':
  main()
