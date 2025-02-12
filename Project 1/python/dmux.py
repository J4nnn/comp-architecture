from and_gate import and_gate
from or_gate import or_gate
from not_gate import not_gate

def dmux(s0, i0):
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

#  Testing some examples. (It's working properly)
# print(dmux(0,  0))
# print(dmux(0,  1))
# print(dmux(1, 0))
# print(dmux(1, 1))
# print(dmux(True, "a"))

# Reference: https://www.geeksforgeeks.org/what-is-demultiplexerdemux/