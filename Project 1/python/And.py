from Nand import nand_gate

def and_gate(input1, input2):
    """
    Returns True (1) only when 'a' and 'b' are True (1); otherwise, it returns False (0).
    """
    return nand_gate(nand_gate(input1, input2), nand_gate(input1, input2))

# Testing, it works
# print("a = 0, b = 0 -> ", and_gate(0, 0))
# print("a = 0, b = 1 -> ", and_gate(0, 1))
# print("a = 1, b = 0 -> ", and_gate(1, 0))
# print("a = 1, b = 1 -> ", and_gate(1, 1))