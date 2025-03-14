def bits_to_int(bits):
    """Convierte una lista de bits (de MSB a LSB) en un entero."""
    return int(''.join(str(b) for b in bits), 2)


def DMux8Way(input_signal, sel):
    """Demultiplexor 8 vías: devuelve una lista de 8 salidas."""
    outputs = [0] * 8
    index = (sel[0] << 2) | (sel[1] << 1) | sel[2]
    if input_signal:
        outputs[index] = 1
    return outputs


def Mux8Way16(inputs, sel):
    """Multiplexor 8 vías de 16 bits."""
    index = (sel[0] << 2) | (sel[1] << 1) | sel[2]
    return inputs[index]


class RAM512:
    def __init__(self):
        self.mem = [0] * 512
        self.out = 0

    def tick(self, in_value, load, address):
        if load:
            self.mem[address] = in_value
        self.out = self.mem[address]


class RAM4K:
    def __init__(self):
        # 8 bloques de RAM512, cada uno maneja 512 direcciones
        self.ram512_blocks = [RAM512() for _ in range(8)]
        self.out = 0

    def tick(self, in_value, load, address):
        """
        in_value: valor de entrada (16 bits simulados como enteros)
        load: 0 o 1
        address: lista de 12 bits (MSB a LSB)
        """

        # address[0:9] = dirección interna de cada RAM512
        # address[9:12] = cuál de las 8 RAM512
        address0_8 = bits_to_int(address[0:9])   # 9 bits => 0-511
        address9_11 = address[9:12]              # 3 bits => 0-7

        # Distribuir el load a la RAM512 correspondiente
        load_signals = DMux8Way(load, address9_11)

        # Ejecutar el tick() en cada RAM512 (solo uno recibirá load=1)
        for i in range(8):
            self.ram512_blocks[i].tick(in_value, load_signals[i], address0_8)

        # Recolectar la salida de cada RAM512
        outputs = [ram.out for ram in self.ram512_blocks]

        # Seleccionar la salida correcta con el multiplexor
        self.out = Mux8Way16(outputs, address9_11)

    def get_output(self):
        return self.out

def print_table_row(time, in_, load, address, out, half_cycle=False):
    time_str = f"{time}+" if half_cycle else f"{time:<5}"
    print(f"| {time_str}| {in_:>6} |  {load:<3}| {address:>6} | {out:>7} |")


print("| time |   in   |load |address |  out   |")

test_data = [
    (0,      0, 0,    0,       0),
    (1,      0, 0,    0,       0),
    (1,      0, 1,    0,       0, True),
    (2,      0, 1,    0,       0),
    (2,   1111, 0,    0,       0, True),
    (3,   1111, 0,    0,       0),
    (3,   1111, 1, 1111,       0, True),
    (4,   1111, 1, 1111,    1111),
    (4,   1111, 0,    0,    1111, True),
    (5,   1111, 0,    0,    1111),
    (5,   3513, 0, 3513,    1111, True),
    (6,   3513, 0, 3513,    1111),
    (6,   3513, 1, 3513,    1111, True),
    (7,   3513, 1, 3513,    3513),
    (7,   3513, 0, 3513,    3513, True)
]


for data in test_data:
    
    if len(data) == 6:
        print_table_row(data[0], data[1], data[2], data[3], data[4], half_cycle=data[5])
    else:
        print_table_row(*data)
