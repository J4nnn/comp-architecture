from nand_gate import nand_gate as nand

def or_gate (input1, input2):
    """
    Simulates an OR logic gate using NAND.
    
    Args:
    input1: The first input (True or False, 1 or 0).
    input2: The second input (True or False, 1 or 0).

    Returns:
    True or False according to the following truth table:
    | a | b | q |
    | 0 | 0 | 0 |
    | 1 | 0 | 1 |
    | 0 | 1 | 1 |
    | 1 | 1 | 1 |
    """

    return nand(nand(input1, input1), nand(input2, input2))

# Testing some examples. (It's working properly)
# print(or_gate(0, 0))
# print(or_gate(True, False))
# print(or_gate(0, True))
# print(or_gate(True, 1))
# print(or_gate(1, "a"))

# Reference: https://www.geeksforgeeks.org/implementation-of-or-gate-from-nand-gate/