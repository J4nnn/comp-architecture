from HalfAdder import HalfAdder
from FullAdder import FullAdder

# Add16 (suma de dos números de 16 bits)
def Add16(a, b):
    out = [0] * 16  # Resultado de 16 bits
    sum_, carry = HalfAdder(a[0], b[0])  # Primer bit sin carry de entrada
    out[0] = sum_

    # Suma en cascada usando FullAdders
    for i in range(1, 16):
        sum_, carry = FullAdder(a[i], b[i], carry)
        out[i] = sum_

    return out

# Función para imprimir números binarios de 16 bits
def bin_str(bits):
    return ''.join(str(b) for b in reversed(bits))  # Invertimos para mostrarlo como en notación binaria normal

# Pruebas con la tabla de verdad de 16 bits (algunos valores)
test_cases = [
    ([0] * 16, [0] * 16),  # 0 + 0
    ([1] * 16, [0] * 16),  # 65535 + 0
    ([1] * 16, [1] * 16),  # 65535 + 65535 (overflow, pero el carry final se ignora)
    ([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]),  # Alternados
]

print(" a                 | b                 | sum               ")
print("------------------------------------------------------------")
for a, b in test_cases:
    result = Add16(a, b)
    print(f" {bin_str(a)} | {bin_str(b)} | {bin_str(result)} ")