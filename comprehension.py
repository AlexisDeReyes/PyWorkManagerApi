from repl_input import run_from_repl_separate_args as run_from_repl
import sys

from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    return run_from_repl(is_prime, int, 23)
