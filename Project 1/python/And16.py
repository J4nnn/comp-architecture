from And import and_gate

def and16(A, B):
    """
    Simula una compuerta AND de 16 bits usando solo compuertas NAND.
    
    Args:
    A: Cadena de 16 bits ('0' o '1').
    B: Cadena de 16 bits ('0' o '1').

    Returns:
    Cadena de 16 bits resultante de A AND B.
    """
    return "".join(str(and_gate(int(a), int(b))) for a, b in zip(A, B))

# Pruebas con valores de la imagen
test_inputs_A = [
    "0000000000000000",
    "0000000000000000",
    "1111111111111111",
    "1010101010101010",
    "0011110011000011",
    "0001001000110100   "
]

test_inputs_B = [
    "0000000000000000",
    "1111111111111111",
    "1111111111111111",
    "0101010101010101",
    "0000111111111000",
    "1001100011111010"
]

# Mostrar los resultados en formato de tabla
print("|       a          |       b          |       out        |")
print("|------------------|------------------|------------------|")
for a, b in zip(test_inputs_A, test_inputs_B):
    result = and16(a, b)
    print(f"| {a} | {b} | {result} |")

