import sys
import math

def square_and_multiply(base: int, exponent: int, modulus: int) -> int:
    bits = []
    for i in range(exponent.bit_length()):
        bits.append((exponent >> i) & 1)
    bits.pop()
    bits.reverse()

    result = base
    for bit in bits:
        result = pow(result, 2, modulus)
        if (bit == 1):
            result *= base
            result %= modulus
    return result

def deterministic_primality_test(i: int) -> bool:
    if (i % 2 == 0):
        return False

    for j in range(3, math.floor(math.sqrt(i)) + 1, 2):
        if (i % j == 0):
            return False
    return True

def miller_rabin_primality_test(n: int, a: int) -> bool:
    if (n % 2 == 0 or n % 3 == 0):
        return n == 2 or n == 3

    s = 0
    d = n - 1
    while (d % 2 == 0):
        d /= 2
        s += 1

    x = square_and_multiply(a, int(d), n)
    for i in range(s):
        y = square_and_multiply(x, 2, n)
        if (y == 1 and x != 1 and x != n - 1):
            return False
        x = y
    return y == 1

if (len(sys.argv) != 4):
    print("Usage: miller-rabin.py [lower_bound] [upper_bound] [display]")
    sys.exit()
else:
    try:
        lower_bound = int(sys.argv[1])
        upper_bound = int(sys.argv[2])
        display = int(sys.argv[3])
    except:
        print("Usage: miller-rabin.py [lower_bound] [upper_bound] [display]")
        sys.exit()

error_rates = []
for i in range(lower_bound, upper_bound + 1):
    if (deterministic_primality_test(i)):
        continue
    else:
        errors = 0
        for j in range(2, i - 1):
            if (miller_rabin_primality_test(i, j)):
                errors += 1
        error_rates.append((i, errors / (i - 3)))

error_rates.sort(key = lambda t: t[1], reverse = True)
print("Error rates for composite bases:")
for i in range(display):
    print(f"{error_rates[i][0]}: {error_rates[i][1]: .3f}")
