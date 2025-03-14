class DMux8Way:
    def __init__(self):
        self.in_value = 0
        self.sel = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0
        self.g = 0
        self.h = 0

    def update(self, in_value, sel):
        """
        Actualiza las salidas del demultiplexor.
        :param in_value: Valor de entrada (0 o 1)
        :param sel: Señal de selección (3 bits)
        :return: Salidas del demultiplexor (a, b, c, d, e, f, g, h)
        """
        self.in_value = in_value
        self.sel = sel

        # Reiniciar todas las salidas
        self.a = self.b = self.c = self.d = self.e = self.f = self.g = self.h = 0

        # Seleccionar la salida correspondiente
        if self.sel == 0:
            self.a = self.in_value
        elif self.sel == 1:
            self.b = self.in_value
        elif self.sel == 2:
            self.c = self.in_value
        elif self.sel == 3:
            self.d = self.in_value
        elif self.sel == 4:
            self.e = self.in_value
        elif self.sel == 5:
            self.f = self.in_value
        elif self.sel == 6:
            self.g = self.in_value
        elif self.sel == 7:
            self.h = self.in_value

        return self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h


class Register:
    def __init__(self):
        self.value = 0  # Valor inicial del registro

    def update(self, in_value, load, clk):
        """
        Actualiza el registro.
        :param in_value: Valor de entrada (16 bits)
        :param load: Señal de carga (0 o 1)
        :param clk: Señal de reloj (0 o 1)
        :return: Valor de salida (16 bits)
        """
        if clk:  # Solo actualiza en el flanco de subida del reloj
            if load:
                self.value = in_value
        return self.value


class Mux8Way16:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0
        self.g = 0
        self.h = 0
        self.sel = 0
        self.out = 0

    def update(self, a, b, c, d, e, f, g, h, sel):
        """
        Actualiza la salida del multiplexor.
        :param a: Valor de entrada a (16 bits)
        :param b: Valor de entrada b (16 bits)
        :param c: Valor de entrada c (16 bits)
        :param d: Valor de entrada d (16 bits)
        :param e: Valor de entrada e (16 bits)
        :param f: Valor de entrada f (16 bits)
        :param g: Valor de entrada g (16 bits)
        :param h: Valor de entrada h (16 bits)
        :param sel: Señal de selección (3 bits)
        :return: Salida del multiplexor (16 bits)
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.sel = sel

        if self.sel == 0:
            self.out = self.a
        elif self.sel == 1:
            self.out = self.b
        elif self.sel == 2:
            self.out = self.c
        elif self.sel == 3:
            self.out = self.d
        elif self.sel == 4:
            self.out = self.e
        elif self.sel == 5:
            self.out = self.f
        elif self.sel == 6:
            self.out = self.g
        elif self.sel == 7:
            self.out = self.h

        return self.out


class RAM8:
    def __init__(self):
        self.dmux = DMux8Way()
        self.registers = [Register() for _ in range(8)]  # 8 registros de 16 bits
        self.mux = Mux8Way16()

    def update(self, in_value, load, address, clk):
        """
        Actualiza la RAM8.
        :param in_value: Valor de entrada (16 bits)
        :param load: Señal de carga (0 o 1)
        :param address: Dirección de 3 bits (0 a 7)
        :param clk: Señal de reloj (0 o 1)
        :return: Valor de salida (16 bits)
        """
        # Demultiplexar la señal de carga
        load_signals = self.dmux.update(load, address)

        # Actualizar los registros
        out_values = []
        for i in range(8):
            out_value = self.registers[i].update(in_value, load_signals[i], clk)
            out_values.append(out_value)

        # Multiplexar la salida
        out = self.mux.update(
            out_values[0], out_values[1], out_values[2], out_values[3],
            out_values[4], out_values[5], out_values[6], out_values[7],
            address
        )

        return out


# Función para simular el circuito en cada ciclo de tiempo
def simulate_ram8(inputs):
    # Instanciar la RAM8
    ram8 = RAM8()

    # Encabezado de la tabla
    print("| time |   in   |load |address|  out   |")
    print("|------|--------|-----|-------|--------|")

    # Simular cada ciclo de tiempo
    for time, (in_value, load, address, clk) in enumerate(inputs):
        # Actualizar la RAM8
        out_value = ram8.update(in_value, load, address, clk)

        # Imprimir el estado actual
        print(f"| {time}+  | {in_value:6} |  {load}  |   {address}   | {out_value:6} |")
        print(f"| {time + 1}    | {in_value:6} |  {load}  |   {address}   | {out_value:6} |")


# Definir las entradas para cada ciclo de tiempo
inputs = [
    (0, 0, 0, 1),      # time 0: Mantener
    (0, 1, 0, 1),      # time 1: Cargar 0 en el registro 0
    (11111, 0, 0, 1),  # time 2: Leer el registro 0 (debería ser 0)
    (11111, 1, 1, 1),  # time 3: Cargar 11111 en el registro 1
    (11111, 0, 0, 1),  # time 4: Leer el registro 0 (debería ser 0)
    (3333, 0, 3, 1),   # time 5: Leer el registro 3 (debería ser 0)
    (3333, 1, 3, 1),   # time 6: Cargar 3333 en el registro 3
    (3333, 0, 3, 1),   # time 7: Leer el registro 3 (debería ser 3333)
    (7777, 0, 1, 1),   # time 8: Leer el registro 1 (debería ser 11111)
    (7777, 1, 7, 1),   # time 9: Cargar 7777 en el registro 7
    (7777, 0, 7, 1),   # time 10: Leer el registro 7 (debería ser 7777)
    (21845, 1, 0, 1),  # time 11: Cargar 21845 en el registro 0
    (21845, 1, 1, 1),  # time 12: Cargar 21845 en el registro 1
    (21845, 1, 2, 1),  # time 13: Cargar 21845 en el registro 2
    (21845, 1, 3, 1),  # time 14: Cargar 21845 en el registro 3
    (21845, 1, 4, 1),  # time 15: Cargar 21845 en el registro 4
    (21845, 1, 5, 1),  # time 16: Cargar 21845 en el registro 5
    (21845, 1, 6, 1),  # time 17: Cargar 21845 en el registro 6
    (21845, 1, 7, 1),  # time 18: Cargar 21845 en el registro 7
    (-21846, 1, 0, 1), # time 19: Cargar -21846 en el registro 0
    (-21846, 0, 0, 1), # time 20: Leer el registro 0 (debería ser -21846)
    (21845, 1, 0, 1),  # time 21: Cargar 21845 en el registro 0
    (-21846, 1, 1, 1), # time 22: Cargar -21846 en el registro 1
    (-21846, 0, 1, 1), # time 23: Leer el registro 1 (debería ser -21846)
    (21845, 1, 1, 1),  # time 24: Cargar 21845 en el registro 1
    (-21846, 1, 2, 1), # time 25: Cargar -21846 en el registro 2
    (-21846, 0, 2, 1), # time 26: Leer el registro 2 (debería ser -21846)
    (21845, 1, 2, 1),  # time 27: Cargar 21845 en el registro 2
    (-21846, 1, 3, 1), # time 28: Cargar -21846 en el registro 3
    (-21846, 0, 3, 1), # time 29: Leer el registro 3 (debería ser -21846)
    (21845, 1, 3, 1),  # time 30: Cargar 21845 en el registro 3
    (-21846, 1, 4, 1), # time 31: Cargar -21846 en el registro 4
    (-21846, 0, 4, 1), # time 32: Leer el registro 4 (debería ser -21846)
    (21845, 1, 4, 1),  # time 33: Cargar 21845 en el registro 4
    (-21846, 1, 5, 1), # time 34: Cargar -21846 en el registro 5
    (-21846, 0, 5, 1), # time 35: Leer el registro 5 (debería ser -21846)
    (21845, 1, 5, 1),  # time 36: Cargar 21845 en el registro 5
    (-21846, 1, 6, 1), # time 37: Cargar -21846 en el registro 6
    (-21846, 0, 6, 1), # time 38: Leer el registro 6 (debería ser -21846)
    (21845, 1, 6, 1),  # time 39: Cargar 21845 en el registro 6
    (-21846, 1, 7, 1), # time 40: Cargar -21846 en el registro 7
    (-21846, 0, 7, 1), # time 41: Leer el registro 7 (debería ser -21846)
    (21845, 1, 7, 1),  # time 42: Cargar 21845 en el registro 7
    (21845, 0, 0, 1),  # time 43: Leer el registro 0 (debería ser 21845)
    (21845, 0, 1, 1),  # time 44: Leer el registro 1 (debería ser 21845)
    (21845, 0, 2, 1),  # time 45: Leer el registro 2 (debería ser 21845)
    (21845, 0, 3, 1),  # time 46: Leer el registro 3 (debería ser 21845)
    (21845, 0, 4, 1),  # time 47: Leer el registro 4 (debería ser 21845)
    (21845, 0, 5, 1),  # time 48: Leer el registro 5 (debería ser 21845)
    (21845, 0, 6, 1),  # time 49: Leer el registro 6 (debería ser 21845)
    (21845, 0, 7, 1),  # time 50: Leer el registro 7 (debería ser 21845)
]

simulate_ram8(inputs)