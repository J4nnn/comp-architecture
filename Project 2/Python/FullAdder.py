from HalfAdder import HalfAdder
from HalfAdder import not_gate
from HalfAdder import and_gate
from HalfAdder import xor_gate
from HalfAdder import or_gate


# Implementación del Full Adder usando dos Half Adders
def FullAdder(a, b, c):
    # Primer Half Adder (suma de a y b)
    HAsum, HAcarry = HalfAdder(b, c)

    # NOT de a
    nota = not_gate(a)

    # Operaciones con NOT a
    sumNotA = and_gate(nota, HAsum)
    carryNotA = and_gate(nota, HAcarry)

    # XOR de b y c
    xorsumA = xor_gate(b, c)
    notxorsumA = not_gate(xorsumA)

    # OR de b y c
    orcarryA = or_gate(b, c)

    # Operaciones con a
    sumA = and_gate(a, notxorsumA)
    carryA = and_gate(a, orcarryA)

    # Calcular suma y carry finales
    sum_ = or_gate(sumNotA, sumA)
    carry = or_gate(carryNotA, carryA)

    return sum_, carry

# Imprimir la tabla de verdad
print(" a | b | c | sum | carry ")
print("--------------------------")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            sum_result, carry_result = FullAdder(a, b, c)
            print(f" {a} | {b} | {c} |  {sum_result}  |   {carry_result}   ")
