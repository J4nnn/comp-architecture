from Nand import nand_gate as nand

def and_gate(input1, input2):
    """
    Simula una puerta lógica AND utilizando NAND.

    Argumentos:
    input1: La primera entrada (True o False, 1 o 0).
    input2: La segunda entrada (True o False, 1 o 0).

    Retorna:
    True o False según la siguiente tabla de verdad:
    | a | b | q |
    | 0 | 0 | 0 |
    | 1 | 0 | 0 |
    | 0 | 1 | 0 |
    | 1 | 1 | 1 |
    """
    return 1 - nand(input1, input2)

print(" | AND Truth Table | Result |")
print(" | A = 0, B = 0 | A AND B =", and_gate(0, 0), " | ")
print(" | A = 0, B = 1 | A AND B =", and_gate(0, 1), " | ")
print(" | A = 1, B = 0 | A AND B =", and_gate(1, 0), " | ")
print(" | A = 1, B = 1 | A AND B =", and_gate(1, 1), " | ")