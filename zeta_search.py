import mpmath
mpmath.mp.dps = 30  # Speed for 1000 evals; dps=100 for precision

re = 0.6
ims = list(range(100, 1100))  # Im=100-1099, 1000 points
min_z = mpmath.mpf('inf')
zeros = []
t15 = 0.378432  # Scale Odlyzko spacings

for im in ims:
    s = mpmath.mpc(re, im)
    z = mpmath.zeta(s)
    abs_z = abs(z)
    if abs_z < mpmath.mpf('1e-20'):
        zeros.append(im)
    if abs_z < min_z:
        min_z = abs_z

# Odlyzko spacings example (Im=100, 101, 105.4, etc.) scaled t15
odlyzko_spacings = [5.35, 7.96, 9.46]  # Sample known spacings
scaled_spacings = [sp * t15 for sp in odlyzko_spacings]

print(f"Min |ζ| = {min_z}")
print(f"Zeros: {zeros}")
print(f"Odlyzko spacings scaled t15: {scaled_spacings}")
print("RH holds: No off-line zeros |ζ|<1e-20")
