# def nand_gate(input1, input2):
#  return 1 if not (input1 and input2)     else 0

# def and_gate(input1, input2):
#  return 1 - nand_gate(input1, input2)

# def or_gate (input1, input2):
#  return nand_gate(nand_gate(input1, input1), nand_gate(input2, input2))

# def not_gate(input):
#  return nand_gate(input, input)

# def xor_gate (input1, input2):
#  return nand_gate(nand_gate(nand_gate(input1, input1), input2), nand_gate(input1, nand_gate(input2, input2)))

# def and16(A, B):
#  return "".join(str(and_gate(int(a), int(b))) for a, b in zip(A, B))

# def not16(inputs):
#  return "".join(str(not_gate(int(bit))) for bit in inputs)

# def or8way(inputs):
#     bits = [int(bit) for bit in inputs]
    
#     # Aplicamos OR en pares de bits usando NAND
#     x1 = or_gate(bits[0], bits[1])
#     x2 = or_gate(bits[2], bits[3])
#     x3 = or_gate(bits[4], bits[5])
#     x4 = or_gate(bits[6], bits[7])

#     # OR de 4 bits
#     y1 = or_gate(x1, x2)
#     y2 = or_gate(x3, x4)

#     # OR final de 8 bits
#     return str(or_gate(y1, y2))
    

# # Implementación del Half Adder
# def HalfAdder(a, b):
#     carry = and_gate(a, b)  # AND de a y b para obtener el bit de acarreo

#     nota = not_gate(a)  # Negación de a
#     notb = not_gate(b)  # Negación de b

#     nota_and_b = and_gate(nota, b)  # (NOT a) AND b
#     a_and_notb = and_gate(a, notb)  # a AND (NOT b)

#     sum_ = or_gate(nota_and_b, a_and_notb)  # OR de los dos valores anteriores

#     return sum_, carry


# # Imprimir la tabla de verdad
# print(" a | b | sum | carry ")
# print("----------------------")
# for a in [0, 1]:
#     for b in [0, 1]:
#         sum_result, carry_result = HalfAdder(a, b)
#         print(f" {a} | {b} |  {sum_result}  |   {carry_result}   ")

# New implementation
from functions import *

def half_adder(input1, input2):
    """
    Adds two bits, returning the sum and carry.
    """
    carry = and_gate(input1, input2)
    sum_result = xor_gate(input1, input2)
    return int(sum_result), int(carry)

# Testing
# print(f"half_adder(0, 0) = {half_adder(0, 0)}  # Esperado: (0, 0)")
# print(f"half_adder(0, 1) = {half_adder(0, 1)}  # Esperado: (1, 0)")
# print(f"half_adder(1, 0) = {half_adder(1, 0)}  # Esperado: (1, 0)")
# print(f"half_adder(1, 1) = {half_adder(1, 1)}  # Esperado: (0, 1)")

print("\nInput1 | Input2 | Sum | Carry")
print("-------|--------|-----|------")

for input1 in [0, 1]:
    for input2 in [0, 1]:
        sum_result, carry = half_adder(input1, input2)
        print(f"   {input1}   |    {input2}   |  {sum_result}  |   {carry}")
print("\n")