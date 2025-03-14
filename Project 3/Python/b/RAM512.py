class RAM64:
    def __init__(self):
        self.mem = [0] * 64

    def update(self, in_value, load, address):
        if load:
            self.mem[address] = in_value
        return self.mem[address]

class RAM512:
    def __init__(self):
        self.blocks = [RAM64() for _ in range(8)]

    def update(self, in_value, load, address):
        block_index = (address >> 6) & 0b111  # address[6..8]
        inner_address = address & 0b111111     # address[0..5]

        # load signals for each block via DMux8Way
        load_signals = [0] * 8
        if load:
            load_signals[block_index] = 1

        # update all blocks, but only one has load=1
        outs = []
        for i in range(8):
            out = self.blocks[i].update(in_value, load_signals[i], inner_address)
            outs.append(out)

        # output via Mux8Way16
        return outs[block_index]


ram = RAM512()

def print_line(time, in_val, load, address, out_val, plus=False):
    plus_sign = '+' if plus else ' '
    print(f"| {str(time)+plus_sign:<4} | {in_val:>6} | {load:^5} | {address:^7} | {out_val:>6} |")


sequence = [
    # (time, in, load, address)
    (0,     0,       0,    0),
    (1,     0,       0,    0),
    (1.5,   0,       1,    0),
    (2,     0,       1,    0),
    (2.5,   13099,   0,    0),
    (3,     13099,   0,    0),
    (3.5,   13099,   1,    130),
    (4,     13099,   1,    130),
    (4.5,   13099,   0,    0),
    (5,     13099,   0,    0),
    (5.5,   4729,    0,    472),
    (6,     4729,    0,    472),
    (6.5,   4729,    1,    472),
    (7,     4729,    1,    472),
    (7.5,   4729,    0,    472),
    (8,     4729,    0,    472),
    (8.5,   5119,    0,    130),
    (9,     5119,    0,    130),
    (9.5,   5119,    1,    511),
    (10,    5119,    1,    511),
    (10.5,  5119,    0,    511),
    (11,    5119,    0,    511),
]

print("| time |   in   |load |address|  out   |")
print("|------|--------|-----|-------|--------|")

current_time = 0
for entry in sequence:
    time, in_val, load, addr = entry
    plus = (int(time) != time)
    current_time = int(time)
    
    out_val = ram.update(in_val, load, addr)
    print_line(current_time, in_val, load, addr, out_val, plus=plus)
