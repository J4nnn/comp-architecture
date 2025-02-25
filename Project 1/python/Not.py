from Nand import nand_gate

def not_gate(input):
    """
    Inverts the input: True (1) becomes False (0), and False (0) becomes True (1).
    """
    return nand_gate(input, input)

# Testing, it works
# print("a = 0 -> ", not_gate(0))
# print("a = 1 -> ", not_gate(1))