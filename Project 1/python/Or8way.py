from Or import or_gate

def or8way(input_bits):
    """
    Returns True (1) if any of the 8 input bits are True (1); otherwise, it returns False (0)
    """
    or1 = or_gate(input_bits[0], input_bits[1])
    or2 = or_gate(input_bits[2], input_bits[3])
    or3 = or_gate(input_bits[4], input_bits[5])
    or4 = or_gate(input_bits[6], input_bits[7])
    or5 = or_gate(or1, or2)
    or6 = or_gate(or3, or4)
    or7 = or_gate(or5, or6)
    return or7

# Testing, it works
# print("input = [0,0,0,0,0,0,0,0] -> ", or8way([0,0,0,0,0,0,0,0]))
# print("input = [1,1,1,1,1,1,1,1] -> ", or8way([1,1,1,1,1,1,1,1]))
# print("input = [0,1,0,1,0,1,0,1] -> ", or8way([0,1,0,1,0,1,0,1]))
# print("input = [1,0,1,0,1,0,1,0] -> ", or8way([1,0,1,0,1,0,1,0]))
# print("input = [0,0,0,0,0,0,0,1] -> ", or8way([0,0,0,0,0,0,0,1]))
# print("input = [1,0,0,0,0,0,0,0] -> ", or8way([1,0,0,0,0,0,0,0]))
# print("input = [0,0,1,0,0,0,0,0] -> ", or8way([0,0,1,0,0,0,0,0]))
# print("input = [0,0,0,0,1,0,0,0] -> ", or8way([0,0,0,0,1,0,0,0]))
# print("input = [0,0,0,0,0,1,0,0] -> ", or8way([0,0,0,0,0,1,0,0]))
# print("input = [0,0,0,1,0,0,0,0] -> ", or8way([0,0,0,1,0,0,0,0]))
# print("input = [0,1,0,0,0,0,0,0] -> ", or8way([0,1,0,0,0,0,0,0]))
# print("input = [0,0,0,0,0,0,1,0] -> ", or8way([0,0,0,0,0,0,1,0]))