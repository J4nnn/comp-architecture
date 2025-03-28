class RAM4K:
    def __init__(self):
        self.memory = [0] * 4096  # Memoria de 4096 posiciones de 16 bits

    def tick(self, in_, load, address):
        if load:
            self.memory[address] = in_ & 0xFFFF  # Mantener en 16 bits
        return self.memory[address]


class RAM16K:
    def __init__(self):
        self.memory = [0] * 16384  # 16K palabras de 16 bits

    def tick(self, in_, load, address):
        """Simula una lectura/escritura en la RAM16K."""
        if load:
            self.memory[address] = in_ & 0xFFFF  # Limitar a 16 bits
        return self.memory[address]


class RAM32K:
    def __init__(self):
        self.ram0 = RAM16K()  # RAM 0-16383
        self.ram1 = RAM16K()  # RAM 16384-32767
        self.screen = [0] * (24576 - 16384)  # Pantalla (8192 posiciones)
        self.kbd = 0  # Teclado

    def tick(self, in_, load, address):
        """Simula una escritura/lectura en la memoria."""
        if 0 <= address < 16384:  # RAM normal
            return self.ram0.tick(in_, load, address)
        elif 16384 <= address < 24576:  # Pantalla
            index = address - 16384
            if load:
                self.screen[index] = in_
            return self.screen[index]
        elif address == 24576:  # Teclado
            if load:
                self.kbd = in_
            return self.kbd
        else:  # Segunda mitad de la RAM
            return self.ram1.tick(in_, load, address - 16384)


def binary_to_int(value):
    """Convierte un número binario de 16 bits en complemento a dos a entero."""
    value &= 0xFFFF  # Asegurar 16 bits
    return value if value < 0x8000 else value - 0x10000  # Manejo de signo


def int_to_binary(value):
    """Convierte un número entero a un valor de 16 bits en complemento a dos."""
    return value & 0xFFFF  # Limitar a 16 bits


def ALU(x, y, zx, nx, zy, ny, f, no):
    """Implementa la ALU de Nand2Tetris."""
    x = binary_to_int(x)
    y = binary_to_int(y)

    if zx: x = 0
    if nx: x = ~x & 0xFFFF
    if zy: y = 0
    if ny: y = ~y & 0xFFFF

    out = (x + y) if f else (x & y)

    if no:
        out = ~out & 0xFFFF  # Asegurar 16 bits

    out = int_to_binary(out)

    zr = 1 if out == 0 else 0
    ng = 1 if binary_to_int(out) < 0 else 0

    return out, zr, ng


class Multiplier:
    def __init__(self):
        self.RAM = RAM32K()
        self.alu = ALU

    def multiply(self):
        """Multiplica R0 y R1 usando sumas repetitivas."""
        k = 0  # Acumulador del resultado
        c = 0  # Contador de iteraciones
        r0 = binary_to_int(self.RAM.tick(0, 0, 0))  # Leer RAM[0]
        r1 = binary_to_int(self.RAM.tick(0, 0, 1))  # Leer RAM[1]

        # Manejo de valores negativos
        neg_result = (r0 < 0) ^ (r1 < 0)
        r0, r1 = abs(r0), abs(r1)  # Operamos con valores absolutos

        # Caso especial: si R1 es 0, el resultado debe ser 0
        if r1 == 0:
            self.RAM.tick(0, 1, 2)  # Guardar 0 en RAM[2]
            return

        # Sumas repetitivas
        while c < r1:
            k, _, _ = self.alu(k, r0, 0, 0, 0, 0, 1, 0)
            c, _, _ = self.alu(c, 1, 0, 0, 0, 0, 1, 0)

        # Convertir resultado a complemento a dos si es negativo
        if neg_result:
            k = int_to_binary(-binary_to_int(k))

        self.RAM.tick(k, 1, 2)  # Guardar resultado en RAM[2]

    def print_ram_state(self):
        """Muestra el estado de la memoria en posiciones clave."""
        r0 = binary_to_int(self.RAM.tick(0, 0, 0))
        r1 = binary_to_int(self.RAM.tick(0, 0, 1))
        r2 = binary_to_int(self.RAM.tick(0, 0, 2))
        print(f"|  RAM[0]  |  RAM[1]  |  RAM[2]  |")
        print(f"|{r0:>8}  |{r1:>8}  |{r2:>8}  |")

    def run(self, test_cases):
        """Ejecuta la simulación con diferentes valores de entrada."""
        for r0, r1 in test_cases:
            self.RAM.tick(int_to_binary(r0), 1, 0)  # Cargar R0 en RAM[0]
            self.RAM.tick(int_to_binary(r1), 1, 1)  # Cargar R1 en RAM[1]
            self.RAM.tick(0, 1, 2)  # Resetear R2
            self.multiply()
            self.print_ram_state()
            print("---")


# Casos de prueba
cases = [
    (0, 0), (1, 0), (0, 2), (3, 1), (2, 4), (6, 7), 
    (-2, 3), (4, -5), (-3, -2), (32767, 1), (-32768, 1)
]

# Ejecutar el simulador
simulator = Multiplier()
simulator.run(cases)
