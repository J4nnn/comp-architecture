
from DFF import *

class Mux:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.sel = 0
        self.out = 0

    def update(self, a, b, sel):
        """
        Actualiza la salida del multiplexor.
        :param a: Entrada a
        :param b: Entrada b
        :param sel: Señal de selección (0 o 1)
        :return: Salida del multiplexor
        """
        self.a = a
        self.b = b
        self.sel = sel
        self.out = self.a if self.sel == 0 else self.b
        return self.out


class Bit:
    def __init__(self):
        self.mux = Mux()  # Multiplexor para seleccionar entre in y outprev
        self.dff = DFF()  # Flip-flop para almacenar el bit
        self.out = 0      # Salida del registro

    def update(self, in_value, load, clk):
        """
        Actualiza el registro de 1 bit.
        :param in_value: Valor de entrada (0 o 1)
        :param load: Señal de carga (0 o 1)
        :param clk: Señal de reloj (0 o 1)
        :return: Salida del registro
        """
        # Usar el multiplexor para seleccionar entre in y outprev
        dffin = self.mux.update(a=self.out, b=in_value, sel=load)

        # Actualizar el DFF con la salida del multiplexor
        self.out = self.dff.update(dffin, clk)

        return self.out

# Función para simular el circuito en cada ciclo de tiempo
def simulate_circuit(inputs):
    # Instanciar el registro de 1 bit
    bit = Bit()

    # Encabezado de la tabla
    print("| time | in  | load | out |")
    print("|------|-----|------|-----|")

    # Simular cada ciclo de tiempo
    for time, (in_value, load, clk) in enumerate(inputs):
        # Actualizar el registro
        out = bit.update(in_value, load, clk)

        # Imprimir el estado actual
        print(f"| {time}+  |  {in_value}  |  {load}  |  {out}  |")
        print(f"| {time + 1}    |  {in_value}  |  {load}  |  {out}  |")


# Definir las entradas para cada ciclo de tiempo
inputs = [
    (0, 0, 1),  # time 0
    (0, 1, 1),  # time 1
    (1, 0, 1),  # time 2
    (1, 1, 1),  # time 3
    (0, 0, 1),  # time 4
    (1, 0, 1),  # time 5
    (0, 1, 1),  # time 6
    (1, 1, 1),  # time 7
    (0, 0, 1),  # time 8
    (0, 0, 1),  # time 9
    (0, 0, 1),  # time 10
    (0, 0, 1),  # time 11
    (0, 0, 1),  # time 12
    (0, 0, 1),  # time 13
    (0, 0, 1),  # time 14
    (0, 0, 1),  # time 15
    (0, 0, 1),  # time 16
    (0, 0, 1),  # time 17
    (0, 0, 1),  # time 18
    (0, 0, 1),  # time 19
    (0, 0, 1),  # time 20
    (0, 0, 1),  # time 21
    (0, 0, 1),  # time 22
    (0, 0, 1),  # time 23
    (0, 0, 1),  # time 24
    (0, 0, 1),  # time 25
    (0, 0, 1),  # time 26
    (0, 0, 1),  # time 27
    (0, 0, 1),  # time 28
    (0, 0, 1),  # time 29
    (0, 0, 1),  # time 30
    (0, 0, 1),  # time 31
    (0, 0, 1),  # time 32
    (0, 0, 1),  # time 33
    (0, 0, 1),  # time 34
    (0, 0, 1),  # time 35
    (0, 0, 1),  # time 36
    (0, 0, 1),  # time 37
    (0, 0, 1),  # time 38
    (0, 0, 1),  # time 39
    (0, 0, 1),  # time 40
    (0, 0, 1),  # time 41
    (0, 0, 1),  # time 42
    (0, 0, 1),  # time 43
    (0, 0, 1),  # time 44
    (0, 0, 1),  # time 45
    (0, 0, 1),  # time 46
    (0, 0, 1),  # time 47
    (0, 0, 1),  # time 48
    (0, 0, 1),  # time 49
    (0, 0, 1),  # time 50
    (0, 0, 1),  # time 51
    (0, 0, 1),  # time 52
    (0, 0, 1),  # time 53
    (0, 0, 1),  # time 54
    (0, 0, 1),  # time 55
    (0, 0, 1),  # time 56
    (0, 1, 1),  # time 57
    (1, 0, 1),  # time 58
    (1, 0, 1),  # time 59
    (1, 0, 1),  # time 60
    (1, 0, 1),  # time 61
    (1, 0, 1),  # time 62
    (1, 0, 1),  # time 63
    (1, 0, 1),  # time 64
    (1, 0, 1),  # time 65
    (1, 0, 1),  # time 66
    (1, 0, 1),  # time 67
    (1, 0, 1),  # time 68
    (1, 0, 1),  # time 69
    (1, 0, 1),  # time 70
    (1, 0, 1),  # time 71
    (1, 0, 1),  # time 72
    (1, 0, 1),  # time 73
    (1, 0, 1),  # time 74
    (1, 0, 1),  # time 75
    (1, 0, 1),  # time 76
    (1, 0, 1),  # time 77
    (1, 0, 1),  # time 78
    (1, 0, 1),  # time 79
    (1, 0, 1),  # time 80
    (1, 0, 1),  # time 81
    (1, 0, 1),  # time 82
    (1, 0, 1),  # time 83
    (1, 0, 1),  # time 84
    (1, 0, 1),  # time 85
    (1, 0, 1),  # time 86
    (1, 0, 1),  # time 87
    (1, 0, 1),  # time 88
    (1, 0, 1),  # time 89
    (1, 0, 1),  # time 90
    (1, 0, 1),  # time 91
    (1, 0, 1),  # time 92
    (1, 0, 1),  # time 93
    (1, 0, 1),  # time 94
    (1, 0, 1),  # time 95
    (1, 0, 1),  # time 96
    (1, 0, 1),  # time 97
    (1, 0, 1),  # time 98
    (1, 0, 1),  # time 99
    (1, 0, 1),  # time 100
    (1, 0, 1),  # time 101
    (1, 0, 1),  # time 102
    (1, 0, 1),  # time 103
    (1, 0, 1),  # time 104
    (1, 0, 1),  # time 105
    (1, 0, 1),  # time 106
    (1, 0, 1),  # time 107
]
simulate_circuit(inputs)