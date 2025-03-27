import time

class ScreenFiller:
    def __init__(self):
        self.RAM = [0] * 32768  # Simulación de la memoria RAM (32K palabras)
        self.SCREEN_START = 16384  # Dirección inicial de la pantalla
        self.SCREEN_END = 24575  # Última dirección de la pantalla
        self.KBD = 24576  # Dirección del teclado
        self.positions = [16384, 17648, 18349, 19444, 20771, 21031, 22596, 23754, 24575]  # Posiciones a mostrar

    def fill_screen(self, color):
        """Llena la pantalla con el color dado (0 para blanco, -1 para negro)"""
        for address in range(self.SCREEN_START, self.SCREEN_END + 1):
            self.RAM[address] = color

    def print_screen_state(self):
        """Muestra el estado de la pantalla en las posiciones clave."""
        print("|" + "|".join(f"RAM[{pos}]" for pos in self.positions) + "|")
        print("|" + "|".join(f"{self.RAM[pos]:>8}" for pos in self.positions) + "|")

    def run(self):
        """Ejecuta el bucle que revisa el teclado y cambia el color de la pantalla."""
        while True:
            key_input = input("Presiona Enter para blanco, cualquier tecla + Enter para negro: ").strip()
            if key_input:
                self.fill_screen(-1)  # Si hay entrada, llenar de negro
            else:
                self.fill_screen(0)  # Si no hay entrada, llenar de blanco
            self.print_screen_state()
            print("Pantalla actualizada.")
            time.sleep(0.5)  # Pequeña pausa para evitar el spam de mensajes

# Ejecutar el simulador
simulator = ScreenFiller()
simulator.run()
