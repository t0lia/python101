#!/usr/local/bin/python3

import sys

print("\n".join(sys.argv))
if len(sys.argv) > 2:
    print('err')
    exit(1)
print('ok')


exit(0)

#for line in sys.stdin:
#    print(f'>>{line}')
