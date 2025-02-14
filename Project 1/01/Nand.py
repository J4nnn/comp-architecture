def nand_gate(input1, input2):
    """
    Simulates a NAND logic gate using 0 and 1.
    
    Args:
    input1: The first input (0 or 1).
    input2: The second input (0 or 1).

    Returns:
    1 or 0 according to the following truth table:
    | a | b | q |
    | 0 | 0 | 1 |
    | 1 | 0 | 1 |
    | 0 | 1 | 1 |
    | 1 | 1 | 0 |
    """
    return 1 if not (input1 and input2)     else 0

print(" | NAND Truth Table | Result |")
print(" | A = 0, B = 0 | A NAND B =", nand_gate(0, 0), " | ")
print(" | A = 0, B = 1 | A NAND B =", nand_gate(0, 1), " | ")
print(" | A = 1, B = 0 | A NAND B =", nand_gate(1, 0), " | ")
print(" | A = 1, B = 1 | A NAND B =", nand_gate(1, 1), " | ")
