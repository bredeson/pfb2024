#!/usr/bin/env python3
"""
A program to report the frequency of DNA nucleotides
This version introduces a count() function and unit test
"""

import sys
import os

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        sys.exit("usage: {} DNA".format(os.path.basename(sys.argv[0])))

    count_a, count_c, count_g, count_t = count(args[0])

    print(count_a, count_c, count_g, count_t)


# --------------------------------------------------
def count(dna):
    """ Count bases in DNA """

    count_a, count_c, count_g, count_t = 0, 0, 0, 0
    for base in dna:
        if base == 'A':
            count_a += 1
        elif base == 'C':
            count_c += 1
        elif base == 'G':
            count_g += 1
        elif base == 'T':
            count_t += 1

    return (count_a, count_c, count_g, count_t)


# --------------------------------------------------
def test_count():
    """ Test count """

    assert count('') == (0, 0, 0, 0)
    assert count('123XYZ') == (0, 0, 0, 0)
    assert count('A') == (1, 0, 0, 0)
    assert count('C') == (0, 1, 0, 0)
    assert count('G') == (0, 0, 1, 0)
    assert count('T') == (0, 0, 0, 1)
    assert count('ACCGGGTTTT') == (1, 2, 3, 4)


# --------------------------------------------------
if __name__ == '__main__':
    main()
