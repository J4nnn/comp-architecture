from nand_gate import nand_gate as nand

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

    return nand(nand(input1, input2), nand(input1, input2))

# Testing some examples. (It's working properly)
# print(and_gate(0, 0))
# print(and_gate(True, False))
# print(and_gate(0, True))
# print(and_gate(True, 1))
# print(and_gate(1, "a"))

# Reference: https://www.geeksforgeeks.org/implementation-and-from-nand/