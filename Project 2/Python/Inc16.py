from Add16 import Add16, bin_str

# Reutilizamos la función Add16
def Inc16(inp):
    one = [1] + [0] * 15  # Representa el número 1 en 16 bits: 0000000000000001
    return Add16(inp, one)  # Suma inp + 1 usando Add16

# Pruebas para Inc16
test_cases = [
    [0] * 16,  # 0 -> 1
    [1] * 16,  # 65535 -> 0 (overflow en complemento a dos)
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 32767 -> 32768
]

print(" in                | out               ")
print("----------------------------------------")
for inp in test_cases:
    result = Inc16(inp)
    print(f" {bin_str(inp)} | {bin_str(result)} ")
