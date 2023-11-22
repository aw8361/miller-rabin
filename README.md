# miller-rabin

A Python script that measures the error rate of the Miller-Rabin primality test
when analyzing composite numbers.

The probabilistic Miller-Rabin primality test uses a randomly generated number
as the base of the algorithm, which can sometimes incorrectly identifies
composite numbers as primes. This script runs the Miller-Rabin algorithm on a
given range of numbers and tests each possible base value, recording the rate
at which "liars" are found.

The script includes a naive deterministic primality test, as well as a Python
implementation of the square-and-multiply algorithm (known also as the fast
exponentiation algorithm) used often in the Miller-Rabin test.

A detailed explanation of the algorithm, as well as the psuedocode used can be
found [on Wikipedia](https://en.wikipedia.org/wiki/Miller-Rabin-primality_test).

## Usage

Run the following command in a terminal. The program accepts three arguments:
`[LOWER-BOUND]` and `[UPPER-BOUND]` as the bounds of the range of numbers to
test, and `[DISPLAY]` as the number of entries (sorted by error rate) to display
upon finish.

    miller-rabin.py [LOWER-BOUND] [UPPER-BOUND] [DISPLAY]
