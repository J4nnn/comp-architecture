class Multiplier:
    def __init__(self):
        self.RAM = [0] * 32768  # Simulación de la memoria RAM (32K palabras)
        self.positions = [0, 1, 2]  # Posiciones de RAM a mostrar (R0, R1, R2)

    def multiply(self):
        """Realiza la multiplicación de R0 y R1 mediante sumas repetitivas."""
        k = 0  # Acumulador del resultado
        c = 0  # Contador de iteraciones
        r0 = self.RAM[0]  # Valor de RAM[0]
        r1 = self.RAM[1]  # Valor de RAM[1]
        
        while c < r1:
            k += r0  # Sumar R0 a k
            c += 1  # Incrementar contador
        
        self.RAM[2] = k  # Almacenar resultado en R2

    def print_ram_state(self):
        """Muestra el estado de la memoria en las posiciones clave."""
        print("|" + "|".join(f" RAM[{pos}] " for pos in self.positions) + "|")
        print("|" + "|".join(f"{self.RAM[pos]:>8}" for pos in self.positions) + "|")
        
    def run(self, test_cases):
        """Ejecuta la simulación con diferentes valores de entrada."""
        for r0, r1 in test_cases:
            self.RAM[0] = r0
            self.RAM[1] = r1
            self.RAM[2] = 0  # Resetear R2 antes de cada ejecución
            self.multiply()
            self.print_ram_state()
            print("---")

# Casos de prueba
cases = [(0, 0), (1, 0), (0, 2), (3, 1), (2, 4), (6, 7)]

# Ejecutar el simulador
simulator = Multiplier()
simulator.run(cases)