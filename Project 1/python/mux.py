from and_gate import and_gate
from or_gate import or_gate
from not_gate import not_gate

def mux (s0, i0, i1):
    """
    Simulates an 2:1 MUX using logical gates built with NAND.

    Args:
    i0, i1: The input lines (True or False, 1 or 0).
    s0: Single select line (True or 1 for i1, False or 0 for i0).

    Returns:
    True or False according to the following truth table:
    | s0 | i0 | i1 | q |
    | 0  | 0  | X  | 0 |
    | 0  | 1  | X  | 1 |
    | 1  | X  | 0  | 0 |
    | 1  | X  | 1  | 1 |
    """

    # This implementation is made taking as reference 2x1 multiplexer circuit diagram
    return or_gate(and_gate(i0, not_gate(s0)), and_gate(i1, s0))

#  Testing some examples. (It's working properly)
# print(mux(0, 0, 1))
# print(mux(0, 1, 0))
# print(mux(1, 1, 0))
# print(mux(1, 0, 1))
# print(mux(True, True, "a"))

# Reference: https://www.geeksforgeeks.org/multiplexers-in-digital-logic/