from nand_gate import nand_gate

def not_gate(input):
    """
    Simulates a NOT logic gate using NAND.

    Args:
    input: True or False, 1 or 0. They must be the same value.

    Returns:
    True or False, 1 or 0 according to the following truth table:
    | a | q |
    | 0 | 1 |
    | 1 | 0 |
    """
    return nand_gate(input, input)

# Testing some examples
print(not_gate(1))
print(not_gate(0))
print(not_gate("a"))