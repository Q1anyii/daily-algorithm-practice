def solve(s, t):
    a = 0; b = 0
    for sc, tc in zip(s, t):
        if sc == tc: continue
        if sc == 'A' and tc == 'T': a += 1
        else: b += 1
    return min(a, b) + abs(a - b)

cases = [
    ("ATTTAA", "TTAATT", 3),
    ("A", "T", 1),
    ("T", "A", 1),
    ("AA", "TT", 2),
    ("AT", "TA", 1),
    ("AAAA", "TTTT", 4),
    ("ATAT", "TATA", 2),
    ("", "", 0),
]
fails = 0
for s, t, exp in cases:
    got = solve(s, t)
    if got != exp:
        fails += 1
        print("FAIL", s, t, "->", got, "exp", exp)
print("PASS" if fails == 0 else f"{fails} FAILED", f"({len(cases)} cases)")
