from And import and_gate
from Not import not_gate

def dmux(i0,s0):
    """
    Simula un demultiplexor 2:1 utilizando puertas lógicas construidas con NAND.

    Argumentos:
    input: La entrada.
    sel: La línea de control o selección (True o 1 para b (última salida), False o 0 para a (primera salida)).

    Retorna:
    True o False según la siguiente tabla:
    | s0 |  a  |  b  |
    | 0  |  0  | i0  |
    | 1  | i0  |  0  |
    """
    return and_gate(i0, not_gate(s0)), and_gate(i0, s0)

print(" | DMUX Truth Table | Result |")
print(" | I = 0, S = 0 | DMUX =", dmux(0, 0), " | ")
print(" | I = 0, S = 1 | DMUX =", dmux(0, 1), " | ")
print(" | I = 1, S = 0 | DMUX =", dmux(1, 0), " | ")
print(" | I = 1, S = 1 | DMUX =", dmux(1, 1), " | ")


