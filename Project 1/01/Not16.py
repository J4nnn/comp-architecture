from Not import not_gate

def not16(inputs):
    """
    Simula una compuerta NOT de 16 bits usando solo compuertas NAND.
    
    Args:
    inputs: Cadena de 16 caracteres ('0' o '1').

    Returns:
    Cadena de 16 caracteres invertidos ('1' por '0' y viceversa).
    """
    return "".join(str(not_gate(int(bit))) for bit in inputs)

# Pruebas con los valores de la imagen
test_inputs = [
    "0000000000000000",
    "1111111111111111",
    "1010101010101010",
    "0011101101100011",
    "0001001000110100"
]

# Mostrar los resultados en formato de tabla
print("|       in        |       out       |")
print("|-----------------|-----------------|")
for binary in test_inputs:
    result = not16(binary)
    print(f"| {binary} | {result} |")
