from Mux16 import mux16

def mux4way16(sel1, sel2, input1_bits, input2_bits, input3_bits, input4_bits):
    """
    Selects and returns one of four 16-bit inputs based on a 2-bit select signal.
    """
    return mux16(sel1 ,mux16(sel2, input1_bits, input2_bits), mux16(sel2, input3_bits, input4_bits))

# Testing, it works
# input1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# input2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# input3 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# input4 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# print("sel1 = 0, sel2 = 0 -> ", mux4way16(0, 0, input1, input2, input3, input4))  # input1
# print("sel1 = 0, sel2 = 1 -> ", mux4way16(0, 1, input1, input2, input3, input4))  # input3
# print("sel1 = 1, sel2 = 0 -> ", mux4way16(1, 0, input1, input2, input3, input4))  # input2
# print("sel1 = 1, sel2 = 1 -> ", mux4way16(1, 1, input1, input2, input3, input4))  # input4