from Dmux import dmux

def dmux8way(in_signal, S2, S1, S0):
    """
    Simula un DMUX8WAY usando solo NAND.

    Args:
    in_signal: Bit de entrada ('0' o '1').
    S2, S1, S0: Bits de selección ('0' o '1').

    Returns:
    (O1, O2, O3, O4, O5, O6, O7, O8): Tupla con los 8 bits de salida.
    """
    # Primera división usando S2
    X1, X2 = dmux(in_signal, S2)

    # Segunda división usando S1
    Y1, Y2 = dmux(X1, S1)
    Y3, Y4 = dmux(X2, S1)

    # Tercera división usando S0
    O1, O2 = dmux(Y1, S0)
    O3, O4 = dmux(Y2, S0)
    O5, O6 = dmux(Y3, S0)
    O7, O8 = dmux(Y4, S0)

    return O1, O2, O3, O4, O5, O6, O7, O8

# Pruebas con los valores de la tabla de verdad
test_cases = [
    ("1", "0", "0", "0"),
    ("1", "0", "0", "1"),
    ("1", "0", "1", "0"),
    ("1", "0", "1", "1"),
    ("1", "1", "0", "0"),
    ("1", "1", "0", "1"),
    ("1", "1", "1", "0"),
    ("1", "1", "1", "1"),
]

# Imprimir la tabla de resultados
print("| in | S2 | S1 | S0 | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |")
print("|----|----|----|----|----|----|----|----|----|----|----|----|")
for in_signal, S2, S1, S0 in test_cases:
    O1, O2, O3, O4, O5, O6, O7, O8 = dmux8way(in_signal, S2, S1, S0)
    print(f"|  {in_signal}  |  {S2}  |  {S1}  |  {S0}  |  {O1}  |  {O2}  |  {O3}  |  {O4}  |  {O5}  |  {O6}  |  {O7}  |  {O8}  |")
