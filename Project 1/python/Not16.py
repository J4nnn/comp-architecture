from Not import not_gate

def not16(input_bits):
    """
    Inverts each of the 16 bits of the input, producing a 16-bit output.
    """
    return [int(not_gate(bit)) for bit in input_bits] # int function for better view in tests.

# Testing, it works
# print("input = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] -> ", not16([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
# print("input = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] -> ", not16([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
# print("input = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] -> ", not16([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]))
# print("input = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0] -> ", not16([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]))
# print("input = [0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,0] -> ", not16([0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,0]))