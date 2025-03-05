# from subprocess import check_output

# from HalfAdder import HalfAdder
# from HalfAdder import not_gate
# from HalfAdder import and_gate
# from HalfAdder import xor_gate
# from HalfAdder import or_gate


# # Implementación del Full Adder usando dos Half Adders
# def FullAdder(a, b, c):
#     # Primer Half Adder (suma de a y b)
#     HAsum, HAcarry = HalfAdder(b, c)

#     # NOT de a
#     nota = not_gate(a)

#     # Operaciones con NOT a
#     sumNotA = and_gate(nota, HAsum)
#     carryNotA = and_gate(nota, HAcarry)

#     # XOR de b y c
#     xorsumA = xor_gate(b, c)
#     notxorsumA = not_gate(xorsumA)

#     # OR de b y c
#     orcarryA = or_gate(b, c)

#     # Operaciones con a
#     sumA = and_gate(a, notxorsumA)
#     carryA = and_gate(a, orcarryA)

#     # Calcular suma y carry finales
#     sum_ = or_gate(sumNotA, sumA)
#     carry = or_gate(carryNotA, carryA)

#     return sum_, carry

# # Imprimir la tabla de verdad
# print(" a | b | c | sum | carry ")
# print("--------------------------")
# for a in [0, 1]:
#     for b in [0, 1]:
#         for c in [0, 1]:
#             sum_result, carry_result = FullAdder(a, b, c)
#             print(f" {a} | {b} | {c} |  {sum_result}  |   {carry_result}   ")

# New implementation
from functions import *
from HalfAdder import half_adder

def full_adder(input1, input2, c_in):
    """Adds three bits (two inputs and carry-in), returning the sum and carry-out."""
    sum_1, carry1 = half_adder(input1, input2)
    sum_2, carry2 = half_adder(sum_1, c_in)
    c_out = or_gate(carry1, carry2)
    return int(sum_2), int(c_out)

# Testing
# print(f"full_adder(0, 0, 0) = {full_adder(0, 0, 0)}  # Esperado: (0, 0)")
# print(f"full_adder(0, 0, 1) = {full_adder(0, 0, 1)}  # Esperado: (1, 0)")
# print(f"full_adder(0, 1, 0) = {full_adder(0, 1, 0)}  # Esperado: (1, 0)")
# print(f"full_adder(0, 1, 1) = {full_adder(0, 1, 1)}  # Esperado: (0, 1)")
# print(f"full_adder(1, 0, 0) = {full_adder(1, 0, 0)}  # Esperado: (1, 0)")
# print(f"full_adder(1, 0, 1) = {full_adder(1, 0, 1)}  # Esperado: (0, 1)")
# print(f"full_adder(1, 1, 0) = {full_adder(1, 1, 0)}  # Esperado: (0, 1)")
# print(f"full_adder(1, 1, 1) = {full_adder(1, 1, 1)}  # Esperado: (1, 1)")

print("\nInput1 | Input2 | Carry-in | Sum | Carry-out")
print("-------|--------|----------|-----|----------")

for input1 in [0, 1]:
    for input2 in [0, 1]:
        for c_in in [0, 1]:
            sum_result, carry_out = full_adder(input1, input2, c_in)
            print(f"   {input1}   |    {input2}   |     {c_in}    |  {sum_result}  |    {carry_out}")

print("\n")