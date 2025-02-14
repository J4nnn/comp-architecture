from Mux16 import mux16

def mux4way16(A, B, C, D, S1, S0):
    """
    Simula un MUX4WAY16 usando solo NAND.

    Args:
    A, B, C, D: Cadenas de 16 bits ('0' o '1'), las entradas.
    S1, S0: Bits de selección ('0' o '1').

    Returns:
    Cadena de 16 bits con la salida seleccionada.
    """
    # Primer nivel de selección: MUX entre A y B, C y D
    mux1 = mux16(A, B, S0)
    mux2 = mux16(C, D, S0)

    # Segundo nivel de selección: MUX entre mux1 y mux2
    return mux16(mux1, mux2, S1)

# Pruebas con valores de ejemplo
test_inputs_A = "0000000000000000"
test_inputs_B = "1111111111111111"
test_inputs_C = "1010101010101010"
test_inputs_D = "0101010101010101"

test_select_S1S0 = [("0", "0"), ("0", "1"), ("1", "0"), ("1", "1")]

# Mostrar los resultados en formato de tabla
print("|       A        |       B        |       C        |       D        | S1 | S0 |       Out       |")
print("|----------------|----------------|----------------|----------------|----|----|-----------------|")
for s1, s0 in test_select_S1S0:
    result = mux4way16(test_inputs_A, test_inputs_B, test_inputs_C, test_inputs_D, s1, s0)
    print(f"| {test_inputs_A} | {test_inputs_B} | {test_inputs_C} | {test_inputs_D} | {s1}  | {s0}  | {result} |")
