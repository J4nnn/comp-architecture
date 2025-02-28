from HalfAdder import *
from Add16 import *


def binary_to_int(bin_str):
    """Convierte una cadena binaria de 16 bits en un entero con signo."""
    num = int(bin_str, 2)  # Convierte la cadena binaria en un entero
    if num >= 2**15:  # Si el número es mayor o igual a 32768, es negativo en complemento a dos
        num -= 2**16
    return num

def int_to_binary(value):
    """Convierte un entero con signo a una cadena binaria de 16 bits."""
    return format(value & 0xFFFF, '016b')  # Asegura que sea de 16 bits

def ALU(x, y, zx, nx, zy, ny, f, no):
    """Implementa la ALU de Nand2Tetris con las señales de control dadas."""
    # Convierte los valores de entrada de binario a enteros
    x = binary_to_int(x)
    y = binary_to_int(y)

    # Aplicar las señales de control
    if zx: x = 0     # Si zx == 1, x se pone a 0
    if nx: x = ~x    # Si nx == 1, se invierte x (complemento a uno)
    if zy: y = 0     # Si zy == 1, y se pone a 0
    if ny: y = ~y    # Si ny == 1, se invierte y (complemento a uno)
    
    # Operación principal (AND o suma)
    if f:
        out = x + y  # Si f == 1, se realiza la suma
    else:
        out = x & y  # Si f == 0, se realiza la operación AND

    if no: out = ~out  # Si no == 1, se invierte la salida (complemento a uno)
    
    # Asegurar que la salida sea de 16 bits
    out = int_to_binary(out)

    # Convertir la salida a entero con signo para verificar las banderas
    out_val = binary_to_int(out)
    zr = 1 if out_val == 0 else 0  # Flag zr (zero)
    ng = 1 if out_val < 0 else 0   # Flag ng (negative)
    
    return out, zr, ng

def generate_table():
    """Genera la tabla con los valores de prueba para la ALU."""
    test_cases = [
        ('0000000000000000', '1111111111111111', 1, 0, 1, 0, 1, 0),
        ('0000000000000000', '1111111111111111', 1, 1, 1, 1, 1, 1),
        ('0000000000000000', '1111111111111111', 1, 1, 1, 0, 1, 0),
        ('0000000000000000', '1111111111111111', 0, 0, 1, 1, 0, 0),
        ('0000000000010001', '0000000000000011', 1, 0, 1, 0, 1, 0),
        ('0000000000010001', '0000000000000011', 0, 1, 0, 1, 0, 1),
    ]
    
    print("|        x         |        y         |zx |nx |zy |ny | f |no |       out        |zr |ng |")
    for x, y, zx, nx, zy, ny, f, no in test_cases:
        out, zr, ng = ALU(x, y, zx, nx, zy, ny, f, no)
        print(f"| {x} | {y} | {zx} | {nx} | {zy} | {ny} | {f} | {no} | {out} | {zr} | {ng} |")

# Generar la tabla de prueba
generate_table()
