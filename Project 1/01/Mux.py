from And import and_gate
from Or import or_gate
from Not import not_gate

def mux (input1, input2, sel):
    """
    Simulates an 2:1 MUX using logical gates built with NAND.

    Args:
    i0, i1: The inputs (True or False, 1 or 0).
    s0: Single select line (True or 1 for i1, False or 0 for i0).

    Returns:
    True or False according to the following truth table:
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