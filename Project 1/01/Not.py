from Nand import nand_gate as nand

def not_gate(input):
    """
    Simula una puerta lógica NOT utilizando NAND.

    Argumentos:
    input: True o False, 1 o 0. Deben tener el mismo valor.

    Retorna:
    True o False según la siguiente tabla de verdad:
    | a | q |
    | 0 | 1 |
    | 1 | 0 |
    """


    return nand(input, input)

print(" | NOT Truth Table | Result |")
print(" | A = 0 | NOT A =", not_gate(0), " | ")
print(" | A = 1 | NOT A =", not_gate(1), " | ")