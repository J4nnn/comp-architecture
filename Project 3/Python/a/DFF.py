class DFF:
    def __init__(self):
        self.state = 0  # Estado inicial del flip-flop (0 o 1)

    def update(self, input_value, clk):
        """
        Actualiza el estado del DFF en el flanco de subida del reloj.
        :param input_value: Valor de entrada (0 o 1)
        :param clk: Señal de reloj (0 o 1)
        :return: El estado actual del DFF
        """
        if clk:  # Flanco de subida del reloj (clk = 1)
            self.state = input_value
        return self.state