from And import and_gate
from Or import or_gate
from Not import not_gate

def mux (input1, input2, sel):
    """
    Simula un multiplexor 2:1 utilizando puertas lógicas construidas con NAND.

    Argumentos:
    i0, i1: Las entradas (True o False, 1 o 0).
    s0: Línea de selección única (True o 1 para i1, False o 0 para i0).

    Retorna:
    True o False según la siguiente tabla de verdad:
    | s0 | i0 | i1 | q |
    | 0  | 0  | X  | 0 |
    | 0  | 1  | X  | 1 |
    | 1  | X  | 0  | 0 |
    | 1  | X  | 1  | 1 |
    """


    return or_gate(and_gate(input1, not_gate(sel)), and_gate(input2, sel))

print(" | MUX Truth Table | Result |")
print(" | A = 0, B = 0, S = 0 | MUX =", mux(0, 0, 0), " | ")
print(" | A = 0, B = 1, S = 0 | MUX =", mux(0, 1, 0), " | ")
print(" | A = 1, B = 0, S = 0 | MUX =", mux(1, 0, 0), " | ")
print(" | A = 1, B = 1, S = 0 | MUX =", mux(1, 1, 0), " | ")
print(" | A = 0, B = 0, S = 1 | MUX =", mux(0, 0, 1), " | ")
print(" | A = 0, B = 1, S = 1 | MUX =", mux(0, 1, 1), " | ")
print(" | A = 1, B = 0, S = 1 | MUX =", mux(1, 0, 1), " | ")
print(" | A = 1, B = 1, S = 1 | MUX =", mux(1, 1, 1), " | ")