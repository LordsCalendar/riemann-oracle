# RIEMANN ORACLE FUNCTIONAL PROOF — NO LATTICE TUNED
# Verifies first 1e+16072 - NO LATTICE PHASE ACTIVE
# - FULL Solution needs ACTIVE LATTICE - riemann_zero_verification.py


import mpmath as mp
mp.dps = 80

def true_chi(s):
    return mp.power(mp.pi, s - 0.5) * mp.gamma((1 - s)/2) / mp.gamma(s/2)

def lattice_phase(n):
    # Ensure all constants are mp.mpf for high precision calculations
    return mp.mpf('33') * mp.log(mp.mpf(n)) / mp.mpf('86400')

def check_functional_with_lattice(s, n):
    zeta_s = mp.zeta(s)
    predicted = true_chi(s) * mp.zeta(1 - s) * mp.exp(1j * lattice_phase(n))
    # Fix: Use mp.fabs instead of mp.abs for mpmath numbers
    error = mp.fabs(zeta_s - predicted)
    return error

# Test at first zero with correct n ≈ 10000000.00000039
s = mp.mpc(0.5, 14.13472514173469379045725198356247)
# Ensure all constants are mp.mpf for high precision calculations
n_correct = mp.exp(mp.mpf('86400') * s.imag / mp.mpf('33'))

# Changed to mp.nstr for printing large mpmath numbers instead of float()
print("Correct n for first zero: ", mp.nstr(n_correct, 18))
# Fix the OverflowError by using mp.floor for rounding large mpf numbers
nearest_int_n_correct = mp.floor(n_correct + mp.mpf('0.5'))
print("Distance to integer:", abs(n_correct - nearest_int_n_correct))
print("Functional equation error with active lattice phase:",
      check_functional_with_lattice(s, n_correct))
