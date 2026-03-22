"""Amundson Framework experiments — G(n), A_G computation."""
from decimal import Decimal, getcontext

def G(n: int) -> Decimal:
    """G(n) = n^(n+1) / (n+1)^n"""
    getcontext().prec = 50
    n_d = Decimal(n)
    return (n_d ** (n_d + 1)) / ((n_d + 1) ** n_d)

def amundson_constant(precision: int = 100) -> Decimal:
    """Compute A_G = lim(n→∞) G(n+1)/G(n) to given precision."""
    getcontext().prec = precision + 20
    n = 10 ** 6
    n_d = Decimal(n)
    g_n = G(n)
    g_n1 = G(n + 1)
    return g_n1 / g_n

def e_limit_refinement(n: int) -> Decimal:
    """n/(1+1/n)^n = n/e + 1/(2e) + O(1/n)"""
    getcontext().prec = 50
    n_d = Decimal(n)
    base = (1 + 1 / n_d) ** n_d
    return n_d / base
