# from HalfAdder import HalfAdder
# from FullAdder import FullAdder

# # Add16 (suma de dos números de 16 bits)
# def Add16(a, b):
#     out = [0] * 16  # Resultado de 16 bits
#     sum_, carry = HalfAdder(a[0], b[0])  # Primer bit sin carry de entrada
#     out[0] = sum_

#     # Suma en cascada usando FullAdders
#     for i in range(1, 16):
#         sum_, carry = FullAdder(a[i], b[i], carry)
#         out[i] = sum_

#     return out

# # Función para imprimir números binarios de 16 bits
# def bin_str(bits):
#     return ''.join(str(b) for b in reversed(bits))  # Invertimos para mostrarlo como en notación binaria normal

# # Pruebas con la tabla de verdad de 16 bits (algunos valores)
# test_cases = [
#     ([0] * 16, [0] * 16),  # 0 + 0
#     ([1] * 16, [0] * 16),  # 65535 + 0
#     ([1] * 16, [1] * 16),  # 65535 + 65535 (overflow, pero el carry final se ignora)
#     ([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]),  # Alternados
# ]

# print(" a                 | b                 | sum               ")
# print("------------------------------------------------------------")
# for a, b in test_cases:
#     result = Add16(a, b)
#     print(f" {bin_str(a)} | {bin_str(b)} | {bin_str(result)} ")

# New implementation
from FullAdder import full_adder

def add16(input1_bits, input2_bits):
    """Adds two 16-bit binary numbers, returning the 16-bit sum and final carry."""
    result = []
    carry = 0

    for bit in range(16):
        sum_bit, carry = full_adder(input1_bits[bit], input2_bits[bit], carry)
        result.append(sum_bit)

    return result # The most-significant carry bit is ignored

# Testing
# a = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Decimal = 5
# b = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Decimal = 3

# print(f"input 1 = ", a[::-1], "\ninput 2 = ", b[::-1], "\nresult = ", add16(a, b)[0][::-1], "\ncarry = ", add16(a, b)[1])

input1 = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 3 en decimal
input2 = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 2 en decimal
result = add16(input1, input2)
print("Input 1:", input1[::-1])
print("Input 2:", input2[::-1])
print("Result:", result[::-1])
print("\n")