from Mux16 import mux16
from Mux4way16 import mux4way16

def mux8way16(sel1, sel2, sel3, input1_bits, input2_bits, input3_bits, input4_bits, input5_bits, input6_bits, input7_bits, input8_bits):
    """
    Selects and returns one of four 16-bit inputs based on a 3-bit select signal.
    """
    return mux16(sel1, mux4way16(sel2, sel3, input1_bits, input2_bits, input3_bits, input4_bits), mux4way16(sel2, sel3, input5_bits, input6_bits, input7_bits, input8_bits))

# Testing, it works
# input1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# input2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# input3 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# input4 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
# input5 = [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
# input6 = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1]
# input7 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1]
# input8 = [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0]

# print("sel=000 -> ", mux8way16(0, 0, 0, input1, input2, input3, input4, input5, input6, input7, input8))
# print("sel=001 -> ", mux8way16(0, 0, 1, input1, input2, input3, input4, input5, input6, input7, input8))
# print("sel=010 -> ", mux8way16(0, 1, 0, input1, input2, input3, input4, input5, input6, input7, input8))
# print("sel=011 -> ", mux8way16(0, 1, 1, input1, input2, input3, input4, input5, input6, input7, input8))
# print("sel=100 -> ", mux8way16(1, 0, 0, input1, input2, input3, input4, input5, input6, input7, input8))
# print("sel=101 -> ", mux8way16(1, 0, 1, input1, input2, input3, input4, input5, input6, input7, input8))
# print("sel=110 -> ", mux8way16(1, 1, 0, input1, input2, input3, input4, input5, input6, input7, input8))
# print("sel=111 -> ", mux8way16(1, 1, 1, input1, input2, input3, input4, input5, input6, input7, input8))
