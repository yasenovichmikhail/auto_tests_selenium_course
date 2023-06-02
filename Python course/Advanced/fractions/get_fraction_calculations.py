from fractions import Fraction

def get_fraction_calculations(m, n):
    m_fr = Fraction(m)
    n_fr = Fraction(n)
    summa = m_fr + n_fr
    diff = m_fr - n_fr
    multiply = m_fr * n_fr
    devision = m_fr / n_fr
    print(f"{m} + {n} = {summa}")
    print(f"{m} - {n} = {diff}")
    print(f"{m} * {n} = {multiply}")
    print(f"{m} / {n} = {devision}")

m = '2/3'
n = '3/7'

get_fraction_calculations(m, n)