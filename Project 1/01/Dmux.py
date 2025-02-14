from And import and_gate
from Not import not_gate

def dmux(i0,s0):
    """
    Simulates a 2:1 DMUX using logical gates built with nand.

    Args:
    input: The input
    sel: The control or select line (True or 1 for b (last output),False or 0 for a (first output))

    Return:
    True or false according to the following table:
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


