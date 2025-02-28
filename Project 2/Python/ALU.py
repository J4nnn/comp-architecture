def binary_to_int(bin_str):
    """Convierte una cadena binaria de 16 bits en un entero con signo."""
    if not isinstance(bin_str, str) or len(bin_str) != 16:
        raise ValueError("La entrada debe ser una cadena binaria de 16 bits.")
    num = int(bin_str, 2)
    if num >= 2**15:  # Si el número es mayor o igual a 32768, es negativo
        num -= 2**16
    return num

def int_to_binary(num):
    """Convierte un entero en una cadena binaria de 16 bits."""
    return format(num & 0xFFFF, '016b')  # Máscara de 16 bits

def not16(bin_str):
    """Invierte una cadena binaria de 16 bits."""
    return ''.join('1' if bit == '0' else '0' for bit in bin_str)

def and16(a, b):
    """Realiza una operación AND bit a bit entre dos cadenas binarias de 16 bits."""
    return ''.join('1' if a_bit == '1' and b_bit == '1' else '0' for a_bit, b_bit in zip(a, b))

def Add16(a, b):
    """Suma dos cadenas binarias de 16 bits."""
    a_int = binary_to_int(a)
    b_int = binary_to_int(b)
    result = a_int + b_int
    return int_to_binary(result)

def ALU(x, y, zx, nx, zy, ny, f, no):
    # Asegurarse de que x e y sean cadenas binarias de 16 bits
    if not isinstance(x, str) or len(x) != 16:
        x = int_to_binary(int(x)) if isinstance(x, int) else '0' * 16
    if not isinstance(y, str) or len(y) != 16:
        y = int_to_binary(int(y)) if isinstance(y, int) else '0' * 16
    
    # Operaciones en x
    if zx: x = '0' * 16  # Si zx == 1, x se pone a 0
    if nx: x = not16(x)   # Si nx == 1, se invierte x
    
    # Operaciones en y
    if zy: y = '0' * 16  # Si zy == 1, y se pone a 0
    if ny: y = not16(y)   # Si ny == 1, se invierte y
    
    # Operación principal
    if f:
        out = Add16(x, y)  # Si f == 1, se realiza la suma
    else:
        out = and16(x, y)  # Si f == 0, se realiza la operación AND
    
    # Inversión de la salida
    if no: out = not16(out)  # Si no == 1, se invierte la salida
    
    # Cálculo de flags
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
        ('0000000000000000', '1111111111111111', 1, 1, 0, 0, 0, 0),
        ('0000000000000000', '1111111111111111', 0, 0, 1, 1, 0, 1),
        ('0000000000000000', '1111111111111111', 1, 1, 0, 0, 0, 1),
        ('0000000000000000', '1111111111111111', 0, 0, 1, 1, 1, 1),
        ('0000000000000000', '1111111111111111', 1, 1, 0, 0, 1, 1),
        ('0000000000000000', '1111111111111111', 0, 1, 1, 1, 1, 1),
        ('0000000000000000', '1111111111111111', 1, 1, 0, 1, 1, 1),
        ('0000000000000000', '1111111111111111', 0, 0, 1, 1, 1, 0),
        ('0000000000000000', '1111111111111111', 1, 1, 0, 0, 1, 0),
        ('0000000000000000', '1111111111111111', 0, 0, 0, 0, 1, 0),
        ('0000000000000000', '1111111111111111', 0, 1, 0, 0, 1, 1),
        ('0000000000000000', '1111111111111111', 0, 0, 0, 1, 1, 1),
        ('0000000000000000', '1111111111111111', 0, 0, 0, 0, 0, 0),
        ('0000000000000000', '1111111111111111', 0, 1, 0, 1, 0, 1),
        ('0000000000010001', '0000000000000011', 1, 0, 1, 0, 1, 0),
        ('0000000000010001', '0000000000000011', 1, 1, 1, 1, 1, 1),
        ('0000000000010001', '0000000000000011', 1, 1, 1, 0, 1, 0),
        ('0000000000010001', '0000000000000011', 0, 0, 1, 1, 0, 0),
        ('0000000000010001', '0000000000000011', 1, 1, 0, 0, 0, 0),
        ('0000000000010001', '0000000000000011', 0, 0, 1, 1, 0, 1),
        ('0000000000010001', '0000000000000011', 1, 1, 0, 0, 0, 1),
        ('0000000000010001', '0000000000000011', 0, 0, 1, 1, 1, 1),
        ('0000000000010001', '0000000000000011', 1, 1, 0, 0, 1, 1),
        ('0000000000010001', '0000000000000011', 0, 1, 1, 1, 1, 1),
        ('0000000000010001', '0000000000000011', 1, 1, 0, 1, 1, 1),
        ('0000000000010001', '0000000000000011', 0, 0, 1, 1, 1, 0),
        ('0000000000010001', '0000000000000011', 1, 1, 0, 0, 1, 0),
        ('0000000000010001', '0000000000000011', 0, 0, 0, 0, 1, 0),
        ('0000000000010001', '0000000000000011', 0, 1, 0, 0, 1, 1),
        ('0000000000010001', '0000000000000011', 0, 0, 0, 1, 1, 1),
        ('0000000000010001', '0000000000000011', 0, 0, 0, 0, 0, 0),
        ('0000000000010001', '0000000000000011', 0, 1, 0, 1, 0, 1),
    ]
    
    print("|        x         |        y         |zx |nx |zy |ny | f |no |       out        |zr |ng |")
    for x, y, zx, nx, zy, ny, f, no in test_cases:
        out, zr, ng = ALU(x, y, zx, nx, zy, ny, f, no)
        print(f"| {x} | {y} | {zx} | {nx} | {zy} | {ny} | {f} | {no} | {out} | {zr} | {ng} |")

# Generar la tabla de prueba
generate_table()
