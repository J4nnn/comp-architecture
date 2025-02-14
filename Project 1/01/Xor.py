from Nand import nand_gate as nand

def xor_gate (input1, input2):
    """
    Simulates an XOR logic gate using NAND.
    
    Args:
    input1: The first input (True or False, 1 or 0).
    input2: The second input (True or False, 1 or 0).

    Returns:
    True or False according to the following truth table:
    | a | b | q |
    | 0 | 0 | 0 |
    | 1 | 0 | 1 |
    | 0 | 1 | 1 |
    | 1 | 1 | 0 |
    """

    return nand(nand(nand(input1, input1), input2), nand(input1, nand(input2, input2)))

print(" | XOR Truth Table | Result |")
print(" | A = 0, B = 0 | A XOR B =", xor_gate(0, 0), " | ")
print(" | A = 0, B = 1 | A XOR B =", xor_gate(0, 1), " | ")
print(" | A = 1, B = 0 | A XOR B =", xor_gate(1, 0), " | ")
print(" | A = 1, B = 1 | A XOR B =", xor_gate(1, 1), " | ")