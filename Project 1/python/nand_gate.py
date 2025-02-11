def nand_gate(input1, input2):
    """
    Simulates a NAND logic gate.

    Args:
    input1: The first input (True or False, 1 or 0).
    input2: The second input (True or False, 1 or 0).

    Returns:
    True or False, 1 or 0 according to the following truth table:
    | a | b | q |
    | 0 | 0 | 1 |
    | 1 | 0 | 1 |
    | 0 | 1 | 1 |
    | 1 | 1 | 0 |
    """

    valid_inputs = {1, 0, True, False}

    if input1 in valid_inputs and input2 in valid_inputs:
        return not (input1 and input2)
    else:
        return "The input values aren't valid."

# Testing some examples. (It's working properly)
# print(nand_gate(0, 0))
# print(nand_gate(True, False))
# print(nand_gate(0, True))
# print(nand_gate(True, 1))
# print(nand_gate(1, "a"))