#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        sys.stdout.write('Weird\n')
    else:
        if 2 <= n <= 5:
            sys.stdout.write('Not Weird\n')
        elif 6 <= n <= 20:
            sys.stdout.write('Weird\n')
        else:
            sys.stdout.write('Not Weird\n')
