#!/usr/bin/env python3

"""Object Practice stuff

Usage:

    python exceptional.py <string>
"""

import sys


def convert(s):
    """Convert to an integer."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {} "
              .format(str(e)), file=sys.stderr)
        raise


if __name__ == '__main__':
    # argv[0] is name of the file so we'll use the first one

    if len(sys.argv) > 1:
        print(convert(sys.argv[1]))
    else:
        print(convert([22, 2]))
