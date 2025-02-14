from Mux16 import mux16
from Mux4way16 import mux4way16

def mux8way16(A, B, C, D, E, F, G, H, S2, S1, S0):
    """
    Simula un MUX8WAY16 usando solo NAND.

    Args:
    A, B, C, D, E, F, G, H: Cadenas de 16 bits ('0' o '1'), las entradas.
    S2, S1, S0: Bits de selección ('0' o '1').

    Returns:
    Cadena de 16 bits con la salida seleccionada.
    """
    # Selección entre los primeros 4 y los últimos 4 usando S1 y S0
    mux1 = mux4way16(A, B, C, D, S1, S0)
    mux2 = mux4way16(E, F, G, H, S1, S0)

    # Selección final entre mux1 y mux2 usando S2
    return mux16(mux1, mux2, S2)

# Pruebas con valores de ejemplo
test_inputs = {
    "A": "0000000000000000",
    "B": "1111111111111111",
    "C": "1010101010101010",
    "D": "0101010101010101",
    "E": "1100110011001100",
    "F": "0011001100110011",
    "G": "0000111100001111",
    "H": "1111000011110000"
}

test_select_S2S1S0 = [
    ("0", "0", "0"), ("0", "0", "1"), ("0", "1", "0"), ("0", "1", "1"),
    ("1", "0", "0"), ("1", "0", "1"), ("1", "1", "0"), ("1", "1", "1")
]

# Mostrar los resultados en formato de tabla
print("|       A        |       B        |       C        |       D        |       E        |       F        |       G        |       H        | S2 | S1 | S0 |       Out       |")
print("|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----|----|----|----------------|")
for s2, s1, s0 in test_select_S2S1S0:
    result = mux8way16(
        test_inputs["A"], test_inputs["B"], test_inputs["C"], test_inputs["D"],
        test_inputs["E"], test_inputs["F"], test_inputs["G"], test_inputs["H"],
        s2, s1, s0
    )
    print(f"| {test_inputs['A']} | {test_inputs['B']} | {test_inputs['C']} | {test_inputs['D']} | {test_inputs['E']} | {test_inputs['F']} | {test_inputs['G']} | {test_inputs['H']} | {s2}  | {s1}  | {s0}  | {result} |")
