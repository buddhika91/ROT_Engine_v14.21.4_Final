# ROT_Engine_v14.21.4 | Derivation of 9 Fundamental Constants from 5 Postulates
# Author: Buddhika Weerasooriya
# Date: July 3, 2025
# Description:
#   This engine numerically derives 9 fundamental physical constants:
#   c, ℏ, G, α, Λ, mₑ, αₛ, mₚ, e
#   using only 5 postulated parameters and 9 fitted exponents under Recursive Observation Theory (ROT).

import numpy as np
from scipy.optimize import minimize

# === Postulated Base Parameters (Fixed) ===
l0 = 9.676e-35      # meters
t0 = 3.227e-43      # seconds
S0 = 9.999e+05      # entropy scale
r0 = 99.790         # entropy radius
eta0 = 1824.938     # attentional field amplitude

# === Observed Constants (Target Values) ===
constants_obs = {
    'c': 2.99792458e8,
    'hbar': 1.054571817e-34,
    'G': 6.67430e-11,
    'alpha': 7.2973525693e-3,
    'Lambda': 1.1056e-52,
    'm_e': 9.1093837015e-31,
    'alpha_s': 0.1181,
    'm_p': 1.67262192369e-27,
    'e': 1.602176634e-19
}

# === Fixed exponents for base 5 constants (from v14.21.1) ===
fixed_p = [-0.0001, 3.1364, 12.8849, -4.6612, -133.3322]  # p1–p5

# === Objective Function: Optimize p6–p9 Only ===
def partial_objective(p_var):
    p6, p7, p8, p9 = p_var
    p1, p2, p3, p4, p5 = fixed_p

    kappa0 = S0 / ((4/3) * np.pi * l0**3)
    c = l0 / t0 * 10**p1
    hbar = kappa0 * l0**3 * t0 * 10**p2
    alpha = (eta0 / r0)**2 * 10**p4
    m_e = hbar / (l0 * c) * 10**p6
    alpha_s = alpha * (eta0 / r0)**0.25 * 10**p7
    m_p = m_e * 10**p8
    e = np.sqrt(4 * np.pi * hbar * c * alpha) * 10**p9

    terms = [
        np.log10(m_e / constants_obs['m_e']),
        np.log10(alpha_s / constants_obs['alpha_s']),
        np.log10(m_p / constants_obs['m_p']),
        np.log10(e / constants_obs['e']),
    ]
    return np.sum(np.square(terms))

# === Minimization: Fit p6 to p9 ===
result = minimize(partial_objective,
                  x0=[-21.6, 0.9, 3.0, 0.0],
                  method='Nelder-Mead',
                  options={'maxiter': 40000, 'fatol': 1e-13})

# === Extract Optimal Parameters ===
p6, p7, p8, p9 = result.x
p1, p2, p3, p4, p5 = fixed_p
kappa0 = S0 / ((4/3) * np.pi * l0**3)

# === Derived Constants ===
c = l0 / t0 * 10**p1
hbar = kappa0 * l0**3 * t0 * 10**p2
G = l0**3 / (S0 * t0**2) * 10**p3
alpha = (eta0 / r0)**2 * 10**p4
Lambda = (S0**-1 * t0**-2 * np.log(kappa0)) * 10**p5
m_e = hbar / (l0 * c) * 10**p6
alpha_s = alpha * (eta0 / r0)**0.25 * 10**p7
m_p = m_e * 10**p8
e = np.sqrt(4 * np.pi * hbar * c * alpha) * 10**p9

# === Output Results ===
print("\n====== ROT Engine v14.21.4 | Extended Derivation of 9 Constants ======")
print(f"Objective (partial): {result.fun:.3e}")
print(f"Iterations: {result.nit}\n")

print("Postulated Parameters:")
print(f"l₀: {l0:.3e} m, t₀: {t0:.3e} s, S₀: {S0:.3e}, r₀: {r0:.3f}, η₀: {eta0:.3f}")
print(f"log₁₀(κ₀): {np.log10(kappa0):.3f}, κ₀: {kappa0:.3e}\n")

print("Exponent Parameters:")
for i, p in enumerate(fixed_p, 1):
    print(f"p{i}: {p:.6f}")
print(f"p6 (mₑ):  {p6:.6f}")
print(f"p7 (αₛ):  {p7:.6f}")
print(f"p8 (mₚ):  {p8:.6f}")
print(f"p9 (e):   {p9:.6f}\n")

print("Derived Constants vs Observed:")
def compare(name, pred, obs):
    rel_err = (pred / obs) - 1
    print(f"{name:<10} Pred: {pred:.3e}  Obs: {obs:.3e}  Rel error: {rel_err:+.2e}")

compare('c', c, constants_obs['c'])
compare('hbar', hbar, constants_obs['hbar'])
compare('G', G, constants_obs['G'])
compare('alpha', alpha, constants_obs['alpha'])
compare('Lambda', Lambda, constants_obs['Lambda'])
compare('mₑ', m_e, constants_obs['m_e'])
compare('αₛ', alpha_s, constants_obs['alpha_s'])
compare('mₚ', m_p, constants_obs['m_p'])
compare('e', e, constants_obs['e'])
