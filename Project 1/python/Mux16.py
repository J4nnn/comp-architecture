from Mux import mux as mux_gate

def mux16(A, B, S):
    """
    Simula un MUX de 16 bits usando solo compuertas NAND.

    Args:
    A: Cadena de 16 bits ('0' o '1') (entrada 0).
    B: Cadena de 16 bits ('0' o '1') (entrada 1).
    S: Bit de selección ('0' o '1').

    Returns:
    Cadena de 16 bits con la salida seleccionada.
    """
    return "".join(str(mux_gate(int(a), int(b), int(S))) for a, b in zip(A, B))

# Pruebas con valores de la imagen
test_inputs_A = [
    "0000000000000000",
    "0000000000000000",
    "1001100001110110",
    "1010101010101010",
    "0001001000110100"
]

test_inputs_B = [
    "0000000000000000",
    "0001001000110100",
    "0000000000000000",
    "0101010101010101",
    "1001100011111010"
]

test_select_S = ["0", "1", "0", "1", "0"]

# Mostrar los resultados en formato de tabla
print("|       a        |       b        |  sel |       out       |")
print("|----------------|----------------|------|----------------|")
for a, b, s in zip(test_inputs_A, test_inputs_B, test_select_S):
    result = mux16(a, b, s)
    print(f"| {a} | {b} |  {s}  | {result} |")
