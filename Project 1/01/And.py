from Nand import nand_gate as nand

def and_gate(input1, input2):
    """
    Simulates an AND logic gate using NAND.

    Args:
    input1: The first input (True or False, 1 or 0).
    input2: The second input (True or False, 1 or 0).

    Returns:
    True or False according to the following truth table:
    | a | b | q |
    | 0 | 0 | 0 |
    | 1 | 0 | 0 |
    | 0 | 1 | 0 |
    | 1 | 1 | 1 |
    """
    return 1 - nand(input1, input2)

print(" | AND Truth Table | Result |")
print(" | A = 0, B = 0 | A AND B =", and_gate(0, 0), " | ")
print(" | A = 0, B = 1 | A AND B =", and_gate(0, 1), " | ")
print(" | A = 1, B = 0 | A AND B =", and_gate(1, 0), " | ")
print(" | A = 1, B = 1 | A AND B =", and_gate(1, 1), " | ")