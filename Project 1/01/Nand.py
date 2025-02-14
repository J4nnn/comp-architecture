def nand_gate(input1, input2):
    """
    Simula una puerta lógica NAND utilizando 0 y 1.

    Argumentos:
    input1: La primera entrada (0 o 1).
    input2: La segunda entrada (0 o 1).

    Retorna:
    1 o 0 según la siguiente tabla de verdad:
    | a | b | q |
    | 0 | 0 | 1 |
    | 1 | 0 | 1 |
    | 0 | 1 | 1 |
    | 1 | 1 | 0 |
    """

    return 1 if not (input1 and input2)     else 0

print(" | NAND Truth Table | Result |")
print(" | A = 0, B = 0 | A NAND B =", nand_gate(0, 0), " | ")
print(" | A = 0, B = 1 | A NAND B =", nand_gate(0, 1), " | ")
print(" | A = 1, B = 0 | A NAND B =", nand_gate(1, 0), " | ")
print(" | A = 1, B = 1 | A NAND B =", nand_gate(1, 1), " | ")
