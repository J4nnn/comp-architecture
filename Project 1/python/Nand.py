def nand_gate(input1, input2):
    """
    Returns False (0) only when 'a' and 'b' are True (1); otherwise, it returns True (1).
    """
    return not (input1 and input2)

# Testing, it works
# print("a = 0, b = 0 -> ", nand_gate(0, 0))
# print("a = 0, b = 1 -> ", nand_gate(0, 1))
# print("a = 1, b = 0 -> ", nand_gate(1, 0))
# print("a = 1, b = 1 -> ", nand_gate(1, 1))