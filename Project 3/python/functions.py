def nand_gate(input1, input2):
    return not (input1 and input2)

def and_gate(input1, input2):
    return nand_gate(nand_gate(input1, input2), nand_gate(input1, input2))

def and16(input1_bits, input2_bits):
    return [int(and_gate(input1_bits[bit], input2_bits[bit])) for bit in range(len(input1_bits))]

def not_gate(input):
    return nand_gate(input, input)

def not16(input_bits):
    return [int(not_gate(bit)) for bit in input_bits]

def or_gate (input1, input2):
    return nand_gate(nand_gate(input1, input1), nand_gate(input2, input2))

def or16(input1_bits, input2_bits):
    return [int(or_gate(input1_bits[bit], input2_bits[bit])) for bit in range(len(input2_bits))]

def xor_gate (input1, input2):
    return and_gate(nand_gate(input1, input2), or_gate(input1, input2))

def or8way(input_bits):
    or1 = or_gate(input_bits[0], input_bits[1])
    or2 = or_gate(input_bits[2], input_bits[3])
    or3 = or_gate(input_bits[4], input_bits[5])
    or4 = or_gate(input_bits[6], input_bits[7])
    or5 = or_gate(or1, or2)
    or6 = or_gate(or3, or4)
    or7 = or_gate(or5, or6)
    return or7

def mux (sel, input1, input2):
    return or_gate(and_gate(input1, not_gate(sel)), and_gate(input2, sel))

def dmux(sel, input):
    return and_gate(input, not_gate(sel)), and_gate(input, sel)

def dmux4way(sel1, sel2, input):
    a, b = dmux(sel1, input)
    q1, q2 = dmux(sel2, a)
    q3, q4 = dmux(sel2, b)
    return int(q1), int(q2), int(q3), int(q4)

def dmux8way(sel1, sel2, sel3, input):
    a, b = dmux(sel1, input)
    c, d, e, f = dmux4way(sel2, sel3, a)
    g, h, i, j = dmux4way(sel2, sel3, b)
    return c, d, e, f, g, h, i, j

def mux16(sel, input1_bits, input2_bits):
    return [int(mux(sel, input1_bits[bit], input2_bits[bit])) for bit in range(len(input1_bits))]

def mux4way16(sel1, sel2, input1_bits, input2_bits, input3_bits, input4_bits):
    return mux16(sel1 ,mux16(sel2, input1_bits, input2_bits), mux16(sel2, input3_bits, input4_bits))

def mux8way16(sel1, sel2, sel3, input1_bits, input2_bits, input3_bits, input4_bits, input5_bits, input6_bits, input7_bits, input8_bits):
    return mux16(sel1, mux4way16(sel2, sel3, input1_bits, input2_bits, input3_bits, input4_bits), mux4way16(sel2, sel3, input5_bits, input6_bits, input7_bits, input8_bits))

def half_adder(input1, input2):
    carry = and_gate(input1, input2)
    sum_result = xor_gate(input1, input2)
    return int(sum_result), int(carry)

def full_adder(input1, input2, c_in):
    sum_1, carry1 = half_adder(input1, input2)
    sum_2, carry2 = half_adder(sum_1, c_in)
    c_out = or_gate(carry1, carry2)
    return int(sum_2), int(c_out)

def add16(input1_bits, input2_bits):
    result = []
    carry = 0
    for bit in range(16):
        sum_bit, carry = full_adder(input1_bits[bit], input2_bits[bit], carry)
        result.append(sum_bit)
    return result # The most-significant carry bit is ignored

def inc16(input_bits):
    one = [0] * 16
    one[0] = 1
    return add16(one, input_bits)

