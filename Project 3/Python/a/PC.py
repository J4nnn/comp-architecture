class Not:
    def __init__(self):
        self.in_value = 0
        self.out = 0

    def update(self, in_value):
        """
        Actualiza la salida de la compuerta NOT.
        :param in_value: Valor de entrada (0 o 1)
        :return: Salida de la compuerta NOT (0 o 1)
        """
        self.in_value = in_value
        self.out = 1 if self.in_value == 0 else 0
        return self.out


class And:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.out = 0

    def update(self, a, b):
        """
        Actualiza la salida de la compuerta AND.
        :param a: Valor de entrada a (0 o 1)
        :param b: Valor de entrada b (0 o 1)
        :return: Salida de la compuerta AND (0 o 1)
        """
        self.a = a
        self.b = b
        self.out = 1 if (self.a == 1 and self.b == 1) else 0
        return self.out


class Or:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.out = 0

    def update(self, a, b):
        """
        Actualiza la salida de la compuerta OR.
        :param a: Valor de entrada a (0 o 1)
        :param b: Valor de entrada b (0 o 1)
        :return: Salida de la compuerta OR (0 o 1)
        """
        self.a = a
        self.b = b
        self.out = 1 if (self.a == 1 or self.b == 1) else 0
        return self.out


class Mux16:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.sel = 0
        self.out = 0

    def update(self, a, b, sel):
        """
        Actualiza la salida del multiplexor.
        :param a: Valor de entrada a (16 bits)
        :param b: Valor de entrada b (16 bits)
        :param sel: Señal de selección (0 o 1)
        :return: Salida del multiplexor (16 bits)
        """
        self.a = a
        self.b = b
        self.sel = sel
        self.out = self.a if self.sel == 0 else self.b
        return self.out


class Inc16:
    def __init__(self):
        self.in_value = 0
        self.out = 0

    def update(self, in_value):
        """
        Incrementa el valor de entrada en 1.
        :param in_value: Valor de entrada (16 bits)
        :return: Valor incrementado (16 bits)
        """
        self.in_value = in_value
        self.out = (self.in_value + 1) & 0xFFFF  # Módulo 2^16
        return self.out


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


class PC:
    def __init__(self):
        self.not_gate = Not()
        self.and_gate1 = And()
        self.and_gate2 = And()
        self.and_gate3 = And()
        self.or_gate1 = Or()
        self.or_gate2 = Or()
        self.mux1 = Mux16()
        self.mux2 = Mux16()
        self.inc = Inc16()
        self.register = Register()
        self.outin = 0  # Valor interno del PC

    def update(self, in_value, inc, load, reset, clk):
        """
        Actualiza el Program Counter (PC).
        :param in_value: Valor de entrada (16 bits)
        :param inc: Señal de incremento (0 o 1)
        :param load: Señal de carga (0 o 1)
        :param reset: Señal de reinicio (0 o 1)
        :param clk: Señal de reloj (0 o 1)
        :return: Valor de salida (16 bits)
        """
        if clk:  # Solo actualiza en el flanco de subida del reloj
            # Lógica para reset
            notR = self.not_gate.update(reset)
            notRL = self.and_gate1.update(notR, load)
            out2 = self.mux1.update(a=0, b=in_value, sel=notRL)

            # Lógica para increment
            notL = self.not_gate.update(load)
            notRnotL = self.and_gate2.update(notR, notL)
            notRnotLI = self.and_gate3.update(notRnotL, inc)
            out3 = self.inc.update(self.outin)
            out4 = self.mux2.update(a=out2, b=out3, sel=notRnotLI)

            # Lógica para mantener el valor actual
            RorL = self.or_gate1.update(reset, load)
            RorLorI = self.or_gate2.update(RorL, inc)

            # Actualizar el registro interno
            self.outin = self.register.update(out4, RorLorI, clk)

        return self.outin


# Función para simular el circuito en cada ciclo de tiempo
def simulate_pc(inputs):
    # Instanciar el Program Counter
    pc = PC()

    # Encabezado de la tabla
    print("| time |   in   |reset|load | inc |  out   |")
    print("|------|--------|-----|------|-----|--------|")

    # Simular cada ciclo de tiempo
    for time, (in_value, reset, load, inc, clk) in enumerate(inputs):
        # Actualizar el PC
        out_value = pc.update(in_value, inc, load, reset, clk)

        # Imprimir el estado actual
        print(f"| {time}+  | {in_value:6} |  {reset}  |  {load}  |  {inc}  | {out_value:6} |")
        print(f"| {time + 1}    | {in_value:6} |  {reset}  |  {load}  |  {inc}  | {out_value:6} |")


# Definir las entradas para cada ciclo de tiempo
inputs = [
    (0, 0, 0, 0, 1),      # time 0: Mantener
    (0, 0, 0, 1, 1),      # time 1: Increment
    (-32123, 0, 0, 1, 1), # time 2: Increment
    (-32123, 0, 1, 1, 1), # time 3: Load
    (-32123, 0, 0, 1, 1), # time 4: Increment
    (-32123, 0, 0, 1, 1), # time 5: Increment
    (12345, 0, 1, 0, 1),  # time 6: Load
    (12345, 1, 1, 0, 1),  # time 7: Reset
    (12345, 0, 1, 1, 1),  # time 8: Load
    (12345, 1, 1, 1, 1),  # time 9: Reset
    (12345, 0, 0, 1, 1),  # time 10: Increment
    (12345, 1, 0, 1, 1),  # time 11: Reset
    (0, 0, 1, 1, 1),      # time 12: Load
    (0, 0, 0, 1, 1),      # time 13: Increment
    (22222, 1, 0, 0, 1),  # time 14: Reset
]

simulate_pc(inputs)