# from HalfAdder import *
# from Add16 import *


# def binary_to_int(bin_str):
#     """Convierte una cadena binaria de 16 bits en un entero con signo."""
#     num = int(bin_str, 2)  # Convierte la cadena binaria en un entero
#     if num >= 2**15:  # Si el número es mayor o igual a 32768, es negativo en complemento a dos
#         num -= 2**16
#     return num

# def int_to_binary(value):
#     """Convierte un entero con signo a una cadena binaria de 16 bits."""
#     return format(value & 0xFFFF, '016b')  # Asegura que sea de 16 bits

# def ALU(x, y, zx, nx, zy, ny, f, no):
#     """Implementa la ALU de Nand2Tetris con las señales de control dadas."""
#     # Convierte los valores de entrada de binario a enteros
#     x = binary_to_int(x)
#     y = binary_to_int(y)

#     # Aplicar las señales de control
#     if zx: x = 0     # Si zx == 1, x se pone a 0
#     if nx: x = ~x    # Si nx == 1, se invierte x (complemento a uno)
#     if zy: y = 0     # Si zy == 1, y se pone a 0
#     if ny: y = ~y    # Si ny == 1, se invierte y (complemento a uno)
    
#     # Operación principal (AND o suma)
#     if f:
#         out = x + y  # Si f == 1, se realiza la suma
#     else:
#         out = x & y  # Si f == 0, se realiza la operación AND

#     if no: out = ~out  # Si no == 1, se invierte la salida (complemento a uno)
    
#     # Asegurar que la salida sea de 16 bits
#     out = int_to_binary(out)

#     # Convertir la salida a entero con signo para verificar las banderas
#     out_val = binary_to_int(out)
#     zr = 1 if out_val == 0 else 0  # Flag zr (zero)
#     ng = 1 if out_val < 0 else 0   # Flag ng (negative)
    
#     return out, zr, ng

# def generate_table():
#     """Genera la tabla con los valores de prueba para la ALU."""
#     test_cases = [
#         ('0000000000000000', '1111111111111111', 1, 0, 1, 0, 1, 0),
#         ('0000000000000000', '1111111111111111', 1, 1, 1, 1, 1, 1),
#         ('0000000000000000', '1111111111111111', 1, 1, 1, 0, 1, 0),
#         ('0000000000000000', '1111111111111111', 0, 0, 1, 1, 0, 0),
#         ('0000000000010001', '0000000000000011', 1, 0, 1, 0, 1, 0),
#         ('0000000000010001', '0000000000000011', 0, 1, 0, 1, 0, 1),
#     ]
    
#     print("|        x         |        y         |zx |nx |zy |ny | f |no |       out        |zr |ng |")
#     for x, y, zx, nx, zy, ny, f, no in test_cases:
#         out, zr, ng = ALU(x, y, zx, nx, zy, ny, f, no)
#         print(f"| {x} | {y} | {zx} | {nx} | {zy} | {ny} | {f} | {no} | {out} | {zr} | {ng} |")

# # Generar la tabla de prueba
# generate_table()

# New implementation

from Add16 import add16
from functions import *

def alu(zx, nx, zy, ny, f, no, x, y):
    if zx: x = [0] * 16
    if nx: x = not16(x)
    if zy: y = [0] * 16
    if ny: y = not16(y)
    if f:
        out = add16(x, y)
    else:
        out = and16(x, y)
    if no: not16(out)

    out_decimal = binary_to_decimal(out)
    if out_decimal == 0:
        zr = 1
    else:
        zr = 0
    if out_decimal < 0:
        ng = 1
    else:
        ng = 0
    return out, zr, ng

def binary_to_decimal(binary_list):
    decimal = 0
    power = 0
    for bit in reversed(binary_list):
        if bit == 1:
            decimal += 2 ** power
        power += 1
    return decimal

x = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 4
y = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 5

print("zx | nx | zy | ny | f | no | Out | zr | ng")
print("---|----|----|----|---|----|-----------|----|---")

for zx in [0, 1]:
    for nx in [0, 1]:
        for zy in [0, 1]:
            for ny in [0, 1]:
                for f in [0, 1]:
                    for no in [0, 1]:
                        out, zr, ng = alu(zx, nx, zy, ny, f, no, x, y)
                        print(f"{zx} | {nx} | {zy} | {ny} | {f} | {no} | {binary_to_decimal(out)} | {zr} | {ng}")
