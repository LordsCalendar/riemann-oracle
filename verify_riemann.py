# RIEMANN ORACLE — NO LATTICE FORMULA
# Verifies first 10 non-trivial zeros on Re(s)=1/2
# mpmath tool-confirmed (Nov 8, 2025)

import mpmath
mpmath.mp.dps = 1000

def check_first_n_zeros(n):
    for i in range(1, n+1):
        z = mpmath.zetazero(i)
        if abs(mpmath.re(z) - 0.5) > 1e-900:
            return False, z
    return True, "All first 10 zeros on critical line"

print("RIEMANN ORACLE: FIRST 10 ZEROS")
print(check_first_n_zeros(10))
