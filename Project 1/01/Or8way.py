from Or import or_gate

def or8way(inputs):
    """
    Simula una compuerta OR8WAY usando solo NAND.

    Args:
    inputs: Cadena de 8 bits ('0' o '1').

    Returns:
    Un bit ('0' o '1') resultado de la operación OR de los 8 bits.
    """
    # Convertimos la cadena de bits en enteros
    bits = [int(bit) for bit in inputs]
    
    # Aplicamos OR en pares de bits usando NAND
    x1 = or_gate(bits[0], bits[1])
    x2 = or_gate(bits[2], bits[3])
    x3 = or_gate(bits[4], bits[5])
    x4 = or_gate(bits[6], bits[7])

    # OR de 4 bits
    y1 = or_gate(x1, x2)
    y2 = or_gate(x3, x4)

    # OR final de 8 bits
    return str(or_gate(y1, y2))

# Pruebas con valores de la imagen
test_inputs = [
    "00000000",
    "00000001",
    "00010000",
    "00000001",
    "00100110"
]

# Mostrar los resultados en formato de tabla
print("|   input   | out |")
print("|-----------|-----|")
for inp in test_inputs:
    result = or8way(inp)
    print(f"| {inp} |  {result}  |")
