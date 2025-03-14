class RAM8:
    def __init__(self):
        self.registers = [0] * 8  # 8 palabras de 16 bits cada una

    def update(self, input_value, load, address):
        if load:
            self.registers[address] = input_value
        return self.registers[address]

class RAM64:
    def __init__(self):
        # 8 bloques de RAM8
        self.rams = [RAM8() for _ in range(8)]

    def update(self, input_value, load, address):
        # Partimos la dirección en dos partes:
        # address[3..5] selecciona el RAM8
        ram_index = (address >> 3) & 0b111
        # address[0..2] selecciona la dirección dentro del RAM8
        ram_address = address & 0b111

        # Generamos señales de carga individuales para cada RAM8 (como el DMux8Way)
        outputs = []
        for i in range(8):
            ram_load = load if i == ram_index else 0
            outputs.append(self.rams[i].update(input_value, ram_load, ram_address))

        # Elige cuál salida va al exterior (como el Mux8Way16)
        out = outputs[ram_index]
        return out

def run_test():
    ram64 = RAM64()
    time = 0

    # Este es el formato del encabezado de tu tabla
    print("| time |   in   |load |address|  out   |")

    # Estado inicial
    inputs = [
        # (in_value, load, address)
        (0,      0,   0),  # time 0+
        (0,      0,   0),  # time 1
        (0,      1,   0),  # time 1+
        (0,      1,   0),  # time 2
        (1313,   0,   0),  # time 2+
        (1313,   0,   0),  # time 3
        (1313,   1,   13), # time 3+
        (1313,   1,   13), # time 4
        (1313,   0,   0),  # time 4+
        (1313,   0,   0),  # time 5
        (4747,   0,   47), # time 5+
        (4747,   0,   47), # time 6
        (4747,   1,   47), # time 6+
        (4747,   1,   47), # time 7
        (4747,   0,   47), # time 7+
        (4747,   0,   47), # time 8
        (4747,   0,   13), # time 8
        (6363,   0,   13), # time 8+
        (6363,   0,   13), # time 9
        (6363,   1,   63), # time 9+
        (6363,   1,   63), # time 10
        (6363,   0,   63), # time 10+
        (6363,   0,   63), # time 11
    ]

    # Simulando los ciclos
    for i, (in_val, load, address) in enumerate(inputs):
        out = ram64.update(in_val, load, address)
        suffix = "+" if i % 2 == 0 else " "  # "+" en los ciclos de transición
        print(f"| {time}{suffix:<3} | {in_val:6} |  {load}  | {address:5} | {out:6} |")

        if suffix == " ":
            time += 1

run_test()
