#!/usr/bin/env python3
"""Print random seed strings, each with a digest of facts found in it.

The digest is raw material for reading the seed, not a recipe. It exists so
that any pattern a direction is built on ("digit sum 41", "kK7 appears twice")
is really in the string rather than miscounted.

    python3 seed.py            # one 64-character seed
    python3 seed.py -n 3       # three independent seeds, one per variant
    python3 seed.py -l 96      # longer seeds
"""

import argparse
import re
import secrets
import string
from collections import Counter

ALPHABET = string.ascii_letters + string.digits
VOWELS = set("aeiouAEIOU")


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def digital_root(n):
    return 0 if n == 0 else 1 + (n - 1) % 9


def repeated_chunks(s, size):
    low = s.lower()
    counts = Counter(low[i:i + size] for i in range(len(low) - size + 1))
    return [(chunk, n) for chunk, n in sorted(counts.items()) if n > 1]


def palindromes(s, min_len=3):
    """Maximal case-insensitive palindromic substrings, shown as written."""
    low = s.lower()
    spans = set()
    for i in range(len(s)):
        for j in range(i + min_len, len(s) + 1):
            sub = low[i:j]
            if sub == sub[::-1]:
                spans.add((i, j))
    maximal = [
        (i, j) for i, j in spans
        if not any((a <= i and j <= b) and (a, b) != (i, j) for a, b in spans)
    ]
    return [s[i:j] for i, j in sorted(maximal)]


def join(items, empty="none"):
    return " · ".join(items) if items else empty


def digest(s):
    digits = [int(c) for c in s if c.isdigit()]
    letters = [c for c in s if c.isalpha()]
    upper = sum(c.isupper() for c in letters)
    vowels = sum(c in VOWELS for c in letters)
    total = sum(digits)

    numbers = [n for n in re.findall(r"\d+", s) if len(n) > 1]
    primes = sorted({int(n) for n in numbers if is_prime(int(n))})
    frequent = Counter(c.lower() for c in s).most_common()
    top = [f"{c}×{n}" for c, n in frequent if n >= 3][:6]
    runs = [f'"{m.group(0)}" at {m.start()}'
            for m in re.finditer(r"(.)\1+", s, re.IGNORECASE)]
    repeats = [f'"{c}"×{n}' for size in (3, 2) for c, n in repeated_chunks(s, size)]
    hex_runs = re.findall(r"[0-9a-fA-F]{3,}", s)
    letter_runs = sorted(re.findall(r"[A-Za-z]+", s), key=len, reverse=True)[:3]
    unused = [str(d) for d in range(10) if d not in digits]

    root = digital_root(total)
    sum_note = " (prime)" if is_prime(total) else ""
    return [
        ("composition", f"{len(letters)} letters ({upper} upper, {len(letters) - upper} lower, "
                        f"{vowels} vowels) · {len(digits)} digits"),
        ("digits", f"sum {total}{sum_note} · digital root {root} · never used: {join(unused)}"),
        ("sequence", " ".join(map(str, digits)) or "none"),
        ("frequent", join(top)),
        ("numbers", join(numbers) + (f"   primes: {join(map(str, primes))}" if primes else "")),
        ("runs", join(runs)),
        ("repeats", join(repeats)),
        ("palindromes", join(f'"{p}"' for p in palindromes(s))),
        ("hex-like", join(f'"{h}"' for h in hex_runs)),
        ("letter runs", join(f'"{r}"' for r in letter_runs)),
        ("ends", f"first {s[0]} · middle {s[len(s) // 2]} · last {s[-1]}"),
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("-n", type=int, default=1, help="number of seeds (default 1)")
    parser.add_argument("-l", "--length", type=int, default=64, help="characters per seed (default 64)")
    args = parser.parse_args()
    length = max(16, args.length)

    for k in range(1, max(1, args.n) + 1):
        seed = "".join(secrets.choice(ALPHABET) for _ in range(length))
        print(f"seed {k}  {seed}")
        for label, value in digest(seed):
            print(f"  {label:<12} {value}")
        print()


if __name__ == "__main__":
    main()
