#!/usr/local/bin/python3

import sys

for line in sys.stdin:
    print(f'>>{line}', file=sys.stderr)
exit(0)


