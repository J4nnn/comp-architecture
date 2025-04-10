import time

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
                self.screen[index] = in_ & 0xFFFF  # Limitar a 16 bits
            return self.screen[index]
        elif address == 24576:  # Teclado
            if load:
                self.kbd = in_ & 0xFFFF  # Limitar a 16 bits
            return self.kbd
        else:  # Segunda mitad de la RAM
            return self.ram1.tick(in_, load, address - 16384)


def binary_to_int(value):
    """Convierte un número binario de 16 bits en complemento a dos a entero."""
    value &= 0xFFFF  # Asegurar 16 bits
    return value if value < 0x8000 else value - 0x10000  # Manejo de signo


class ScreenFiller:
    def __init__(self):
        self.RAM = RAM32K()  # Usamos RAM32K en vez de una lista
        self.positions = [16384, 17648, 18349, 19444, 20771, 21031, 22596, 23754, 24575]  # Posiciones clave

    def fill_screen(self, color):
        """Llena la pantalla con el color dado (0 para blanco, 0xFFFF para negro)"""
        value = 0xFFFF if color == -1 else 0
        for address in range(16384, 24576):  # Rango de direcciones de la pantalla
            self.RAM.tick(value, 1, address)  # Escribimos en la memoria

    def print_screen_state(self):
        """Muestra el estado de la pantalla en las posiciones clave."""
        print("|" + "|".join(f"RAM[{pos}]" for pos in self.positions) + "|")
        print("|" + "|".join(f"{binary_to_int(self.RAM.tick(0, 0, pos)):>8}" for pos in self.positions) + "|")

    def run(self):
        """Ejecuta el bucle que revisa el teclado y cambia el color de la pantalla."""
        while True:
            key_input = input("Presiona Enter para blanco, cualquier tecla + Enter para negro: ").strip()
            color = -1 if key_input else 0  # Si hay entrada, negro (0xFFFF); si no, blanco (0x0000)
            self.fill_screen(color)
            self.print_screen_state()
            print("Pantalla actualizada.")
            time.sleep(0.5)  # Pequeña pausa para evitar el spam de mensajes

# Ejecutar el simulador
simulator = ScreenFiller()
simulator.run()
