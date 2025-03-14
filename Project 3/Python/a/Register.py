from Bit import *

class Register:
    def __init__(self):
        # Crear 16 instancias de Bit para almacenar los 16 bits
        self.bits = [Bit() for _ in range(16)]

    def update(self, in_value, load, clk):
        """
        Actualiza el registro de 16 bits.
        :param in_value: Valor de entrada (entero con signo de 16 bits)
        :param load: Señal de carga (0 o 1)
        :param clk: Señal de reloj (0 o 1)
        :return: Valor de salida (entero con signo de 16 bits)
        """
        # Convertir el valor de entrada en una lista de 16 bits
        in_bits = self._int_to_bits(in_value)

        out_bits = []
        for i in range(16):
            # Actualizar cada bit individualmente
            out_bit = self.bits[i].update(in_bits[i], load, clk)
            out_bits.append(out_bit)

        # Convertir la lista de bits en un entero con signo
        out_value = self._bits_to_int(out_bits)
        return out_value

    def _int_to_bits(self, value):
        """
        Convierte un entero con signo de 16 bits en una lista de 16 bits.
        """
        if value < 0:
            value += 65536  # Convertir a equivalente positivo en 16 bits
        return [int(bit) for bit in f"{value:016b}"]

    def _bits_to_int(self, bits):
        """
        Convierte una lista de 16 bits en un entero con signo de 16 bits.
        """
        binary_str = "".join(str(bit) for bit in bits)
        value = int(binary_str, 2)
        if value >= 32768:  # Si es negativo en complemento a 2
            value -= 65536
        return value


# Función para simular el circuito en cada ciclo de tiempo
def simulate_circuit(inputs):
    # Instanciar el registro de 16 bits
    register = Register()

    # Encabezado de la tabla
    print("| time |   in   | load |  out   |")
    print("|------|--------|------|--------|")

    # Simular cada ciclo de tiempo
    for time, (in_value, load, clk) in enumerate(inputs):
        # Actualizar el registro
        out_value = register.update(in_value, load, clk)

        # Imprimir el estado actual
        print(f"| {time}+  | {in_value:6} |  {load}  | {out_value:6} |")
        print(f"| {time + 1}    | {in_value:6} |  {load}  | {out_value:6} |")


# Definir las entradas para cada ciclo de tiempo
inputs = [
    (0, 0, 1),        # time 0
    (0, 1, 1),        # time 1
    (-32123, 0, 1),   # time 2
    (11111, 0, 1),    # time 3
    (-32123, 1, 1),   # time 4
    (-32123, 1, 1),   # time 5
    (-32123, 0, 1),   # time 6
    (12345, 1, 1),    # time 7
    (0, 0, 1),        # time 8
    (0, 1, 1),        # time 9
    (1, 0, 1),        # time 10
    (1, 1, 1),        # time 11
    (2, 0, 1),        # time 12
    (2, 1, 1),        # time 13
    (4, 0, 1),        # time 14
    (4, 1, 1),        # time 15
    (8, 0, 1),        # time 16
    (8, 1, 1),        # time 17
    (16, 0, 1),       # time 18
    (16, 1, 1),       # time 19
    (32, 0, 1),       # time 20
    (32, 1, 1),       # time 21
    (64, 0, 1),       # time 22
    (64, 1, 1),       # time 23
    (128, 0, 1),      # time 24
    (128, 1, 1),      # time 25
    (256, 0, 1),      # time 26
    (256, 1, 1),      # time 27
    (512, 0, 1),      # time 28
    (512, 1, 1),      # time 29
    (1024, 0, 1),     # time 30
    (1024, 1, 1),     # time 31
    (2048, 0, 1),     # time 32
    (2048, 1, 1),     # time 33
    (4096, 0, 1),     # time 34
    (4096, 1, 1),     # time 35
    (8192, 0, 1),     # time 36
    (8192, 1, 1),     # time 37
    (16384, 0, 1),    # time 38
    (16384, 1, 1),    # time 39
    (-32768, 0, 1),   # time 40
    (-32768, 1, 1),   # time 41
    (-2, 0, 1),       # time 42
    (-2, 1, 1),       # time 43
    (-3, 0, 1),       # time 44
    (-3, 1, 1),       # time 45
    (-5, 0, 1),       # time 46
    (-5, 1, 1),       # time 47
    (-9, 0, 1),       # time 48
    (-9, 1, 1),       # time 49
    (-17, 0, 1),      # time 50
    (-17, 1, 1),      # time 51
    (-33, 0, 1),      # time 52
    (-33, 1, 1),      # time 53
    (-65, 0, 1),      # time 54
    (-65, 1, 1),      # time 55
    (-129, 0, 1),     # time 56
    (-129, 1, 1),     # time 57
    (-257, 0, 1),     # time 58
    (-257, 1, 1),     # time 59
    (-513, 0, 1),     # time 60
    (-513, 1, 1),     # time 61
    (-1025, 0, 1),    # time 62
    (-1025, 1, 1),    # time 63
    (-2049, 0, 1),    # time 64
    (-2049, 1, 1),    # time 65
    (-4097, 0, 1),    # time 66
    (-4097, 1, 1),    # time 67
    (-8193, 0, 1),    # time 68
    (-8193, 1, 1),    # time 69
    (-16385, 0, 1),   # time 70
    (-16385, 1, 1),   # time 71
    (32767, 0, 1),    # time 72
    (32767, 1, 1),    # time 73
]

simulate_circuit(inputs)