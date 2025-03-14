class RAM4K:
    def __init__(self):
        self.memory = [[0] * 16 for _ in range(4096)]

    def tick(self, in_, load, address):
        if load:
            self.memory[address] = in_[:]
        return self.memory[address]

def DMux4Way(load, sel):
    load0 = load if sel == 0 else 0
    load1 = load if sel == 1 else 0
    load2 = load if sel == 2 else 0
    load3 = load if sel == 3 else 0
    return load0, load1, load2, load3

def Mux4Way16(a, b, c, d, sel):
    if sel == 0:
        return a
    elif sel == 1:
        return b
    elif sel == 2:
        return c
    elif sel == 3:
        return d
    else:
        raise ValueError("Selector fuera de rango")

class RAM16K:
    def __init__(self):
        self.ram0 = RAM4K()
        self.ram1 = RAM4K()
        self.ram2 = RAM4K()
        self.ram3 = RAM4K()

    def tick(self, in_, load, address):
        addr_low = address & 0xFFF  
        addr_high = (address >> 12) & 0x3  

        load0, load1, load2, load3 = DMux4Way(load, addr_high)

        out0 = self.ram0.tick(in_, load0, addr_low)
        out1 = self.ram1.tick(in_, load1, addr_low)
        out2 = self.ram2.tick(in_, load2, addr_low)
        out3 = self.ram3.tick(in_, load3, addr_low)

        return Mux4Way16(out0, out1, out2, out3, addr_high)


def int_to_bin_list(n, bits=16):
    """Convierte un número entero en una lista de bits de longitud fija."""
    if n < 0:
        n = (1 << bits) + n
    return [(n >> i) & 1 for i in range(bits)]

def bin_list_to_int(bits):
    """Convierte una lista de bits en número entero con signo."""
    n = sum([bit << i for i, bit in enumerate(bits)])
    if bits[-1] == 1:  
        n -= (1 << len(bits))
    return n

ram = RAM16K()


trace = []
time = 0

def print_trace():
    print("|time |   in   |load| address |   out  |")
    for entry in trace:
        t, in_, load, addr, out = entry
        t_str = f"{t:<5}"
        in_str = f"{in_:>7}"
        load_str = f"{load:>4}"
        addr_str = f"{addr:>7}"
        out_str = f"{out:>7}"
        print(f"| {t_str}| {in_str} |{load_str}| {addr_str} | {out_str} |")

def tick_and_record(ram, in_value, load, address):
    global time
    in_bits = int_to_bin_list(in_value)
    out_bits = ram.tick(in_bits, load, address)
    out_value = bin_list_to_int(out_bits)
    trace.append((time, in_value, load, address, out_value))
    time += 1


tick_and_record(ram, 0, 0, 0)
tick_and_record(ram, 0, 0, 0)
tick_and_record(ram, 0, 1, 0)
tick_and_record(ram, 0, 1, 0)
tick_and_record(ram, 4321, 0, 0)
tick_and_record(ram, 4321, 0, 0)
tick_and_record(ram, 4321, 1, 4321)
tick_and_record(ram, 4321, 1, 4321)
tick_and_record(ram, 4321, 0, 0)
tick_and_record(ram, 4321, 0, 0)
tick_and_record(ram, 12345, 0, 12345)
tick_and_record(ram, 12345, 0, 12345)
tick_and_record(ram, 12345, 1, 12345)
tick_and_record(ram, 12345, 1, 12345)
tick_and_record(ram, 12345, 0, 12345)
tick_and_record(ram, 12345, 0, 12345)
tick_and_record(ram, 12345, 0, 4321)
tick_and_record(ram, 16383, 0, 4321)
tick_and_record(ram, 16383, 0, 4321)
tick_and_record(ram, 16383, 1, 16383)
tick_and_record(ram, 16383, 1, 16383)
tick_and_record(ram, 16383, 0, 16383)
tick_and_record(ram, 16383, 0, 16383)
tick_and_record(ram, 16383, 0, 12345)
tick_and_record(ram, 16383, 0, 16383)

for addr in range(10920, 10928):
    tick_and_record(ram, 21845, 1, addr)

for addr in range(10920, 10928):
    tick_and_record(ram, 21845, 0, addr)


tick_and_record(ram, -21846, 1, 10920)
tick_and_record(ram, -21846, 0, 10920)


print_trace()
