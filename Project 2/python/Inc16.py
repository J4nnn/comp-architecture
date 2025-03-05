from Add16 import add16

def inc16(input_bits):
    """Increments a 16-bit binary number by one, returning the 16-bit result."""
    one = [0] * 16
    one[0] = 1

    return add16(one, input_bits)

# print(inc16([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])[::-1])

# Ejemplo 1: Incremento de un número binario pequeño
input1 = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]  # 2^15 + 14
result = inc16(input1)
print("\n")
print("Input:", input1[::-1])
print("Result:", result[::-1])
print()
