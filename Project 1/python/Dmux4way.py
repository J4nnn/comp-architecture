from Dmux import dmux

def dmux4way(in_signal, S1, S0):
    """
    Simula un DMUX4WAY usando solo NAND.

    Args:
    in_signal: Bit de entrada ('0' o '1').
    S1, S0: Bits de selección ('0' o '1').

    Returns:
    (O1, O2, O3, O4): Tupla con los 4 bits de salida.
    """
    # Primera división usando S1
    X, Y = dmux(in_signal, S1)

    # Segunda división usando S0
    O1, O2 = dmux(X, S0)
    O3, O4 = dmux(Y, S0)

    return O1, O2, O3, O4

# Pruebas con los valores de la tabla de verdad
test_cases = [
    ("0", "00", "0"),
    ("0", "01", "0"),
    ("0", "10", "0"),
    ("0", "11", "0"),
]

# Imprimir la tabla de resultados
print("| in | S1 | S0 | O1 | O2 | O3 | O4 |")
print("|----|----|----|----|----|----|----|")
for in_signal, S1, S0 in test_cases:
    O1, O2, O3, O4 = dmux4way(in_signal, S1, S0)
    print(f"|  {in_signal}  |  {S1}  |  {S0}  |  {O1}  |  {O2}  |  {O3}  |  {O4}  |")
