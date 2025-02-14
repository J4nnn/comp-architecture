from Nand import nand_gate as nand

def not_gate(input):
    """
    Simulates a NOT logic gate using NAND.

    Args:
    input: True or False, 1 or 0. They must be the same value.

    Returns:
    True or False according to the following truth table:
    | a | q |
    | 0 | 1 |
    | 1 | 0 |
    """

    return nand(input, input)

print(" | NOT Truth Table | Result |")
print(" | A = 0 | NOT A =", not_gate(0), " | ")
print(" | A = 1 | NOT A =", not_gate(1), " | ")