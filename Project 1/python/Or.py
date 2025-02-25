from Nand import nand_gate

def or_gate (input1, input2):
    return nand_gate(nand_gate(input1, input1), nand_gate(input2, input2))

# Testing, it works
# print("a = 0, b = 0 -> ", or_gate(0, 0))
# print("a = 0, b = 1 -> ", or_gate(0, 1))
# print("a = 1, b = 0 -> ", or_gate(1, 0))
# print("a = 1, b = 1 -> ", or_gate(1, 1))