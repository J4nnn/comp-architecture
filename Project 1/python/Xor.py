from Nand import nand_gate
from Or import or_gate
from And import and_gate

def xor_gate (input1, input2):
    """
    Returns True (1) only when 'a' and 'b' are different; otherwise, it returns False (0).
    """
    return and_gate(nand_gate(input1, input2), or_gate(input1, input2))

# Testing, it works
# print("a = 0, b = 0 -> ", xor_gate(0, 0))
# print("a = 0, b = 1 -> ", xor_gate(0, 1))
# print("a = 1, b = 0 -> ", xor_gate(1, 0))
# print("a = 1, b = 1 -> ", xor_gate(1, 1))