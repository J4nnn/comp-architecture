from Mux import mux

def mux16(sel, input1_bits, input2_bits):
    """
    Selects and returns a 16-bit value from either input 'a' or input 'b', based on a single select bit.
    """
    return [int(mux(sel, input1_bits[bit], input2_bits[bit])) for bit in range(len(input1_bits))]

# Testing, it works
# print("sel = 0, input1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], input2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] -> ", mux16(0, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
# print("sel = 1, input1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], input2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] -> ", mux16(1, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
# print("sel = 0, input1 = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], input2 = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] -> ", mux16(0, [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]))
# print("sel = 1, input1 = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], input2 = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] -> ", mux16(1, [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]))
# print("sel = 0, input1 = [0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,0], input2 = [1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,1] -> ", mux16(0, [0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,0], [1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,1]))
# print("sel = 1, input1 = [0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,0], input2 = [1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,1] -> ", mux16(1, [0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,0], [1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,1]))